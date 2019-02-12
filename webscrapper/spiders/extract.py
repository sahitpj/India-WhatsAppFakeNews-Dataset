

'''in your shell type "scrapy shell" 


After the shell opens open do the following 

f = open('article_links_final.txt', 'r')
article_links = f.read().split()

to see if it was loaded successfully,  type len(article_links) , you should get an answer of about 10lacs

then run the following code


fill "number_of_choice", with the starting index of the article you wat to scrape.


scrapped article indecies

0-2lac
3lac - 3010000


Make sure you have a article_data directory because that is where the files will be saved. You can change if you want


to retrive data, run the extract_csv_data.py file
'''


# the following to be run on scrapy shell

#


'''
t = 0
for link in xrange(number_of _choice, len(article_links)):
    fetch(article_links[link])
    r = response.css('div.Normal::text').extract()
    p = response.css('meta[itemprop="dateModified"]::attr(content)').extract()
    print p,r
    if r != [] and p != []:
        text = ' '.join(r).encode('utf-8')
        string = 'article_data/'+p[0]+'->'+str(link+1)+'.txt'
        f = open(string, 'w')
        f.write(text)
        f.close()
        t += 1
        print ''
        print 'an article has been extracted'
        print ''
        print t
    if t == 1000: #this value is the batch size of the number of files you want to scrape
        break
    print link    











