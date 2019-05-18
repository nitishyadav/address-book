#!/bin/bash

# this script is tested for ubuntu and it will install Jenkins with docker enabled to be used by Jenkins user

# This will install docker as a container
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
apt-get update
apt-get install -y docker-engine
#enable Docker
systemctl enable docker
systemctl start docker
usermod -aG docker ubuntu

# Steps to run jenkins
mkdir -p /var/jenkins_home
chown -R 1000:1000 /var/jenkins_home/
docker run -p 8080:8080 -p 50000:50000 -v /var/jenkins_home:/var/jenkins_home -d --name jenkins jenkins/jenkins:lts

# To show endpoint
echo 'Jenkins has been successfully installed'
echo 'Access jenkins at: http://'$(curl -s ifconfig.co)':8080'
