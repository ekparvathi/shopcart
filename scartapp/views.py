from django.shortcuts import render,redirect
from .models import profile
from .models import products
from django.contrib import messages
from .models import cart
# Create your views here.

def navbar(request):
    return render(request,'navbar,html')

def home(request):
    if 'Email' in request.session:
        current_user=request.session['Email']
        user=profile.objects.get(Email=current_user)
        return render(request,'home.html',{'current_user':current_user,'user':user})
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def logout(request):
    print(request.session['Email'])
    del request.session['Email']
    return redirect('/')
    
def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        address=request.POST['address']
        pin=request.POST['pin']
        phone=request.POST['phone']
        img=request.FILES.get('profilepic')
        emailexists=profile.objects.filter(Email=email)
        if emailexists:
            messages.error(request,"Email already Exists!!!!")
        elif password!=cpassword:
            messages.error(request,'Password should match Confirm Password')        
        else:
            profile.objects.create(Name=name,Email=email,Password=password,Address=address,PIN=pin,Phone=phone,Image=img)
            return redirect("/login")
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=profile.objects.filter(Email=email,Password=password)
        if user:
            request.session['Email']=email
            return redirect('/')
    return render(request,'login.html')
    
def account(request,id):    
    if 'Email' in request.session:
        current_user=request.session['Email']
        user=profile.objects.get(id=id)
        return render(request,'account.html',{'current_user':current_user,'user':user})

def addProducts(request):
    if request.method=='POST':
        pName=request.POST['pName']
        pType=request.POST['pType']
        pModel=request.POST['pModel']
        pMeterial=request.POST['pMeterial']
        pDescription=request.POST['pDescription']
        pImage=request.FILES.get('pImage') 
        pPrice=request.POST['pPrice']
        pSize=request.POST['pSize']
        pColor=request.POST['pColor']
        pQty=request.POST['pQty']
        pPerson=request.POST['pPerson']
        # if pName or pQty or pModel or pMeterial or pDescription or pImage or pSize or pPerson=="":
        #     messages.error(request,"products details cannot be blank")
        # else:
        products.objects.create(P_Name=pName,P_Type=pType,P_Model=pModel,P_Meterial=pMeterial,P_Description=pDescription,
        P_Image=pImage,P_Price=pPrice,P_Size=pSize,P_Color=pColor,P_Qty=pQty,P_Person=pPerson)
    return render(request,'addProducts.html')

def viewProducts(request):
    prod=products.objects.all()
    return render(request,'viewProducts.html',{'prod':prod})

def search(request):
    if request.method=='POST':
        search=request.POST['search']
        print(search)        
        prod=products.objects.filter(P_Meterial=search)  
        print(prod)        
    return render(request,'search.html',{'prod':prod})
    
def viewProdDetail(request,id):
    prod=products.objects.get(id=id)
    
    print(prod)
    return render(request,'viewProdDetail.html',{'prod':prod})

# def addToCart(request,id):   
#     if 'Email' in request.session:
#         current_user=request.session['Email']
#         user=profile.objects.get(Email=request.session['Email'])
#         prod=products.objects.get(id=id)                
#         cart.objects.create(prof=user,prods=prod,qty=1,price=0)
#         return redirect('/showCart')
#     return render(request,'addToCart.html',{'user':user})

def getid(request):
    prod=products.objects.get(id=id)
    if request.method=='POST':
        q=request.POST['quantity']
        print(q)

def addToCart(request,id):   
    if 'Email' in request.session:
        current_user=request.session['Email']
        user=profile.objects.get(Email=request.session['Email'])
        prod=products.objects.get(id=id)         
        if request.method=='POST':
            q=request.POST['quantity']  
            price=prod.P_Price*q
            print(q,price)
            cart.objects.create(prof=user,prods=prod,qty=q,price=price)
            
            return redirect('/showCart')
    return render(request,'addToCart.html',{'user':user})


def showCart(request):
    if 'Email' in request.session:
        current_user=request.session['Email']
        user=profile.objects.get(Email=current_user)
        mycart=cart.objects.filter(prof_id=user.id)  
        product=[]
        total=0    
        counter=0   
        for i in mycart:
            print(i.prods.P_Name)
            total=total+i.prods.P_Price
            product.append(i.prods)
            print(i.prods.P_Image)
            counter+=1    
        return render(request,'showCart.html',{'current_user':current_user,'user':user,'total':total,'counter':counter,'product':product})
    return render(request,"showCart.html")  
        
