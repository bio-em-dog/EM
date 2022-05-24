# 2022.05.24
# python join_jspr.py <hostname>
# !/usr/bin/env python3
import sys
import os
import time


if len(sys.argv) == 2:
    host = sys.argv[1]



runlist=(1,2,3,4,5,11,12,21,22,23,24,25,26,27,31,32,33,34,35,36)
# runpar: host_iteration_runp em7_12_runp
# orientation-center.32.0.lst
# runpar.12.ortcen.txt

def stop():
    runpar_pid = [i.strip() for i in os.popen("ps -aux | grep '"+host+"_.*_runp proc="+str(PROC)+"' | awk {'print $2'}")]
    for i in runpar_pid:
        os.system("kill "+i)
    return(0)

def watch(host, iteration):
    with open(host+"_"+str(iteration)+"_runp",'r') as f:
        runp=[i.split()[3] for i in f.readlines()]
    total_command=len(runp)+0.1-0.1
    while 1:
        if os.path.exists(host+"_"+str(iteration)+"_runp"):
            donelst = [i.strip() for i in os.popen("ls orientation-center."+str(iteration)+".*.lst").readlines() if i.strip() in runp]
            print("%.2f %% done"%(len(donelst)/total_command*100))
        elif not os.path.exists(host+"_"+str(iteration)+"_runp"):
            stop()
            print("Exit by delet runpar file")
            return(0)
        elif os.path.exists("orientation-center."+str(i)+".lst"):
            stop()
            print("Exit, over run")
            return(0)
        time.sleep(120)


def genRunparFile(host, iteration):
    # read config
    global PROC
    host_lst = []
    local_speed=0
    all_speed=0
    with open("multi_runpar.cofig",'r') as f:
        for i in f.readlines():
            if i.strip() == "" or "#" in i:
                continue
            line=i.strip().split()
            host_lst.append("line[0]")
            if line[0] == host:
                PROC = int(line[3])
                local_speed = float(line[1])*int(line[3])/int(line[2])
            all_speed += float(line[1])*int(line[3])/int(line[2]) 

    # read all jalign command
    with open("runpar."+str(iteration)+".ortcen.txt",'r') as f:
        all_command = [i for i in f.readlines() if not (i=='' or "#" in i)]
    # done lst
    donelst = [i.strip() for i in os.popen("ls orientation-center."+str(iteration)+".*.lst").readlines()]
    # quened lst
    quenedlst = []
    for h in host_lst:
        if os.path.exists(h+"_"+str(iteration)+"_runp"):
            with open(h+"_"+str(iteration)+"_runp") as f:
                quenedlst += [i.split()[3] for i in f.readlines() if not (i=='' or "#" in i)]
    
    # unprocessed list
    unprolist=[]
    for index,command in enumerate(all_command[::-1]):
        if command.split()[3] in (donelst + quenedlst):
            continue
        else:
            unprolist.append(command)
    
    # output runpar
    with open(host+"_"+str(iteration)+"_runp",'w') as f:
        f.writelines(unprolist[:int(local_speed/all_speed*len(unprolist))])


if __name__ == "__main__":
    try:
        while 1:
            for i in runlist:
                if os.path.exists("runpar."+str(i)+".ortcen.txt") and os.path.exists("orientation-center."+str(i)+".lst"):
                    print("run %s finished"%(i))
                elif os.path.exists("runpar."+str(i)+".ortcen.txt") and not os.path.exists("orientation-center."+str(i)+".lst"):
                    genRunparFile(host, i)
                    os.popen("runpar file="+host+"_"+str(i)+"_runp proc="+str(PROC)+" &")
                    print("running run %s "%(i))
                    watch(host,i)
            time.sleep(300)
    except KeyboardInterrupt:
        stop()
        exit(0)

