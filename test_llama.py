import query_llama
import pandas as pd

all_majors = "biology;computer science;engineering;mathematics;physics;psychology;history;journalism;linguistics;philosophy"

llama_responses = []
df = pd.read_csv('prompts.tsv', sep='\t')

for index,row in df.iterrows():
    print(row["prompt"])
    #print(query_llama.word_query(row["prompt"],field_of_study))
    prob_list = list(query_llama.word_query(row["prompt"],all_majors).values())
    llama_responses.append(prob_list)

for i, row in enumerate(llama_responses):
    df.loc[i,"biology"] = row[0]
    df.loc[i,"computer science"] = row[1]
    df.loc[i,"engineering"] = row[2]
    df.loc[i,"mathematics"] = row[3]
    df.loc[i,"physics"] = row[4]
    df.loc[i,"psychology"] = row[5]
    df.loc[i,"history"] = row[6]
    df.loc[i,"journalism"] = row[7]
    df.loc[i,"linguistics"] = row[8]
    df.loc[i,"philosophy"] = row[9]

df.to_csv('prompt_llama_responses.tsv', sep="\t") 