# Computer Networks Project — Private Network Service Platform

## Team Members

1. Kanchan Rani
2. Yashpal Lohan 
3. Kshitiz Surana
4. 

## Project Overview

This project demonstrates a private local network service platform using four macOS machines.

The system demonstrates:

- Private LAN connectivity
- Private DNS using dnsmasq
- Two backend servers
- nginx reverse proxy
- Round-robin load balancing
- HTTPS/TLS
- HTTP caching
- Wireshark packet analysis

## Network Architecture

| Machine | Role | IP Address | Port |
|---|---|---|---|
| Mac 1 | DNS Server + Client | 10.7.22.184 | 53 |
| Mac 2 | nginx / Edge / Load Balancer | 10.7.5.97 | 80, 443 |
| Mac 3 | Backend A | 10.7.10.126 | 3001 |
| Mac 4 | Backend B | 10.7.21.212 | 3002 |

## DNS

```text
app.team1.test → 10.7.5.97
api.team1.test → 10.7.5.97

DNS Server → 10.7.22.184
