FROM ubuntu:latest
COPY openssl.conf /usr/lib/ssl/openssl.cnf 
RUN mkdir /ssl/ && mkdir /ssl/private && mkdir /ssl/certs
RUN cd /ssl/
RUN apt-get update -y
RUN apt-get install openssl -y
RUN cd /ssl/ && openssl req -new -x509 -days 3650 -extensions v3_ca -keyout private/cakey.pem -out certs/cacert.pem -passout pass:"Pomegranate" -subj "/C=GB/ST=Wells/L=Wells/O=NonProductionTestCert/CN=*.example2.com"
RUN touch /ssl/provider-req.pem
RUN apt-get install vim -y
RUN rm -rf /usr/lib/ssl/openssl.cnf
COPY openssl.conf /usr/lib/ssl/openssl.cnf 
RUN touch /ssl/index.txt
RUN echo 0100 > /ssl/serial
RUN mkdir /ssl/newcerts
