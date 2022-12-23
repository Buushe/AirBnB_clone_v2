<<<<<<< HEAD
#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
=======
ets up my web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

touch /data/web_static/releases/test/index.html
>>>>>>> d9300d757dec339740964d514bd5966b2aa4deb5
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
<<<<<<< HEAD
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
=======
</html>" >> /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu: /data/

print %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	server_name _;
	add_header X-Served-By $HOSTNAME;
	location /hbnb_static/ {
		alias /data/web_static/current/hbnb_static/;
		index index.html;
	}
}" > /etc/nginx/sites-enabled/default

service nginx restart
>>>>>>> d9300d757dec339740964d514bd5966b2aa4deb5
