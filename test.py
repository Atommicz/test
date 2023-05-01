import os
import shutil
p = os.getcwd()

data = str(p)+"\\Hello.py"
file = open(data,"w")
file.write("print('hello world')")
# file.write("\nprint('hello world')\n")
file.close()
# file = open(data,"w")
# file.write("Hello")
# file.close()
# file = open(data,"r")
# text = file.read()
# print(text)

# ย้าย file
# shutil.move(str(p)+"\\test.py",str(p)+"\\Hello\\"+"test.py")

# สร้าง folder ชื่อ hello 
# os.mkdir(f"C:/Users/Tum/Desktop/pyth/Hello")

# เปลี่ยนชื่อ file
# os.rename(str(p)+"\\Hello2\\",str(p)+"\\Hello_ta")

# ลบ file
# os.remove(str(p)+"\\Hello_ta\\"+"Hello.txt")

# ลบ folder
# os.removedirs(str(p)+"\\Hello0")
#หา folder
#print(os.path.isdir("Hello"))
#หา file
# print(os.path.isfile("Hello.py"))
# print(p)
# file = open(data,"r")
# text = file.read()
# print(text)

