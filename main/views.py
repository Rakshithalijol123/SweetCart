from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import Product,Review,Cart
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.
def index(request):
    retrive = Product.objects.all()
    ##to print how many cart items present for the given user
    if request.user.is_authenticated:
        user = request.user
        get_cart = Cart.objects.filter(user=user)
        return render(request,'index.html',{'retrive':retrive,'cart_length':len(get_cart)})
    else:
        return render(request, 'index.html', {'retrive': retrive})
def show(request,id):
    if request.user.is_authenticated:
        details = Product.objects.filter(id=id)
        retrive_review = Review.objects.filter(products=details[0])
        count = len(retrive_review)
        return render(request,'show.html',{'details':details[0],'retrive_review':retrive_review,'count':count})
    else:
        return redirect('/accounts/login/')

def reviews(request,id):
    if request.method == 'POST':
        review = request.POST.get('review','')
        user = request.user
        if review != "":
            product = Product.objects.filter(id=id)
            create = Review.objects.create(review=review,user=user,products=product[0])
            create.save()
        else:pass
        return redirect(f"/show/{product[0].id}/")

def cart(request):
    user = request.user
    id1 = int(request.POST.get('get_id',-1))
    if id1 == -1:
        retrive_cart = Cart.objects.filter(user=user)
    else:
        item = Product.objects.filter(id=id1)
        #[obj1,obj2,...]
        get_product_from_cart = Cart.objects.filter(user=user,item=item[0])
        if len(get_product_from_cart) == 0:
            create_cart = Cart.objects.create(item=item[0],user=user,price=item[0].price)
            create_cart.save()
        else:pass
    # retrive_cart = Cart.objects.filter(user=user)
    # retrive_price = Cart.objects.filter(user=user)
    total_price = 0
    get_cart_price = Cart.objects.filter(user=user)
    for price in get_cart_price:
        total_price += price.price
    retrive_cart = Cart.objects.filter(user=user)
    return render(request, 'cart.html', {'retrive_cart': retrive_cart[::-1],'total_price':total_price})

def delete_cart_item(request,id):
    #########my code didn't explained
    update_original_quntity = Cart.objects.filter(id=id).update(quantity=1)
    #########my code didn't explained
    delete_item = Cart.objects.filter(id=id).delete()
    messages.success(request,'you are successfully deleted your item')
    return redirect('/cart/')
    # return HttpResponse(f"{id}-deleted and deleted item is {delete_item}")

def update_quantity(request,id):
    user = request.user
    get_item = Cart.objects.filter(id=id)
    get_quantity = int(request.POST.get('get_quantity',''))
    price = Product.objects.filter(id=get_item[0].item.id)
    if get_quantity >= 0:
        update_cart = Cart.objects.filter(id=id).update(quantity=get_quantity,price=price[0].price*get_quantity)
    else:pass
    retrive_price = Cart.objects.filter(user=user)
    # for obj in retrive_price:
    #     obj.item.price *= obj.quantity
    return redirect('/cart/')

def go_to_carts(request):
    return redirect('/cart/')

def delete_review(request,id):
    get_review = Review.objects.filter(id=id)
    get_product = Product.objects.filter(id=get_review[0].products.id)
    delete = Review.objects.filter(id=id).delete()
    messages.success(request,'review deleted successfully')
    return redirect(f'/show/{get_product[0].id}/')
    # return HttpResponse(get_review[0].products.name)
    # delete = Review.objects.filter(id=id).delete()
    # print(get_review[0].id)
    # get_product = Product.objects.filter(id= get_review[0].products.id)
    #
    # return redirect(f'/show/{get_product[0].id}/')

def adress(request):
    return render(request,'adress.html')

def order(request):
    user = request.user
    delete_cart_item = Cart.objects.filter(user=user).delete()
    messages.success(request,'Your order placed successfully')
    return redirect('/')









