from gns3fy import Gns3Connector, Project, Node
import telnetlib
import time
import json

# Connect to GNS3
server = Gns3Connector("http://localhost:3080")
project_name = "NAS2025_Groupe1_TC_Dang_Thien_Paul_Julien"
project = Project(name=project_name, connector=server)
project.get()

# Assurer le projet est ouvert
if project.status != "opened":
    project.open()


with open('routers_data.json', 'r') as file:
    data = json.load(file)

def start_router(router_name):
    router = next((node for node in project.nodes if node.name == router_name), None)  # Search and parcourir for all the nodes we have in projet
    if not router:
        print(f"Cant find {router_name} in {project_name}.")
        return None

    if router.status != "started":
        print(f"Starting {router_name}...")
        router.start()
        time.sleep(5)  # just wait for it to setting up
    else:
        print(f"Router {router_name} is already running.")
    return router

def send_telnet_commands(tn, commands):
    for cmd in commands:
        tn.write(f"{cmd}\r\n".encode("utf-8"))
        time.sleep(0.1)  # Wait router execute

def configure_router(node):
    router_name = node.name
    console_port = node.console

    # Verifier Router dans intent file
    if router_name not in data["Routers"]:
        print(f"{router_name} is not configured in intent file.")
        return

    try:
        # Connexion à Telnet
        tn = telnetlib.Telnet(node.console_host, console_port)
        print(f"Connexion {router_name} passed!")
        for i in range(3):
            tn.write("\r\n".encode("utf-8"))
            time.sleep(0.5)
        time.sleep(1)
        #Configure vrf
        
        configure_vrf(tn, data["Routers"][router_name])
        # Configuration adresse IPV4
        for interface, details in data["Routers"][router_name]["Interfaces"].items():
            commands = ["configure terminal",
                f"interface {interface}",
                f"ip address {details['IP']} {details['Mask']}",
                 "no shutdown"]
            if "mpls" in details.keys():
                commands.append("mpls ip")
            commands.append("end")
            send_telnet_commands(tn, commands)

        # Protocoles
        for protocol, settings in data["Routers"][router_name]["Protocols"].items():
            if protocol == "OSPF":
                configure_ospf(tn, settings)
            elif protocol == "BGP":
                configure_bgp(tn, settings, data["Routers"][router_name]["AS"], data["Routers"][router_name]["Router ID"])

        tn.close()
    except Exception as e:
        print(f"Error when configure {router_name}: {e}")
def configure_vrf(tn,configr):  #settings la PE1,PE2       
        if "vrf" in configr.keys():
            for u,v in configr["vrf"].items():
                send_telnet_commands(tn,[
                "configure terminal",
                f"vrf definition {u}",
                f"rd {v["rd"]}",
                f"route-target export {v["export"]}",
                f"route-target import {v["import"]}",
                "address-family ipv4",
                "exit-address-family",
                "end"
                ])
            for interface,config in configr["Interfaces"].items():
                if "vrf" in config.keys():
                    send_telnet_commands(tn, [
                    "configure terminal",
                    f"interface {interface}",
                    f"vrf forwarding {config["vrf"]}",
                    "end"
                    ])
            

def configure_ospf(tn, ospf):        # Same as RIP
    commands= ["configure terminal",
               f"router ospf {ospf['Name']}"]
    for interface in ospf["Network"]:
        commands.append(f"network {interface} area 0")
    commands.append("end")
    send_telnet_commands(tn, commands)


def configure_bgp(tn, bgp, as_number, router_id):
    # Neighbors configurations
    commands = [
        "configure terminal",
        f"router bgp {as_number}",
        f"bgp router-id {router_id}"
    ]
    for neighbor, remote_as in bgp["Neighbors"].items():               
        commands.append(f"neighbor {neighbor} remote-as {remote_as}")
        if remote_as ==  as_number:
            commands.append(f"neighbor {neighbor} update-source loop 0")
    commands.append("end")
    send_telnet_commands(tn, commands)
    if "vpnv4" in bgp.keys():
        commands = [
            "configure terminal",
            f"router bgp {as_number}",
            f"bgp router-id {router_id}",
            "address-family vpnv4"
        ]
        for neighbor in bgp["vpnv4"]: 
            commands.append(f"neighbor {neighbor} activate")
            commands.append(f"neighbor {neighbor} send-community both")
            if "RR" in bgp["vpnv4"]:
                commands.append(f"neighbor {neighbor} route-reflector-client")
        commands.append("end")
        send_telnet_commands(tn, commands)
    elif "ipv4" in bgp.keys():
        commands = [
            "configure terminal",
            f"router bgp {as_number}",
            f"bgp router-id {router_id}",
            "address-family ipv4"
        ]
        for action,network in bgp["ipv4"].items():
            if action == "neighbor":
                commands.append(f"neighbor {network} activate")
            elif action =="network":
                commands.append(f"network {network}")
        commands.append("end")
        send_telnet_commands(tn, commands)
    if "vrf" in bgp.keys():
        commands = [
            "configure terminal",
            f"router bgp {as_number}",
            f"bgp router-id {router_id}",
        ]
        for client,address in bgp["vrf"].items():
            commands.append(f"address-family ipv4 vrf {client}")            
            commands.append(f"neighbor {address[0]} remote-as {address[1]}")            
            commands.append(f"neighbor {address[0]} activate")
            commands.append("exit") 
        commands.append("end")
        send_telnet_commands(tn, commands)
    # Advertising
    if "Advertise" in bgp:
        send_telnet_commands(tn, ["address-family ipv6 unicast"] + [f"network {net}" for net in bgp["Advertise"]] + ["end"])

# Process
for node in project.nodes:
    start_router(node.name)
    configure_router(node)
