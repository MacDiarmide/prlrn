from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_date', 'comment_text')
    readonly_fields = ('comment_date',)
    extra = 1  # регулирует количество комментариев в карточке


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_date')
    list_display_links = ('id', 'order_name')  # эти поля будут кликабельными
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')  # по этим полям можно будет делать поиск
    list_filter = ('order_status',)  # нужно ставить запятую, хотя в кортеже один объект
    list_editable = ('order_status', 'order_phone')  # эти поля можно будет редактировать прямо в странице заказов
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_date', 'order_name', 'order_phone')  # задаем порядок отображения полей в карточке
    readonly_fields = ('id', 'order_date')
    inlines = [Comment, ]  # это чтобы видет комментарии в карточке каждого заказа


admin.site.register(Order, OrderAdmin) # регистрируем модель в админке, второй аргумент изменяет столбцы класса Order в админке
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)


