# Phase 1 Architecture

## Project Overview

This project implements a private network service platform using four macOS machines.

The request flow is:

Client → Private DNS → nginx → Backend A / Backend B

Application URL:

`https://app.team1.test`

## Machine Roles

| Machine | Role | IP Address | Port |
|---|---|---|---|
| Mac 1 | Private DNS Server + Client | `10.7.22.184` | 53 |
| Mac 2 | nginx Reverse Proxy + Load Balancer | `10.7.5.97` | 80, 443 |
| Mac 3 | Backend A | `10.7.10.126` | 3001 |
| Mac 4 | Backend B | `10.7.21.212` | 3002 |

## DNS Configuration

DNS Server:

`10.7.22.184`

DNS Records:

app.team1.test → 10.7.5.97
api.team1.test → 10.7.5.97

Backend Services
Backend A
- Machine: Mac 3
- IP: 10.7.10.126
- Port: 3001
- Response: Hello from Backend A - Mac 3
- Header: X-Backend: A
Backend B
- Machine: Mac 4
- IP: 10.7.21.212
- Port: 3002
- Response: Hello from Backend B - Mac 4
- Header: X-Backend: B
nginx Reverse Proxy and Load Balancing
Mac 2 runs nginx as the reverse proxy and load balancer.
nginx forwards requests to:
Backend A → 10.7.10.126:3001
Backend B → 10.7.21.212:3002

Round-robin load balancing is used to distribute requests between Backend A and Backend B.
The X-Backend header identifies which backend served the request.
HTTPS / TLS
nginx terminates HTTPS on port 443.
Certificate domain:
app.team1.test
The client connects to nginx using HTTPS, and nginx forwards requests to the backend servers.
HTTP Caching
nginx is configured with HTTP caching.
Cache status is shown using:
X-Cache-Status
Possible cache states include:
MISS
HIT
EXPIRED

A repeated request can demonstrate cached content.
Wireshark Evidence
Wireshark is used to observe:
- DNS traffic — UDP port 53
- Backend A traffic — TCP port 3001
- Backend B traffic — TCP port 3002
- HTTPS/TLS traffic — TCP port 443
Final Request Flow
Client
   |
   | DNS Query
   v
Mac 1 — DNS Server
10.7.22.184
   |
   | app.team1.test → 10.7.5.97
   v
Mac 2 — nginx
10.7.5.97
   |
   | HTTPS / TLS
   |
   +------> Mac 3 — Backend A
   |         10.7.10.126:3001
   |
   +------> Mac 4 — Backend B
             10.7.21.212:3002

Technologies Used
- macOS
- Python
- dnsmasq
- nginx
- mkcert
- HTTPS/TLS
- curl
- dig
- Wireshark
