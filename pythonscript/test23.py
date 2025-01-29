import random as rn
import sys
import os

print(rn.randint(1,5))

for i in range(1,11):
    print(i)

print(sys.path)    
print(sys.argv[0])
print(sys.argv[1:])
#print(sys.exit())
print("rajesh")
os.chdir("/home/ubuntu/")
os.makedirs("dir1",exist_ok=True)
print(os.getcwd())

for path,dir,files in os.walk("/home/ubuntu/dir1"):
    print(path,dir,files)
