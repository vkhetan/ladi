
### Latin American Digital Initiative Newspaper OCR

Our project uses Google's Vision and Natural Language APIs to generate text transcriptions and name entity values for a Spanish language corpus from 19th century newspapers from the Latin American Digital Initiative (LADI) collection. The generated text values feed into a select group of elements from an existing MODS-compliant metadata schema. 

### Getting Started
To reproduce this work, one needs to have working knowledge of python and unix. The following tasks must also be completed prior to executing optical character recognition or natural language processing activities outlined in this project. 

- Sign in or create Google cloud account
- set up a Linux Instance with `Ubuntu 16.04.3 LTS`
- Configure the google vision api first. documentation 
- Enable Billing
- Create a Cloud Storage bucket
- Enable Cloud Vision API
- Set up Cloud Platform Console project
- Enable Cloud Natural Language for project
- Download a private key as JSON
- Authenticate Cloud Natural Language API using code

### Motivation

Prior to the OCR of the newspapers, news content were not searchable beyond item level descriptions. Our project gathered key terms such as PERSON, LOCATION,  and ORGANIZATION to facilitate researchers to search across content from the newspaper articles. The tangible feature and added value of this project is the creation of a list of 'topic' properties for each newspaper article that will function as keywords search terms, ultimately providing LADI database users with a more robust, searchable database.  

### Installation
- project utilized python 3.6 using the Google Python Style Guide version 2.59 ( more info: https://google.github.io/styleguide/pyguide.html )

### API Reference
The following links provide guidance on setting up google cloud and activating its vision and nlp apis
- To set up google cloud
	- https://cloud.google.com/dataproc/docs/guides/setup-project
- To get vision api working
	- https://cloud.google.com/vision/docs/quickstart
- To get language api working
	- https://cloud.google.com/natural-language/docs/getting-started 

### Contributors

Project contributors include Itza Carbajal, Vivek Khetan, Emma Whittington as part of a Metadata Generation and Interfaces for Massive Datasets graduate course taught by Unmil Karadkar at the University of Texas School of Information.
