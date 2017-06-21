# -*- coding: UTF-8 -*-
#参照されている数を入力
number = raw_input('Enter number : ')
print number

manyReferredList = []
wordCnt = 0

#referredCnt.txtから参照カウント値を取得
for line in open('referredCnt.txt', 'r'):
	referList = line[:-1].split('\t')
	if int(referList[1]) >= int(number):
		manyReferredList.append(int(referList[0]))
		wordCnt += 1

for line in open('pages.txt', 'r'):
	pageList = line[:-1].split('\t')
	if manyReferredList != []:
		if int(pageList[0]) == int(manyReferredList[0]):
			manyReferredList.pop(0)
			print pageList[1]

print "cnt: " + str(wordCnt)
