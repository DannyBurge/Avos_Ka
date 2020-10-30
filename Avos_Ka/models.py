from django.db import models
from django.contrib.auth.models import User


class Measurment(models.Model):
    name = models.CharField(max_length=200, null=True,)

    def display_name(self):
        return f"{self.name}"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True,)
    measure = models.ForeignKey(Measurment, on_delete=models.CASCADE, null=True)

    def display_name(self):
        return f"{self.name}"

    def display_measure(self):
        return f"{self.measure.display_name()}"

    def __str__(self):
        return self.name


class ProductList(models.Model):
    title = models.CharField(max_length=200)
    product_list = models.ManyToManyField(Product, through="Amount")

    def display_product_list(self):
        show_list = ''
        for product in self.product_list.all():
            show_list += f"{product.display_name()}\n"
        return show_list

    def display_title(self):
        return self.title

    def __str__(self):
        return self.title


class Amount(models.Model):
    for_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,)
    for_product_list = models.ForeignKey(ProductList, on_delete=models.CASCADE, null=True,)
    amount = models.CharField(max_length=10)

    def display_product_name(self):
        return self.for_product.display_name()

    def display_product_list_title(self):
        return self.for_product_list.title

    def display_product_measure(self):
        return self.for_product.display_measure()

    def display_amount(self):
        return self.amount


class Recepie(models.Model):
    title = models.CharField(max_length=200, null=True,)
    recepie_products = models.OneToOneField(ProductList, on_delete=models.SET_NULL, null=True,)
    describe = models.TextField(null=True,)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def display_title(self):
        return self.title

    def display_recepie_products(self):
        return self.recepie_products.display_product_list()

    def display_describe(self):
        return self.describe

    def display_author(self):
        return self.author

    # TODO:
    # Аналитическая подборка рецептов
    # типа, перекрестное сравнение с другими пользователями
    # по лайканым или авторским рецептам
    # подборка внутри одного пользователя на основе любимых продуктов
