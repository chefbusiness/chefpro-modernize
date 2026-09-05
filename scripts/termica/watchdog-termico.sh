#!/bin/zsh
# Vigilante térmico: congela procesos pesados de agentes (python/node/esbuild/grep/rg) por encima de 65 °C y los reanuda por debajo de 60 °C.
LOG=$1; END=$((SECONDS+3600)); typeset -A FROZEN
while [ $SECONDS -lt $END ]; do
  T=$(istats cpu temp | grep -o '[0-9]*\.[0-9]*' | head -1)
  if [ "$(echo "$T >= 66" | bc)" = "1" ]; then
    ps -Ao %cpu,pid,comm | awk '$1>60' | grep -i -E "python|node|esbuild|grep|rg$" | while read cpu pid comm; do
      kill -STOP $pid 2>/dev/null && echo "$(date +%H:%M:%S) $T STOP $pid $comm ($cpu%)" >> $LOG && echo $pid >> $LOG.frozen
    done
  elif [ "$(echo "$T <= 63" | bc)" = "1" ] && [ -s $LOG.frozen ]; then
    for pid in $(sort -u $LOG.frozen); do kill -CONT $pid 2>/dev/null && echo "$(date +%H:%M:%S) $T CONT $pid" >> $LOG; done
    : > $LOG.frozen
  fi
  echo "$(date +%H:%M:%S) $T" >> $LOG.temp
  sleep 5
done
# al terminar, descongela lo que quede
[ -s $LOG.frozen ] && for pid in $(sort -u $LOG.frozen); do kill -CONT $pid 2>/dev/null; done
echo "fin watchdog" >> $LOG
