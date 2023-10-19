# Description:
#   This runtime environment example Dockerfile creates a container with a telnet server and a ssh server
# Usage:
#   From this directory, run $ docker build -t ttermsvr .
#   By default, runs as root
# this container was modified to support a custom website. 
# https://www.gnu.org/software/inetutils/
# https://ubuntu.com/server/docs/service-openssh

FROM ubuntu:latest

#https://grigorkh.medium.com/fix-tzdata-hangs-docker-image-build-cdb52cc3360d
ENV TZ=US/Eastern
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#avoid question/dialog during apt-get installs
ARG DEBIAN_FRONTEND noninteractive

# Setup container's ENV for systemd
ENV container docker

#update
RUN apt-get update

#install utilities
RUN apt-get install apt-utils dpkg-dev debconf debconf-utils -y
RUN apt-get install net-tools iputils-ping iptables iproute2 wget nmap bind9-dnsutils dnsutils inetutils-traceroute openssh-server isc-dhcp-common -y
RUN apt-get install vim acl sudo telnet ssh netcat nano nfs-common -y

#install dependencies for systemd and syslog
RUN apt-get install systemd systemd-sysv syslog-ng syslog-ng-core syslog-ng-mod-sql syslog-ng-mod-mongodb -y
VOLUME [ "/tmp", "/run", "/run/lock" ]
# Remove unnecessary units
RUN rm -f /lib/systemd/system/multi-user.target.wants/* \
  /etc/systemd/system/*.wants/* \
  /lib/systemd/system/local-fs.target.wants/* \
  /lib/systemd/system/sockets.target.wants/*udev* \
  /lib/systemd/system/sockets.target.wants/*initctl* \
  /lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup* \
  /lib/systemd/system/systemd-update-utmp*
#start systemd
CMD [ "/lib/systemd/systemd", "log-level=info", "unit=sysinit.target" ]

#install all the things (inetutils-inetd, openssh-server)
RUN apt-get install inetutils-inetd inetutils-telnetd -y
RUN apt-get install openssh-server -y

COPY etc_ssh_sshd_config /etc/ssh/sshd_config
COPY etc_inetd.conf /etc/inetd.conf

#create a user student with password nwsec
RUN useradd -m bowser
RUN echo 'bowser:goombaMask' | chpasswd

# Install website utilities and set environment
RUN apt-get install python3-pip curl inetutils-inetd inetutils-telnetd openssh-server telnet iputils-ping nano -y
RUN mkdir -p /home/admin/mario
COPY mario_notes.conf /home/bowser/
# Copy marioweb 
# Creator of website: v4run.academics@gmail.com
COPY requirements.txt requirements.txt
COPY mario /home/admin/mario
COPY instance /home/admin


RUN pip install waitress
RUN pip install -r requirements.txt

WORKDIR /home/admin/
CMD ["waitress-serve", "--listen=192.168.25.131:80","--call", "mario:create_app"]
