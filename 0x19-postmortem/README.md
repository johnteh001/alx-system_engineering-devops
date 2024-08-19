Postmortem: Web Application Outage

Issue Summary
Duration: August 12, 2024, from 14:00 to 15:30 UTC (1 hour 30 minutes).
Impact: 85% of users experienced 502 errors, unable to access the web app.
Root Cause: Nginx server misconfiguration; worker-connections set too low, causing memory exhaustion and server crashes.

Timeline
14:00 UTC: Issue detected by monitoring system (502 errors).
14:05 UTC: On-call engineer confirmed the outage.
14:10 UTC: Initial focus on load balancer—no issues found.
14:30 UTC: Backend API checked—operating normally.
14:45 UTC: High memory usage on Nginx server identified.
15:00 UTC: Nginx worker-connections increased and servers restarted.
15:30 UTC: Service fully restored.

Root Cause and Resolution
Root Cause: Nginx couldn’t handle traffic due to low worker-connections, causing memory crashes.
Resolution: Increased worker-connections and worker-rlimit-nofile, then restarted servers.

Preventative Measures
Configuration Review: Optimize server settings.
Enhanced Monitoring: Add alerts for memory usage and connection limits.
Regular Load Testing: Simulate traffic to identify potential issues.
Team Training: Improve Nginx troubleshooting skills.

