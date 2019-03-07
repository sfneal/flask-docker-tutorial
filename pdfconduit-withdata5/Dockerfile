# Start from latest ubuntu image
FROM ubuntu:latest
LABEL maintainer="Stephen Neal <stephen@stephenneal.net>"

# Updating operating system
RUN apt-get update

# Install Python and nginx
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN pip3 install --upgrade pip
RUN pip3 install uwsgi

# Install Python package dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Set working directory
RUN mkdir -p /mnt/efs_data
RUN chown -R root:root /mnt/efs_data
VOLUME /mnt/efs_data
WORKDIR /app

# Expose port 5000
EXPOSE 5000

# Copy source files to container
COPY . /app

# Copy nginx config
COPY ./nginx.conf /etc/nginx/sites-enabled/default

# Start nginx servers
CMD service nginx start && uwsgi -s /tmp/uwsgi.sock --chmod-socket=666 --manage-script-name --mount /=app:app

# Run app at the conclusion of build
CMD ["python3", "app.py"]
