export number=25
export sourceSubIp1=192.168.0.190
export sourceSubIp2=192.168.0.53
docker-compose -f ../end.yml up -d
docker-compose -f ../source.yml up -d
