#!/bin/sh

DIR_TO_COPY="./notebooks"

for var in "$@"
do
      echo "Copying $DIR_TO_COPY to $var ..."
      cp -rf $DIR_TO_COPY "/root/datascience/master/$var"
done