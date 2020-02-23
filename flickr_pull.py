#from requests_oauthlib import OAuth1Session
import requests
import re
import os

#secret = 'ee2439ef1cdacc95'
payload = { 'api_key': 'd40d7f5f310fddb83275b08199b49eea' }
photos = []

def flickr_search(tags):
  payload['method'] = 'flickr.photos.search'
  payload['sort'] = 'relevance'
  payload['text'] = tags
  payload['per_page'] = '200'

  r = requests.get('https://api.flickr.com/services/rest/', params=payload)
  text = r.text
  print(text)

  p = re.compile('photo id="(\d*)')
  photo_ids = p.findall(text)
  p = re.compile('secret="([a-z0-9]*)')
  secrets = p.findall(text)
  p = re.compile('server="([0-9]*)')
  server_ids = p.findall(text)
  p = re.compile('farm="([0-9]*)')
  farm_ids = p.findall(text)
  
  for i in range(len(photo_ids)):
    photos.append({ 'photo_id': photo_ids[i],
                    'secret': secrets[i],
                    'farm_id': farm_ids[i],
                    'server_id': server_ids[i]})
  print(photos)

def flickr_download(path):
  i = 0
  for photo in photos:
    name = path + photo['photo_id'] + '.jpg'
    f = open(name, 'wb')
    f.write(requests.get('https://farm{farm_id}.staticflickr.com/{server_id}/{photo_id}_{secret}.jpg'.format(
                             farm_id=photo['farm_id'],
                             server_id=photo['server_id'],
                             photo_id=photo['photo_id'],
                             secret=photo['secret']
                            )).content)
    f.close()
    i += 1
    print(i)


tags = 'hedgehog'
path = './hedgehogs/'
flickr_search(tags)
flickr_download(path)

tags = 'porcupine'
path = './porcupines/'
flickr_search(tags)
flickr_download(path)




