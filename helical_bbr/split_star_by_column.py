import sys

def main():
    with open(sys.argv[1],'r') as f:
        infile=f.readlines()
        #print(get_metadata(infile))
        outfile=[]
        name1=""
        coor_header=["\n","data_\n","\n","loop_\n","_rlnCoordinateX #1\n","_rlnCoordinateY #2\n"]

        for i in range(len(get_metadata(infile)),len(infile)):
            if infile[i] == "":
                continue    # skip empty line
            line=infile[i].split("\n")[0].split() # list
            #print(line)
            name2=line[COL_mic-1]
            if name1 == "" : #first file
                name1 = name2

            if name1 == name2 :
                outfile.append(line[COL_coordx-1]+"\t"+line[COL_coordy-1]+"\n")
            elif name1 != name2 :
                write_star(name1.split(".")[0]+"_warppicking.star", coor_header, outfile)
                #with open(name1.split(".")[0]+"_warppicking.star","w") as k:
                #    k.write("\ndata_\n\nloop_\n_rlnCoordinateX #1\n_rlnCoordinateY #2\n")
                #    k.writelines(outfile)
                name1=name2
                outfile=[line[COL_coordx-1]+"\t"+line[COL_coordy-1]+"\n",]
        write_star(name1.split(".")[0]+"_warppicking.star", coor_header, outfile)    # write last



def write_star(name, head, body):
    with open(name ,'w') as f:
        f.writelines(head)
        f.writelines(body)



def get_metadata(inputstar):
    metadata=[]
    end=0
    for i in range(len(inputstar)):
        line=inputstar[i]
        metadata.append(line)
        if "_rln" in line:
            end=i

        if "_rlnMicrographName" in line:
            global COL_mic
            COL_mic = int(line.split("#")[1])
        if "_rlnCoordinateX" in line:
            global COL_coordx
            COL_coordx = int(line.split("#")[1])
        if "_rlnCoordinateY" in line:
            global COL_coordy
            COL_coordy = int(line.split("#")[1])
    return(metadata[:end+1])

if __name__ == "__main__":
    main()

