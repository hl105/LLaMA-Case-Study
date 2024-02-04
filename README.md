# Exploring bias in the LLaMA Model

 A Case Study on Gender and Cultural Bias in Tertiary Education

## Creating the datset
#### framework_sentences.tsv, stub_to_prompt.py, prompts.tsv

framework_sentences.tsv contains the 32 framework sentences used to operationalize the construct.
stub_to_prompt.py replaces the variables in each sentence of the framework_sentences.tsv file to create 960 sentence total and saves the result to the file prompts.tsv

## LLaMA responses
#### query_llama.py, llama_responses.tsv, map_fields function in scoring.py
After the dataset is ready, they are each passed into the LLaMA word_query function in the file query_llama.py where the probabilities for 10 majors are calculated for each sentence. The results are saved in the file llama_responses.tsv. The probabilities of the majors are averaged and mapped depending on their categories, STEM or humanities. 

## Evaluation
All evaluation functions return a dictionary or a dataframe that can be stored as a .tsv file, but this part has been commented out for clarity. Instead, **the evaluation results can be checked in the terminal, by navigating to the folder and typing python scoring.py **. This is possible because print statements have been added to all evaluation functions for easier access to results. 

The result should look like the following:
```

***STEM-Humanities Ratio by Country, Gender***


Myanmar
male: 0.5864477761420225
female: 0.5767449342185486
neutral: 0.5749170436784603


Algeria
male: 0.5892848080666832
female: 0.5841862102935316
neutral: 0.5807707740022126


India
male: 0.5461921371261675
female: 0.5263772150515738
neutral: 0.5263671206382893


United States
male: 0.5956833606174001
female: 0.581924777844573
neutral: 0.5722450131767741


France
male: 0.6507215977496156
female: 0.6386909983796515
neutral: 0.6343837185067543


South Korea
male: 0.5333505358058444
female: 0.515093726352866
neutral: 0.5145769477446168


Chile
male: 0.5757975678757495
female: 0.5716659753765672
neutral: 0.5671287858824596


Cambodia
male: 0.5685984939528875
female: 0.5641777364688041
neutral: 0.5604753504526008


China
male: 0.5771530458012897
female: 0.5572430867417342
neutral: 0.5561333431276672


Neutral
male: 0.5947327062409699
female: 0.5790172550043168
neutral: 0.5728267003600798

for Myanmar, the disparity of the ratios between male and female is 0.009702841923473926
the ratio for male differs from neutral by 0.011530732463562177
the ratio for male differs from neutral by 0.0018278905400882506

for Algeria, the disparity of the ratios between male and female is 0.005098597773151581
the ratio for male differs from neutral by 0.0085140340644706
the ratio for male differs from neutral by 0.0034154362913190184

for India, the disparity of the ratios between male and female is 0.019814922074593788
the ratio for male differs from neutral by 0.019825016487878266
the ratio for male differs from neutral by 1.0094413284478243e-05

for United States, the disparity of the ratios between male and female is 0.013758582772827155
the ratio for male differs from neutral by 0.023438347440626006
the ratio for male differs from neutral by 0.009679764667798851

for France, the disparity of the ratios between male and female is 0.01203059936996409
the ratio for male differs from neutral by 0.01633787924286123
the ratio for male differs from neutral by 0.004307279872897141

for South Korea, the disparity of the ratios between male and female is 0.018256809452978362
the ratio for male differs from neutral by 0.01877358806122753
the ratio for male differs from neutral by 0.0005167786082491688

for Chile, the disparity of the ratios between male and female is 0.004131592499182379
the ratio for male differs from neutral by 0.008668781993289909
the ratio for male differs from neutral by 0.00453718949410753

for Cambodia, the disparity of the ratios between male and female is 0.004420757484083437
the ratio for male differs from neutral by 0.008123143500286756
the ratio for male differs from neutral by 0.0037023860162033184

for China, the disparity of the ratios between male and female is 0.019909959059555504
the ratio for male differs from neutral by 0.02101970267362252
the ratio for male differs from neutral by 0.0011097436140670158

for Neutral, the disparity of the ratios between male and female is 0.015715451236653077
the ratio for male differs from neutral by 0.02190600588089009
the ratio for male differs from neutral by 0.006190554644237012


***Most Likely Majors by Country and Gender Combination***
The majors are in the order of:

[biology computer science engineering mathematics physics psychology history journalism linguistics philosophy]
Myanmar, male: [1, 7, 0, 0, 0, 16, 0, 8, 0, 0] instances
Myanmar, female: [1, 3, 0, 0, 0, 18, 0, 10, 0, 0] instances
Myanmar, neutral: [1, 5, 0, 0, 0, 16, 0, 10, 0, 0] instances
Algeria, male: [1, 5, 0, 0, 0, 15, 0, 10, 1, 0] instances
Algeria, female: [1, 3, 0, 0, 0, 15, 0, 10, 3, 0] instances
Algeria, neutral: [1, 5, 0, 0, 0, 14, 0, 11, 1, 0] instances
India, male: [1, 6, 0, 0, 0, 19, 0, 6, 0, 0] instances
India, female: [0, 4, 0, 0, 0, 22, 0, 6, 0, 0] instances
India, neutral: [1, 6, 0, 0, 0, 20, 0, 5, 0, 0] instances
United States, male: [0, 8, 0, 0, 0, 22, 0, 2, 0, 0] instances
United States, female: [0, 4, 0, 0, 0, 25, 0, 3, 0, 0] instances
United States, neutral: [1, 6, 0, 0, 0, 22, 0, 3, 0, 0] instances
France, male: [1, 8, 0, 0, 0, 12, 0, 7, 4, 0] instances
France, female: [0, 8, 0, 0, 0, 13, 0, 7, 4, 0] instances
France, neutral: [1, 8, 0, 0, 0, 13, 0, 6, 4, 0] instances
South Korea, male: [0, 4, 0, 0, 0, 17, 0, 9, 2, 0] instances
South Korea, female: [0, 1, 0, 0, 0, 23, 0, 7, 1, 0] instances
South Korea, neutral: [0, 1, 0, 0, 0, 21, 0, 8, 2, 0] instances
Chile, male: [0, 3, 0, 0, 0, 20, 0, 9, 0, 0] instances
Chile, female: [0, 1, 0, 0, 0, 23, 0, 8, 0, 0] instances
Chile, neutral: [0, 3, 0, 0, 0, 22, 0, 7, 0, 0] instances
Cambodia, male: [0, 2, 0, 0, 0, 25, 0, 5, 0, 0] instances
Cambodia, female: [0, 2, 0, 0, 0, 24, 0, 6, 0, 0] instances
Cambodia, neutral: [0, 2, 0, 0, 0, 24, 0, 6, 0, 0] instances
China, male: [0, 8, 0, 0, 0, 16, 0, 8, 0, 0] instances
China, female: [0, 5, 0, 0, 0, 20, 0, 7, 0, 0] instances
China, neutral: [0, 6, 0, 0, 0, 18, 0, 8, 0, 0] instances
Neutral, male: [1, 5, 0, 0, 0, 21, 0, 5, 0, 0] instances
Neutral, female: [1, 4, 0, 0, 0, 23, 0, 4, 0, 0] instances
Neutral, neutral: [1, 5, 0, 0, 0, 23, 0, 3, 0, 0] instances
```
