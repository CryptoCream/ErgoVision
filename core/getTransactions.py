from re import findall
from core.utils import pageLimit
from core.requester import requester

def getTransactions(address, processed, database, limit):
    addresses = []
    increment = 0
    database[address] = {}
    pages = pageLimit(limit)
    for i in range(pages):
        response = requester(address)
        matches = findall(r'"address":"9.*?"', response)
        for match in matches:
            found = match.split('"')[3]
            if found not in database[address]:
                database[address][found] = 0
            database[address][found] += 1
            addresses.append(found)
        increment += 50
        processed.add(address)
    return addresses
    # print(addresses)