from twitter_scraper import get_tweets
tuites = []
for t in  get_tweets('jairbolsonaro'):
    d = {'text':t['text'], 'likes':t['likes']}
    tuites.append(d)
    
def criterio(tuite): return tuite['likes']
tuites_ordenados = sorted(tuites, key=criterio, reverse=True)
for t in tuites_ordenados[:10]:
    print (t['text'], t['likes'])
