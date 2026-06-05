#!/bin/bash

LOGFILE="logs/monitor.log"
mkdir -p logs

echo "===== $(date) =====" >> $LOGFILE

docker stats --no-stream --format "{{.Name}} {{.CPUPerc}} {{.MemPerc}}" | while read name cpu mem
do
    cpu_val=$(echo $cpu | tr -d '%')
    mem_val=$(echo $mem | tr -d '%')

    echo "$name CPU:$cpu MEM:$mem" >> $LOGFILE

    cpu_int=${cpu_val%.*}
    mem_int=${mem_val%.*}

    if [ "$cpu_int" -gt 80 ] || [ "$mem_int" -gt 80 ]; then
        python3 alert.py "$name High Resource Usage"
    fi
done

bash healer.sh
