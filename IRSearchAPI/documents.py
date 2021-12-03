import pandas as pd

import json
import gzip

import pyterrier as pt

if not pt.started():
    pt.init()


class Documents(object):

    def __init__(self):

        index = pt.IndexFactory.of(
            "C:/Users/david/Workspace/level-4-project/SampleIRSystem/index_docs/data.properties")

        with gzip.open('dataset/coronacentral_with_altmetric.json.gz', 'r') as f:
            print("Reading file")
            cc = f.read()

            json_str = cc.decode('utf-8')
            data = json.loads(json_str)
            print("File read")
            self.coronacentral = pd.DataFrame.from_dict(data)
            self.coronacentral = self.coronacentral.rename(
                columns={'cord_uid': 'docno'})

        # filter it down to remove docs without altmetric
        altmetrics = self.coronacentral['altmetric']
        altmetrics = [altmetric['response'] for altmetric in altmetrics]
        self.coronacentral['response'] = altmetrics
        self.coronacentral = self.coronacentral[self.coronacentral['response'] == True]

        altmetric_scores = self.coronacentral['altmetric']
        scores = []
        for altmetric in altmetric_scores:
            if 'score' in dict(altmetric):
                scores.append(altmetric['score'])
            else:
                scores.append(0)

        self.coronacentral['score'] = scores

        print("Dataframe created")
        # get tf_idf representation of it
        self.tf_idf = pt.BatchRetrieve(index, wmodel="TF_IDF")

    def get_documents(self, query):
        # return the documents which were retrieved as json
        results = self.tf_idf(query)
        doc_results = self.coronacentral[self.coronacentral['docno'].isin(results['docno'])].sort_values(
            by='score', ascending=False)[['title', 'abstract', 'score']]
        return doc_results.to_dict("records")
