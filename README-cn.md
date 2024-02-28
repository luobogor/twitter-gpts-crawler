# Twitter GPTs Crawler

[English](./README.md) | 中文

基于 [tweety](https://github.com/mahrtayyab/tweety) 封装，从推特上爬取 GPTs 链接。推荐结合 [Gpts Detail Crawler](https://github.com/luobogor/gpts-detail-crawler) 爬取 GPTs 详情页的数据。

<p align="center">
★ 由 <a target="_blank" href="https://gptshappy.tools?utm_source=twitter-gpts-crawler">GPTsHappy.tools</a> 提供支持 ★
</p>

<p align="center">
  <a target="_blank" href="https://gptshappy.tools?utm_source=twitter-gpts-crawler">
    <img alt="GPTsHunter" src="./logo.png">
  </a>
</p>

## 安装

```
pip3 install tweety-ns
pip3 install requests
```

## 配置用户
编辑 `index.py` 的 `login` 方法，配置推特账号密码，或者使用[其他方式](https://mahrtayyab.github.io/tweety_docs/basic/singing-in.html)登录。

## 启动
爬取最新 GPTs 数据，从当天开始爬直到没有数据为止：

``` shell
python3 index.py
```

按日期区间爬取，结束日期必须比开始日期晚一天：

``` shell
python3 index.py 2023-12-01 2023-12-05
```

如果程序中断，可以设置 `startLatest/startDateRange` 的 `cursor`，接着上一页继续爬取。

输出范例：

```text
https://chat.openai.com/g/g-alKfVrz9K-canva
https://chat.openai.com/g/g-2fkFE8rbu-dall-e
```

如需要使用代理，修改 `index.py` 里的 `PROXY_SERVER` 变量。
