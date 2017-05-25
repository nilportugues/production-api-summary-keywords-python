FROM ubuntu:16.04
LABEL Description="A container for the production hosting of a flask application"

RUN apt-get update && apt-get upgrade -y

# Install nginx
RUN apt-get install -y nginx

## Python 2.7 installation and required packages
RUN apt-get install libterm-readline-perl-perl apt-utils -y
RUN apt-get install -y python python-pip python3-virtualenv mlocate

## For this project DEPENDENCIES
RUN apt-get install -y cython libblas-dev liblapack-dev gfortran python-numpy python-scipy \
    python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

RUN pip install --upgrade pip
RUN pip install flask uwsgi


COPY ./summarize_api-0.1.tar.gz /tmp/build.tar.gz
RUN pip install /tmp/build.tar.gz --upgrade

## Copy files for uwsgi
RUN mkdir -p /opt/uwsgi/
COPY ./uwsgi/uwsgi.ini /opt/uwsgi/uwsgi.ini
COPY ./uwsgi/app.wsgi /var/www/app.wsgi

## Copy files for nginx
COPY ./nginx/conf/app.conf /etc/nginx/sites-enabled/app.conf
RUN rm /etc/nginx/sites-enabled/default

# Exposed ports
EXPOSE 80

## Copy over the entrypoint
COPY ./entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
