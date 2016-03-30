import nltk
import os
from flask import Flask, render_template,request, redirect
from Category import retrieve2,directoryScan
from Category.directoryScan import directoryScanClass
from Category.retrieve2 import nltkOps

app = Flask(__name__)
location=""
text_files=[]
categorized_text_files=[]
selected_text_files=[]
category_list=['film','programming','science']


def decide_category(match_indeces):
	global category_list
	return category_list[match_indeces.index(max(match_indeces))]
#Returns the match ratio with each category
def groundSupport(file):
	global location
	x=directoryScanClass()
	indata=x.get_text_at(location,file)
	y=nltkOps()
	avar=[]
	for current_category in category_list:
		avar.append(y.compare(indata,current_category))
	return avar

@app.route('/')
def location_fetcher():
	return render_template('form_bootstrap.html')

@app.route('/listItems', methods = ['POST'])
def listItems():
	global text_files
	global location
	del text_files[:]
	location=0
	location=request.form['location']
	#print (""+location)
	x=directoryScanClass()
	text_files=x.getContent(location)
	#text_files=set(text_files)
	return render_template('list_bootstrap.html', text_files=text_files)

@app.route('/testit',methods = ['POST'])
def goof():
	i=0
	exxx=[]
	bootvar=[]
	del bootvar[:]
	bootvar.append([])
	
	global categorized_text_files,category_list
	del categorized_text_files[:]
	categorized_text_files.append([])
	categorized_text_files.append([])
	selected_text_files = request.form.getlist('final_list')
	for current in selected_text_files:	
		try:
			bootvar[i].append(decide_category((groundSupport(current))))
			bootvar.append([])
			bootvar[i].append(current)
			i=i+1
		except BaseException:
			pass
	print bootvar
	return render_template('done.html',bootvar=bootvar,category_list=category_list)

if __name__ == '__main__':
	app.run()