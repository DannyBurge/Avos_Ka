from django.shortcuts import render
from Avos_Ka.models import ProductList, Product, Amount, Measurment


def show_list(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    username = 'Дорогой друг' if request.user == 'AnonymousUser' else request.user
    shoplist_to_show = ""
    try:
        shoplist = ProductList.objects.get(title=f"user{request.user.id}_tmp")
    except ProductList.DoesNotExist:
        shoplist = ProductList(title=f"user{request.user.id}_tmp")
        shoplist.save()

    if request.method == 'POST':
        prod_name = f'{request.POST["product"]}'
        amount = f'{request.POST["how_much"]}'
        if len(prod_name) > 0:
            try:
                prod = Product.objects.get(name=prod_name)
            except Product.DoesNotExist:
                measure = Measurment.objects.get(name='шт.')
                measure.save()
                prod = Product(name=prod_name, measure=measure)
                prod.save()
            try:
                Amount.objects.get(for_product_list=shoplist, for_product=prod)
            except Amount.DoesNotExist:
                Amount.objects.create(for_product=prod, for_product_list=shoplist, amount=amount)

    for product_amount in Amount.objects.filter(for_product_list=shoplist):
        shoplist_to_show += f'<input type="checkbox" id="{product_amount}"'
        shoplist_to_show += f'<label for="{product_amount}">'
        shoplist_to_show += f' {product_amount.display_product_name()} - '
        shoplist_to_show += f'{product_amount.display_amount()} '
        shoplist_to_show += f'{product_amount.display_product_measure()}</label><br>'

    context = {'shoplist': shoplist_to_show,
               'num_visits': num_visits,
               'username': username}
    return render(request, 'ShoppingList/shoplist.html', context)
