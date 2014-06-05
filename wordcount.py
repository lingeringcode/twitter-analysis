import re,sys,csv,json,collections

stopwords = set([ "rt","teh","i","me","my","myself","we","us","#rsa14","rsa14","http","amp","like",
                                "our","ours","ourselves","you","your","yours","yourself","just",
                                "yourselves","he","him","his","himself","she","her","hers",
                                "herself","it","its","itself","they","them","their","theirs",
                                "themselves","what","which","who","whom","whose","this",
                                "that","these","those","am","is","are","was","were","be","been",
                                "being","have","has","had","having","do","does","did","doing",
                                "will","would","should","can","could","ought","i'm","you're","he's",
                                "she's","it's","we're","they're","i've","you've","we've","they've",
                                "i'd","you'd","he'd","she'd","we'd","they'd","i'll","you'll","he'll",
                                "she'll","we'll","they'll","isn't","aren't","wasn't","weren't","hasn't",
                                "haven't","hadn't","doesn't","don't","didn't","won't","wouldn't","wont",
                                "shouldn't","can't","cannot","couldn't","mustn't","let's","that's","who's",
                                "what's","here's","there's","when's","where's","why's","how's","a","an",
                                "the","and","but","if","or","because","as","until","while","of","at","by","for",
                                "with","about","against","between","into","through","during","before","after",
                                "above","below","to","from","up","upon","down","in","out","on","off","over",
                                "under","again","further","then","once","here","there","when","where",
                                "why","how","all","any","both","each","few","more","most","other","some",
                                "such","no","nor","not","only","own","same","so","than","too","very","say","says","said","shall"])
re_word = re.compile(r'[a-z0-9\']+')
words = collections.Counter()

def tally_words():
    for tweets in json.load(open('merge.json')):
        for word in re_word.findall(tweets['text'].lower()):
            if len(word) > 2 and word not in stopwords:
                words[word] += 1

def write_word_count():
    with open('testing_rsaCount.csv', 'wb') as c:
        writer = csv.writer(c, lineterminator='\n')
        writer.writerow(['word', 'count'])
        for word, count in words.most_common():
            writer.writerow([word.encode('utf8'), count])

def main():
    tally_words()
    write_word_count()

if __name__ == '__main__':
    main()