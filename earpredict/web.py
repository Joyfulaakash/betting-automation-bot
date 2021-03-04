from urllib.request import urlopen
import json
import time
def webs():
    urls = "https://earnpredict.com/earnservice.php"
    with urlopen(urls) as response:
        source = response.read()

    datas = json.loads(source)
    
    for item in datas['data']:
        issue = item['issue']
        predict = item['predict']
        amount = item['amount']
        print(amount)
        amount=float(amount) * 3
        print(issue,predict,amount)
        break
    return predict,amount

webs()