#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:30:30 2018

@author: Sahit
"""


#whatsapp && (police || arrest || crime || jail || lynch || kill || fire || riots || hate || death || dead || FIR)



import pandas as pd
import os
import nltk
import re

folder = nltk.data.find(
    '/Users/Sahit/Documents/GitHub/Article-Analysis/webscrapper/webscrapper/article_data')

path = '/Users/Sahit/Documents/GitHub/Article-Analysis/webscrapper/webscrapper/article_data'
dirListing = os.listdir(path)
editFiles = []
for item in dirListing:
    if ".txt" in item:
        editFiles.append(path+'/'+item)
print len(editFiles)

g = open('article_links_final.txt', 'r')
g = g.read().split('--')


def get_dictionary_word_list(filepath):
    # with context manager assures us the
    # file will be closed when leaving the scope
    with open(filepath) as f:
        # return the split results, which is all the words in the file.
        return f.read().lower().split()


def get_keywords(text):
    keywords = []
    lst = ['police', 'arrest', 'crime', 'jail', 'lynch', 'kill', 'fire', 'riots', 'hate', 'death', 'dead', 'fir']
    flag = 0
    if 'whatsapp' in text:
        keywords.append('whatsapp')
        for word in lst:
            if word in text:
                keywords.append(word)
                flag = 1            
    keywords.append(flag)
    return keywords


data = []
t = 0
for filepath in editFiles:
    entry = {}
    id = re.search(r'(\d+).txt$', filepath)
    filepath_num = int(id.group(1))-1
    entry['link'] = g[filepath_num]
    content = get_dictionary_word_list(filepath)
    try:
        place_ = re.search(r'([a-zA-Z]+):', content[0])
        try:
            place = place_.group(1)
        except:
            place = 'NA'
    except:
        place = 'NA'

    _date_ = re.search(r'^/Users/Sahit/Documents/GitHub/Article-Analysis/webscrapper/webscrapper/article_data/(\d+)-(\d+)-(\d+)T', filepath)
    try:
        year = _date_.group(1)
    except:
        year = 'NA'
    try:
        month = _date_.group(2)
    except:
        month = 'NA'
    try:
        day = _date_.group(3)
    except:
        day = 'NA'

    date = str(year)+'/'+str(month)+'/'+str(day)

    l = get_keywords(content)
    flag = l[-1]
    keywords = l[:-1]


    entry['year'] = year
    entry['month'] = month
    entry['day'] = day
    entry['date'] = date
    entry['place'] = place
    entry['id'] = filepath_num+1
    entry['publisher'] = 'TOI'
    #entry['content'] = content
    entry['filename'] = filepath
    entry['flag'] = flag
    entry['keywords'] = keywords
    if flag == 1:
        data.append(entry)
    t += 1
    

article_df = pd.DataFrame(data)
#print article_df

article_df.to_csv('data_nec.csv')








