export decision=decision66
39.100.79.76
192.168.0.53
export autoVolumes=/root/wym/code/wafer/auto:/exp
export autoPubIp=39.100.79.76
export autoSubIp=39.100.79.76
export autoCpu=13,14,15
export statisVolumes=/home/nano/code/wafer/statis:/exp
export statisPubIp=192.168.0.53
export statisSubIp=192.168.0.53
export statisCpu=0,1,2
export cnnVolumes=/root/wym/code/wafer/cnn:/exp
export cnnPubIp=39.100.79.76
export cnnSubIp=39.100.79.76
export cnnCpu=10,11,12
export ensembleVolumes=/root/wym/code/wafer/ensemble:/exp
export ensembleSubIp=39.100.79.76
export ensembleCpu=8,9
docker-compose -f ../auto.yml up -d
docker-compose -f ../cnn.yml up -d
export decision=decision66
docker-compose -f ../ensemble.yml up -d
export decision=decision66
