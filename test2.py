# encoding:utf-8



import json


with open('Data_JSON/prognosis.json', encoding='utf-8') as f:
    intent = json.load(f)

all_words = []
tags = []
xy = []
# loop through each sentence in our intents patterns
for inte in intent['prognosis']:
    tag = inte['tag']
    # add to tag list
    tags.append(tag)



#tags = sorted(set(tags))


print(len(tags), "tags:", tags)

