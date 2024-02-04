import pandas as pd
"""
Script for taking a list of prompts and creating different gender and country variants.
"""

df = pd.DataFrame(columns = ["stub_index", "country_alphabet", "gender_num", "prompt"])

countries = ["Myanmar","Algeria","India","United States","France","South Korea", "Chile", "Cambodia", "China","a Country"]
genders = ["male", "female", ""]
gender_pronoun = ["his","her","their"]
letters = "ABCDEFGHIJ"
numbers = "012"
stubs = [l.strip() for l in open('./framework_sentences.tsv','r').readlines()] #stub list
for s,stub in enumerate(stubs): #s is index of each stub
	for c,country in enumerate(countries): #c is a varient of each stub
		for g, gender in enumerate(genders):
			fields = [s,letters[c],g,stub.replace('QQQ',country).replace('ZZZ',gender).replace('XXX',gender_pronoun[g])] #[stub(1-32)index, country index(A-F), prompt]
			df.loc[len(df)] = fields #creates tsv file: each element joined by tabs

# saving as tsv file 
df.to_csv('prompts.tsv', sep="\t") 