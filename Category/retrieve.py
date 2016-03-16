import nltk
import pickle
def categorization(file_text):
	
	t=nltk.word_tokenize(file_text)
	a=nltk.pos_tag(t)
	secondary_word_list=[]
	primary_word_list=[]
	
	def union(a, b):
		""" return the UNION of two lists """
		return list(set(a) | set(b))
	
	with open("D:\DFE\\base\\sample.txt",'r') as f:
		source_list=pickle.load(f)
	
	for c in a:
		if (c[1]=='NN') or (c[1]=='NNS') or (c[1]=='NNP') or (c[1]=='NNPS') or (c[1]=='VB') or (c[1]=='VBD') or (c[1]=='VBG') or (c[1]=='VBN') or (c[1]=='VBP') or (c[1]=='VBZ'):	
			secondary_word_list.append(c[0])
	
	primary_word_list=union(source_list,secondary_word_list)
	
	with open("D:\DFE\\base\\sample.txt",'wb') as f:
		pickle.dump(primary_word_list,f)

f_text=open("D:\DFE\\Gravity(film).txt").read()
categorization(f_text)