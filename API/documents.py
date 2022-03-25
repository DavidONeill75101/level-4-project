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

        # get BM25 representation of it, ensuring to get the metadata at the same time
        self.bm25 = pt.BatchRetrieve(
            index, wmodel="BM25", metadata=["title", "abstract"])
        print("BM25 retrieval done")

        # get the classification model
        url = 'https://github.com/DavidONeill75101/level-4-project/blob/master/Models/mlpclassifier_coronaBERT.pickle?raw=true'
        filename = wget.download(url)
        self.classifier = pickle.load(open(filename, 'rb'))
        print("got classifier")

        # prepare for using CoronaBERT
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

    def get_score(self, title, abstract, query):
        # concatenate doc title and abstract
        doc = title + "\n" + abstract

        # get embeddings
        query_embedding = self.text_to_embed(query)
        doc_embedding = self.text_to_embed(doc)
        concat_embedding = np.concatenate([query_embedding, doc_embedding])

        # make prediction
        prediction = self.classifier.predict_proba([concat_embedding])[0]
        score = prediction[1]
        return score

    def get_documents(self, query):

        # transformer used for reranking by CoronaBERT relevance score
        scorer = pt.apply.doc_score(lambda row: self.get_score(
            row['title'], row['abstract'], query))

        # create pipeline which performs BM25 retrieval and reranks top 24 docs by CoronaBERT relevance score
        pipeline = (self.bm25 % 24) >> scorer
        results = pipeline.search(query)

        # return the results as a dictionary for json output
        return results.to_dict("records")
