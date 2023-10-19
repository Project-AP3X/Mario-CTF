FROM kaminskypavel/mario 

# Install utilities
RUN apt-get update && apt-get install -y python3 nano curl inetutils-inetd inetutils-telnetd telnet iputils-ping nano expect

WORKDIR /app

# Copy necessary files and flags into the app
COPY entrypoint.sh /app
COPY . /app
COPY index.html /app/
COPY FullScreenMario-0.10.1.min.js /app/ 

# This script runs the automated telnet
RUN chmod +x /app/entrypoint.sh
CMD ["/bin/bash","-c","/app/entrypoint.sh & python3 -m http.server --bind 192.168.25.130 80"]
