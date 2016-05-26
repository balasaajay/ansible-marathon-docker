#! /usr/bin/env python
# -*- coding: utf-8 -*-
# syntax check for an ansible yaml
import yaml
import sys

try:
    playbook = yaml.load(open('main.yml','r')) # Update with path to your playbook
except:
    print "Error loading the ansible-playbook, must be a yaml syntax problem"
    sys.exit(1)
else:
    print "YAML syntax looks good."
