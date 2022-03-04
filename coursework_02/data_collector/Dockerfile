FROM debian:buster

RUN apt-get update && apt-get -y install cron ssh

# copy the ssh keys
COPY ssh/id_rsa /root/.ssh/id_rsa
COPY ssh/id_rsa.pub /root/.ssh/id_rsa.pub
COPY ssh/known_hosts /root/.ssh/known_hosts

RUN chmod 600 /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa.pub

# copy the bandwidth collector script
COPY bandwidth-collector /root/bandwidth-collector
RUN chmod 0744 /root/bandwidth-collector

# Copy bandwidth-cron file to the cron.d directory
COPY bandwidth-cron /etc/cron.d/bandwidth-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/bandwidth-cron

# Apply cron job
RUN crontab /etc/cron.d/bandwidth-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log