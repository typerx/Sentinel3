#!/usr/bin/python

import matplotlib.pyplot as plt
from netCDF4 import Dataset
import zipfile
import os, sys
import glob
	
def get_lastest(folder):
	file = [os.path.join(folder,f) for f in os.listdir(folder)]
	file.sort(key=lambda x: os.path.getmtime(x), reverse=True)
	return file[0]
	
#create directory old_zip and images if doesn't exist
if not os.path.exists("old_zip"):
    os.makedirs("old_zip")
if not os.path.exists("images"):
    os.makedirs("images")
	
## extract zip
for file in os.listdir("."):
	if file.endswith(".zip"):
		print(file)
		with zipfile.ZipFile(file, "r") as z:
			z.extractall("extract/")
		os.rename(file, "old_zip/"+file)

## Open a last modified file

#files = os.listdir("extract/")
file = get_lastest("extract/")
path_file = file.strip("extract/")
#print (path_file)
#files.sort()
#files.reverse()
path = file
print (path)

dirs = os.listdir(path)
# This would print all the files and directories

if not os.path.exists("images/"+path_file):
	os.makedirs("images/"+path_file)


for file in dirs:
	if file.endswith('.nc'):
		pf=os.path.join(path, file)
		print ("pf: "+str(pf))
		rootgrp = Dataset(pf, "r")
		print ("rootgrp.variables.keys: "+str(rootgrp.variables.keys()))
		var_num=rootgrp.variables.keys()
		for var in var_num:
			if var+".nc" == file:
				print (var)
				var_desc=rootgrp.variables[var]
				print (var_desc.long_name)
				plt.imshow(var_desc)
				plt.axis('off')
				plt.savefig("images/"+path_file+"/"+var+'.png')	
		rootgrp.close()
sys.exit()	
'''		
fotos = []
	
for file in dirs:
	if file.endswith('.nc'):
		if file.endswith('.nc')
		pf=os.path.join(path, file)
		#print pf
		rootgrp = Dataset(pf, "r")
		print ("var_num: "+str(rootgrp.variables.keys()))
		var_num=rootgrp.variables.keys()
		for var in var_num:
			if var+".nc" == file:
				print ("var: "+var)
				var_desc=rootgrp.variables[var]
				print ("var_desc.long_name: "+var_desc.long_name)
				fotos.append(var_desc)
		rootgrp.close()
		
print("lenght: "+str(len(fotos)))

for i in range(len(fotos)):
	#print(fotos[i])		
	plt.imshow(fotos[i])
	plt.axis('off')
	plt.savefig("images/"+path_file+"/"+fotos[i]+'.png')	

for file in dirs:
	if file.endswith('.nc'):
		pf=os.path.join(path, file)
		#print pf
		rootgrp = Dataset(pf, "r")
		print (rootgrp.variables.keys())
		var_num=rootgrp.variables.keys()
		var=file.strip(".nc")
		print (var)
		var_desc=rootgrp.variables[var]
		print (var_desc.long_name)
		plt.imshow(var_desc)
		plt.axis('off')
		plt.savefig("images/"+path_file+"/"+var+'.png')	
		rootgrp.close()
'''	
# # # examine the variables
# print rootgrp.variables.keys()
# var=rootgrp.variables.keys()[0]
# print var
# var2=rootgrp.variables["F1_BT_in"]
# print var2
# print rootgrp.variables["F1_BT_in"].ncattrs()

# # # sample every 10th point of the 'z' variable
# # topo = rootgrp.variables['Oa02_radiance']


# plt.imshow(var2) #Needs to be in row,col order
# plt.axis('off')
# plt.title(rootgrp.title)
# plt.savefig('image2.png')

sys.exit()
