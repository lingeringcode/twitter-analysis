import sys,json,csv,codecs,argparse,re,datetime
import pandas as pd
from datetime import datetime
from time import strptime

'''
	I want to add the following argparse options later:
		1. input json file
		2. output csv file
'''

json_file = "merge.json" # change to your input/json file
time = []
kwtweet = []
count = []
archive_content = []

parser = argparse.ArgumentParser(usage="-h for full usage")
parser.add_argument('-k', dest="keyword", help='keyword to search twitter corpus, e.g. rhetoric',required=True)
parser.add_argument('-output', dest="output", help='CSV file name to save results',required=False)
args = parser.parse_args()
keyword = args.keyword
filename = args.output


f = open(keyword+"_rsaCount.csv", 'wb')
writer = csv.writer(f, lineterminator='\r\n')
writer.writerow(['time','kwtweet'])

def prime_writer():

	with codecs.open(json_file, encoding="utf-8-sig") as data_file:
		data = json.load(data_file)
	return data

def get_tweets(archive_content, keyword):

	for tweet in archive_content:
		
		dirty_time = tweet['createdat'].encode('utf-8')
		new_time = date_formatter(dirty_time)
		time = new_time

		kwtweet = tweet['text'].lower().encode('utf-8')

		if keyword in kwtweet:
			written_csv = writer.writerow([time, kwtweet])
	
	return written_csv

def date_formatter(dirty_time):

	clean_time = re.sub(('\+0000 '), (r''), dirty_time)
	a = re.compile("^([0-9])")

	if a.match(clean_time):
		clean_time = re.sub(('T'), (r' '), dirty_time)
		clean_time = datetime.strptime(clean_time, '%Y-%m-%d %H:%M:%S')

	else:
		clean_time = datetime.strptime(clean_time, '%c')

	return clean_time

def main():
	archive_content = prime_writer()
	get_tweets(archive_content, keyword)

if __name__ == '__main__':
	main()