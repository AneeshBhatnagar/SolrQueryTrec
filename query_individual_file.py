# -*- coding: utf-8 -*-
"""
A program to do the following:
- Run multiple queries on a Solr instance (fetched from a text file)
- Format for input query is xxx <Query>, 
	where xxx is the query number and <Query> is the query text
- Save the returned output in a file in Trec format for the Trec Evaluation 
Thanks to the author Ruhan Sa, who was the TA of IR Project 3 in Fall 2015 for providing the
initial code
"""
import json
import urllib2


queryFile = open('test_query.txt')
queries = queryFile.readlines();
qId = ''
qText = ''
IRModel='BM25'
fileCount = 1

for q in queries:
	f = open(IRModel +"/" + str(fileCount)+".txt","w")	
	qID, qText = map(str, q.strip().split(" ",1))
	qText = qText.replace(":","\:")
	qText = urllib2.quote(qText)
	inurl = 'http://localhost:8983/solr/train/select?q='+qText+'&fl=id%2Cscore&wt=json&indent=true&rows=20&qf=tweet_hashtags^1.2%20text_en^1.6%20text_de^1.5%20text_ru^1.6&defType=dismax'
	data = urllib2.urlopen(inurl)
	docs = json.load(data)['response']['docs']
	rank = 1
	for doc in docs:
		f.write(qID + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
		rank += 1
	f.close()
	fileCount+=1

queryFile.close()