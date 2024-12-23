from collections import OrderedDict

n=int(input())

items=OrderedDict()
for _ in range(n):
    line=input().rsplit(' ',1)
    item_name=line[0]
    price=int(line[1])

    if item_name in items:
        items[item_name]+=price
    else:
        items[item_name]=price
    
for item_name,net_price in items.items():
    print(item_name,net_price)