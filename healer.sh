#!/bin/bash

docker ps -a --format "{{.Names}} {{.Status}}" | while read name status
do
    if [[ "$status" == Exited* ]]; then
        docker restart $name
        python3 alert.py "$name Restarted Automatically"
    fi
done
