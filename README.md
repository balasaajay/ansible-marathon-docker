[![Build Status](https://drone.io/github.com/balasaajay/ansible-marathon-docker/status.png)](https://drone.io/github.com/balasaajay/ansible-marathon-docker/latest)

## ansible-marathon
Sample program to deploy docker nginx container, restart existing container and to get the status of running contianers using ansible and Marathon API.

This application pulls latest docker nginx image from docker hub: <https://hub.docker.com/_/nginx/> and **starts container**.

- Command to check **ansible syntax**:  ``ansible-playbook main.yml --syntax-check -i inventory``

- Commands to **execute playbook**:

 1) To restart and get the status of already running applications use:  ``ansible-playbook -v main.yml -i inventory  --tags test-restart``

 2) To start nginx contianer: ``ansible-playbook -v main.yml -i inventory  --tags nginx``
