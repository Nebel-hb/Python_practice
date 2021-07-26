import time
old = time.time()
s = '根菜町１丁目２番地　人参\n' * 1000000
print(time.time()-old, '秒')
