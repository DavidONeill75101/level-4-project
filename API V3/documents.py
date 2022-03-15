import pandas as pd
import numpy as np
import pickle
import wget
import os
import sys
import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification

import pyterrier as pt

if not pt.started():
    pt.init()


class Documents(object):
    def __init__(self):

        # load index - insert any path to data.properties
        index = pt.IndexFactory.of(
            os.path.join(sys.path[0], "index_docs/data.properties")
        )
        print("Index created")

        # get tf_idf representation of it
        self.bm25 = pt.BatchRetrieve(index, wmodel="BM25")
        print("BM25 retrieval done")

        # load coronacentral docnos and scores
        self.coronacentral = pd.read_csv('coronacentral.csv')
        print("Got doc contents")

        # get the classification model
        url = 'https://github.com/DavidONeill75101/level-4-project/blob/master/Models/mlpclassifier_coronaBERT.pickle?raw=true'
        filename = wget.download(url)
        self.classifier = pickle.load(open(filename, 'rb'))
        print("got classifier")
        print(self.classifier)

        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained("jakelever/coronabert")
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "jakelever/coronabert", output_hidden_states=True)
        self.model = self.model.to(self.device)
        print("prepared transformers")

    def text_to_embed(self, text):
        # Tokenize it with appropriate padding and truncation
        inputs = self.tokenizer(text, return_tensors="pt",
                                padding=True, truncation=True, max_length=500)

        # Move the IDs of the tokens over to the GPU
        input_ids = inputs['input_ids'].to(self.device)

        # Run the model on the data
        outputs = self.model(input_ids=input_ids)

        # Extract the embeddings
        with torch.no_grad():
            # Get the final layer of the neural network, and average the embedding for all the tokens
            # Some researchers use the vector just for the first or final token of the sentence
            # instead of an average. I don't think there is a definitive best approach.
            # You could stick to the mean for now.
            embed = outputs.hidden_states[-1].squeeze().mean(axis=0)

            # Return the embedding to the CPU and convert to a numpy array
            embed = embed.cpu().numpy()

        return embed

    def get_documents(self, query):

        # search for results given the query
        results = self.bm25(query)

        top_results = results[:24]

        query_embedding = self.text_to_embed(query)

        docnos = top_results['docno']

        doc_embeddings = []
        for docno in docnos:
            doc_content = self.coronacentral[self.coronacentral['docno']
                                             == docno].iloc[0]['text']
            doc_embeddings.append(self.text_to_embed(doc_content))

        overall_embeddings = [np.concatenate(
            [query_embedding, doc_embedding]) for doc_embedding in doc_embeddings]

        predictions = self.classifier.predict_proba(overall_embeddings)
        scores = [prediction[1] for prediction in predictions]

        docno_scores = [[docno, score] for docno, score in zip(docnos, scores)]

        reranked = pd.DataFrame(docno_scores, columns=['docno', 'score']).sort_values(
            by='score', ascending=False)
        reranked['rank'] = list(range(len(docno_scores)))
        reranked['qid'] = [str(query) for i in range(len(docno_scores))]

        return reranked.to_dict("records")
