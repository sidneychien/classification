#-*- coding: utf-8 -*-
"""
OUHandleHelper training and servicing functions.

I hope to provide several training solutions in this file.

Author: Adrian
Date: March 6, 2017
"""
from tgrocery import Grocery
import jieba

def grocery_predict(pred_src):
    grocery = Grocery('handleHelper')
    grocery.load()
    return grocery.predict(pred_src)
    
def grocery_test(test_src):
    grocery = Grocery('handleHelper')
    grocery.load()
    test_result = grocery.test(test_src, delimiter='\t')
    print test_result.accuracy_overall
    print test_result.show_result()

def grocery_predict_m(pred_src):
    grocery = Grocery('handleHelper')
    grocery.load()
    return grocery.predict(pred_src)

def analyze_json(json_data):
    rst = ""
    if json_data.has_key('RequestTitle'):
        rst += json_data['RequestTitle']
    if json_data.has_key('Description'):
        rst += json_data['Description']
    if json_data.has_key('SuQiuAddress'):
        rst += json_data['SuQiuAddress']
    return rst

if __name__ =="__main__":
    jieba.set_dictionary('../lib/dict.txt')
    #s = u"家里水表坏了如何处理"
    #print grocery_predict_m(s)
    grocery_test('../data/ouhandlehelper/test/testone.txt')
    # train_grocery("../data/ouhandlehelper/test/train.txt")