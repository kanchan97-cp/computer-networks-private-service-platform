# Phase 2 – Private Service Platform Extensions

## 1. Introduction
Phase 2 extends the private service platform created in Phase 1. It focuses on DNS TTL behavior, DNS client caching, firewall-based access restrictions, Nginx availability and backend service availability.

## 2. DNS TTL Behavior
DNS TTL (Time to Live) determines how long a DNS record can be cached before a resolver needs to refresh it.

The TTL value was configured and tested to observe how DNS responses behave before and after a record change.

### Testing
- Checked the original DNS record.
- Recorded the TTL.
- Changed the DNS record or TTL configuration.
- Verified the updated response.

## 3. Client Cache Behavior
Client DNS caching can affect how quickly a client observes DNS changes.

The DNS resolution behavior was tested before and after the DNS record update and cache expiration or flushing.

### Testing
- Initial resolution.
- DNS record modification.
- Client cache behavior.
- Cache refresh verification.

## 4. Firewall Access Restrictions
Firewall rules were used to restrict direct access to backend ports.

The intended architecture allows clients to access the application through Nginx while limiting direct backend access.

### Testing
- Direct backend access test.
- Firewall-blocked connection verification.
- Nginx access verification.

## 5. Nginx Access After Firewall
After firewall rules were implemented, HTTPS requests were tested through Nginx.

Nginx forwarded requests to the backend services while direct backend access was restricted according to the firewall rules.

## 6. Backend Failover
Backend failover was tested by temporarily stopping one backend service.

The application continued responding through the available backend.

## 7. Backend Recovery
The stopped backend service was restarted and tested again through the reverse proxy.

## 8. Standby Nginx
A standby Nginx server was configured and tested as an alternate entry point to the private service platform.

## 9. DNS Cutover
DNS was modified to direct the application hostname to the standby Nginx server.

Client resolution and application access were verified after the cutover.

## 10. Troubleshooting
A fault was introduced during testing, diagnosed and resolved. The application was tested again after the fix.

## 11. Conclusion
Phase 2 extends the private service platform with DNS behavior testing, controlled backend access, backend failover and recovery, standby proxy testing and troubleshooting.

The tests demonstrate additional availability and access control mechanisms in the private network environment.
