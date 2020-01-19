#!/usr/local/bin/python3
#-*-coding: UTF-8 -*-
from lxml import html
import codecs
import json
from googletrans import Translator
import requests
import pdb
import sys

#url = 'http://ysweb.yonsei.ac.kr:8888/curri120601/curri_pop2.jsp?&hakno=POL1004&bb=02&sbb=00&domain=H1&startyy=2011&hakgi=1&ohak=0601'
url = 'http://ysweb.yonsei.ac.kr:8888/curri120601/curri_pop2.jsp?&hakno=UCB1103&bb=05&sbb=00&domain=H1&startyy=2011&hakgi=1&ohak=2021'
proxy = {
        'http': 'http://username:password@1.1.1.1:1234',
        'https': 'http://username:password@1.1.1.1:1234',
}
tr_pairs=dict()
#translator = Translator(proxies=proxy)# .sleep(.4)
translator = Translator()
page = requests.get(url)
tree = html.fromstring(page.content)

page2 = requests.get(url)
page_txt_2 = page2.content.decode('cp949').replace('&nbsp', '')

page_translated = codecs.open('page_translated.txt', 'w', encoding='utf8')
testtest = translator.translate(page_txt_2, dest='en', src='ko').text
page_translated.write(testtest)
page_translated.close()

sys.exit(1)

def my_trans(string):
    string = string.replace('\xa0', ' ').replace('\0', '').strip() #sub.replace('\t', '').replace('\n', '').replace('\0', '').strip() # .encode('utf8')
    if string:
        print('string:{}'.format(string))
        return translator.translate(string, dest='en', src='ko').text
    return string
'''
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
'''
# fh = codecs.open(url, 'r', encoding='utf8')
# html_text = '\n'.join(fh.readlines())

page_fh = codecs.open('pagepage', 'w', encoding='utf8')
string_dict = codecs.open('dict_fh.cp', 'r', encoding='utf8')
# maybe_dict = json.load(string_dict) #, 'r', encoding='utf8')
maybe_dict = eval(string_dict.read())
page_txt = page.content.decode('cp949').replace('&nbsp','') #.replace('\n', '').replace('\r', '')
before_replace = codecs.open('pagepage.ori', 'w', encoding='utf8')
before_replace.write(page_txt)
# for key in tr_pairs.keys():
for key in sorted(maybe_dict.keys(),key=len, reverse=True):
    ori_key = key
    key = key.replace('\xa0', '')
    # html_text = html_text.sub(key, tr_pairs[key])
    if key not in page_txt:
        pdb.set_trace()
    page_txt = page_txt.replace(key, maybe_dict[ori_key])
page_fh.write(page_txt)
# dict_fh.close()
