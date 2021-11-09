import requests

def requester(url):
	request = requests.get('https://api.ergoplatform.com/api/v1/addresses/' + url + '/transactions').text
	# print(request)
	return request