from django.shortcuts import render

def runoob(request):
	num=11
	return render(request,"runoob.html",{"num":num})
	
	