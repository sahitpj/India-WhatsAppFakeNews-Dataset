#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:30:30 2018

@author: Sahit
"""
from datetime import datetime

f = open('article_month_list.txt', 'r')
l = f.read()
month_links = l.split('--')
#print month_links
import math, re
import pandas as pd


def archivelist_number(year, month, day):
    startdate = datetime(1899, 12, 30, 0, 0)
    finishdate = datetime(year, month, day, 11,0)
    l = finishdate-startdate
    return int(math.floor(l.total_seconds()/86400))

data = []
string = 'https://timesofindia.indiatimes.com/'
for i in month_links:
    year_ = re.search(r'year-(\d+),', i)
    year = int(year_.group(1))
    month_ = re.search(r'month-(\d+).', i)
    month  = int(month_.group(1))
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        for j in xrange(31):
            date = j+1
            p = string+str(year)+'/'+str(month)+'/'+str(date)+'/archivelist/year-'+str(year)+',month-'+str(month)+',starttime-'+str(archivelist_number(year,month, date))+'.cms'
            link_data = {}
            link_data['year'] = year
            link_data['month'] = month
            link_data['day'] = date
            link_data['link'] = p
            data.append(link_data)
    elif month == 2:
        if year%4 == 0:
            for j in xrange(29):
                date = j+1
                p = string+str(year)+'/'+str(month)+'/'+str(date)+'/archivelist/year-'+str(year)+',month-'+str(month)+',starttime-'+str(archivelist_number(year,month, date))+'.cms'
                link_data = {}
                link_data['year'] = year
                link_data['month'] = month
                link_data['day'] = date
                link_data['link'] = p
                data.append(link_data)
        else:
            for j in xrange(28):
                date = j+1
                p = string+str(year)+'/'+str(month)+'/'+str(date)+'/archivelist/year-'+str(year)+',month-'+str(month)+',starttime-'+str(archivelist_number(year,month, date))+'.cms'
                link_data = {}
                link_data['year'] = year
                link_data['month'] = month
                link_data['day'] = date
                link_data['link'] = p
                data.append(link_data)
    elif month != 13:
        for j in xrange(30):
            date = j+1
            p = string+str(year)+'/'+str(month)+'/'+str(date)+'/archivelist/year-'+str(year)+',month-'+str(month)+',starttime-'+str(archivelist_number(year,month, date))+'.cms'
            link_data = {}
            link_data['year'] = year
            link_data['month'] = month
            link_data['day'] = date
            link_data['link'] = p
            data.append(link_data)
    
df = pd.DataFrame(data)
archivelinks = df['link'].values
f = open('archivelist_links.txt', 'w')
f.write('--'.join(archivelinks))
f.close()  