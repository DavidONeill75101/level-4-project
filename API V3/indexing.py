'''
takes ~5 minutes to run this and is very computationally intensive
'''

import pandas as pd

import json
import gzip
import os
import sys

import pyterrier as pt

if not pt.started():
    pt.init()


# load the coronacentral dataset
# you must insert the latest version of coronacentral into the API V3 directory and name it coronacentral.json.gz
with gzip.open("coronacentral.json.gz", "r") as f:
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

# create index
indexer = pt.DFIndexer(
    os.path.join(sys.path[0], "index_docs"), overwrite=True
)
index_ref = indexer.index(
    cc_filtered["title"] + '\n' + cc_filtered["abstract"], cc_filtered["docno"]
)
index_ref.toString()
index = pt.IndexFactory.of(index_ref)

print("Created index")
