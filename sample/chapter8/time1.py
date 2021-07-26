import time
old = time.time()
s = ''
for i in range(1000000):
    s += '根菜町１丁目２番地　人参\n'
print(time.time()-old, '秒')
