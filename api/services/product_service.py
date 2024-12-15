from api.models import Product

def create_product(data):
    return Product.objects.create(**data)

def get_all_products():
    return Product.objects.all()

def get_product_by_id(product_id):
    return Product.objects.filter(id=product_id).first()

def update_product(product_id, data):
    product = get_product_by_id(product_id)
    if product:
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return product
    return None

def delete_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        product.delete()
