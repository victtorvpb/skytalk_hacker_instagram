FROM python:3.7.2-slim-stretch

### define env and args
ENV PYTHONUNBUFFERED 1

### add code
COPY . /code
WORKDIR /code


RUN apt update
RUN apt-get -y install build-essential git


### clean pyc and file caches
RUN find /code -name '*.pyc' -delete
RUN find /code -name '*__pycache__' -delete

### upgrade pip
RUN pip install -U pip


# ### install requirements
RUN pip install -r requirements.txt
RUN pip install git+https://git@github.com/ping/instagram_private_api.git@1.6.0
