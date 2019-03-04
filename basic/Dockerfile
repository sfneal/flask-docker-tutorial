FROM ubuntu:latest

LABEL maintainer="Stephen Neal <stephen@stephenneal.net>"

# Installing Python 3.5
RUN apt-get update -y && apt-get install -y python3-pip python3-dev python3

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]