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
