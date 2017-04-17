#! python 3
# findAndCopyFilesByType.py - a program that walks through a folder tree and searches for files with
# a certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder.

import os, shutil
# let user choose what extension they want to search for:
print('Enter extension type you want to search for:')
extension = input()
# set a path, where files with certain extensions will be searched for.
# let user choose the location, where they want to search for files:
print('Enter the location, where you want to search for files:')
location = input()
while os.path.isdir(location) == False:
	print('Directory ' + location + ' does not exist or is not valid.')
	print('Please, reenter correct directory:')
	location = input()	

# set a path, where found files will be copied to.
print('Enter the location, where you want to copy found files:')
destination = input()
while os.path.isdir(destination) == False:
	print('Directory ' + destination + ' does not exist or is not valid.')
	print('Please, reenter correct directory:')
	destination = input()

# walk the folder tree.
for foldername, subfolders, filenames in os.walk(location):
	for filename in filenames:
		# check if each file is with required extension.
		if filename.endswith(extension):
			# get the absolute path of found file.
			filename = os.path.join(foldername, filename)
			# print found file to the screen.
			print ('Found ' + "'" + os.path.basename(filename) + "'" + ' in ' +  "'" + os.path.dirname(filename) + "'" + '. ' + 'File copied to ' + "'" + destination +   "'" +'.')
			# copy file to the path.
			shutil.copy(filename, destination)

print('All files with ' + extension + ' extension were copied.')



