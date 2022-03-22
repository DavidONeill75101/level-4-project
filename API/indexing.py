'''
takes ~5 minutes to run this and is very computationally intensive
'''

import pandas as pd

import json
import gzip
import os
import sys
import wget

import pyterrier as pt

if not pt.started():
    pt.init()


# load the coronacentral dataset

url = 'https://github.com/DavidONeill75101/level-4-project/blob/master/Datasets/coronacentral_with_altmetric.json.gz?raw=true'
filename = wget.download(url)


with gzip.open("coronacentral_with_altmetric.json.gz", "r") as f:
    cc = f.read()

    json_str = cc.decode("utf-8")
    data = json.loads(json_str)

    coronacentral = pd.DataFrame.from_dict(data)

    coronacentral = coronacentral.rename(columns={"cord_uid": "docno"})

print("Downloaded CoronaCentral")

# filter it down to remove docs without altmetric
altmetrics = coronacentral["altmetric"]
altmetrics = [altmetric["response"] for altmetric in altmetrics]
coronacentral["response"] = altmetrics
cc_filtered = coronacentral[coronacentral["response"] == True]

print("Filtered by Altmetric")

# store the contents of the documents so they can be reranked by classifier score
coronacentral_doc_contents = cc_filtered[['docno', 'title', 'abstract']]
coronacentral_doc_contents['text'] = coronacentral_doc_contents['title'] + \
    '\n' + coronacentral_doc_contents['abstract']
coronacentral_doc_contents = coronacentral_doc_contents.drop(
    columns=['title', 'abstract'])
coronacentral_doc_contents.to_csv(
    "coronacentral.csv", index=False, header=True)

print("Saved documents for later")
