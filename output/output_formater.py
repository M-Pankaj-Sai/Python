a = 10
b = 20

print(a,b)
print(a,b,sep=",")
print("%d" % (a) )
print("%5d" % (a) )

f=3.1415926

print("%6.3f"%(f))

print('%d %s cost $%.2f' % (6, 'bananas', 1.74))
print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))
print('{quantity} {item} cost ${price}'.format(quantity=6,item='bananas',price=1.74))

print('{}{}'.format('foo', 'bar', 'baz'))
print("'{:%}'.format(0.65)")

s=f'{a}/pav'
print(s)