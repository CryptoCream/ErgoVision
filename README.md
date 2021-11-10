### Usage
ErgoVision's default crawling depth is 3 i.e. it fetches the history of target wallet(s), crawls the newly found wallets and then crawls the wallets in the result again. The crawling depth can be increased or decresead with `-d` option.
```
python3 ergovision.py -s 9fowPvQ2GXdmhD2bN54EL9dRnio3kBQGyrD3fkbHwuTXD6z1wBU -d 2
```

ErgoVision fetches last 50 transactions from each wallet by default, but it can be tuned with `-l` option.

```
python3 ergovision.py -s 9fowPvQ2GXdmhD2bN54EL9dRnio3kBQGyrD3fkbHwuTXD6z1wBU -l 5
```

Crawling multiple wallets is no different.
```
python3 ergovision.py -s 9fowPvQ2GXdmhD2bN54EL9dRnio3kBQGyrD3fkbHwuTXD6z1wBU,9iKFBBrryPhBYVGDKHuZQW7SuLfuTdUJtTPzecbQ5pQQzD4VykC
```

Wallets that have made just a couple of interactions with our target may not be important, ergovision can be told to crawl top N wallets at each level by using the `-t` option.
```
python3 ergovision.py -s 9fowPvQ2GXdmhD2bN54EL9dRnio3kBQGyrD3fkbHwuTXD6z1wBU -t 20
```

### Graph
The graph will look messy at first, it's recomended to click `Make Clusters` and `Node Labels`
The graph is generated using [Quark](https://github.com/s0md3v/Quark)
