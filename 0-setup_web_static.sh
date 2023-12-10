#!/usr/bin/env bash

# Update and install nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create directory structure and test HTML filie

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

echo "<html>
    <head></head>
    <body>Holberton School</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership
sudo chown -R ubuntu:ubuntu /data/

# Check if location block exists before appending
if ! sudo grep -q 'location /hbnb_static {' /etc/nginx/sites-enabled/default; then
    sudo sed -i '/listen 80 default_server/ a\location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
fi

# Restart nginx
sudo service nginx restart

