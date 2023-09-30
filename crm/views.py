from django.shortcuts import render
from .models import Order
from .forms import OrderForm, NewOrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendMessage import sendTelegram

def query_set (request):
    list = Order.objects.all()
    form = OrderForm()
    return render(request, './query_set.html', {'list': list,
                                                'form': form})


def thanks_page(request):
    name = request.POST['name']  # записываем в переменную данные из формы
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)  # записываем значения из формы в БД
    element.save()
    return render(request, './thanks_old.html', {'name': name,
                                                 'phone': phone})


def inheritance_page(request):
    return render(request, './inheritance.html')


def site_view(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    new_form = NewOrderForm()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'new_form': new_form,
                }
    return render(request, './index.html', dict_obj)


def thanks_2(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone)
        return render(request, './thanks_2.html', {'name': name,
                                                   'phone': phone})
    else:
        return render(request, './thanks_2.html')




