FROM alpine:latest
RUN apk --update add postgresql-client
ADD ./fill_db.sh /opt/scripts/fill_db.sh
RUN chmod +x /opt/scripts/fill_db.sh
ENTRYPOINT ["sh", "/opt/scripts/fill_db.sh"]