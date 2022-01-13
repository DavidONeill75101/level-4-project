# Level 4 Project - Searching for Coronavirus Literature

Building and evaluating an information retrieval system to perform optimally with [CoronaCentral](https://coronacentral.ai/)

## Contributors

David O'Neill - Student</br>
Jake Lever - Supervisor

## Design

Below are a collection of Colab Notebooks providing experiments carried out on the CoronaCentral dataset during the design stage:

Metadata Analysis</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1b5oL0K_blDHHBnFKBPsxYISg9W6HojXO?usp=sharing)

Document Embedding Analysis</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1eQIZUgrNlgZHViHKBc5HCMoFi3rS6KZ_?usp=sharing)

Removing Boilerplate Information</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1L2VaXN7czK3iZfboi5r-lbRXj4nm7MUc?usp=sharing)

Feature Training Analysis</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16JLjoqqwPkfmpLh9hBNMS6CMxBqr8nvo?usp=sharing)

Neural Indexing Analysis</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-mVRfvf0SlOPlfjumdcF8ulxIUe6aNSD?usp=sharing)

Neural Reranking Analysis</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15d1H5gO6_hEYsOsQdT5Pg7XI1Zjjys-9?usp=sharing)

## Implementation

The first iteration of the information retrieval tool is shown in the Colab notebook below:</br>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17ouHiejxzF8bG_JGqq8efg56cBOMHgb-?usp=sharing)

## Evaluation

Evaluations of the information retrieval tool are detailed in the Colab notebooks below:

CoronaCentral Search Log Analysis</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1iVV0BnRDYnh3itJti2XeG37c1Rog9_sN?usp=sharing)

Error Analysis</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11ffvxjqEDkW7E7sPsif74ILeA67YV5nj?usp=sharing)

Pyterrier Evaluations</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16O3MBTAb1LX_fk2jxB118oVyvzCh3-1p?usp=sharing)

Evaluating the Current CoronaCentral Search Tool</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aOiVSNrOw6w97upd-GARGAOFDTJWN5WB?usp=sharing)

Evaluating with searches with "and"</br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1JK_StdUl0XtIJesq0c8gqykspqJlmMEf?usp=sharing)

## Installation and Usage

In order to run the IR tool locally, it is best to view it using the provided front-end using the following instructions:

1. Clone the repository

2. In the API V2 directory, create a sub-directory called <em>dataset</em> and add the latest version of CoronaCentral to it, named <em>coronacentral.json.gz</em>.

3. In the file <em>indexing.py</em>, update line 51 to write the index to API V2 on your local machine.

4. In the file <em>documents.py</em>, update line 14 to read the index from your local machine.

5. Run the file <em>indexing.py</em> which will automatically index the CoronaCentral dataset and also create a .csv file for easy access to the altmetric scores. This execution should take around 5 minutes and is very computationally intensive.

6. Run the file <em>application.py</em> which will start running the RESTful API for the IR tool. Now API calls can be made directly, returning raw json which simply contains a list of the IDs for the documents retrieved.

7. In order to view this in a clearer format, open a new command prompt, ensuring the API is still running. Navigate to the directory <em>api-front-end</em> and run the command <em>npm run dev</em>. From there, the front end will be accessible to view the results in a more convenient manner.

## Licence

TBC
