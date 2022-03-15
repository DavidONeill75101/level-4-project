# Level 4 Project - Searching for Coronavirus Literature

## Contributors

David O'Neill - Student</br>
Jake Lever - Supervisor

## Goals

Primary Goal - Designing and Evaluating information retrieval methods which make use of [CoronaBERT](https://huggingface.co/jakelever/coronabert) on the [CORD-19](https://www.semanticscholar.org/cord19) dataset, in line with Round 5 of [TREC-COVID](https://ir.nist.gov/trec-covid/).

Secondary Goal - Building an information retrieval system to perform optimally with [CoronaCentral](https://coronacentral.ai/)

## Repository Structure

### Datasets

Under the [Datasets](./Datasets/) directory, there is a collection of datasets required for the purpose of the project, in order to make the execution of experiments more efficient. They are stored on my public GitHub repository for convenience, and are accessed when running the accompanying notebooks.

### Models

Under the [Models](./Models/) directory, there is a collection of models created for the project. They are stored in the repo in order to provide quick access to them in the notebooks, instead of requiring to create and train the models each time they are required.

### Notebooks

Under the [Notebooks](./Notebooks/) directory, there is a collection of Python notebooks which provide all the practical experiments and analysis carried out for the project, which is detailed extensively in the dissertation. They are ready to run but may take a significant amount of processing time. As such, I would suggest downloading the particular notebook and running it in Google Colab. For the compuatationally intense notebooks, such as those dealing with neural indexing and reranking, I would highly recommend using the Colab GPU to speed up execution. Further information regarding the topics of each of the notebooks is detailed in the [manual](./manual.md).

### Project Admin

Under the [Project Admin](./ProjectAdmin/) directory, there is a collection of administrative documents which were required for the project.

### API

Under the [API](./API%20V3/) directory, there is a Flask REST API which has been designed to return search results for the CoronaCentral website. Further guidance on how to run the API locally can be found in the [manual](./manual.md).

### API Front End

Under the [api-front-end](./api-front-end/) directory, there is a Next JS front end application which can be used to view the results of the CoronaCentral REST API in an easy to read format. Further guidance on how to run the front end application locally can be found in the [manual](./manual.md).

## Installation and Usage

### CORD-19 Information Retrieval Experiments

### CoronaCentral Search API

In order to run the CoronaCentral IR tool locally, it is best to view it using the provided front-end using the following instructions:

1. Clone the repository

2. In the API V3 directory add the latest version of CoronaCentral, named <em>coronacentral.json.gz</em>.

3. Create a new virtual environment and install all the dependencies via requirements.txt.

4. Run the file <em>indexing.py</em> which will automatically index the CoronaCentral dataset and also create a .csv file for easy access to the altmetric scores. This execution should take around 5 minutes (depending on the machine) and is very computationally intensive.

5. Run the file <em>application.py</em> which will start running the RESTful API for the IR tool. Now API calls can be made directly, returning raw JSON which simply contains a list of the IDs for the documents retrieved.

6. To access this raw JSON, simply access the following URL in a browser:

   http://127.0.0.1:5000/search?query=insert_you_query_here

7. In order to view this in a clearer format, open a new command prompt, ensuring the API is still running. Navigate to the directory <em>api-front-end</em> and run the command <em>npm run dev</em>. From there, the front end will be accessible to view the results in a more convenient manner.

## Licence

TBC
