def switch(x):
    return {
        0: '0000',
        1: '1111',
    }.get(x, 'xxxx')

print(switch(0))
print(switch(1))
print(switch(5))
