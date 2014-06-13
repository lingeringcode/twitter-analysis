# Twitter analysis tools

A repo for some of my twitter data analysis/viz scripts/work.

## In Python

### dup-rm.py

This script removes duplicate entries, when merging multiple twitter archives.

### keyword_csv.py

This is a commandline tool to extract tweets that mention the provided keyword from a json file, which then provides a csv file as output with the time of the tweet and the tweet itself.

### wordcount.py

This is script that tallies up how many times a word is used within a corpus of tweets. It then creates a simple CSV file with the word, its respective count, and respective id numbers. Here is a website using data created from this script: http://rsa14cloud.clindgrencv.com/

### iPython Notebooks

Example ipython notebook entries, utilizing the keyword csv data output.

## In Javascript/d3.js

The d3.js directory currently contains my first, simple attempt to produce a line graph that uses the mousemove() to display the respective word and its count as the mouse hovers along the x-axis.