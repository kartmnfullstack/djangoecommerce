from django.conf import settings
from products.models import Products
from cart.models import Cartitems,Cart_model
#Cart object initialization using session. 
class Cart():
    #initialize cart
    def __init__(self,request):
        self.request = request
        self.session = request.session

        cart_session = self.session.get(settings.CARTID)

        if cart_session is None:
            self.session[settings.CARTID] = {}
            cart_session = self.session[settings.CARTID]
            

        self.cart_session = cart_session

        if self.request.user.is_authenticated and not self.cart_session:
            self.load_from_db()


    def load_from_db(self):
        cart_in_db,_ = Cart_model.objects.get_or_create(user=self.request.user)
        items = Cartitems.objects.filter(cart=cart_in_db)

        for i in items:
            self.cart_session[str(i.product_id)] = {'quantity': i.quantity}
        self.session.modified = True

    def save_to_db(self):
        if not self.request.user.is_authenticated:
            return None
        
        cart_in_db,_ = Cart_model.objects.get_or_create(user=self.request.user)

        Cartitems.objects.filter(cart=cart_in_db).delete()
        
        product_items = []

        for p_id,items_data in self.cart_session.items():
            product_items.append(Cartitems(
                cart = cart_in_db,
                product_id = int(p_id),
                quantity = int(items_data['quantity'])
            ))

        if product_items:
            Cartitems.objects.bulk_create(product_items)
        
        self.session.modified = True

        return cart_in_db
    #adding items to cart
    def addtocart(self,product,qty):
        product_id = str(product.id)

        if product_id in self.cart_session:
            self.cart_session[product_id]['quantity'] += int(qty)
        else:
            self.cart_session[product_id] = {'quantity':int(qty)}
        self.save_to_db()

        self.session.modified = True

    #length of cart for display purposes
    def __len__(self):
        return len(self.cart_session.values())


    #items in the cart
    def cart_items(self):

        products_in_cart = self.cart_session.keys()

        products_list = Products.objects.filter(id__in=products_in_cart)

        for prod in products_list:
            data = self.cart_session.get(str(prod.id),{'quantity':0})
            prod.quantity = data['quantity']


            prod.subtotal = prod.price * prod.quantity

        return products_list

    #updating cart
    def cart_update(self,product,qty):
        product_id = str(product)
        product_qty = int(qty)

        if product_qty > 0:
            self.cart_session[product_id] = {'quantity':product_qty}
        else:
            self.cart_delete(product)

        self.save_to_db()

        self.session.modified = True

        return self.cart_session

    #removing items from cart
    def cart_delete(self,product):
        product_id = str(product)

        if product_id in self.cart_session:
            del self.cart_session[product_id]
        self.save_to_db()
        self.session.modified = True


#context processor

def cart(request):

    return {'cart':Cart(request)}