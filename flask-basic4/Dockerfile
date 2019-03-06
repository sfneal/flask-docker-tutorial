FROM ubuntu:latest

LABEL maintainer="Stephen Neal <stephen@stephenneal.net>"

# Updating operating system
RUN apt-get update -y

# Installing Python 3.5
RUN apt-get install -y python3-pip python3-dev python3

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Set docker container working directory
WORKDIR /app

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 5000

# Copy source files to container
COPY . /app

# Run app.py at conclusion of build
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]