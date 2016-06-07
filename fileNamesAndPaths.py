import os

#the file whose information we seek
fileName=raw_input("Give file name : ")

#current working directory
print("cwd : "+os.getcwd())

if (os.path.exists(fileName)):
	print(os.path.abspath(fileName))

if (os.path.isdir(fileName)):
	print(os.listdir(fileName))

#true if file exists in the cwd
print(os.path.isfile(fileName))
