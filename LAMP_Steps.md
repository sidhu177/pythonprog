This markdown is for the steps to set up the LAMP stack using AWS Centos. This file is for the setting up of Apache, Php and Mysql following which will be installation of Drupal. It is assumed that the Ec2 and the RDS are setup with the base requirements.

sudo su

yum update

yum install wget

yum install zip

yum install unzip

yum install httpd

systemctl start httpd.service

systemctl enable httpd.service

yum install mariadb-server mariadb

systemctl start mariadb

systemctl enable mariadb.service

yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm

yum install yum-utils

yum-config-manager --enable remi-php70

yum install php php-mcrypt php-cli php-gd php-curl php-mysql php-ldap php-zip php-fileinfo php-dom

systemctl restart httpd.service

cd /var/www/html

wget https://ftp.drupal.org/files/projects/thunder-8.x-2.20-core.tar.gz

tar -xf thunder-8.x-2.20-core.tar.gz

chmod 777 -R thunder-8.x-2.20-core

cd thunder-8.x-2.20-core

mv * ..

cd ..

cd sites

cd default

cp default.settings.php settings.php

mkdir files

chmod 777 *

chcon -R -t httpd_sys_content_rw_t /var/www/html/sites/

SELinux could cause a problem in EC2 to RDS connection, if the commandline connection to RDS succeeds and the GUI web to Database connection fails, then the reason is most likely to be SELinux. The way to avoid this is to set SELinux to permissive as opposed to enforcing-which is the default. you will find SELinux hosts file in /etc/SELinux.


