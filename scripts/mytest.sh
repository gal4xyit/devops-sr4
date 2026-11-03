#!/usr/bin/env bash
set -euo pipefail

while true; do
    printf '%s mytest heartbeat\n' "$(date --iso-8601=seconds)" | tee -a /tmp/test.log
    sleep 60
done
