# importing the needed packages
import pandas as pd
import re
import numpy as np
import csv
import newspaper

# definig the function that gets the article titles (using newspaper3k)
def get_titles(url):
    try:
        article = newspaper.Article(url) 
        article.download() 
        article.parse() 
        return article.title
# this prevents the function from throwing an error when a link has been removed
    except:
        return None


# here any of the csv files can be inserted
csv_file = 'amzn_data.csv'

# importing the file in a bit of a weird way
# the csv file is space delimeted, but spaces are also present within the tweets, so pandas can't be used
# instead taking first 5 coma separated words as first 5 columns and everything that remains as the 6th one
with open(csv_file, 'r+', encoding='utf-8') as f:
    data = []
    lines = f.readlines()
    for line in lines:
        try:
            text = line.split(' ')
            data.append([text[0], text[1], text[2], text[3], text[4], ' '.join(text[5:])])
        except:
            data.append([None, None, None, None, None, None])
                              
    # regular expression pattern for identifying any url
    regex = r"http\S+"

    # finding all urls within the tweets and appending them to the dataset
    for i, tweet in enumerate(data):
        text = str(tweet[5])
        links = re.findall(regex, text)
        data[i].append(links)

    # creating a dataframe, only selecting the column with the date and a link
    data = pd.DataFrame(data)
    data = data.loc[:,[1,6]]
    data.rename(columns={6: 'link'},inplace=True)

    # in case multiple links were found, putting them in separate rows with the same date
    data = pd.DataFrame({
            col:np.repeat(data[col].values, data["link"].str.len())
            for col in data.columns.drop("link")}
            ).assign(**{"link":np.concatenate(data["link"].values)})[data.columns]
    
    # dropping any duplicate links
    data.drop_duplicates(inplace=True)
    # applying the function that finds article titles to all the links
    data["title"] = data["link"].map(lambda x: get_titles(x))
    # dropping the missing values
    data.dropna(inplace=True)
    # saving the file
    data.to_csv("proc_"+csv_file)


