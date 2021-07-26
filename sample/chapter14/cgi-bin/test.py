#!/usr/bin/env python3
import codecs
import sys

sys.stdout = codecs.getwriter('utf_8')(sys.stdout.detach())

# buffer = sys.stdout.detach()
# writer = codecs.getwriter('utf_8')
# sys.stdout = writer(buffer)

print('Content-type: text/html; charset=UTF-8')

print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Python Web Programming</title>
</head>
<body>

<p>
<img src="/daikon_happy.png" alt="大根">
このページが表示されたら、無事にCGIプログラムが動いているよ！
</p>

<p>
<img src="/ninjin_happy.png" alt="人参">
CGIプログラムを使うと、色々な処理をするWebサイトが作れるよ！
</p>

</body>
</html>
''')
