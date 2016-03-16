import nltk
import pickle
def categorizeation(file_text):
	
	t=nltk.word_tokenize(file_text)
	a=nltk.pos_tag(t)
	
	word_list=[]
	for c in a:
		if (c[1]=='NN') or (c[1]=='NNS') or (c[1]=='NNP') or (c[1]=='NNPS') or (c[1]=='VB') or (c[1]=='VBD') or (c[1]=='VBG') or (c[1]=='VBN') or (c[1]=='VBP') or (c[1]=='VBZ'):	
			word_list.append(c[0])
	with open("D:\DFE\\base\\sample.txt",'a') as f:
		pickle.dump(word_list, f)		
	
	

	
	