## ansible-marathon
Sample program to deploy docker nginx container using ansible and Marathon API.

This application pulls latest docker nginx image from docker hub: <https://hub.docker.com/_/nginx/> and **starts nginx container**.

- Command to check **ansible syntax**:  ``ansible-playbook main.yml --syntax-check``

- Command to **execute playbook**:  ``ansible-playbook -v main.yml -i inventory``
