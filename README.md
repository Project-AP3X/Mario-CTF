### Capture The Flag (CTF) - Super Mario Theme
This project is a Capture The Flag (CTF) scenario that involves a Super Mario theme. It leverages Docker, JavaScript, and networking principles to create an engaging challenge. In this CTF, participants will explore various objectives to uncover flags hidden within the Mario-themed environment.

### Obtaining Credentials

Location
Packet Capture in network LAN segment

Path
Use a packet sniffer (e.g., Wireshark) to capture Telnet traffic between the client (supermario) and the server (marioweb).

Notes:
A developer (automated script) connects via Telnet to the marioweb and retrieves a file named "mario_notes.conf." This file contains configuration details, URL information, and change log notes from the developers of a Mario Game adaptation. There are several credentials leaked in this packet capture.

### Reconnaissance Objectives
Wireshark Packet Capture

Listen to all the traffic within the created network
Obtain unencrypted Telnet traffic
Results: Credentials for Website
NMAP Network and Port Scan

Identify open ports for available hosts
Identify software and hardware of hosts
Results: Identification of two websites (HTTP)

### Infiltration Objectives
Data Analysis (Follow the Breadcrumbs)

Nmap results show open ports; access websites (FLAG3)
Visit open ports and find base64 encoded data (FLAG1)
Telnet credentials provide access to websites (FLAG2)
Steganography attack reveals encoded data (FLAG4)
Brute Force Attack

Use marioweb credentials to attempt a login to the website (FLAG2)
Gain access to supermario website (FLAG3)
Play the Game! Find all the FLAGS!


#### Flag 1 - JavaScript Message

Location: MarioWeb
Container: marioweb
URL: marioweb.netsec-docker.isi.jhu.edu
Path: Successful login to the website and decode base64 embedded message on the welcome page. (Inspect the webpage)

#### Flag 2 - Static HTML Message
Location: MarioWeb
Container: marioweb
URL: marioweb.netsec-docker.isi.jhu.edu
Path: Play the game and obtain a score <7 to reveal a base64 encoded message

#### Flag 3 - Super Mario Game
Location: Super Mario Game
Container: supermario
URL: supermario.netsec-docker.isi.jhu.edu
Path: Hover over the "Editor" Menu to find the text string

#### Flag 4 - Steganography
Location: MarioWeb
Container: marioweb
URL: marioweb.netsec-docker.isi.jhu.edu/static/images/mario-back.png
Path: Successful login to the website, save the image to the local host, and use a Python script to reveal the flag.


Have fun exploring the Super Mario-themed CTF challenge and finding all the hidden flags!




