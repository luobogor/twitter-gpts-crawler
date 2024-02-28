# Twitter GPTs Crawler

English | [中文](./README-cn.md)

Crawls GPTs links from Twitter based on [tweety](https://github.com/mahrtayyab/tweety). It is recommended to use it in conjunction with [Gpts Detail Crawler](https://github.com/luobogor/gpts-detail-crawler) to crawl GPTs detail page data.

<p align="center">
★ Powered by <a target="_blank" href="https://gptshappy.tools?utm_source=twitter-gpts-crawler">GPTsHappy.tools</a> ★
</p>

<p align="center">
  <a target="_blank" href="https://gptshappy.tools?utm_source=twitter-gpts-crawler">
    <img alt="GPTsHunter" src="./logo.png">
  </a>
</p>


## Installation

```shell
pip3 install requests
pip3 install tweety-ns
```

## Configure User
Edit the `login` method in `index.py` to configure your Twitter account and password, or use [other methods](https://mahrtayyab.github.io/tweety_docs/basic/singing-in.html) to log in.

## Start
Crawl the latest GPTs data, starting from today and crawling until there is no more data:

``` shell
python3 index.py
```

Crawl by date range, the end date must be one day later than the start date:

``` shell
python3 index.py 2023-12-01 2023-12-05
```

If the program is interrupted, you can set the `cursor` of `startLatest/startDateRange` to continue crawling from the previous page.

Output example:

```text
https://chat.openai.com/g/g-alKfVrz9K-canva
https://chat.openai.com/g/g-2fkFE8rbu-dall-e
```

If you need to use a proxy, modify the `PROXY_SERVER` variable in `index.py`.
