export decision=decision62
192.168.0.190
192.168.0.190
export autoVolumes=/home/zjq/wym/code/wafer/auto:/exp
export autoPubIp=192.168.0.86
export autoSubIp=192.168.0.190
export autoCpu=3,4,5
export statisVolumes=/home/zjq/wym/code/wafer/statis:/exp
export statisPubIp=192.168.0.53
export statisSubIp=192.168.0.190
export statisCpu=0,1,2
export cnnVolumes=/home/ljr/code/wafer/cnn:/exp
export cnnPubIp=192.168.0.53
export cnnSubIp=192.168.0.86
export cnnCpu=9,10,11
export ensembleVolumes=/home/nano/code/wafer/ensemble:/exp
export ensembleSubIp=192.168.0.53
export ensembleCpu=1,2
docker-compose -f ../auto.yml up -d
docker-compose -f ../statis.yml up -d
export decision=decision62
