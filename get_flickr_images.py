import config
import requests
import re
import random

payload = { 'api_key': config.FLICKR_KEY }

def flickr_search(tag):
  photos = []
  payload['method'] = 'flickr.photos.search'
  payload['sort'] = 'relevance'
  payload['text'] = tag
  payload['per_page'] = '200'

  r = requests.get('https://api.flickr.com/services/rest/', params=payload)
  text = r.text
  #print(text)

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
  #print(photos)
  return photos

def flickr_download(base_path, photos, tag):
  i = 0
  random.shuffle(photos)
  train_path = base_path + '/train/' + tag + 's/'
  val_path = base_path + '/val/' + tag + 's/'
  print(train_path, val_path)
  for photo in photos:
    path = train_path if i < 133 else val_path
    name = path + photo['photo_id'] + '.jpg'
    f = open(name, 'wb')
    try:
      f.write(requests.get('https://farm{farm_id}.staticflickr.com/{server_id}/{photo_id}_{secret}.jpg'.format(
                             farm_id=photo['farm_id'],
                             server_id=photo['server_id'],
                             photo_id=photo['photo_id'],
                             secret=photo['secret']
                            )).content)
      f.close()
    except requests.ConnectionError:
      next
    i += 1
    print(i)


print(payload)

path = './data'
tags = ['hedgehog', 'porcupine']

for tag in tags:
    photos = flickr_search(tag)
    flickr_download(path, photos, tag)

