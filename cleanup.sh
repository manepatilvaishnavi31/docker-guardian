#!/bin/bash

docker system prune -f

sudo truncate -s 0 /var/lib/docker/containers/*/*-json.log

echo "Cleanup Completed at $(date)" >> logs/cleanup.log
