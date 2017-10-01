#!/bin/bash

nvidia-settings -a '[gpu:0]/GPUGraphicsClockOffset[3]=170'
nvidia-settings -a '[gpu:0]/GPUMemoryTransferRateOffset[3]=1300' #max 1400, and as this GPU is the main one, lets put it a bit less than others.
nvidia-settings -a '[gpu:0]/GPUPowerMizerMode=1'
nvidia-settings -a '[gpu:0]/GPUFanControlState=1'
nvidia-settings -a '[fan:0]/GPUTargetFanSpeed=90'
nvidia-smi -i 0 -pl 166 #max 170, don't go higher please

nvidia-settings -a '[gpu:1]/GPUGraphicsClockOffset[3]=180'
nvidia-settings -a '[gpu:1]/GPUMemoryTransferRateOffset[3]=1400' #max 1400, don't go higher please
nvidia-settings -a '[gpu:1]/GPUPowerMizerMode=1'
nvidia-settings -a '[gpu:1]/GPUFanControlState=1'
nvidia-settings -a '[fan:1]/GPUTargetFanSpeed=90'
nvidia-smi -i 1 -pl 166 #max 170, don't go higher please

#Strix gtx 1070 OC edition
nvidia-settings -a '[gpu:2]/GPUGraphicsClockOffset[3]=150' #OC edition clock offset is less than ordinary Gameing edition
nvidia-settings -a '[gpu:2]/GPUMemoryTransferRateOffset[3]=1400' #max 1400, don't go higher please
nvidia-settings -a '[gpu:2]/GPUPowerMizerMode=1'
nvidia-settings -a '[gpu:2]/GPUFanControlState=1'
nvidia-settings -a '[fan:2]/GPUTargetFanSpeed=90'
nvidia-smi -i 2 -pl 190 #max 200, don't go higher please

nvidia-settings -a '[gpu:3]/GPUGraphicsClockOffset[3]=180'
nvidia-settings -a '[gpu:3]/GPUMemoryTransferRateOffset[3]=1400' #max 1400, don't go higher please
nvidia-settings -a '[gpu:3]/GPUPowerMizerMode=1'
nvidia-settings -a '[gpu:3]/GPUFanControlState=1'
nvidia-settings -a '[fan:3]/GPUTargetFanSpeed=90'
nvidia-smi -i 3 -pl 166 #max 170, don't go higher please

nvidia-settings -a '[gpu:4]/GPUGraphicsClockOffset[3]=180'
nvidia-settings -a '[gpu:4]/GPUMemoryTransferRateOffset[3]=1400' #max 1400, don't go higher please
nvidia-settings -a '[gpu:4]/GPUPowerMizerMode=1'
nvidia-settings -a '[gpu:4]/GPUFanControlState=1'
nvidia-settings -a '[fan:4]/GPUTargetFanSpeed=90'
nvidia-smi -i 4 -pl 166 #max 170, don't go higher please

nvidia-settings -a '[gpu:5]/GPUGraphicsClockOffset[3]=180'
nvidia-settings -a '[gpu:5]/GPUMemoryTransferRateOffset[3]=1400' #max 1400, don't go higher please
nvidia-settings -a '[gpu:5]/GPUPowerMizerMode=1'
nvidia-settings -a '[gpu:5]/GPUFanControlState=1'
nvidia-settings -a '[fan:5]/GPUTargetFanSpeed=90'
nvidia-smi -i 5 -pl 166 #max 170, don't go higher please

#On Linux, you can set GPUs to persistence mode to keep the NVIDIA driver loaded even when no applications are accessing the cards. This is particularly useful when you have a series of short jobs running. Persistence mode uses more power, but prevents the fairly long delays that occur each time a GPU application is started. It is also necessary if you’ve assigned specific clock speeds or power limits to the GPUs (as those changes are lost when the NVIDIA driver is unloaded). Enable persistence mode on all GPUS by running:
nvidia-smi -pm 1

#Check powers on each GPU, 0 is the GPU id
#nvidia-smi -i 0 -q -d POWER

#Set power limit for all GPUs
#sudo nvidia-smi -pl 166

export GPU_FORCE_64BIT_PTR=0
export GPU_MAX_HEAP_SIZE=100
export GPU_USE_SYNC_OBJECTS=1
export GPU_SINGLE_ALLOC_PERCENT=100
export GPU_MAX_ALLOC_PERCENT=100
