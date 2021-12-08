# python3
# -*-conding:utf-8-*-

def main():
    InputStar = open("h1w_exp.star","r").readlines()



    metadata=get_metadata(InputStar)
    # print metadata
    print(COL_img, COL_mic, COL_optgp, COL_coordx, COL_coordy, COL_defu, COL_defv, COL_defa)
    print(COL_rot, COL_tilt, COL_psi, COL_oxa, COL_oya)
    #print(COL_ox, COL_oy)


def get_metadata(inputstar):  # 剥离metadata部分, 获得每个label的列数
    metadata=[]
    end=0
    global COL_img, COL_mic, COL_optgp, COL_coordx, COL_coordy, COL_defu, COL_defv, COL_defa
    global COL_rot, COL_tilt, COL_psi, COL_ox, COL_oxa, COL_oy, COL_oya
    for i in range(len(inputstar)):
        line=inputstar[i]
        metadata.append(line)
        if "_rln" in line:
            endl=i
        
        if "_rlnImageName" in line:
            COL_img = int(line.split("#")[1])
        if "_rlnCoordinateX" in line:
            COL_coordx = int(line.split("#")[1])
        if "_rlnCoordinateY" in line:
            COL_coordy = int(line.split("#")[1])
        if "_rlnMicrographName" in line:
            COL_mic = int(line.split("#")[1])
        if "_rlnOpticsGroup" in line:
            COL_optgp = int(line.split("#")[1])
        if "_rlnDefocusU" in line:
            COL_defu = int(line.split("#")[1])
        if "_rlnDefocusV" in line:
            COL_defv = int(line.split("#")[1])
        if "_rlnDefocusAngle" in line:
            COL_defa = int(line.split("#")[1])
        if "_rlnAngleRot" in line:
            COL_rot = int(line.split("#")[1])
        if "_rlnAngleTilt" in line:
            COL_tilt = int(line.split("#")[1])
        if "_rlnAnglePsi" in line:
            COL_psi = int(line.split("#")[1])
        if "_rlnOriginXAngst" in line:
            COL_oxa = int(line.split("#")[1])
        if "_rlnOriginYAngst" in line:
            COL_oya = int(line.split("#")[1])
#        if "_rlnOriginX " in line:
#            COL_ox = int(line.split("#")[1])
#        if "_rlnOriginY " in line:
#            COL_oy = int(line.split("#")[1])
    return(metadata[:end+1])



if __name__=="__main__":
    main()
