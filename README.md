# Level 4 Project - Searching for Coronavirus Literature

Primary Goal - Designing and Evaluating information retrieval methods which make use of [CoronaBERT](https://huggingface.co/jakelever/coronabert) on the CORD-19 dataset, in line with Round 5 of TREC-COVID.

Secondary Goal - Building an information retrieval system to perform optimally with [CoronaCentral](https://coronacentral.ai/)

## Contributors

David O'Neill - Student</br>
Jake Lever - Supervisor

## Datasets

Under the <em>Datasets</em> directory, there is a collection of datasets required for the purpose of the project, in order to make the execution of experiments more efficient. They can be downloaded in the accompanying notebooks.

## Models

Under the <em>Models</em> directory, there is a collection of models created for the project. They are stored in the repo in order to provide quick access to them in the notebooks, instead of requiring to create and train the models each time they are required.

## Notebooks

Under the <em>Notebooks</em> directory, there is a collection of .ipynb notebooks which provide all the practical experiments and analysis carried out for the project, which is detailed extensively in the dissertation. They are ready to run but may take a significant amount of processing time. As such, I would suggest downloading the particular notebook and running it in Google Colab. For the compuatationally intense notebooks, such as those dealing with neural indexing and reranking, I would highly recommend using the Colab GPU to speed up execution.

## Installation and Usage

In order to run the CoronaCentral IR tool locally, it is best to view it using the provided front-end using the following instructions:

1. Clone the repository

2. In the API V2 directory add the latest version of CoronaCentral, named <em>coronacentral.json.gz</em>.

3. Create a new virtual environment and install all the dependencies via requirements.txt.

4. Run the file <em>indexing.py</em> which will automatically index the CoronaCentral dataset and also create a .csv file for easy access to the altmetric scores. This execution should take around 5 minutes (depending on the machine) and is very computationally intensive.

5. Run the file <em>application.py</em> which will start running the RESTful API for the IR tool. Now API calls can be made directly, returning raw json which simply contains a list of the IDs for the documents retrieved.

6. In order to view this in a clearer format, open a new command prompt, ensuring the API is still running. Navigate to the directory <em>api-front-end</em> and run the command <em>npm run dev</em>. From there, the front end will be accessible to view the results in a more convenient manner.

## Licence

TBC
