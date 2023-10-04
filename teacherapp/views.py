import os
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from teacherapp.models import ProductDetails


def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html') 





def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('loginpage')
    else:
        return render(request,'signup.html')


#User login functionality view
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.info(request, f'Welcome {username}')
			return redirect('crud')
		else:
			messages.info(request, 'Invalid Username or Password. Try Again.')
			return redirect('loginpage')
	else:
		#messages.info(request, 'Oops, Something went wrong.')
		return redirect('loginpage')

#User logout functionality view
def logout(request):
	auth.logout(request)
	return redirect('home')



def crud(request):
    return render(request,'crude.html')


def add_details(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        age=request.POST['age']
        dob=request.POST['dob']
        gend=request.POST['gender']
        
        dept=request.POST['department']
        nof=request.POST['nof']
        nom=request.POST['nom']
        email=request.POST['email']
        ph=request.POST['phone']
        add=request.POST['address']
        image=request.FILES.get('file')
        product=ProductDetails(firstname=fname,lastname=lname,age=age,dob=dob,gender=gend,department=dept,nof=nof,nom=nom,email=email,phone=ph,address=add,image=image)
        print("Save data...")
        product.save()
        return redirect('show_products')
    

    
def show_products(request):
    products=ProductDetails.objects.all()
    return render(request,'showproduct.html',{'product':products})

def editpage(request,pk):
    pr=ProductDetails.objects.get(id=pk)
    return render(request,'edit.html',{'product':pr})

def edit_Product_Details(request,pk):
    if request.method == 'POST':
        pr = ProductDetails.objects.get(id=pk)
        pr.firstname = request.POST.get('firstname')
        pr.lastname = request.POST.get('lastname')
        pr.age = request.POST.get('age')
        pr.dob = request.POST.get('dob')
        pr.gender = request.POST.get('gender')
    
        pr.department = request.POST.get('department')
        pr.nof = request.POST.get('nof')
        pr.nom = request.POST.get('nom')
        pr.email = request.POST.get('email')
        pr.phone = request.POST.get('phone')
        pr.address = request.POST.get('address')

        old=pr.image
        new=request.FILES.get('file')
        if old !=None and new==None:
            pr.image=old
        else:
            pr.image=new

        pr.save()
        return redirect('show_products')
    return render(request,'edit.html')

def deletepage(request,pk):
    Productdetails=ProductDetails.objects.get(id=pk)
    Productdetails.delete()
    return redirect ('show_products')



# Create your views here.



    



