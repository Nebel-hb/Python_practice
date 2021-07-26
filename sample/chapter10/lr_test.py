from sklearn import datasets, externals, model_selection

print('MNISTの取得：', end='', flush=True)
mnist = datasets.fetch_mldata('MNIST original', data_home='.')
data, label = mnist.data, mnist.target
print('完了')

TRAIN_SIZE = 60000
TEST_SIZE = 10000

t = model_selection.train_test_split(
    data, label, train_size=TRAIN_SIZE, test_size=TEST_SIZE)
train_data, test_data, train_label, test_label = t
print('訓練データ：', train_data.shape)
print('テストデータ：', test_data.shape)

model = externals.joblib.load('lr.model')

print('テスト結果：')
predict = model.predict(test_data)
count = [[0 for i in range(10)] for j in range(10)]
for i in range(TEST_SIZE):
    count[int(predict[i])][int(test_label[i])] += 1
print('正解   ', end='')
for i in range(10):
    print('   [{0}]'.format(i), end='')
print()
for i in range(10):
    print('予測[{0}]'.format(i), end='')
    for j in range(10):
        print('{0:6d}'.format(count[i][j]), end='')
    print()

print('正解率：', model.score(test_data, test_label)*100, '%')
