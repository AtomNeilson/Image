# import wget 
import urllib
from collections import Counter
import httplib 
import requests


words = []
for line in open('female.txt'):
    line.split()
    words.append(line)

i = 0
downloaded = 0 
cancelled = 0

for images in words:

    def exists(path):
        output_1 = "True"
        output_2 = "False"
        r = requests.head(path)
        if (r.status_code == requests.codes.ok):
            return output_1
        else:
            return output_2 

    res = exists(images)    
    
    print res
    print images

    if (res == "True"):
    	# urllib.urlretrieve(images, "kaggle_images/male/img" + str(i) +".jpg")
		# wget.download(images, 'kaggle_images/male/img' + str(i) + ".jpg")
		# i = i + 1
		try:
			urllib.urlretrieve(images, "kaggle_images/female/female-" + str(i) +".jpg")	
			i = i + 1 
			downloaded = downloaded + 1
		except requests.exceptions.RequestException as e:
			print e
			# i = i + 1 
			sys.exit(1)

    else:
    	print "cannot download" 
	cancelled = cancelled + 1 
print("Total downloaded images",downloaded)
print("Total cancelled images",cancelled)
