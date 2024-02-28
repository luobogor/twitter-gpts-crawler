# https://mahrtayyab.github.io/tweety_docs/

from tweety import Twitter
from tweety.filters import SearchFilters
from datetime import datetime, timedelta
import time
import requests
import datetime
import sys

# PROXY_SERVER = 'http://127.0.0.1:7890'
PROXY_SERVER = None
isCreatedFile = False
outputFileName = ''

def create_file():
  global isCreatedFile
  global outputFileName
  if isCreatedFile:
    return outputFileName

  outputFileName = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.txt'
  with open(outputFileName, "w") as f:
    pass

  isCreatedFile = True
  print('created file:' + outputFileName)
  return outputFileName

def resolve_short_url(short_url):
  response = requests.head(short_url, allow_redirects=True)
  final_url = response.url
  return final_url

def login():
  print('logining...')
  global app
  global PROXY_SERVER
  app = Twitter("session", PROXY_SERVER)
  # input your twitter username and password
  app.sign_in('account', 'password')

def genDate(start_date_str, end_date_str):
  start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
  end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

  date_range = []
  current_date = start_date
  while current_date < end_date:
    next_date = current_date + timedelta(days=1)
    date_range.append({'start_date': current_date.strftime('%Y-%m-%d'), 'end_date': next_date.strftime('%Y-%m-%d')})
    current_date = next_date

  return date_range

def get_short_url(urlItem):
  try:
    if 'https://chat.openai.com/g/' in urlItem.expanded_url:
      return urlItem.expanded_url.replace('https://chat.openai.com/g/', '').strip().split('?')[0]

    real_url = resolve_short_url(urlItem.url)
    if 'https://chat.openai.com/g/' in real_url:
      return real_url.replace('https://chat.openai.com/g/', '').strip().split('?')[0]
    return None
  except Exception as e:
    return None

def insert_list(tweets):
  for tweet in tweets:
    for item in tweet['urls']:
      short_url = get_short_url(item)
      if short_url is not None:
        url = 'https://chat.openai.com/g/' + short_url
        with open(create_file(), "a") as f:
          f.seek(0, 2)
          f.write(url + '\n')
          print('wrote:' + url)

def scroll_page(keyword, next_cursor):
  print('start...................:', keyword, ' cursor:', next_cursor)
  try:
    tweets = app.search(
      keyword=keyword,
      wait_time=2,
      cursor=next_cursor,
      filter_=SearchFilters.Latest()
      )
  except Exception as e:
    print("error cursor:", next_cursor)
    print("error:", e)
    print("try again........")
    time.sleep(23)
    scroll_page(keyword, next_cursor)
    return

  if len(tweets) == 0:
    return

  insert_list(tweets)
  # Search has 50 requests per 15 minutes limit , slow down your requests
  time.sleep(23)
  scroll_page(keyword, tweets.cursor)


def startDateRange(start_date, end_date):
  dates = genDate(start_date, end_date)

  for date_range in dates:
    # 如果程序中断可以在这里设置最后的 cursor，接着上一页继续爬取
    cursor = None
    keyword = "(chat.openai.com/g/) until:" + date_range['end_date'] + " since:" + date_range['start_date']
    scroll_page(keyword, cursor)
    print('all success.....:', keyword)

def startLatest():
  # 如果程序中断可以在这里设置最后的 cursor，接着上一页继续爬取
  cursor = None
  keyword = "chat.openai.com/g/"
  scroll_page(keyword, cursor)
  print('all success............')

def startCrawler():
  if len(sys.argv) > 1:
    startDateRange(sys.argv[1], sys.argv[2])
  else:
    startLatest()

login()
startCrawler()
