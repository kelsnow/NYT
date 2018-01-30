#new yorks times 

from secrets import *
import requests



CACHE_FNAME = 'cache_file_name.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

except:
    CACHE_DICTION = {}


def params_unique_combination(baseurl, params):
    alphabetized_keys = sorted(params.keys())
    res = []
    for k in alphabetized_keys:
        res.append("{}-{}".format(k, params[k]))
    return baseurl + "_".join(res)



# gets stories from a particular section of NY times
def get_stories(section):

    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': nyt_key}
    unique_ident = params_unique_combination(baseurl,params)

    if unique_ident in CACHE_DICTION:
    	return CACHE_DICTION[unique_ident]
    else:
    	print("Making a request for new data"):
    	resp = requests.get(extendedurl, params).json()
    	dumped_json_cache = json.dumps(CACHE_DICTION)
    	fw = open(CACHE_FNAME,"w")
    	fw.write(dumped_json_cache)
    	fw.close()
    	return CACHE_DICTION[unique_ident]

   


def get_headlines(nyt_results_dict):
    results = nyt_results_dict['results']
    headlines = []
    for r in results:
        headlines.append(r['title'])
    return headlines

story_list_json = get_stories('science')
headlines = get_headlines(story_list_json)
for h in headlines:
    print(h)


