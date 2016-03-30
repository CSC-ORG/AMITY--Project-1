import nltk
import pickle
class nltkOps:
	#updates vocabulary takes following parameters-(text of file which matched,name of library to be updated)
	def updateVocabulary(self,file_text,lib_name):
		
		t=nltk.word_tokenize(file_text)
		a=nltk.pos_tag(t)
		secondary_word_list=[]
		primary_word_list=[]
		initial_obj=['initial','obj']
		def union(a, b):
			""" return the UNION of two lists """
			return list(set(a) | set(b))
		
		with open(self.getPath(lib_name),'r+') as f:
			if (f.read()==''):
				pickle.dump(initial_obj,f)
		with open(self.getPath(lib_name),'r') as f:
			source_list=pickle.load(f)
		
		for c in a:
			if (c[1]=='NN') or (c[1]=='NNS') or (c[1]=='NNP') or (c[1]=='NNPS') or (c[1]=='VB') or (c[1]=='VBD') or (c[1]=='VBG') or (c[1]=='VBN') or (c[1]=='VBP') or (c[1]=='VBZ'):	
				secondary_word_list.append(c[0])
		
		primary_word_list=union(source_list,secondary_word_list)
		
		with open(self.getPath(lib_name),'wb') as f:
			pickle.dump(primary_word_list,f)
		

	def getPath(self,lib_name):
		return ("D:\DFE\\base\\"+lib_name+".txt")
	
	def compare(self,file_text,lib_name):
		secondary_word_list=[]
		dictionary=[]
		file_text=nltk.pos_tag(nltk.word_tokenize(file_text))
		for c in file_text:
			if (c[1]=='NN') or (c[1]=='NNS') or (c[1]=='NNP') or (c[1]=='NNPS') or (c[1]=='VB') or (c[1]=='VBD') or (c[1]=='VBG') or (c[1]=='VBN') or (c[1]=='VBP') or (c[1]=='VBZ'):	
				secondary_word_list.append(c[0])
		with open(self.getPath(lib_name),'r') as f:
			dictionary=pickle.load(f)
		common_words=(len(list(set(secondary_word_list) & set(dictionary))))
		match_ratio=(float(common_words)/float(len(set(secondary_word_list))))*100.0
		return match_ratio