import wikipedia
import os
parent_dir = "C:/Users/mavbe/Desktop/Coding Folder/Languages/"
lang = wikipedia.page("List of programming languages")
black_list = ['Аналитик','Lists of programming languages','List of programming languages by type','Comparison of programming languages','List of BASIC dialects by platform','List of markup languages','List of stylesheet languages','History of programming languages','Category:Programming languages','List of hello world programs','Programming language','Programming Language for Business','Programming language for Computable Functions']
for i in lang.links:
	if i not in black_list:
		try:
			os.mkdir(os.path.join(parent_dir,i.replace(chr(0xa0),'').replace('(programming language)','').replace('*',' Star').strip().replace('/','_').replace(':','_')))
		except:
			print("issue with " + str(i))