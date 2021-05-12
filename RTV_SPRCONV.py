#%%
###################################################################################
####                        SPR CONVERTER COMBINED                             ####
###################################################################################
#spr conv
#import PIL
from PIL import Image
import struct
files =[
['CHARME','PAL1.PAL',0],
['CHARME2','PAL1.PAL',0],
['CHARME3','PAL1.PAL',0],
['CHARME4A','PAL1.PAL',0],
['CHARME4D','PAL1.PAL',0],
['CHARME4F','PAL1.PAL',0],
['CHARME4I','PAL1.PAL',0],
['MONS0','MONS0.PAL',0],
['MONS1','PAL1.PAL',0],
['MONS3','PAL1.PAL',0],
['MONS3','PAL1.PAL',0],
['MONS4','PAL1.PAL',0],
['MONS5','PAL1.PAL',0],
['MONS6','PAL1.PAL',0],
['MONS7','PAL1.PAL',0],
['MONS8','PAL1.PAL',0],
['MONS9','PAL1.PAL',0],
['MENU2', 'PAL_MENU.PAL',0],
['A_LEVEL','PAL1.PAL',0],
['BALLE0','PAL1.PAL',0],
['ARME0','PAL1.PAL',0],
['ARME1','PAL1.PAL',0],
['ARME2','PAL1.PAL',0],
['ARME3','PAL1.PAL',0],
['ARME4','PAL1.PAL',0],
['ARME5','PAL1.PAL',0],
['A_BOMB'	,'PAL1.PAL',0],
['ADALLE'	,'PAL1.PAL',0],
['B_CODE'	,'PAL1.PAL',0],
['B_PLAN2'	,'PAL1.PAL',0],
['B_PLAN3'	,'PAL1.PAL',0],
['B_PORTE'	,'PAL1.PAL',0],
['BALLE1'	,'PAL1.PAL',0],
['BALLE2'	,'PAL1.PAL',0],
['BALLE3'	,'PAL1.PAL',0],
['BALLE4'	,'PAL1.PAL',0],
['BALLE5'	,'PAL1.PAL',0],
['BOMBE'	,'PAL1.PAL',0],
['BOUSSOLE'	,'PAL1.PAL',0],
['CASQUE'	,'PAL1.PAL',0],
['CH_LEVEL'	,'PAL1.PAL',0],
['CH_OBJ2'	,'PAL1.PAL',0],
['CH_OBJ3'	,'PAL1.PAL',0],
['CH_OBJ4A'	,'PAL1.PAL',0],
['CH_OBJ4D'	,'PAL1.PAL',0],
['CH_OBJ4F'	,'PAL1.PAL',0],
['CH_OBJ4I'	,'PAL1.PAL',0],
['CON_VISA'	,'PAL1.PAL',0],
['CON_VUET'	,'PAL1.PAL',0],
['FSEQ2_2'	,'PAL1.PAL',0],
['FSEQ4_2'	,'PAL1.PAL',0],
['GOUTTE'	,'PAL1.PAL',0],
['INBASE'	,'PAL1.PAL',0],
['INVENT_A'	,'PAL1.PAL',0],
['INVENT_D'	,'PAL1.PAL',0],
['INVENT_F'	,'PAL1.PAL',0],
['INVENT_I'	,'PAL1.PAL',0],
['INVENT_T'	,'PAL1.PAL',0],
['MORT0'	,'PAL1.PAL',0],
['NAV_INS2'	,'PAL1.PAL',0],
['NAV_INST'	,'PAL1.PAL',0],
['NAV_SEQ2'	,'PAL1.PAL',0],
['OBJET1'	,'PAL1.PAL',0],
['OBJET10'	,'PAL1.PAL',0],
['OBJET2'	,'PAL1.PAL',0],
['OBJET4'	,'PAL1.PAL',0],
['OBJET5'	,'PAL1.PAL',0],
['OBJET6'	,'PAL1.PAL',0],
['OBJET7'	,'PAL1.PAL',0],
['OBJET8'	,'PAL1.PAL',0],
['OBJET9'	,'PAL1.PAL',0],
['PAUSE'	,'PAL1.PAL',0],
['PSEQ10_2'	,'PAL1.PAL',0],
['PSEQ10_3'	,'PAL1.PAL',0],
['PSEQ11_2'	,'PAL1.PAL',0],
['PSEQ12_2'	,'PAL1.PAL',0],
['PSEQ14_3'	,'PAL1.PAL',0],
['PSEQ2_3'	,'PAL1.PAL',0],
['PSEQ6_2'	,'PAL1.PAL',0],
['PSEQ7_2'	,'PAL1.PAL',0],
['TYPOOVER'	,'PAL1.PAL',0]
]
for fileobj in files:
    pal = []
    #f = open('PAL1.PAL', 'rb') # opening a binary file
    f = open(fileobj[1], 'rb') # opening a binary file
    
    contents=bytearray(f.read())
    f.close()
    #print(len(contents))
    length = len(contents)/3

    for i in range(0, length):
        ci = i*3
        r = contents[ci] << 2
        g = contents[ci+1] << 2
        b = contents[ci+2] << 2
        pal.append([r,g,b])

    filecounts=[]
    # format [offset(with 4 already added), width, height]
    filename=fileobj[0]#'CHARME2'
    f = open(filename+'.SPR', 'rb') # opening a binary file
    contents=bytearray(f.read())
    f.seek(2)
    imagecount= struct.unpack('H', f.read(2))[0]
    for ic in range(0, imagecount):
        filecounts.append([struct.unpack('I', f.read(4))[0]+4, 0,0])
    for ic in range(0, imagecount):
        f.seek(filecounts[ic][0])
        filecounts[ic][1]=struct.unpack('H', f.read(2))[0]
        filecounts[ic][2]=struct.unpack('H', f.read(2))[0]

    f.close()
    #raise

    for ic in range(0, imagecount):
        xmax=filecounts[ic][1]
        ymax=filecounts[ic][2]
        img=Image.new(mode='RGBA', size=(xmax, ymax))
        x=0
        y=0
        coffset=filecounts[ic][0]+8
        cend=coffset+ xmax*ymax
        for i in range(coffset, cend):
            palid=pal[contents[i]]
            alpha=255
            if contents[i]==0:
                alpha=0
            img.putpixel((x,y), (palid[0], palid[1], palid[2], alpha))
            x+=1
            if x>=xmax:
                x=0
                y+=1
            if y>=ymax:
                break
        img.save('sprs/'+filename+'_'+str(ic)+'.png', "PNG")
