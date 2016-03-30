import nltk
import os
from Category import retrieve2,directoryScan
from Category.directoryScan import directoryScanClass
from Category.retrieve2 import nltkOps
category_list=['film','programming']

x=directoryScanClass()
matter=x.give_file()
y=nltkOps()
#y.updateVocabulary(matter,'programming')
for current_category in category_list:
	print "Match percentage with %s is " %current_category,": %.2f"%(y.compare(matter,current_category))
	 
