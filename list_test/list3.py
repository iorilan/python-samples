list3 = [
    [['name','bob smith'], ['age',42],['pay',10000]],
    [['name','sue jones'], ['age',45],['pay',20000]]
]

def field(list, key):
    for (k,v) in list:
        if k == key:
            return v
    return ''

print(field(list3[0], 'name'))
print(field(list3[1], 'age'))
