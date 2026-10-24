from django.test import TestCase,Client,SimpleTestCase
from django.urls import resolve,reverse 
from frontend.views import productview
from products.models import Products,Category

#unit testing for products model
class ProductsTesting(TestCase):
    def test_entry_matches(self):
        product = Products(name="Test1",price=67.8,description="Loreum")
        self.assertEqual(product.name,"Test1")
        self.assertIs(product.price,67.8)
        self.assertIs(product.description,"Loreum")
        self.assertIsNone(product.id)

    def test_product_display(self):
        product = Products(name="Test1",price=67.8,description="Loreum")
        name = product.__str__()
        self.assertEqual(name,"Test1")

#unit testing for category model
class CategoryTesting(TestCase):
    def test_name_is_same_as_input(self):
        cat = Category(title="Test2")
        self.assertEqual(cat.title,"Test2")
        self.assertIsNone(cat.id)

    def test_category_display(self):
        category = Category(title="cat1")
        title = category.__str__()
        self.assertEqual(title,"cat1")

#unit testing for product views
class ProductViewTesting(TestCase):
    def setUp(self):
        self.client = Client()

    def test_products_view(self):
        res = self.client.get("/products")
        self.assertEqual(res.status_code,200)

    def test_products_view_content(self):
        res = self.client.get("/products")
        self.assertTemplateUsed(res,"pages/products.html")

#unit testing for product urls
class ProductUrlsTesting(SimpleTestCase):

    def test_products_page(self):
        url_link = reverse('products')
        self.assertEqual(resolve(url_link).func,productview)

#integration testing for paginator and search of products
class ProductIntegrationTest(TestCase):

    def test_product_page_paginator(self):
        Products.objects.create(name="Test1",price=67.8,description="Loreum")
        Products.objects.create(name="Test2",price=47.8,description="Loreum")
        Products.objects.create(name="Test3",price=27.8,description="Loreum")
        Products.objects.create(name="Test4",price=77.8,description="Loreum")

        p1 = self.client.get(reverse('products'))
        page_con_p1 = p1.context.get('page_obj')
        p2 = self.client.get(reverse('products')+'?page=2')
        page_con_p2 = p2.context.get('page_obj')
        self.assertEqual(len(page_con_p1),3)
        self.assertEqual(len(page_con_p2),1)

    def test_product_page_search(self):
        p1 = Products.objects.create(name="T1",price=47.8,description="Loreum")
        p2 = Products.objects.create(name="A1",price=47.8,description="Loreum")

        p1_s = self.client.get(reverse('products')+'?search=t&price=47.8')
        page_con_p1_s = p1_s.context.get('page_obj')
        re = [i['name'] for i in page_con_p1_s.object_list]
        self.assertIn(p1.name,re)
        self.assertNotIn(p2.name,re)


