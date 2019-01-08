FROM ubuntu:latest

# Install Pip
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y cron

# Install and configure python packages
RUN pip3 install pyhkconnect
RUN pip3 install redis

# Copy python app
ADD ./price.py /
ADD ./hold.py /
ADD ./echo.sh /

RUN chmod +x /*.py
RUN chmod +x /echo.sh

# Add crontab file in the cron directory
ADD cronfile /etc/cron.d/simple-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/simple-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log