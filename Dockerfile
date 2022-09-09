FROM ubuntu:bionic

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8

RUN apt-get update && apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa 
RUN apt-get update && apt-get install -y \
    # std libs
    git less nano curl \
    ca-certificates \
    wget build-essential\
    # python basic libs
    python3.9 python3.9-dev python3.9-venv python3-pip gettext \
    # geodjango
    gdal-bin binutils libproj-dev libgdal-dev \
    # postgresql
    libpq-dev postgresql-client && \
    apt-get clean all && rm -rf /var/apt/lists/* && rm -rf /var/cache/apt/*

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src
COPY . /opt/services/djangoapp/src
RUN rm -rf /opt/services/djangoapp/src/venv
RUN chmod +x entrypoint.sh

# install our two dependencies
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip
RUN pip3 install django
RUN pip3 install djangorestframework-gis
RUN pip3 install psycopg2
RUN pip3 install tensorflow
RUN pip3 install tensorflow-text
RUN pip3 install gunicorn

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--limit-request-line", "0", "vocus.wsgi:application"]
ENTRYPOINT ["sh",  "entrypoint.sh" ]