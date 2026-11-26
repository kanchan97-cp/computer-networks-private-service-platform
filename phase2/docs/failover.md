# Phase 2 – Failover and Recovery

## 1. Backend Failover

### Objective
To verify that the private application remains accessible when one backend service becomes unavailable.

### Initial Setup
- Backend A: Port 3001
- Backend B: Port 3002
- Nginx: HTTPS reverse proxy
- Application domain: app.team1.test

### Procedure
1. Start Backend A.
2. Start Backend B.
3. Verify both backend services.
4. Send requests through Nginx.
5. Stop Backend A.
6. Send additional requests through Nginx.
7. Verify that Backend B continues responding.
8. Record the result.

### Expected Result
The reverse proxy should continue serving requests through the available backend, subject to the configured upstream failover behavior.

## 2. Backend Recovery

### Procedure
1. Restart Backend A.
2. Verify Backend A is listening on port 3001.
3. Send requests through Nginx.
4. Verify that Backend A becomes available again.

### Expected Result
The recovered backend should become available to Nginx again after it is healthy and the configured failure timeout has elapsed.

## 3. Standby Nginx

### Objective
To test an alternate Nginx reverse proxy host.

### Procedure
1. Configure the standby Nginx server.
2. Start the standby Nginx service.
3. Verify the HTTPS configuration.
4. Test the application through the standby server using the correct hostname.
5. Verify backend connectivity.

## 4. DNS Cutover

### Procedure
1. Record the original application DNS record.
2. Change the DNS record to the standby Nginx IP.
3. Verify the DNS resolution.
4. Flush or wait for relevant client caches.
5. Access the application through HTTPS.
6. Record the result.

### Expected Result
Clients resolving the updated application hostname should be able to access the application through the standby Nginx server, assuming the standby is correctly configured and reachable.

## 5. Conclusion
The failover and recovery tests demonstrate backend service continuity and an alternate reverse proxy entry point.
