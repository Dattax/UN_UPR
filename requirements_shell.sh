apt-get -qqy update
apt-get -qqy install python-virtualenv
apt-get -qqy install python-setuptools
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip
pip install bleach
pip install oauth2client
pip install requests
pip install httplib2
pip install redis
pip install passlib
pip install itsdangerous
pip install flask-httpauth
pip install bcrypt
pip install flask-sqlalchemy
pip install flask-login
pip install flask-wtf
pip install uwsgi
su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb'