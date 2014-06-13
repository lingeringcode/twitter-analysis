import json
import sys
from collections import OrderedDict

'''
	removes duplicate tweets from merged corpuses:
	TAGSExplorer and TweetArchive

	My 2 respective json files were first merged using
	kinlane's tool @: https://github.com/kinlane/data-json-file-merger/
'''

json_file = "enter file path here"
json_loaded = json.load(open(json_file), object_pairs_hook=OrderedDict)
seen = OrderedDict()
for id_check in json_loaded:
    old_id = id_check["idstr"]
    if old_id not in seen:
        seen[old_id] = id_check

json.dump(seen.values(), sys.stdout,  indent=2)