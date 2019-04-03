from PIL import Image

ima = Image.open("littleschoolbus.bmp")
im=ima.load()
width = ima.width
height = ima.height
binary=[]
char=[]


for x in range(0, height):
    for y in range(0, width):
        pixel=im[y,x]
        for z in range(3)[::-1]:
            binary.append(bin(pixel[z])[-1]) #add last bit value of every red,green and blue value


for a in range(0,len(binary)-8,8):
    temp=[]
    for b in range(8):
        temp.append(binary[b+a])
    char.append(chr(int(''.join(temp),2)))


print(''.join(char))
