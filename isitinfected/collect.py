# Collect pictures of infected homebrew from r/Homebrewing
# 
# This script expects an 'images/' dir in the same dir as the script.
# It will will search the r/Homebrewing subreddit for <search_str>
# for 100 posts after <last_post> (which is <post>.name of the last analyzed post).
# 
# It will output the number of downloaded images and the post name of the last
# post that had an image. This is the new <last_post> for the next run.

import os
import requests
import urllib.request
import glob

images_subdir = 'images'

# collect existing images
existing_images = os.listdir(images_subdir)

# remember which was the last post that we analyzed
last_post = 't3_3ml3ti'
search_str = 'infected'

# get next 100 posts
url = f'https://www.reddit.com/r/Homebrewing/search.json?q={search_str}&restrict_sr=1&limit=100&after={last_post}'
headers = {
  'User-Agent': 'isitinfected-bot 0.1'
}

response = requests.get(url, headers=headers)
content = response.json()
posts = content['data']['children']

# check for a preview file and write it to disk if we don't already have it
for post in posts:
  if 'preview' in post['data'] and len(post['data']['preview']['images']) > 0:
    preview_img = post['data']['preview']['images'][0]['source']

    # download the image    
    if preview_img:
      last_post = post['data']['name']
      filename = os.path.basename(preview_img['url'])
      filename = filename[:filename.find('?')]  # strip ? from filename
      if not filename in existing_images:
        urllib.request.urlretrieve(preview_img['url'], os.path.join(images_subdir, filename))

current_images = os.listdir(images_subdir)
new_images = len(current_images) - len(existing_images)

print(f'Downloaded {new_images} new images')
print(f'The last post we downloaded an image for was: {last_post}')