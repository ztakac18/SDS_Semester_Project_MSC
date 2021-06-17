# SDS_Semester_Project_MSC
 semester_project


We recommend opening the .ipynb files in colab, as it will allow for viewing interactive graphs.


## The intended order of viewing files:

**1. Bibliometric analysis**

*This file is disconnected from the rest of the pipeline, it's just the analysis of our search string for the projects literature review*


**2. Exploratory analysis**

*In this notebook we're downloading stock data and conducting exploratory analysis based on which a set of companies to be used for SML is chosen. At the end of the file a dataset with all the needed data for selected companies is exported.*


**3. Twitter scraper**

*This code was run in the visual studio code console to scrape the tweets for the four companies chosen in the previous notebook*


**4. Title scraper**

*This code was run in visual studio code, because scraping was too time consuming to be run in colab (taking multiple days per dataset).*


**5. Supervised ml without text data**

*This notebook uses the data acquired in notebook 2 to do random forest regression, linear regression and a simple neural network for stock predictions*
    

**6. Supervised ml with text data**

*The notebook using stock data and the scraped headlines for stock prediction to run additiional machine learning models*


**7. Backtesting**

*The notebook providing final financial insight into the models*



## Contents of the data folder:

**- ticker_data.zip** - the databases with the tweets about the three chosen companies (out of four - the tesla one was too big even after zipping, we will figure out a way to provide it if it will be used in code)

**- proc_ticker_data.csv** - the databases containing headlines of news articles for the chosen companies

**- raw_partner_headlines.csv.zip** - a very large dataset containing many financial news titles, we're using it for training the embedding layer (to avoid fitting it specifically to our data). Source: https://www.kaggle.com/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests

**- sentiment_data.csv** - dataset for training a sentiment model. Source: https://www.kaggle.com/ankurzing/sentiment-analysis-for-financial-news

**- yf_chosen_comp.csv** - the dataset created in the notebook from point 2. Contains daily closing information for the chosen companies.

**- bibliometric_data.csv** - the scopus dataset for our literature review search string

**- ticker_pred.csv** - a dataset containing all the predictions for the companies used in backtesting file
