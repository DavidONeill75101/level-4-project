# Level 4 Project - Searching for Coronavirus Literature - Manual

## Notebooks

### Document Encoding

The process of encoding documents using BERT based models is time consuming and so I performed these tasks in a series of notebooks and saved the results in the [Datasets](./Datasets/) directory. The notebooks have been run and the results are visible but if you would like to re-run them, simply run all the cells. I would advise doing this on a Google Colab GPU as it can be very time consuming and resource intensive.

### Experiments

As I aimed to make my experiments repeatable, I created a series of Python Notebooks in which they could easily be repeated. To re-run an experiment, simply download the corresponding Notebook, open it in Google Colab and execute all the cells. For the notebooks which make use of neural indexing, neural reranking or natural language processing, I would suggest making use of the Colab GPU.

### Miscellaneous Analysis

For the <em>Discussion</em> section of the dissertation, it was necessary to perform some analysis of the datasets in question. The notebooks used to do so are ready to be executed.

### Model Creation

There are notebooks which were used to create the CoronaBERT models. They are ready to run, but do take some time to train. Consequently, the models have been saved in the repository under the [Models](./Models/) directory.

## CoronaCentral Search API

In order to run the CoronaCentral search API locally, it is best to view it using the provided front-end using the following instructions:

1. Clone the repository

   ```console
   git clone https://github.com/DavidONeill75101/level-4-project
   ```

2. In the API directory add the latest version of CoronaCentral, named <em>coronacentral.json.gz</em>.

3. Navigate to the API directory

   ```console
   cd API
   ```

4. Create a new Python 3 virtual environment and install all the dependencies via requirements.txt.

   ```console
   pip install -r requirements.txt
   ```

5. Run the file <em>indexing.py</em> which will automatically retrieve the documents from the CoronaCentral dataset and perform the necessary preprocessing. There will be warnings which can be ignored.

   ```console
   python indexing.py
   ```

6. Run the file <em>application.py</em> which will start running the RESTful API for the IR tool. Now API calls can be made directly, returning raw JSON which simply contains a list of the IDs for the documents retrieved. There will be warnings which can be ignored.

   ```console
   python application.py
   ```

7. To access this raw JSON, simply access the following URL in a browser:

   http://127.0.0.1:5000/search?query=insert_you_query_here

8. In order to view this in a clearer format, open a new command prompt, ensuring the API is still running. Navigate to the directory <em>api-front-end</em> and run the command <em>npm run dev</em>.

   ```console
   cd api-front-end
   npm run dev
   ```

9. To access the application, simply access the following URL in a browser:

   http://127.0.0.1:3000

10. Use the search bar to receive a list of the returned documents for your query. It is possible that if a query returns no documents an error will occur.
