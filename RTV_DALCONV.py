#%%
from PIL import Image
filenums=[1,2,4,6,7,8,9,10]
for fvc in filenums:
    pal = []
    f = open('PAL'+str(fvc)+'.PAL', 'rb') # opening a binary file
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
    fname = 'DALLE'+str(fvc)
    f = open(fname+'.DAL', 'rb') # opening a binary file
    contents=bytearray(f.read())
    f.close()
    xmax=60#(contents[7]<<8)+(contents[8])
    ymax=74#(contents[9]<<8)+(contents[10])
    img = Image.new(mode='RGB', size=(xmax, ymax))
    x=0
    y=0
    icount=0
    for i in range(0, len(contents)):
        palid=pal[contents[i]]
        img.putpixel((x,y), (palid[0], palid[1], palid[2],255))
        y+=1
        if y>=ymax:
            y=0
            x+=1
        if x>=xmax:
            img.save(fname+'_'+str(icount)+'.png', "PNG")
            icount+=1
            x=0
            y=0
            img=Image.new(mode='RGB', size=(xmax, ymax))
