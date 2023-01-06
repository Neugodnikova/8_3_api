import requests
import time
current_time = (int(time.time()))
two_days_ago = current_time - 172800
url = 'https://api.stackexchange.com/2.3/questions'
params = {'pagesize': 100,
          'fromdate': two_days_ago,
          'todate': current_time,
          'order': 'desc',
          'sort': 'creation',
          'tagged': 'Python',
          'site': 'stackoverflow'
          }
response = requests.get(url=url, params=params)
data = response.json()
for a in data['items']:
    print(a['title'])