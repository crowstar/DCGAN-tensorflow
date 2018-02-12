import os
import shutil
import csv


verbose = True

current_dir = os.path.dirname(os.path.realpath(__file__))

# recursively remove everything in genres folder
dest_folder = 'data/genres'
if os.path.isdir(dest_folder):
	shutil.rmtree(dest_folder)
# create a new empty genre folder
os.mkdir(dest_folder) 

# read csv file into memory
reader = csv.DictReader(open('train_info.csv'))
train_info = list(reader)

# iterate through each item in paintings list
count = 0
for item in train_info:

	count += 1

	filename = item['filename']
	genre = item['genre']
	src_path = current_dir + '/data/paint/' + filename
	dest_path = current_dir + '/data/genres/' + genre + '/' + filename

	# create a new folder for new genre
	if not (os.path.isdir(current_dir + '/data/genres/' + genre)):
		os.mkdir(current_dir + '/data/genres/' + genre) 

	# make copy of file from train folder and put it into its genre folder
	if os.path.exists(src_path) and genre != '':
		shutil.copyfile(src_path, dest_path)

	if verbose:
		if (count % 1000 == 0):
			print('Progress:' + str(count))


