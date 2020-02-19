from django.conf import settings
from shop.models import Candy
from decimal import Decimal


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'count': 0,
                                     'price': str(product.price)}

        if update_count:
            self.cart[product_id]['count'] = count
        else:
            self.cart[product_id]['count'] += count
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Candy.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['count'] * item['price']
            yield item

    def __len__(self):
        res = sum(x['count'] for x in self.cart.values())
        return res

    def get_total_price(self):
        res = sum(Decimal(x['count']) * Decimal(x['price']) for x in self.cart.values())
        return res

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

# self.cart = {"0": {'quantity': 0,
#                    'price': 5000,
#                    'product': ProductObj,
#                    'total_price': 'qua' * 'price'},
#              "1": {'quantity': 2,
#                    'price': 7000,
#                    'product': ProductObj},
#              }
