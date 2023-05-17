from django.shortcuts import render,redirect
from . models import Admin

# Create your views here.

def index(request):
	data=Admin.objects.all()
	return render(request,'index.html',{'data':data})

def add(request):
	if request.method=="POST":
		Admin.objects.create(
				product_name=request.POST['name'],
				product_price=request.POST['price'],
				product_model=request.POST['model'],
				product_image=request.FILES['image'],
			)
		data=Admin.objects.all()
		return render(request,'index.html',{'data':data})

def edit(request):
	data=Admin.objects.all()
	return redirect(request,'index.html',{'data':data})

def update(request,id):
	if request.method=="POST":
		product_name=request.POST.get('name')
		product_price=request.POST.get('price')
		product_model=request.POST.get('model')
		data=Admin(
				id=id, 
				product_name=product_name,
				product_price=product_price,
				product_model=product_model,
				
			)
		data.save()
		return redirect('index')
	else:
		data=Admin.objects.all()
		return redirect(request,'index.html',{'data':data})

def delete(request,id):
	data=Admin.objects.filter(id=id)
	data.delete()
	context={
		'data':data
	}
	return redirect('index')
