sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/gunicorn
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'admin'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('pass111')"
mysql -uroot -e "CREATE DATABASE mybase"
mysql -uroot -e "GRANT ALL ON mybase.* TO 'admin'@'localhost'"


cd  /home/box/web/ask/
sudo python manage.py syncdb
