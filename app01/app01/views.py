from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
	# book=models.Book(title='菜鸟教程',price=300,publish='菜鸟出版社',pub_date="2021-12-10")
	# book.save()
	# book=models.Book.objects.create(title='如来神掌',price=300,publish='菜鸟出版社',pub_date="2021-12-10")
	books=models.Book.objects.all()
	print(books,type(books))

	return HttpResponse("<p>查找成功！</p>")