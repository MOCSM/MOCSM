export decision=decision46
192.168.0.190
192.168.0.53
export autoVolumes=/home/zjq/wym/code/wafer/auto:/exp
export autoPubIp=192.168.0.190
export autoSubIp=192.168.0.190
export autoCpu=3,4,5
export statisVolumes=/home/nano/code/wafer/statis:/exp
export statisPubIp=192.168.0.53
export statisSubIp=192.168.0.53
export statisCpu=0,1,2
export cnnVolumes=/home/zjq/wym/code/wafer/cnn:/exp
export cnnPubIp=192.168.0.86
export cnnSubIp=192.168.0.190
export cnnCpu=0,1,2
export ensembleVolumes=/home/ljr/code/wafer/ensemble:/exp
export ensembleSubIp=192.168.0.86
export ensembleCpu=10,11
docker-compose -f ../auto.yml up -d
docker-compose -f ../cnn.yml up -d
export decision=decision46
