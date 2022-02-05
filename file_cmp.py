import filecmp

s=filecmp.cmp("jabir.txt",'jabir_cpy.txt')
print(s)