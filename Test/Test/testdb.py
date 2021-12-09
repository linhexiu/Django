from django.http import HttpResponse
from TestModel.models import Test

#添加数据
# def testdb(request):
# 	test1=Test(name='runoob')
# 	test1.save()
# 	return HttpResponse("<p>数据添加成功！</p>")

#获取数据
# def testdb(request):
# 	#初始化
# 	response=""
# 	response1=""

# 	list=Test.objects.all()#相当于SQL中SELECT * FROM
# 	response2=Test.objects.filter(id=1)#相当于SQL中WHERE
# 	response3=Test.objects.get(id=1)#获取单个对象
# 	Test.objects.order_by('name')[0:2]#限制返回的数据，相当于SQL中的OFFSET 0 LIMIT 2
# 	Test.objects.order_by("id")#数据排序
# 	Test.objects.filter(name='runoob').order_by("id")#方法可以连锁使用

# 	#输出数据
# 	for var in list:
# 		response1+=var.name+" "
# 	response=response1
# 	return HttpResponse("<p>"+response+"</p>")
# 	
#更新数据
# def testdb(request):
# 	test1=Test.objects.get(id=1)
# 	test1.name='Google'
# 	test1.save()

# 	#Test.objects.filter(id=1).update(name='Google')
# 	#修改所有的列
# 	#Test.objects.all().update(name='Google')

# 	return HttpResponse("<p>修改成功！</p>")

#删除数据
def testdb(request):
	test1=Test.objects.get(id=1)
	test1.delete()

	#Test.objects.filter(id=1).delete()
	#删除所有数据
	#Test.onjects.all().delete()

	return HttpResponse("<p>删除成功！</p>")