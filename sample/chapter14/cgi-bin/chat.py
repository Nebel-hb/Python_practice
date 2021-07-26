#!/usr/bin/env python3
import cgi
import codecs
import json
import sys

sys.stdout = codecs.getwriter('utf_8')(sys.stdout.detach())

try:
    with open('chat.txt', 'r') as file:
        chat = json.load(file)
except IOError:
    chat = []

form = cgi.FieldStorage()
image = form.getfirst('image')
text = form.getfirst('text')
if image and text:
    chat.append({'image': image, 'text': text})
    with open('chat.txt', 'w') as file:
        json.dump(chat, file, indent=4)

print('Content-type: text/html; charset=UTF-8')

print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Python Web Programming</title>
</head>
<body>
<h2>根菜チャット</h2>
<form action="chat.py" method="post">
<select name="image">
<option value="daikon">大根</option>
<option value="ninjin">人参</option>
</select>
<input type="text" name="text">
<input type="submit" value="発言">
</form>
<hr>
''')

for line in chat:
    print('<p><img src="/{0}.png" alt="image" width="100">{1}</p>'.format(
        line['image'], line['text']))

print('''
</body>
</html>
''')
