import numpy
import sys
from PIL import Image
from sklearn import externals

if len(sys.argv) != 2:
    print('python lr_user.py [画像ファイル名]')
    exit()

SIZE = 28
image = Image.open(sys.argv[1]).convert('L')
image = image.resize((SIZE, SIZE), Image.LANCZOS)
test_data = [numpy.array(image).ravel()]

for y in range(SIZE):
    for x in range(SIZE):
        print('{0:4d}'.format(test_data[0][x+y*SIZE]), end='')
    print()

model = externals.joblib.load('lr.model')
predict = model.predict([t/255 for t in test_data])
print('予測：', int(predict[0]))
