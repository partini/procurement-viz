# Visualizing Procurement Data of Serbia
A prototype on procurement visualizations

# Technical Instructions
### 1. Server Installation
#### Environment
- Ubuntu 16.04 LTS 64 bit
- MongoDB 3.2.x
- Apache Virtual Hosts (httpd)

#### Initial Setup
Apache Virtual Host:
```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
```

Installing Python Dev libs:
```
sudo apt-get install python-dev
```

Move to WWW folder:
```
cd /var/www
```

Clone the project:
```
git clone https://github.com/partini/procurement-viz.git
cd procurement-viz
```

Install project dependencies:
```
sudo bash install.sh
```

Make a copy of the wsgi template file and edit it with root privileges:
```
cp app-template.wsgi app.wsgi
sudo nano app.wsgi
```

And configure the project's path:
```
app_dir_path = '/var/www/procurement-viz'
```

Create and edit project config file:
```
sudo cp config-template.cfg config.cfg
sudo nano config.cfg
```


#### Create New Virtual Host
Copy default virtual host config file to create new file specific to the project:
```
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/procurement-viz.conf
```

Open the new file in your editor with root privileges:
```
sudo nano /etc/apache2/sites-available/procurement-viz.conf
```

And configure it to point to the project's app.wsgi file:
```
<VirtualHost *:80>
  ServerAdmin admin@localhost
  ServerName IPADDRESS

  WSGIScriptAlias / /var/www/procurement-viz/app.wsgi
  <Directory /var/www/procurement-viz>
    Order allow,deny
    Allow from all
  </Directory>

  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

#### Enable New Virtual Host
First disable the defaul one:
```
sudo a2dissite 000-default.conf
```

Then enable the new one we just created:
```
sudo a2ensite procurement-viz.conf
```

Restart the server for these changes to take effect:
```
sudo service apache2 restart
```


### 2. Local Installation (UBUNTU)


First create a folder in your desktop called dev:
```
cd ~
mkdir dev
cd dev
```

Getting the project in your local machine:
```
git clone https://github.com/partini/procurement-viz.git
cd procurement-viz
```

Install and run the app:
```
bash install.sh
bash run-debug.sh
```
### 3. Installing MongoDB
Step 1 — Adding the MongoDB Repository
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

```
Issue the following command to create a list file for MongoDB.
```
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
```
After adding the repository details, we need to update the packages list.
```
sudo apt-get update
```

Step 2 — Installing and Verifying MongoDB

```
sudo apt-get install -y mongodb-org
```

Step 3 - Running MongoDB

```
sudo service mongod start
```
### 4. Run the importers
```
bash import.sh
```


### 5. Getting an error? How do I debug?

First thing you should do is to try having a look at error logs.

The most common error log if you are running this app on a server is to have a look at apache2 error logs.

Issue the following command in terminal to get the error logs:

```
sudo tail -f /var/log/apache2/error.log
```

There is also a logs folder in the flask app itself where you can find traces of errors.
