#! python 3
# findAndCopyFilesByType.py - a program that walks through a folder tree and searches for files with
# a certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder.

import os, shutil
# TODO: extension we are searhing for:
extension = '.pdf'
# TODO: set a path, where files with certain extensions will be searched for.
location = 'C:\\Users\\rudol\\Dropbox\\HUMF'
# TODO: set a path, where found files will be copied to.
destination = 'C:\\FilesFound'
# TODO: walk the folder tree.
for foldername, subfolders, filenames in os.walk(location):
	for filename in filenames:
		# TODO: check if each file is with required extension.
		if filename.endswith(extension):
			filename = os.path.join(foldername, filename)
			# TODO: print found file to the screen.
			print ('Found ' + "'" + os.path.basename(filename) + "'" + ' in ' +  "'" + os.path.dirname(filename) + "'" + '. ' + 'File copied to ' + "'" + destination +   "'" +'.')
			# TODO: copy file to the path.
			shutil.copy(filename, destination)

print('All files with ' + extension + ' extension were copied.')



