import json

dict = {
    "Routers": {
        "PE1": {
            "Router ID": "2.2.2.2",
            "AS": "100",
            "vrf":{
                "clientA": {"rd":"100:110","export":"100:1000","import":"100:1000"},
                "clientB": {"rd":"100:120","export":"100:2000","import":"100:2000"},
                },       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "vrf":"clientA",
                    "IP": "192.168.1.1",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet2/0": {
                    "mpls":"True",
                    "IP": "192.168.2.2",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet3/0": {
                    "vrf":"clientB",
                    "IP": "192.168.6.3",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "2.2.2.2",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "1",
                    "Network": [
                        "2.2.2.2 0.0.0.0",
                        "192.168.2.0 0.0.0.255"
                    ],
                },
                "BGP": {
                    "Neighbors": {
                        "9.9.9.9":"100",
                        "192.168.1.2": "200",
                        "192.168.6.1": "500",
                    },
                    "vpnv4":[   
                        "9.9.9.9"
                    ],
                    "vrf":{
                        "clientA": ["192.168.1.2","200"],
                        "clientB": ["192.168.6.1","500"],
                    },                     
                }
            }
        },
        "PE2": {
            "Router ID": "5.5.5.5",
            "AS": "100",
            "vrf":{
                "clientA": {"rd":"100:110","export":"100:1000","import":"100:1000"},
                "clientB": {"rd":"100:120","export":"100:2000","import":"100:2000"},
                },       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "mpls":"True",
                    "IP": "192.168.4.1",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet2/0": {
                    "vrf":"clientA",                    
                    "IP": "192.168.5.2",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet3/0": {
                    "vrf":"clientB",
                    "IP": "192.168.7.3",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "5.5.5.5",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "1",
                    "Network": [
                        "5.5.5.5 0.0.0.0",
                        "192.168.4.0 0.0.0.255" 
                    ],
                },
                "BGP": {
                    "Neighbors": {                        
                        "9.9.9.9": "100",                                                                       
                        "192.168.5.1":"300",
                        "192.168.7.1":"400"
                    },
                    "vpnv4":[
                        
                        "9.9.9.9",
                        
                    ],
                    "vrf":{
                        "clientA": ["192.168.5.1","300"],
                        "clientB": ["192.168.7.1","400"],
                    },                     
                }
            }
        },
        "PE3": {
            "Router ID": "10.10.10.10",
            "AS": "100",
            "vrf":{
                "clientA": {"rd":"100:110","export":"100:1000","import":"100:1000"},
                "clientB": {"rd":"100:120","export":"100:2000","import":"100:2000"},
                },       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "mpls":"True",
                    "IP": "192.168.9.1",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet2/0": {
                    "vrf":"clientA",                    
                    "IP": "192.168.10.2",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet3/0": {
                    "vrf":"clientB",
                    "IP": "192.168.11.3",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "10.10.10.10",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "1",
                    "Network": [
                        "10.10.10.10 0.0.0.0",
                        "192.168.9.0 0.0.0.255" 
                    ],
                },
                "BGP": {
                    "Neighbors": {                        
                        "9.9.9.9": "100",                                                                       
                        "192.168.10.1":"600",
                        "192.168.11.1":"700"
                    },
                    "vpnv4":[                       
                        "9.9.9.9",                        
                    ],
                    "vrf":{
                        "clientA": ["192.168.10.1","600"],
                        "clientB": ["192.168.11.1","700"],
                    },                     
                }
            }
        },
        "P1": {
            "Router ID": "3.3.3.3",
            "AS": "100",       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "mpls":"True",
                    "IP": "192.168.2.1",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet2/0": {
                    "mpls":"True",
                    "IP": "192.168.3.2",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet3/0": {
                    "mpls":"True",
                    "IP": "192.168.8.3",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "3.3.3.3",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "1",
                    "Network": [
                        "3.3.3.3 0.0.0.0" ,
                        "192.168.2.0 0.0.0.255",
                        "192.168.3.0 0.0.0.255",
                        "192.168.8.0 0.0.0.255"
                    ],
                },
                "BGP": {
                    "Neighbors": {
                        
                        "9.9.9.9": "100",                                                 
                        
                    },
                    "vpnv4":[  
                        
                        "9.9.9.9",
                                                                  
                    ],                    
                }
            }
        },
        "P2": {
            "Router ID": "4.4.4.4",
            "AS": "100",       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "mpls":"True",
                    "IP": "192.168.3.1",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet2/0": {
                    "mpls":"True",
                    "IP": "192.168.4.2",
                    "Mask": "255.255.255.0"
                },
                "GigabitEthernet3/0": {
                    "mpls":"True",
                    "IP": "192.168.9.3",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "4.4.4.4",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "1",
                    "Network": [
                        "4.4.4.4 0.0.0.0" ,
                        "192.168.3.0 0.0.0.255",
                        "192.168.4.0 0.0.0.255",
                        "192.168.9.0 0.0.0.255"
                    ],
                },
                "BGP": {
                    "Neighbors": {
                        "9.9.9.9": "100",                                                                       
                    },
                    "vpnv4":[  
                        "9.9.9.9",                                                                
                    ],                    
                }
            }
        },        
        "CE1": {
            "Router ID": "1.1.1.1",
            "AS": "200",       
            "Interfaces": {
                "GigabitEthernet2/0": {
                    "IP": "192.168.1.2",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "1.1.1.1",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "BGP": {
                    "Neighbors": {
                        "192.168.1.1": "100"                   
                    },
                    "ipv4":{
                        "neighbor":"192.168.1.1",
                        "network":"192.168.1.0"
                    },                    
                }
            }
        },
        "CE2": {
            "Router ID": "6.6.6.6",
            "AS": "300",       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "192.168.5.1",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "6.6.6.6",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "BGP": {
                    "Neighbors": {
                        "192.168.5.2": "100"                   
                    },
                    "ipv4":{
                        "neighbor":"192.168.5.2",
                        "network":"192.168.5.0"
                    },                    
                }
            }
        },
        "CE3": {
            "Router ID": "7.7.7.7",
            "AS": "500",       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "192.168.6.1",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "7.7.7.7",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "BGP": {
                    "Neighbors": {
                        "192.168.6.3": "100"                   
                    },
                    "ipv4":{
                        "neighbor":"192.168.6.3",
                        "network":"192.168.6.0"
                    },                    
                }
            }
        },
        "CE4": {
            "Router ID": "8.8.8.8",
            "AS": "400",       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "192.168.7.1",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "8.8.8.8",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "BGP": {
                    "Neighbors": {
                        "192.168.7.3": "100"                   
                    },
                    "ipv4":{
                        "neighbor":"192.168.7.3",
                        "network":"192.168.7.0"
                    },                    
                }
            }
        },
        "CE5": {
            "Router ID": "11.11.11.11",
            "AS": "600",       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "192.168.10.1",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "11.11.11.11",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "BGP": {
                    "Neighbors": {
                        "192.168.10.2": "100"                   
                    },
                    "ipv4":{
                        "neighbor":"192.168.10.2",
                        "network":"192.168.10.0"
                    },                    
                }
            }
        },
        "CE6": {
            "Router ID": "12.12.12.12",
            "AS": "700",       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "192.168.11.1",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "12.12.12.12",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "BGP": {
                    "Neighbors": {
                        "192.168.11.3": "100"                   
                    },
                    "ipv4":{
                        "neighbor":"192.168.11.3",
                        "network":"192.168.11.0"
                    },                    
                }
            }
        },
        "Route-Reflector": {
            "Router ID": "9.9.9.9",
            "AS": "100",       
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "192.168.8.1",
                    "Mask": "255.255.255.0"
                },
                "Loopback 0": {
                    "IP": "9.9.9.9",
                    "Mask": "255.255.255.255"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "1",
                    "Network": [
                        "192.168.8.0 0.0.0.255",
                        "9.9.9.9 0.0.0.0"
                    ],
                },
                "BGP": {
                    "Neighbors": {
                        "2.2.2.2": "100",  
                        "3.3.3.3": "100",
                        "4.4.4.4": "100",  
                        "5.5.5.5": "100",
                        "10.10.10.10": "100"            
                    },
                    "vpnv4":[
                        "RR",
                        "2.2.2.2",
                        "3.3.3.3",
                        "4.4.4.4",
                        "5.5.5.5",
                        "10.10.10.10"
                    ]                    
                }
            }
        } 

    }
}

# Créer le fichier JSON à partir du dictionnaire
with open('routers_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(dict, json_file, indent=4, ensure_ascii=False)

print("Le fichier JSON a été créé avec succès.")