# USAGE:
# python create_daily_post.py cat1,cat2 tagX,tagY,tagZed 'Parks n Rec'

import requests
import os, sys, json
from datetime import datetime
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint

api_instance = giphy_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.

# FNAME

now = datetime.now()
title = now.strftime("%B-%d,-%Y")
fname = './_posts/'+now.strftime('%Y')+'-'+now.strftime('%m')+'-'+now.strftime('%d')+'-'+title+'.md'

# FRONTMATTER

categories = sys.argv[1]
if categories:
    categories = categories.replace(',',', ')
tags = sys.argv[2]
if tags:
    tags = tags.replace(',',', ')
frontmatter = '---\ntitle: {}\nauthor: PT\ndate: {} 00:00:00 −0500\ncategories: [{}]\ntags: [{}]\n---\n'.format(title.replace('-',' '), now.strftime('%Y-%m-%d'), categories, tags)

# RANDOM QUOTE

quote = 'Find one yourself, lazy.'
res = requests.get('http://api.forismatic.com/api/1.0/', {'method':'getQuote','lang':'en','format':'json'})
if res:
    quote = json.loads(res.text)['quoteText'].strip()
quote_md = '\n# Quote of the Day\n> '+quote+'\n'

# RANDOM GIF

giftag = sys.argv[3]    
if not giftag:
    giftag = 'The Office'
# api_response = api_instance.gifs_random_get(api_key, tag=giftag, rating='g', fmt='json')
# url = api_response.data.url
url = 'https://giphy.com/gifs/MofD6FusyLKzktNYPp'
gif_md = '<iframe src=\"https://giphy.com/embed/{}\" width=\"480\" height=\"285\" frameBorder=\"0\" class=\"giphy-embed\" allowFullScreen></iframe>'.format(url.split('/')[-1])

# CREATE FILE

os.system('touch '+fname)
with open(fname, 'w') as f:
    f.write(frontmatter)
    f.write(quote_md)
    f.write(gif_md) 
print('Done.')
