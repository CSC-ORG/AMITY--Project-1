import os
import nltk
class directoryScanClass:
	
	#global variables
	dir_path=''
	txt_file=[]
	txt_file_path=''
	def __init__(self):
		print "Chgggg"
	#Tokenize the recovered text
	def token_content(Content):
		return nltk.word_tokenize(Content)

	#Creates a new text file
	def createFile(tokens):
		name=raw_input('Name the file')+'.txt'
		file=open(name,'a')	
		file.write()
		file.close()

	#sets the value of global variable dir_path
	def setPath(self,given_path):
		global dir_path
		self.dir_path=given_path
		return self.dir_path

	#Fetches all the files inside a directory with .txt extension
	def getContent(self,location):
		global txt_file
		dir_items=os.listdir(self.setPath(location))
		for file in dir_items:
			if file.endswith(".txt"):
				(self.txt_file).append(file)
		return self.txt_file		

	#Fetches the text form a file
	def get_file_content(self,n,loc):
		indata=open(loc+'\\'+self.txt_file[n]).read()
		return indata

	def set_text_file_loc(self,n,loc):
		self.txt_file_path=(loc+'\\'+self.txt_file[n])
	def get_text_file_loc(self,):
		return self.txt_file_path
	#Generates a list of all the text files to be classified
	def give_file(self,file_index,file_location):
		#folder_location=raw_input('Enter path')
				
		a=int(file_index)
		fileContent=self.get_file_content(file_index,file_location)
		self.set_text_file_loc(a,file_location)
		
		return fileContent

	def get_text_at(self,loc,file):
		self.myDat=open(loc+'\\'+file).read()
		return self.myDat