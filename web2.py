# import Web
#
#
# x = Web.web()
#
# x.connect1('https://www.walla.co.il')

import urllib3

myhttp = urllib3.PoolManager()
req1 = myhttp.request('GET', '')

print(req1.data.decode('utf-8'))