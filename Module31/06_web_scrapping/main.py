import re

import requests


def web_scrapping():
    h3_name_list = []

    my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
    data = my_req.text

    h3_pattern = r'<h3.+h3>'

    all_h3 = re.findall(h3_pattern, data)

    for h3 in all_h3:
        start = h3.find('>')
        finish = h3.rfind('<')

        h3_name_list.append(h3[start + 1:finish])

    print(h3_name_list)


web_scrapping()
