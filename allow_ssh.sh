#!/bin/bash

ssh-keygen -f "/home/asadiakhou/.ssh/known_hosts" -R "172.168.2.5"
ssh-keygen -f "/home/asadiakhou/.ssh/known_hosts" -R "172.168.2.6"

ssh-keyscan -H 172.168.2.5 >> ~/.ssh/known_hosts
ssh-keyscan -H 172.168.2.6 >> ~/.ssh/known_hosts