from django.shortcuts import render, redirect
from Backend.models import *
from Webapp.models import ContactDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# To run index page
def index_page(request):
    C_data = CategoriesDB.objects.all()
    return render(request, "index.html", {'C_data': C_data})


# To run add categories page and take input data frm user
def add_categories_page(request):
    return render(request, "Add_Categories.html")


# To display added Categories
def display_categories(request):
    data = CategoriesDB.objects.all()
    return render(request, "Display_Categories.html", {'data': data})


# To save inputted data to DB
def save_categories(request):
    if request.method == "POST":
        cn = request.POST.get('cat_name')
        cd = request.POST.get('cat_description')
        c_img = request.FILES['cat_image']
        obj = CategoriesDB(Category_Name=cn, Category_Description=cd, Category_Image=c_img)
        obj.save()
        return redirect(add_categories_page)


# To edit categories data
def edit_category_page(request, cat_id):
    data = CategoriesDB.objects.get(id=cat_id)
    return render(request, "Edit_Categories.html", {'data': data})


# Create function to update edited data
def update_category_page(request, cat_id):
    if request.method == "POST":
        cn = request.POST.get('edit_cat_name')
        cd = request.POST.get('edit_cat_description')
        # Give an exception block to avoid errors while getting image
        try:
            img = request.FILES['edit_cat_image']
            # FileSystem storage need to import
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoriesDB.objects.get(id=cat_id).Category_Image
        CategoriesDB.objects.filter(id=cat_id).update(Category_Name=cn, Category_Description=cd, Category_Image=file)
        return redirect(display_categories)


# create function to delete each data
def delete_category_item(request, cat_id):
    delete_item = CategoriesDB.objects.filter(id=cat_id)
    delete_item.delete()
    return redirect(display_categories)


# Add products by selecting Category
def add_product_page(request):
    cat = CategoriesDB.objects.all()
    return render(request, "Add_Product.html", {'cat': cat})


# To save Products
def save_products(request):
    if request.method == "POST":
        pct = request.POST.get('category_select')
        pn = request.POST.get('product_name')
        pp = request.POST.get('product_price')
        pd = request.POST.get('product_description')
        pimg = request.FILES['product_image']
        obj = ProductsDB(Category=pct, Product_Name=pn, Product_Price=pp, Product_Description=pd, Product_Image=pimg)
        obj.save()
    return redirect(add_product_page)


# Create function to display products page
def display_products_page(request):
    pdata = ProductsDB.objects.all()
    return render(request, "Display_Products.html", {'pdata': pdata})


# Create page to edit products
def edit_products_page(request, pro_id):
    cat = CategoriesDB.objects.all()
    pdata = ProductsDB.objects.get(id=pro_id)
    return render(request, "Edit_Products.html", {'pdata': pdata, 'cat': cat})


# create function to update product edit page
def update_edit_products(request, pro_id):
    if request.method == "POST":
        ecs = request.POST.get('edit_category_select')
        epn = request.POST.get('edit_product_name')
        epp = request.POST.get('edit_product_price')
        epd = request.POST.get('edit_product_description')
        try:
            ep_img = request.FILES['edit_product_image']
            fs = FileSystemStorage()
            file = fs.save(ep_img.name, ep_img)
        except MultiValueDictKeyError:
            file = ProductsDB.objects.get(id=pro_id).Product_Image
        ProductsDB.objects.filter(id=pro_id).update(Category=ecs, Product_Name=epn, Product_Price=epp,
                                                    Product_Description=epd, Product_Image=file)
    return redirect(display_products_page)


# create function to delete product item

def delete_product_item(request, pro_id):
    del_pro = ProductsDB.objects.get(id=pro_id)
    del_pro.delete()
    return redirect(display_products_page)


def login_page(request):
    return render(request, "Admin_login.html")


def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(index_page)
            else:
                return redirect(login)
        else:
            return redirect(login)


def feedback_page(request):
    f_data = ContactDB.objects.all()
    return render(request, "FeedBack.html", {'f_data': f_data})


def feedback_data_delete(request, f_id):
    x = ContactDB.objects.get(id=f_id)
    x.delete()
    return redirect(feedback_page)