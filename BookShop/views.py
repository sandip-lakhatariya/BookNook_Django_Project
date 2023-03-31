from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Contact, Order
from math import ceil
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import razorpay
from myProject.settings import RAJORPAY_API_KEY, RAJORPAY_API_SECRET_KEY
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

# Create your views here.

def index(request):
    products = Book.objects.all()
    params = {'product': products}
    return render(request, 'index.html', params)

def productview(request, myid):
     product = Book.objects.filter(id=myid)
     return render(request, 'productview.html', {'product':product[0]})

def shopview(request, data=None):
    if data == None:
        products = Book.objects.all()
        book_type = "All Books"
    if data == "Gujarati" or data == "Hindi" or data == "English":
        products = Book.objects.filter(book_language = data)
        book_type = data + " Books"
    if data == "Novel" or data == "Biography" or data == "Self-Help":
        products = Book.objects.filter(category = data)
        book_type = data + " Books"
    if data == "BA":
        products = Book.objects.filter(category = "Business & Analysis")
        book_type = "Business & Analysis Books"
    if data == "SC":
        products = Book.objects.filter(category = "School/College")
        book_type = "School/College Books"
    if data == "G_Novel":
        products = Book.objects.filter(book_language = "Gujarati").filter(category = 'Novel')
        book_type = "Gujarati Novel"
    if data == "G_Biography":
        products = Book.objects.filter(book_language = "Gujarati").filter(category = "Biography")
        book_type = "Gujarati Biography"
    if data == "G_BA":
        products = Book.objects.filter(book_language = "Gujarati").filter(category = "Business & Analysis")
        book_type = "Gujarati Business & Analysis Books"
    if data == "G_SF":
        products = Book.objects.filter(book_language = "Gujarati").filter(category = "Self-Help")
        book_type = "Gujarati Self-Help Books"
    if data == "G_SC":
        products = Book.objects.filter(book_language = "Gujarati").filter(category = "School/College")
        book_type = "Gujarati School/College Books"
    if data == "H_Novel":
        products = Book.objects.filter(book_language = "Hindi").filter(category = "Novel")
        book_type = "Hindi Novel"
    if data == "H_Biography":
        products = Book.objects.filter(book_language = "Hindi").filter(category = "Biography")
        book_type = "Hindi Biography"
    if data == "H_BA":
        products = Book.objects.filter(book_language = "Hindi").filter(category = "Business & Analysis")
        book_type = "Hindi Business & Analysis Books"
    if data == "H_SF":
        products = Book.objects.filter(book_language = "Hindi").filter(category = "Self-Help")
        book_type = "Hindi Self-Help Books"
    if data == "H_SC":
        book_type = "Hindi School/College Books"
        products = Book.objects.filter(book_language = "Hindi").filter(category = "Scholl/College")
    if data == "E_Novel":
        products = Book.objects.filter(book_language = "English").filter(category = "Novel")
        book_type = "English Novel"
    if data == "E_Biography":
        products = Book.objects.filter(book_language = "English").filter(category = "Biography")
        book_type = "English Biography"
    if data == "E_BA":
        products = Book.objects.filter(book_language = "English").filter(category = "Business & Analysis")
        book_type = "English Business & Analysis Books"
    if data == "E_SF":
        products = Book.objects.filter(book_language = "English").filter(category = "Self-Help")
        book_type = "English Self-Help Books"
    if data == "E_SC":
        products = Book.objects.filter(book_language = "English").filter(category = "Scholl/College")
        book_type = "English School/College Books"

    params = {'product': products, 'book_type':book_type}
    return render(request, 'shopview.html', params)

def handle_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email= request.POST['email']

        # Password Validation
        if (password1 != password2):
             messages.error(request, " Passwords do not match")
             return redirect('Home')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname 
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your has been successfully created")
        return redirect('Home')
    else:
        return HttpResponse("404 - Not Found")

def handle_signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "You Are Successfully Logged In")
            return redirect('Home')
        else:
            messages.error(request, "Invalid Credentials ! Please Try Again")
            return redirect('Home')
    else:
        return HttpResponse("404 - Not Found")
        

def handle_logout(request):
    logout(request)
    messages.success(request, "You Are Successfully Logged Out")
    return redirect('Home')

def contactUs(request):
    if request.method == "POST":
        contact_fname = request.POST['contact_fname']
        contact_lname = request.POST['contact_lname']
        contact_email = request.POST['contact_email']
        contact_msg = request.POST['contact_msg']

        contact = Contact(First_name=contact_fname, Last_name=contact_lname, Email=contact_email, Message=contact_msg)
        contact.save()
        messages.success(request, "We Are Reply You Soon.")
        return redirect('Home')
    else:
        return HttpResponse("404 - Not Found")
    
def aboutUs(request):
    return render(request, 'about.html')

def shoppingCart(request):
    return render(request, 'add_cart.html')

client = razorpay.Client(auth=(RAJORPAY_API_KEY, RAJORPAY_API_SECRET_KEY))
def shipping(request):
    if request.method == "POST":
        order_item = request.POST['order_item']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        city = request.POST['city']
        zip_code = request.POST['zip_code']
        address = request.POST['address']
        email = request.POST['email']
        total_price = request.POST['total_price']

        order = Order(order_item=order_item, first_name=first_name, last_name=last_name, city=city, zip_code=zip_code, address=address, email=email, total_price=total_price)
        order.save()

        add = address + ", " + city + " - " + zip_code
        params = {'name':first_name, 'address':add, 'total_price':total_price}

        payment = client.order.create(dict(amount=50000, currency= 'INR', payment_capture= 1))
        return render(request,'payment_test.html', params)
    return render(request, 'shipping.html')

def ship_order(request):
    return

def payment_test(request):
    return render(request, 'payment_test.html')

@csrf_exempt
def success(request):
    messages.success(request, "Thank You For Shopping. Keep Shopping!")
    # thank = True
    return redirect('Home')
    # return render(request, 'test.html' , {'thank':thank})