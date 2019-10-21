#!/usr/bin/env bash


ENFFILE=env 

ENVLINE=`cat ${ENFFILE}`
for i in ${ENVLINE}; do
  realenv=${i}
  sed -i "s/((${realenv}))/${i}/g" ${WORKSPACE}/deploy/deploy.yaml
done 
