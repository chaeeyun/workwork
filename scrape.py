#!/usr/local/bin/python3
#-*-coding: UTF-8 -*-
from lxml import html
import codecs
from googletrans import Translator
import requests
import pdb

url = 'http://ysweb.yonsei.ac.kr:8888/curri120601/curri_pop2.jsp?&hakno=POL1004&bb=02&sbb=00&domain=H1&startyy=2011&hakgi=1&ohak=0601'
proxy = {
        'http': 'http://username:password@1.1.1.1:1234',
        'https': 'http://username:password@1.1.1.1:1234',
}
tr_pairs=dict()
#translator = Translator(proxies=proxy)# .sleep(.4)
translator = Translator()
page = requests.get(url)
#pdb.set_trace()
tree = html.fromstring(page.content)

def my_trans(string):
    string = string.replace(u'\xa0', u' ').replace(u'\t', u'').replace(u'\n', u'').replace(u'\0', u'').strip() # .encode('utf8')
    if string:
        print('string:{}'.format(string))
        return translator.translate(string, dest='en', src='ko').text
    return string

box = tree.xpath('//td[@class="BoxText_1"]/text()')
pre = tree.xpath('//pre/text()')
for btext in box:
    if btext:
        tr_pairs[btext] = my_trans(btext)
for ptext in pre:
    if ptext:
        tr_pairs[ptext] = my_trans(ptext)

dict_fh = codecs.open('dict_fh', 'w', encoding='utf8')
dict_fh.write(str(tr_pairs))
# fh = codecs.open(url, 'r', encoding='utf8')
# html_text = '\n'.join(fh.readlines())
page_txt = page.content.encode('utf8')
for key in tr_pairs.keys():
    # html_text = html_text.sub(key, tr_pairs[key])
    page_txt = page_txt.sub(key, tr_pairs[key])
page_fh.write(page_txt)
dict_fh.close()
pdb.set_trace()
