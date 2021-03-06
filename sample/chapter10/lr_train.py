from sklearn import datasets, externals, linear_model, model_selection
import time

print('MNISTの取得：', end='', flush=True)
mnist = datasets.fetch_mldata('MNIST original', data_home='.')
data, label = mnist.data, mnist.target
print('完了')

TRAIN_SIZE = 600
TEST_SIZE = 100

t = model_selection.train_test_split(
    data, label, train_size=TRAIN_SIZE, test_size=TEST_SIZE)
train_data, test_data, train_label, test_label = t
print('訓練データ：', train_data.shape)
print('テストデータ：', test_data.shape)

print('学習：', end='', flush=True)
old = time.time()
model = linear_model.LogisticRegression().fit(train_data, train_label)
print(time.time()-old, '秒')

externals.joblib.dump(model, 'lr.model')

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
