# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from collections import Counter
from copy import deepcopy

# +
items_dict = {}
items_dict['极其聪明的寄居蟹'] = ('穆勒尔', {'养生鱼人午餐':4, '超沉的石头':2, '超粘的蜗牛':3})

items_dict['粘滑的娜迦眼球'] = ('穆勒格勒勒', {'金币':1})
items_dict['正在崩解的沙雕'] = ('穆勒格勒勒', {'甜美的海菜':4})
items_dict['超沉的石头'] = ('穆勒格勒勒', {'一袋不可名状之物':3, '一罐鱼脸':3})
items_dict['一堆臭糊'] = ('穆勒格勒勒', {'非常普通的黄油':2})

items_dict['胀气鱼'] = ('格姆勒格', {'金币':1})
items_dict['奇特的鱼人之角'] = ('格姆勒格', {'粘滑的娜迦眼球':3})
items_dict['超粘的蜗牛'] = ('格姆勒格', {'正在崩解的沙雕':5})
items_dict['海巨人的脚灰'] = ('格姆勒格', {'清洁的鱼人袜子':3})

items_dict['甜美的海菜'] = ('胡勒格勒', {'金币':1})
items_dict['一罐鱼脸'] = ('胡勒格勒', {'胀气鱼':5})
items_dict['脏兮兮的鱼人袜子'] = ('胡勒格勒', {'未鉴定的物质':6})
items_dict['养生鱼人午餐'] = ('胡勒格勒', {'奇特的鱼人之角':5})

items_dict['未鉴定的物质'] = ('弗勒格勒', {'金币':1})
items_dict['一袋不可名状之物'] = ('弗勒格勒', {'胀气鱼':2})
items_dict['非常普通的黄油'] = ('弗勒格勒', {'甜美的海菜':4})
items_dict['幽魂的食物'] = ('弗勒格勒', {'奇特的鱼人之角':6})

# +
str_formater = '从{}使用{}购买{} {}个'

target = '超粘的蜗牛'
needed_dict = Counter()
needed_dict[target] = 3
print_list = []

while True:
    new_needed_dict = Counter()
    for new_target, count in needed_dict.items():
        seller_name, new_need_items_dict = deepcopy(items_dict[new_target])
        # 叠加购买次数
        for k in new_need_items_dict:
            new_need_items_dict[k] *= count 
        
        print_list.append(str_formater.format(seller_name, new_need_items_dict, new_target, count))
        new_needed_dict += Counter(new_need_items_dict)
        
    if len(new_needed_dict) == 1 and '金币' in new_needed_dict:
        break
    else:
        needed_dict = deepcopy(new_needed_dict)

for print_str in print_list[::-1]:
    print(print_str)
# -


