# India WhatsApp Fake News Dataset [![DOI](https://zenodo.org/badge/157810232.svg)](https://zenodo.org/badge/latestdoi/157810232)

The following repository consists of about !million+ News Articles scraped from the Times of India website, from late 2017 to June 2018. 

The data was then checked for keyowrds which could point us to news articles which covered stories about WhatsApp fake news cases in India, which was a growing concern at that time. To be clear, this is **not a dataset for fake articles**


### Details 
- The file `Data.csv` has the following files, with the date, place, and the keywords mentioned. 
- The `webscrapper` consists of a `scrapy` spider which can be used to extract files from the news site
- The files `archivelist_finder.py` and `extract_csv_data.py` can be used for reference in the process


### Labelling Data and Insights

After textfiles were preprocessed, keywords were found in the following dataset, which were selected to find news articles which had a good probabilty of being articles **about** Fake News. These were then crosschecked to see if the stories did correspond to them. 

The following data was used by the BBC in order to help generate useful insights about Fake News trends in India, what type of fake news cases were being spread and how they were being spread. 


 The complete file containing all articles in the form of `.txt` files can be found at the following link. https://drive.google.com/file/d/19IbOlTO18BAXYRQoVkWfQ6paad4v9sfB/view?usp=sharing
 
 
 ### Interesting things which could be done with this dataset
 
 A few helper ideas in case you were wondering, how this dataset can be useful.
 
 1. Understanding fake news trends (the initial idea of this project). Could probably be extended to identifying trends and interesting facts, while trying to understand contemporary articles to them
 
 2. Understanding news headlines. If news headlines to these articles definitely portray the matter they have. 
 3. Is there a particular trend for newspaper articles? News paper websites have been known to put click bait articles to help increase CTR for their website, but however contain matter which is questionable. 
 
 4. Understanding quality of news articles. What makes a good news artcile?
 
 These are some few good ideas, which I believe have a large potential in the field of Data journalism. Do feel free to open an issue, regarding any query related to this. 
 
 
https://zenodo.org/badge/latestdoi/157810232

Please do cite this repository if you happen to use this dataset in your research. :smiley:

