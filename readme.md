# Query Solr and Save in Trec Format

A Python Script to Query a Solr Instance and save the returned query results into text file(s) in the Trec Evaluation format. This script was made for an Information Retrieval Project at University at Buffalo.

* query_solr.py - Script to query the Solr instance and save the returned output in the trec format in a single file for trec evaluation
* query_individual_file.py - Script to query the Solr instance and save the returned result in trec format in individual files (one file per query, starting from 1.txt to n.txt)

#### Format for the Input Query File:
* One query per line
* xxx QueryText, where xxx is the query number and QueryText is the text that needs to be queried to Solr.


#### Credits:
Credits to Ruhan Sa, who was the TA for the Information Retrieval course in Fall 2015	for providing the initial code to query Solr.
