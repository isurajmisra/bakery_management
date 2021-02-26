from .models import Product

def get_total_price(order):
    total_price = 0
    for product in order.products_details['products']:
        prod_id = product['id']
        prod_name = product['name']
        prod_quant = product['quantity']
        prod = Product.objects.filter(id=int(prod_id)).first()
        if prod:
            prod_pirce = int(prod_quant) * prod.selling_price
            if prod.discount > 0:
                prod_pirce -= (prod_pirce * prod.discount) / 100
        total_price += prod_pirce

    return total_price
