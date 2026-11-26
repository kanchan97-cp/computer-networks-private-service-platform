# Phase 2 – Firewall Rules

## Objective
The objective is to restrict direct client access to the backend servers while allowing the Nginx reverse proxy to communicate with the backend services.

## Network Design
- Backend A listens on port 3001.
- Backend B listens on port 3002.
- Nginx acts as the reverse proxy.
- Clients access the application through HTTPS on port 443.
- Backend access should be permitted only from the Nginx host, where the firewall rules are successfully implemented.

## Firewall Implementation
macOS Packet Filter (PF) is used to implement firewall restrictions on the backend hosts.

### Intended Rules
1. Allow backend traffic originating from the Nginx host.
2. Block direct incoming connections from other hosts to backend ports.
3. Keep necessary system and SSH access unaffected.
4. Verify backend connectivity through Nginx after applying the rules.

### Backend A
Port: 3001

### Backend B
Port: 3002

## Verification
- Test direct access to the backend from the client.
- Confirm direct access is blocked.
- Test HTTPS access through Nginx.
- Confirm Nginx can still communicate with the backend.

## Security Result
The backend services are not intended to be accessed directly by clients. The reverse proxy acts as the controlled entry point to the application.
<<<<<<< HEAD

## Example macOS PF Rule Template

The following is a reference template for restricting backend ports using macOS Packet Filter (PF).

Replace NGINX_IP with the actual IP address of the Nginx host.

### Backend A Rule Concept
Allow Nginx to access port 3001, then block other incoming connections to that port.

### Backend B Rule Concept
Allow Nginx to access port 3002, then block other incoming connections to that port.

### Example Rule Structure

```pf
pass in quick proto tcp from NGINX_IP to any port 3001
block in quick proto tcp from any to any port 3001

pass in quick proto tcp from NGINX_IP to any port 3002
block in quick proto tcp from any to any port 3002
```

The above is a conceptual rule template. It must be adapted to the actual backend host, interface, IP addresses and existing PF rules.

### Safety
Do not replace the system firewall configuration without reviewing the existing rules. Incorrect firewall rules may block SSH or other network access.

### Verification
The rules must be tested from both the client and Nginx host to confirm direct access restrictions and proxy connectivity.
```
=======
>>>>>>> 9832b2d3eb393385ea744b453eac3c8473b0b23b
