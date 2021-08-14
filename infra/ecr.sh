#! /usr/bin/env bash

aws ecr create-repository \
    --repository-name igti-repository \
    --image-scanning-configuration scanOnPush=true \
    --region us-east-2