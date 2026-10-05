# Computer Networks Project — Private Network Service Platform

## Team Members

1. Kanchan Rani
2. Yashpal Lohan
3. Kshitiz Surana
4. Ayush

## Overview

A local private network service platform built using four macOS machines. The project demonstrates DNS, TCP, HTTPS/TLS, nginx reverse proxy, load balancing, HTTP caching, and Wireshark packet analysis.

## Architecture

| Machine | Role | IP | Port |
|---|---|---|---|
| Mac 1 | DNS Server + Client | `10.7.22.184` | `53` |
| Mac 2 | nginx / Load Balancer | `10.7.5.97` | `80, 443` |
| Mac 3 | Backend A | `10.7.10.126` | `3001` |
| Mac 4 | Backend B | `10.7.21.212` | `3002` |

## DNS

app.team1.test → 10.7.5.97  
api.team1.test → 10.7.5.97  
DNS Server → 10.7.22.184

Configuration: `dns/dnsmasq.conf`

## Backend Servers

- **Backend A:** `10.7.10.126:3001` — `X-Backend: A`
- **Backend B:** `10.7.21.212:3002` — `X-Backend: B`

Source code:

- `backend-a/server.py`
- `backend-b/server.py`

## nginx

nginx runs on Mac 2 and works as a reverse proxy and round-robin load balancer.

Configuration: `nginx/nginx.conf`

Application: `https://app.team1.test`

## HTTPS / TLS

HTTPS is terminated at nginx on port `443`. The certificate for `app.team1.test` was created using `mkcert`.

## HTTP Caching

nginx is configured with HTTP caching using the `X-Cache-Status` header.

Possible states:

- `MISS`
- `HIT`
- `EXPIRED`

## Wireshark

Network traffic is analyzed using the following filters:

- `dns`
- `tcp.port == 3001`
- `tcp.port == 3002`
- `tcp.port == 443`

## Project Structure

```text 
computer-networks-private-service-platform/
│
├── README.md
│
├── backend-a/
│   └── server.py
│
├── backend-b/
│   └── server.py
│
├── nginx/
│   └── nginx.conf
│
├── dns/
│   └── dnsmasq.conf
│
├── docs/
│   ├── architecture.md
│   ├── topology.png
│   └── request-flow.png
│
└── evidence/
    ├── dns-wireshark.png
    ├── backend-a-wireshark.png
    ├── backend-b-wireshark.png
    ├── tls-wireshark.png
    ├── caching.png
    └── load-balancing.png
   ``` 
## Technologies Used
- macOS
- Python
- dnsmasq
- nginx
- mkcert
- HTTP
- HTTPS
- TLS
- TCP/IP
- curl
- dig
- Wireshark
- Git
- GitHub
