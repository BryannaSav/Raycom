from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import Item, Cart
from ..login_app.models import User
from django.contrib import messages

def home(request):
    context={
        'items' : Item.objects.all()
    }
    if 'first_name' not in request.session:
        return redirect('/')
    return render(request, 'home_app/home.html', context)

def account(request):
    context={
        'user':User.objects.get(id=request.session['id']),
    }
    return render(request, "home_app/profile.html", context)

def store(request):
    context={
        'user':User.objects.get(id=request.session['id']),
        'items':User.objects.get(id=request.session['id']).items.all(),
    }
    return render(request, "home_app/store.html", context)

def new_item(request):
    errors=Item.objects.item_validator(request.POST)
    print errors
    if len(errors) == 0:
        messages.success(request, "Item successfully created")
        Item.objects.create_item(request.POST, request.session['id'])
    else:
        for error in errors.itervalues():
            messages.error(request, error)
    return redirect('/home/store')

def show_item(request, id):
    context={
        'item': Item.objects.get(id=id)
    }
    return render(request, "home_app/show_item.html", context)

def edit_profile(request, id):
    context={
        'user':User.objects.get(id=id),
    }
    return render(request, 'home_app/edit_profile.html', context)

def add_to_cart(request, id):
    current_user=User.objects.get(id=request.session['id'])
    current_cart=Cart.objects.create(users=current_user)
    print "CURRENT CART:", current_cart
    print "CURRENT CART items:", current_cart.items

    # current_item=Item.objects.get(id=id)
    # qty=request.POST['qty']
    # current_user.carts.add(current_item,qty)
    # current_user.save()
    
    return redirect('/home')

def checkout(request):
    context = {
        'currentUser': User.objects.get(id=request.session['id'])
    }
    return render(request, "home_app/checkout.html", context)


        


