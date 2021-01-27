import pandas as pd
def cau1():
	listA=[1,10,20,5,60,50,10,9,10]
	listB=[]
	for x in listA:
		if x!=10:
			listB.append(x)
	print(listB)

def cau2():
	list1=["A","B","C","D","E","F"]
	list2=[1,2,3,4,5,6]
	dic={}
	for x in range(len(list1)):
		dic[list1[x]] = list2[x]
	print(dic)

def cau3():
	person={
			"Name":"Quoc Nam",
			"Age": 28,
			"Salary":8000,
			"City":"Tuy Hoa"
	}
	KeyRemove=['Salary','Name']
	for x in KeyRemove:
		if x in person:
			del person[x]
	print(person)

def cau4a():
	mobile = pd.read_csv('mobile_data.csv')
	print(mobile.head(5))
	print(mobile.tail(5))
	
def cau4c():
	mobile = pd.read_csv('mobile_data.csv')
	a=0
	for x in mobile['price']:
		if a<x:
			a=x
	print(a)

def cau4b():
	mobile = pd.read_csv('mobile_data.csv')
	na_values=["?","n.a"]
	mobile1=mobile.replace(na_values, 'NaN')
	print(mobile1)


def cau4d():
	mobile = pd.read_csv('mobile_data.csv')
	print(mobile['company'].value_counts())
	print(mobile['company'].value_counts().plot(kind='bar'))

def cau4e():
	mobile = pd.read_csv('mobile_data.csv')
	df = mobile.sort_values('price', ascending=True)
	print('Sau khi sắp xếp\n', df)

print(cau4b())