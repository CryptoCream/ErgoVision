### Usage

Let's start by crawling transaction history of a wallet
```
python3 ergovision.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F
```
Crawling multiple wallets is no different.
```
python3 ergovision.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F,1ETBbsHPvbydW7hGWXXKXZ3pxVh3VFoMaX
```
ergovision fetches last 50 transactions from each wallet by default, but it can be tuned with `-l` option.
```
python3 ergovision.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -l 100
```
ergovision's default crawling depth is 3 i.e. it fetches the history of target wallet(s), crawls the newly found wallets and then crawls the wallets in the result again. The crawling depth can be increased or decresead with `-d` option.
```
python3 ergovision.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -d 2
```
Wallets that have made just a couple of interactions with our target may not be important, ergovision can be told to crawl top N wallets at each level by using the `-t` option.
```
python3 ergovision.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -t 20
```