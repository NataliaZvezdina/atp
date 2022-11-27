## Project Overview

The automation should be implemented using `Ansible` for configuring several operating systems:

- Ubuntu 22.04
- Centos 7
- Arch Linux

The configuration should be done as a `role`.

---

Tasks to perform:

1. Install `nginx`
2. Change nginx configuration in such a way as to get file contents `/opt/service_state` by request `GET /service_data`
3. Locate file `/opt/service_state` consisting of 2 lines:

> Seems work
> 
> Service uptime is 0 minutes

4. Enable `nginx` to be launched
5. Add the cron job to execute once per minute:
> sed -i "s/is .*$/is $(($(ps -o etimes= -p $(cat /var/run/nginx.pid)) / 60)) minutes/" /opt/service_state

6. Verify that the uptime value in the `/opt/service_state` file has started to change
---

#### Notes:

Ansible configuration must be idempotent.

