dates = ['20000302', '20130302', '20220302']
pageurl = "onet.pl"
urls = []

for val in dates:
    url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(val)
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    urls.append(page)

for val1 in urls:
    print(val1)


