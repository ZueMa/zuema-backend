from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Seller
from products.models import Product

import json

@csrf_exempt
def register(request):
    if (request.method != 'POST'):
        return HttpResponse(status=501)
  
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    Seller(
        username=body['username'],
        password=body['password'],
        first_name=body['first_name'],
        last_name=body['last_name'],
        company_name=body['company_name'],
        address=body['address'],
        description=body['description']
    ).save()

    return HttpResponse(status=204)

def current_seller(request):
    if (request.method != 'GET'):
        return HttpResponse(status=501)
    if ('user_id' not in request.COOKIES):
        return HttpResponse(status=404)

    seller = get_object_or_404(Seller, id=request.COOKIES['user_id'])

    return JsonResponse({
        'seller_id': seller.id,
        'username': seller.username,
        'first_name': seller.first_name,
        'last_name': seller.last_name,
        'company_name': seller.company_name,
        'address': seller.address,
        'description': seller.description
    })

@csrf_exempt
def create_product(request):
    if (request.method != 'POST' and request.method != 'GET'):
        return HttpResponse(status=501)
    if ('user_id' not in request.COOKIES):
        return HttpResponse(status=404)
    
    if (request.method == 'POST'):
        seller = get_object_or_404(Seller, id=request.COOKIES['user_id'])

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        product = Product(
        name=body['name'],
        category=body['category'],
        price=body['price'],
        num_stocks=body['num_stocks'],
        short_description=body['short_description'],
        full_description=body['full_description'],
        image=body['image'],
        seller=seller
        )
        product.save()

        return JsonResponse({
        'product_id': product.id
        }, status=201)

    else: 
 
        seller = get_list_or_404(Product, id=request.COOKIES['user_id'])

        products_response = []
        for product in seller:
            products_response.append({
            'product_id': product.id,
            'name': product.name,
            'category':product.category,
            'price': product.price,
            'short_description': product.short_description,
            'image': 'http://localhost:8000/' + str(product.image)
            })
        
        return JsonResponse({
            'products': products_response
            })

@csrf_exempt
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if (request.method == 'PUT'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        product.name = body['name']
        product.category = body['category']
        product.price = body['price']
        product.num_stocks = body['num_stocks']
        product.short_description = body['short_description']
        product.full_description = body['full_description']
        product.image = body['image']
        product.save()

        return HttpResponse(status=204)
    elif (request.method == 'DELETE'):
        product.delete()

        return HttpResponse(status=204)
    else:
        return HttpResponse(status=501)


    
    
