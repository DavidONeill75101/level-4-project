import pandas as pd

import pyterrier as pt

if not pt.started():
    pt.init()


class Documents(object):
    def __init__(self):

        # load index - insert any path to data.properties
        index = pt.IndexFactory.of(
            "C:/Users/david/Workspace/level-4-project/API V2/index_docs/data.properties"
        )

        # get tf_idf representation of it
        self.tf_idf = pt.BatchRetrieve(index, wmodel="TF_IDF")

        # load coronacentral docnos and scores
        self.coronacentral = pd.read_csv('scores.csv')

    def get_documents(self, query):

        # search for results given the query
        results = self.tf_idf(query)

        # sort the results by altmetric and return them
        doc_results = self.coronacentral[
            self.coronacentral["docno"].isin(results["docno"])
        ].sort_values(by="score", ascending=False)[["docno"]]

        return doc_results.to_dict("records")
