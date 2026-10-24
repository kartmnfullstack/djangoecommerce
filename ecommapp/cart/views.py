from django.shortcuts import render,get_object_or_404
from .cartinit import Cart
from products.models import Products
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages


@login_required()
def cart(request):
    cart = Cart(request)
    products_in_cart = cart.cart_items()
    total = 0

    for c in products_in_cart:
        total += c.subtotal
    context = {
        'products_in_cart':products_in_cart,
        'total': total
    }
    return render(request,'pages/cart.html',context)

def cart_add(request):

    if not request.user.is_authenticated:
        return JsonResponse({
            'authenticated': False,
            'redirect_url': reverse('register') 
        },status=401)
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Products,id=product_id)
        cart.addtocart(product=product,qty=product_qty)
        cart_length = cart.__len__()
        # res = JsonResponse({'Product': product.name})
        res = JsonResponse({'cart_qty':cart_length,'message':'Product has been added'})
        return res
    return JsonResponse({'error':'Invalid request'},status=400)

def cart_remove(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            'authenticated': False,
            'redirect_url': reverse('register') 
        },status=401)
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.cart_delete(product=product_id)
        cart_length = cart.__len__()
        res = JsonResponse({'cart_qty':cart_length,'message':'Product has been deleted'})
        return res

def cart_update(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            'authenticated': False,
            'redirect_url': reverse('register') 
        },status=401)
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.cart_update(product=product_id,qty=product_qty)
        cart_length = cart.__len__()
        res = JsonResponse({'cart_qty':cart_length,'message':'Product has been updated'})
        return res