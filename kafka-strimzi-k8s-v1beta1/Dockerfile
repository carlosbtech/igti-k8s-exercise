# kafka version = 2.7 [latest]
# https://www.confluent.io/hub/confluentinc/kafka-connect-jdbc
# get image from strimzi repository
# https://quay.io/repository/strimzi/kafka

FROM quay.io/strimzi/kafka:latest-kafka-2.7.0
MAINTAINER Carlos Barbosa <carlos.barbosa@a3data.com.br>

# using root user
USER root:root

# create dirs
RUN mkdir -p /opt/kafka/plugins/kafka-connect-jdbc

# copy jar files
COPY ./jars/ /opt/kafka/plugins/kafka-connect-jdbc/