#! /usr/bin/env bash

helm repo add pinot https://raw.githubusercontent.com/apache/incubator-pinot/master/kubernetes/helm

helm install pinot pinot/pinot \
    -n datastorage \
    --set cluster.name=pinot \
    --set server.replicaCount=2