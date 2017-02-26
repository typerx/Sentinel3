#!/usr/bin/python

import matplotlib.pyplot as plt
from netCDF4 import Dataset
import zipfile
import os, sys

## extract zip
for file in os.listdir("."):
	if file.endswith(".zip"):
		print(file)
		with zipfile.ZipFile(file, "r") as z:
			z.extractall("extract/")
		os.rename(file, "old_zip/"+file)

## Open a last modified file
files = os.listdir("extract/")
#print files
files.sort()
files.reverse()
path = files[0]
path = "extract/"+path
print path

#path = "extract\S3A_SL_1_RBT____20170207T220155_20170207T220455_20170208T002904_0179_014_115_0720_SVL_O_NR_002.SEN3"
#path = "S3A_OL_1_EFR____20170207T075602_20170207T075653_20170208T200019_0051_014_106_4499_LN1_O_NT_002"

dirs = os.listdir(path)
# This would print all the files and directories
for file in dirs:
	if file.endswith('.nc'):
		pf=os.path.join(path, file)
		#print pf
		rootgrp = Dataset(pf, "r")
		#print rootgrp.variables.keys()
		var_num=rootgrp.variables.keys()
		for var in var_num:
			if var+".nc" == file:
				print var
				var_desc=rootgrp.variables[var]
				print var_desc.long_name
				plt.imshow(var_desc)
				plt.axis('off')
				plt.savefig("images/"+var+'.png')
		rootgrp.close()

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
