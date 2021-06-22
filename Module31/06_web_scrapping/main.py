import re

import requests


def web_scrapping():
    my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
    data = my_req.text

    h3_pattern = r'<h3.+?>(.+?)</h3>'

    print(re.findall(h3_pattern, data))


web_scrapping()
