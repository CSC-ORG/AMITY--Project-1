import os
import nltk
class directoryScanClass:
	
	#global variables
	dir_path=''
	txt_file=[]
	txt_file_path=''
	def __init__(self):
		print "Initiated"
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
		dir_path=given_path
		return dir_path

	#Fetches all the files inside a directory
	def getContent(self,location):
		return os.listdir(self.setPath(location))

	#Fetches the text form a file
	def get_file_content(self,n,loc):
		indata=open(loc+'\\'+self.txt_file[n]).read()
		return indata

	def set_text_file_loc(self,n,loc):
		self.txt_file_path=(loc+'\\'+self.txt_file[n])
	def get_text_file_loc(self):
		return self.txt_file_path
	#Generates a list of all the text files to be classified
	def give_file(self):
		folder_location=raw_input('Enter path')
		dir_items=self.getContent(folder_location)
		for file in dir_items:
			if file.endswith(".txt"):
				(self.txt_file).append(file)

		print(self.txt_file)

		a=int(raw_input('Enter index postion of file'))
		fileContent=self.get_file_content(a,folder_location)
		self.set_text_file_loc(a,folder_location)
		
		return fileContent




