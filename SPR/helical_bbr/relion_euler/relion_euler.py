import sys
import numpy as np

def main():
    x, y, z, c = 400, 420, 510, 320
    #with open(sys.argv[1],"r") as f:
    with open("test.star","r") as f:
        infile=f.readlines()
        for i in range(len(get_metadata(infile)),len(infile)):
            if infile[i] == "":
                continue
            line=infile[i].split('\n')[0].split()
            #print(line)
            rot=float(line[COL_rot-1])
            tilt=float(line[COL_tilt-1])
            psi=float(line[COL_psi-1])
            ox=float(line[COL_ox-1])
            oy=float(line[COL_oy-1])
            #print(rot,tilt,psi,ox,oy)
            model_coor=np.array([[x-c],[y-c],[z-c]])
            rot_coor=rz(psi).dot(ry(tilt)).dot(rz(rot)).dot(model_coor)
            print(np.rint(rot_coor2[0]+320-ox),np.rint(rot_coor2[1]+320-oy),rot_coor2[2]+320)

#            model_coor=np.array([0,0,510-320])
#            rot_coor=model_coor.dot(rz(rot)).dot(ry(tilt)).dot(rz(psi))
#            #print(rot_coor+320)
#            print(rot_coor[0]+320,rot_coor[1]+320,rot_coor[2]+320)

            

def rz(angle):
    angle=np.deg2rad(angle)
    array=np.array([[np.cos(angle), np.sin(angle), 0], [-1*np.sin(angle), np.cos(angle), 0], [0,0,1]])
    return(array)

def ry(angle):
    angle=np.deg2rad(angle)
    array=np.array([[np.cos(angle),0,-1*np.sin(angle)], [0,1,0], [np.sin(angle), 0, np.cos(angle)]])
    return(array)

def euler_angle2matrix(rot,tilt,psi):
    a1, a2, a3 = np.deg2rad(rot), np.deg2rad(tilt), np.deg2rad(psi)
    c1 = np.cos(a1)
    c2 = np.cos(a2)
    c3 = np.cos(a3)
    s1 = np.sin(a1)
    s2 = np.sin(a2)
    s3 = np.sin(a3)
    array=np.array([[c3*c2*c1-s3*s1, c3*c2*s1+s3*c1, -c3*s2],
                    [-s3*c2*c1-c3*s1, -s3*c2*s1+c3*c1, s3*s2],
                    [s2*c1, s2*s1, c2]])
    return(array)

def euler_matrix2angle(array):
    #a1 = 
    a2 = np.arccos(array[2,2])

def get_metadata(inputstar):  # 剥离metadata部分, 获得每个label的列数
    metadata=[]
    end=0
    global COL_img, COL_mic, COL_optgp, COL_coordx, COL_coordy, COL_defu, COL_defv, COL_defa
    global COL_rot, COL_tilt, COL_psi, COL_ox, COL_oxa, COL_oy, COL_oya
    for i in range(len(inputstar)):
        line=inputstar[i]
        metadata.append(line)
        if "_rln" in line:
            end=i
        
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
#        if "_rlnOriginXAngst" in line:
#            COL_oxa = int(line.split("#")[1])
#        if "_rlnOriginYAngst" in line:
#            COL_oya = int(line.split("#")[1])
        if "_rlnOriginX " in line:
            COL_ox = int(line.split("#")[1])
        if "_rlnOriginY " in line:
            COL_oy = int(line.split("#")[1])
    return(metadata[:end+1])


    
def test():
    print(rot_wikiZYZ(11,22,33))
    print("\n")
    print(rz(33).dot(ry(22)).dot(rz(11)))
    print(np.linalg.inv(rz(33).dot(ry(22)).dot(rz(11))))
    print(np.linalg.inv(rz(11)).dot(np.linalg.inv(ry(22))).dot(np.linalg.inv(rz(33))))    
    a=np.array([[1,2],[1,1],[2,1]])
    b=np.array([[3],[2]])
    c=np.array([[1,3,2]])
    #print(np.dot(a,b).dot(c))
    #print(a.dot(b).dot(c))


#test()
main()


"""
test.star
xy320 z510 box320
0       center=422,322
1       center=319,231
2       center=414,345
3       center=397,369
4       center=258,217
5       center=238,332
6       center=246,292
7       center=392,351
8       center=420,351
9       center=283,294

x400 y420 z510
0       center=477,431
1       center=205,180
2       center=488,243
3       center=397,492
4       center=352,133
5       center=153,243
6       center=213,173
7       center=494,281
8       center=483,240
9       center=162,335
"""