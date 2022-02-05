f=open("jabir.txt",'r')
s=f.read()
print(s)

f=open("jabir_cpy.txt",'w')
f.write(s)
f.close()