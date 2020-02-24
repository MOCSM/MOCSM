import os
import pandas as pd
#
ip=['192.168.0.53','192.168.0.86','192.168.0.190','39.100.79.76']

number=["cloud60"]
#python3 end.py ${number} fault-losso ${sourceSubIp}

#nano,lattop,miniserver,aliyun
#1.43,2.2,3.6,2.5
container=['preprocess','predict']
#wafer

#soureVolumes=['/home/wym/code/waferedgeaidemomqtt/wafersource:/exp','/home/zjq/wym/code/waferedgeaidemomqtt/wafersource:/exp','/home/dns/wym/code/waferedgeaidemomqtt/wafersource:/exp','/root/wym/code/waferedgeaidemomqtt/wafersource:/exp']
volumes=[['/home/nano/code/rul/preprocess:/exp','/home/ljr/code/rul/preprocess:/exp','/home/zjq/wym/code/rul/preprocess:/exp','/root/wym/code/rul/preprocess:/exp'],
['/home/nano/code/rul/predict:/exp','/home/ljr/code/rul/predict:/exp','/home/zjq/wym/code/rul/predict:/exp','/root/wym/code/rul/predict:/exp'],
#['/home/wym/code/rul/storage:/exp','/mnt/d/rul/storage:/exp','/home/zjq/wym/code/rul/storage:/exp','/root/wym/code/rul/storage:/exp'],
]
address=[]
for i in range(0,3):#0,1,2,3
    for j in range(0,3):
        if j==0:
            continue;
        a=[i,j]
        address.append(a)        #
#address.append([3,3])

results=[]
envfileContents=[]
realAddress=[]

demand = {
    0: 3,
    1: 11,
    2: 7,
    3: 23
}
flag=1
for k in range(len(address)):
    flag = 1
    d = {
        0: -1,
        1: -1,
        2: -1,
        3: -1
    }

    content=[]
    #losso的ip
    aourePubIp=ip[address[k][0]]

    content.append(aourePubIp)
    #content.append(sourePubIp)
    for z in range(len(container)):

        volume = "export "+container[z] + "Volumes=" + volumes[z][address[k][z]]
        subip = "export "+container[z] + "SubIp=" + ip[address[k][z]]
        if container[z]=="predict":
            #print("hhhh")
            d[address[k][z]]=d[address[k][z]]+3
            #cpu = "export "+container[z] + "Cpu=" + str(d[address[k][z]])+","+str(d[address[k][z]]-1)+","+str(d[address[k][z]]-2)

            if (int(d[address[k][z]]) <= int(demand[address[k][z]])):
                cpu = "export " + container[z] + "Cpu=" + str(d[address[k][z]]) + "," + str(d[address[k][z]] - 1)+ ","+str(d[address[k][z]] - 2)
            else:
                flag = 0
        else:

           d[address[k][z]] = d[address[k][z]] + 1
        # cpu = "export "+container[z] + "Cpu=" + str(d[address[k][z]])
           if (int(d[address[k][z]]) <= int(demand[address[k][z]])):
             cpu = "export " + container[z] + "Cpu=" + str(d[address[k][z]])
           else:
            flag = 0;
        if z!=len(container)-1:#2

            pubip = "export " + container[z] + "PubIp=" + ip[address[k][z+1]]

            if (flag != 0):
                content.append(volume)
                content.append(pubip)
                content.append(subip)
                content.append(cpu)
           # content.append(cpu)

        else:
            #if (ip[address[k][z]] == "202.117.219.111"):
             #   mongoip = "export mongoIp=192.168.0.101"
            #else:
             #   mongoip = "export mongoIp=" + ip[address[k][z]]
            if (flag != 0):
                content.append(volume)
                content.append(subip)
                content.append(cpu)
               # content.append(mongoip)
                results.append(subip)
    if (flag != 0):
        realAddress.append(address[k])
        envfileContents.append(content)

for i in range(len(realAddress)):
    print(i,realAddress[i])
attribute=['preprocess','predict']
addressPD=pd.DataFrame(columns=attribute,data=realAddress)
addressPD.to_csv("rul-edge-address.csv")

for decisionk in  range(len(realAddress)):
    os.makedirs('decision' + str(decisionk))
    for num in number:
        # python3 end.py ${number} fault-losso ${sourceSubIp}
        filesource = 'decision' + str(decisionk) + "/source"+str(num)+".sh"#
        filesourcedown = 'decision' + str(decisionk) + "/sourcedown" + str(num) + ".sh"
        with open(filesource, 'a+') as f:
            f.write("export number=" + str(num) + '\n')
            f.write("export sourceSubIp=" + envfileContents[decisionk][0] + '\n')
            f.write("docker-compose -f ../end.yml up -d" + '\n')
            f.write("docker-compose -f ../source.yml up -d" + '\n')

        with open(filesourcedown, 'a+') as f:
            f.write("docker-compose -f ../end.yml down" + '\n')
            f.write("docker-compose -f ../source.yml down" + '\n')

    decision=realAddress[decisionk]

    for conk in range(len(decision)):
        device=decision[conk]

        filename='decision' + str(decisionk)+"/device"+str(decisionk)+str(device)+".sh"
        downname='decision' + str(decisionk)+"/down"+str(decisionk)+str(device)+".sh"

        if(os.path.exists(filename)):
            with open(filename, 'a+') as f:
                f.write("docker-compose -f ../"+container[conk] +".yml up -d"+ '\n')
            with open(downname, 'a+') as f:
                f.write("docker-compose -f ../" + container[conk] + ".yml down" + '\n')
            with open(filename, 'a+') as f:
                f.write("export decision=decision" + str(decisionk) + '\n')
        else:
            with open(filename, 'a+') as f:
                f.write("export decision=decision" + str(decisionk) + '\n')
            with open(filename, 'a+') as f:
                for strs in envfileContents[decisionk]:
                    f.write(strs+ '\n')
                f.write("docker-compose -f ../" + container[conk] + ".yml up -d" + '\n')

            with open(downname, 'a+') as f:
                f.write("docker-compose -f ../" + container[conk] + ".yml down" + '\n')












