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


indexer = pt.DFIndexer(
    os.path.join(sys.path[0], "index_docs"), overwrite=True
)
index_ref = indexer.index(
    cc_filtered["title"] + '\n' +
    cc_filtered["abstract"], cc_filtered["docno"], cc_filtered['title'], cc_filtered['abstract']
)
index_ref.toString()
index = pt.IndexFactory.of(index_ref)

print("Created index")
