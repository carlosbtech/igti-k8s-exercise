#! /usr/bin/env bash

helm repo add strimzi https://strimzi.io/charts/

helm install kafka strimzi/strimzi-kafka-operator --namespace ingestion --version 0.22.0