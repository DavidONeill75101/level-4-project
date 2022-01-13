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


# load latest version of coronacentral
with gzip.open("coronacentral.json.gz", "r") as f:
    cc = f.read()

    json_str = cc.decode("utf-8")
    data = json.loads(json_str)

    coronacentral = pd.DataFrame.from_dict(data)

    coronacentral = coronacentral.rename(columns={"cord_uid": "docno"})

# filter it down to remove docs without altmetric
altmetrics = coronacentral["altmetric"]
altmetrics = [altmetric["response"] for altmetric in altmetrics]
coronacentral["response"] = altmetrics
cc_filtered = coronacentral[coronacentral["response"] == True]

# add altmetric scores as a column
altmetric_scores = cc_filtered["altmetric"]
scores = []
for altmetric in altmetric_scores:
    if "score" in dict(altmetric):
        scores.append(altmetric["score"])
    else:
        scores.append(0)
cc_filtered["score"] = scores


# save new dataframe which only has docnos and scores for quicker access in API
docnos_to_scores = cc_filtered[['docno', 'score']]
docnos_to_scores.to_csv(
    "scores.csv", index=False, header=True)
print("CSV Created")

# create index
indexer = pt.DFIndexer(
    os.path.join(sys.path[0], "index_docs"), overwrite=True
)
index_ref = indexer.index(
    cc_filtered["title"] + cc_filtered["abstract"], cc_filtered["docno"]
)
index_ref.toString()
index = pt.IndexFactory.of(index_ref)
