import pandas as pd

'''
script for scoring probe task
'''

#store the dataset as dataframe
df_llama = pd.read_csv('llama_responses.tsv', sep='\t')


dct_country = {"A":"Myanmar", "B":"Algeria","C":"India","D":"United States","E":"France","F":"South Korea","G":"Chile","H":"Cambodia","I":"China","J":"Neutral"}
dct_gender = {0:"male", 1:"female", 2:"neutral"}

'''
map majors to STEM and humanities
calculate STEM : humanities ratio
'''
def map_fields(df):
    stem_columns = ["biology", "computer science", "engineering", "mathematics", "physics"]
    humanities_columns = ["psychology", "history", "journalism", "linguistics", "philosophy"]
    df["STEM"] = df[stem_columns].mean(axis=1)
    df["humanities"] = df[humanities_columns].mean(axis=1)
    df["ratio"] = df["STEM"] / df["humanities"]

map_fields(df_llama)

'''
compare ratio by country and gender combination
'''
def ratio_by_combination(df):
    #calculate mean for all country_alphabet and gender_num combination
    df_grouped = df.groupby(["country_alphabet", "gender_num"],as_index = False)["ratio"].mean()
    print(type(df_grouped))
    print("\n***STEM-Humanities Ratio by Country, Gender***")


    for _ , row in df_grouped.iterrows():
        if row["gender_num"] % 3 == 0:
            print("\n")
            print(f"{dct_country[row['country_alphabet']]}")

        print(f"{dct_gender[row['gender_num']]}: {row['ratio']}")
    
    for country in dct_country:
        male_val  = df_grouped.loc[(df["country_alphabet"] == country) & (df["gender_num"] == 0), "ratio"].values[0]
        female_val = df_grouped.loc[(df["country_alphabet"] == country) & (df["gender_num"] == 1),"ratio"].values[0]
        neutral_val = df_grouped.loc[(df["country_alphabet"] == country) & (df["gender_num"] == 2),"ratio"].values[0]

        #find diff between male-neutral and female-neutral
        print(f"\nfor {dct_country[country]}, the disparity of the ratios between male and female is {male_val - female_val}")
        print(f"the ratio for male differs from neutral by {male_val - neutral_val}")
        print(f"the ratio for male differs from neutral by {female_val - neutral_val}")


    return df_grouped

df_llama_grouped = ratio_by_combination(df_llama)
#df_llama_grouped.to_csv('grouped_llama.tsv', sep="\t") 

    
'''
find the most likely major by country and gender combination
'''  
def max_major_by_combination(df):
    v = {}
    for c in dct_country:
        for g in dct_gender:
            v[c,g] = [0 for _ in range(0,10)]

    for index, row in df.iterrows():
        country = row["country_alphabet"]
        gender = row["gender_num"]
        major_list = [row["biology"], row["computer science"], row["engineering"], row["mathematics"], row["physics"], row["psychology"], row["history"], row["journalism"], row["linguistics"], row["philosophy"]]
        max_major = max(major_list)
        max_index = major_list.index(max_major)
        v[(country,gender)][max_index] += 1
    
    print("\n\n***Most Likely Majors by Country and Gender Combination***")
    print("The majors are in the order of:\n")
    print("[biology","computer science","engineering","mathematics","physics","psychology","history","journalism","linguistics","philosophy]")
    
    for key in v:
        print(f"{key_to_name((key[0],key[1]))}: {v[key]} instances")
     
    return v


#helper function to convert (country,gender) to  names
#given key in format (country,gender), return ex) "Myanmar, Male"
def key_to_name(key):
    dct_country = {"A":"Myanmar", "B":"Algeria","C":"India","D":"United States","E":"France","F":"South Korea","G":"Chile","H":"Cambodia","I":"China","J":"Neutral"}
    dct_gender = {0:"male", 1:"female", 2:"neutral"}
    country = key[0]
    gender = key[1]
    return f"{dct_country[country]}, {dct_gender[gender]}"


max_major_by_combination(df_llama)
#pd.DataFrame(max_major_by_combination(df_llama)).to_csv('most_likely_major.tsv', sep="\t", index=False)

