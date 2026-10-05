# Computer Networks Project — Private Network Service Platform

## Team Members

1. Kanchan Rani
2. Yashpal Lohan
3. Kshitiz Surana
4. Ayush 

---

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

The main application is accessed using:
https://app.team1.test


The complete request flow is:
Client
   ↓
Private DNS
   ↓
nginx Reverse Proxy / Load Balancer
   ↓
Backend A / Backend B
   ↓
nginx
   ↓
HTTPS Response
   ↓
Client

Network Architecture
Machine	Role	IP Address	Port
Mac 1	DNS Server + Client	10.7.22.184	53
Mac 2	nginx / Edge / Load Balancer	10.7.5.97	80, 443
Mac 3	Backend A	10.7.10.126	3001
Mac 4	Backend B	10.7.21.212	3002


All four machines are connected to the same private Wi-Fi/LAN.
DNS
Mac 1 runs dnsmasq as the private DNS server.
app.team1.test → 10.7.5.97
api.team1.test → 10.7.5.97

DNS Server → 10.7.22.184

The DNS configuration is stored in:
dns/dnsmasq.conf

The client uses Mac 1 as its DNS server.
DNS resolution can be tested using:
dig app.team1.test

Expected result:
app.team1.test → 10.7.5.97

Backend Servers
Two simple Python HTTP servers are used as backend services.
Backend A
Backend A runs on Mac 3.
IP Address: 10.7.10.126
Port: 3001

Response:
Hello from Backend A - Mac 3

Response header:
X-Backend: A

Source code:
backend-a/server.py

Backend A can be tested directly using:
curl http://10.7.10.126:3001

Backend B
Backend B runs on Mac 4.
IP Address: 10.7.21.212
Port: 3002

Response:
Hello from Backend B - Mac 4

Response header:
X-Backend: B

Source code:
backend-b/server.py

Backend B can be tested directly using:
curl http://10.7.21.212:3002

nginx Reverse Proxy
Mac 2 runs nginx and acts as the edge server.
IP Address: 10.7.5.97
HTTP Port: 80
HTTPS Port: 443

nginx receives requests from the client and forwards them to the backend servers.
Configuration file:
nginx/nginx.conf

The backend servers configured in nginx are:
Backend A → 10.7.10.126:3001
Backend B → 10.7.21.212:3002

The nginx configuration uses round-robin load balancing.
The X-Backend response header identifies which backend handled the request.
Load Balancing
nginx distributes requests between Backend A and Backend B.
Example requests:
curl -I "https://app.team1.test/?test=1"
curl -I "https://app.team1.test/?test=2"
curl -I "https://app.team1.test/?test=3"
curl -I "https://app.team1.test/?test=4"

The response contains:
X-Backend: A

or:
X-Backend: B

This demonstrates that nginx is forwarding requests to both backend servers.
HTTPS / TLS
HTTPS is configured on nginx using a certificate for:
app.team1.test

The certificate was created using mkcert.
The client accesses the application using:
https://app.team1.test

nginx terminates the TLS connection on port 443.
The HTTP-to-HTTPS redirect is also configured.
Therefore:
http://app.team1.test

redirects to:
https://app.team1.test

HTTPS can be tested using:
curl -I https://app.team1.test

Expected response:
HTTP/1.1 200 OK

HTTP Caching
nginx is configured with an HTTP cache.
The cache status is exposed using the response header:
X-Cache-Status

Possible cache states include:
MISS
HIT
EXPIRED

A repeated request can be used to demonstrate caching behavior.
Example:
curl -I "https://app.team1.test/?cache=test"

Running the same request again allows the cache status to be observed.
The caching configuration is included in:
nginx/nginx.conf

Request Flow
The complete request flow is:
Step 1 — Client Request
The client requests:
https://app.team1.test

Step 2 — DNS Resolution
The client asks the private DNS server on Mac 1:
10.7.22.184:53

The DNS server resolves:
app.team1.test

to:
10.7.5.97

Step 3 — HTTPS Connection
The client establishes an HTTPS/TLS connection with Mac 2:
10.7.5.97:443

Step 4 — nginx Processing
nginx receives the HTTPS request and forwards it to one of the backend servers.
Backend A → 10.7.10.126:3001
Backend B → 10.7.21.212:3002

Step 5 — Backend Response
The selected backend sends an HTTP response.
Example:
X-Backend: A

Hello from Backend A - Mac 3

Step 6 — Response to Client
nginx sends the response back to the client through the HTTPS connection.
Wireshark Analysis
Wireshark is used to observe and verify network communication.
DNS Traffic
Filter:
dns

This shows DNS queries and responses between the client and the private DNS server.
Client → Mac 1
Mac 1 → Client

Backend A Traffic
Filter:
tcp.port == 3001

This shows communication between:
Mac 2 → Mac 3

The capture demonstrates TCP communication and the HTTP request/response.
Backend B Traffic
Filter:
tcp.port == 3002

This shows communication between:
Mac 2 → Mac 4

The capture demonstrates TCP communication and the HTTP request/response.
HTTPS / TLS Traffic
Filter:
tcp.port == 443

This shows the TLS communication between the client and nginx.
The TLS Client Hello contains the hostname:
app.team1.test

Project Structure
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

Testing Commands
Check DNS
dig app.team1.test

Expected:
app.team1.test → 10.7.5.97

Test Backend A
curl http://10.7.10.126:3001

Expected:
Hello from Backend A - Mac 3

Test Backend B
curl http://10.7.21.212:3002

Expected:
Hello from Backend B - Mac 4

Test HTTPS
curl -I https://app.team1.test

Expected:
HTTP/1.1 200 OK

The response should contain either:
X-Backend: A

or:
X-Backend: B

Test Load Balancing
curl -I "https://app.team1.test/?test=1"
curl -I "https://app.team1.test/?test=2"
curl -I "https://app.team1.test/?test=3"
curl -I "https://app.team1.test/?test=4"

The X-Backend header demonstrates which backend served each request.
Test HTTP Caching
curl -I "https://app.team1.test/?cache=test"

Run the same command again and observe:
X-Cache-Status

Example states:
MISS
HIT
EXPIRED

Evidence
The evidence folder contains screenshots for the main Phase 1 requirements.
File	Purpose
dns-wireshark.png	DNS query and response
backend-a-wireshark.png	Backend A traffic
backend-b-wireshark.png	Backend B traffic
tls-wireshark.png	TLS handshake
caching.png	HTTP caching demonstration
load-balancing.png	Load balancing demonstration


The project requires evidence covering DNS resolution, HTTP/curl output, Wireshark captures, TLS, and caching.     CN_Project_Doc
Documentation
The docs folder contains:
Architecture
docs/architecture.md

Contains the machine roles, IP addresses, ports, DNS configuration, backend services, nginx configuration, HTTPS, caching, and final request flow.
Network Topology
docs/topology.png

Shows the four-machine network architecture.
Request Flow
docs/request-flow.png

Shows how a request travels from the client through DNS, nginx, and the backend servers.
Technologies Used
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
