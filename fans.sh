#!/bin/bash

#export DISPLAY=:0

NUM_CARDS=6
NS="/usr/bin/nvidia-settings"

while true
do
for ((i=0; i<$NUM_CARDS; i++))
{
	GPU_TEMP=`nvidia-smi -i $i --query-gpu=temperature.gpu --format=csv,noheader`
	FAN_SPEED=`nvidia-smi -i $i --query-gpu=fan.speed --format=csv,noheader,nounits`
	if (($GPU_TEMP > 60)); then
		$NS -a [gpu:$i]/GPUFanControlState=1 -a [fan:$i]/GPUTargetFanSpeed=100 > /dev/null 2>&1
	fi

	if (($GPU_TEMP < 60)); then
		(($GPU_TEMP!=$(($FAN_SPEED-10)))) && $NS -a [gpu:$i]/GPUFanControlState=1 -a [fan:$i]/GPUTargetFanSpeed=$(($GPU_TEMP + 20)) > /dev/null 2>&1
	fi
}
sleep 5
done
