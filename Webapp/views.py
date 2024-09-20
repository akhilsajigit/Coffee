from django.shortcuts import render, redirect
from Backend.models import *
from Webapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
import razorpay

def home_page(request):
    cat = CategoriesDB.objects.all()
    return render(request, "Home.html", {'cat': cat})


def about_page(request):
    cat = CategoriesDB.objects.all()
    return render(request, "About.html", {'cat': cat})


def contact_page(request):
    cat = CategoriesDB.objects.all()
    return render(request, "Contact.html", {'cat': cat})


def service_page(request):
    cat = CategoriesDB.objects.all()
    return render(request, "Services.html", {'cat': cat})


def blog_page(request):
    cat = CategoriesDB.objects.all()
    pdata = ProductsDB.objects.all()
    return render(request, "Blog.html", {'cat': cat,'pdata':pdata})


def shop_page(request):
    cat = CategoriesDB.objects.all()
    pdata = ProductsDB.objects.all()
    return render(request, "Shop.html", {'cat': cat, 'pdata': pdata})


def product_filtered(request, cat_name):
    cat = CategoriesDB.objects.all()
    data = ProductsDB.objects.filter(Category=cat_name)
    return render(request, "Product_Filtered.html", {'data': data, 'cat': cat})


def single_product_page(request, p_id):
    cat = CategoriesDB.objects.all()
    pdata = ProductsDB.objects.get(id=p_id)
    return render(request, "Single_Product.html", {'pdata': pdata, 'cat': cat})


def user_register_page(request):
    return render(request, "User_Register.html")


def user_login_page(request):
    return render(request, "User_Login.html")


def save_user_register(request):
    if request.method == "POST":
        una = request.POST.get('username')
        uem = request.POST.get('email_id')
        upd = request.POST.get('password')
        obj = RegisterDB(User_Name=una, User_Email=uem, User_Password=upd)
        obj.save()
        messages.success(request, "User Registered")
        return redirect(user_register_page)


def user_login_session(request):
    if request.method == "POST":
        lun = request.POST.get('uname')
        lpd = request.POST.get('pwd')
        if RegisterDB.objects.filter(User_Name=lun, User_Password=lpd).exists():
            request.session['Username'] = lun
            request.session['Password'] = lpd
            messages.success(request, "Login Successfully")
            return redirect(home_page)
        else:
            return redirect(user_login_page)
    else:
        return redirect(user_login_page)


def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Successfull Logout")
    return redirect(home_page)


def cart_data_save(request, c_id):
    if request.method == "POST":
        try:
            c_img = request.FILES['cart_image']
            fs = FileSystemStorage()
            file = fs.save(c_img.name, c_img)
        except MultiValueDictKeyError:
            file = ProductsDB.objects.get(id=c_id).Product_Image
        cpn = request.POST.get('product_name')
        csn = request.POST.get('session_name')
        cqn = request.POST.get('quantity')
        c_tot = request.POST.get('total')
        obj = CartDB(Ct_User=csn, Ct_Product_Name=cpn, Ct_Quantity=cqn, Ct_Total_price=c_tot,
                     Ct_Image=file)
        obj.save()
        messages.success(request, "Added to cart")
    return redirect(cart_page)


def delete_cart_data(request, c_id):
    x = CartDB.objects.filter(id=c_id)
    x.delete()
    messages.error(request, "Deleted from cart")
    return redirect(cart_page)


def cart_page(request):
    cat = CategoriesDB.objects.all()
    cart_data = CartDB.objects.filter(Ct_User=request.session['Username'])
    sub_total = total = delivery_charge = 0
    for i in cart_data:
        sub_total = sub_total + i.Ct_Total_price
        if sub_total >= 500:
            delivery_charge = 50
        else:
            delivery_charge = 100
        total = sub_total + delivery_charge
    return render(request, "Cart.html", {'cat': cat, 'cart_data': cart_data, 'sub_total': sub_total,
                                         'delivery_charge': delivery_charge, 'total': total})


def checkout_page(request):
    cat = CategoriesDB.objects.all()
    cart_data = CartDB.objects.filter(Ct_User=request.session['Username'])
    sub_total = total = delivery_charge = 0
    for i in cart_data:
        sub_total = sub_total + i.Ct_Total_price
    if sub_total >= 500:
        delivery_charge = 50
    else:
        delivery_charge = 100
    total = sub_total + delivery_charge
    return render(request, "CheckOut.html", {'cat': cat, 'cart_data': cart_data,
                                             'total': total, 'sub_total': sub_total,
                                             'delivery_charge': delivery_charge})


def save_customer_data(request):
    if request.method == "POST":
        cname = request.POST.get('customer_name')
        c_cy = request.POST.get('customer_country')
        c_add = request.POST.get('customer_address')
        c_city = request.POST.get('customer_city')
        c_mob = request.POST.get('customer_mobile')
        c_em = request.POST.get('customer_email')
        pp = request.POST.get('price')
        obj = OrderDB(Customer_Name=cname, Customer_State=c_cy, Customer_Address=c_add,
                      Customer_City=c_city, Customer_Mobile=c_mob, Customer_Email=c_em, Price=pp)
        obj.save()
    return redirect(payment_page)


def payment_page(request):
    customer = OrderDB.objects.order_by('-id').first()
    name = customer.Customer_Name
    pay = customer.Price
    amount = int(pay * 100)
    pay_str = str(amount)
    if request.method == "POST":
        order_currency = "INR"
        client = razorpay.Client(auth=('rzp_test_PMmGnroCxOlaJ0', 'rD9yidEziI0RjKCkl2HUPe7u'))
        payment = client.order.create({'amount':amount, 'currency':order_currency, 'payment_capture':'1'})
    return render(request, "Payment.html", {'name': name,'pay_str':pay_str})


def save_feedback_data(request):
    if request.method == "POST":
        f_Name = request.POST.get('f_Name')
        f_Mob = request.POST.get('f_Mob')
        f_Em = request.POST.get('f_Em')
        f_Sub = request.POST.get('f_Sub')
        f_msg = request.POST.get('f_msg')
        obj = ContactDB(fd_back_Name=f_Name, fd_back_Mobile=f_Mob, fd_back_Email=f_Em,
                        fd_back_Subject=f_Sub, fd_back_Message=f_msg)
        obj.save()
        return redirect(contact_page)
