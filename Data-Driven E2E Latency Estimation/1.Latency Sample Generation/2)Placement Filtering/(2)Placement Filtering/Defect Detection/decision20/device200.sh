export decision=decision20
192.168.0.86
192.168.0.86
export autoVolumes=/home/ljr/code/wafer/auto:/exp
export autoPubIp=192.168.0.53
export autoSubIp=192.168.0.86
export autoCpu=9,10,11
export statisVolumes=/home/ljr/code/wafer/statis:/exp
export statisPubIp=192.168.0.53
export statisSubIp=192.168.0.86
export statisCpu=6,7,8
export cnnVolumes=/home/nano/code/wafer/cnn:/exp
export cnnPubIp=192.168.0.86
export cnnSubIp=192.168.0.53
export cnnCpu=0,1,2
export ensembleVolumes=/home/ljr/code/wafer/ensemble:/exp
export ensembleSubIp=192.168.0.86
export ensembleCpu=4,5
docker-compose -f ../cnn.yml up -d
export svmVolumes=/home/nano/code/wafer/svm:/exp
export svmSubIp=192.168.0.53
export svmPubIp=192.168.0.86
export svmCpu=3
docker-compose -f ../svm.yml up -d
