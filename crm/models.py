from django.db import models


class StatusCrm(models.Model): # теперь в заказе появится поле статуса
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta():
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True) # это поля в админке
    order_name = models.CharField(max_length=200, verbose_name='Имя')  # второй аргумент нужен исключительно для изменения отображения в админке
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')
    #                                          пользователи не могут     одобрение   одобрение
    #                                          удалить статус            пустоты     пустоты в
    #                                                                     в базе      поле ввода
    #                                                                    данных

    def __str__(self):  # все, что ниже, нужно исключительно для изменения отображения в админке
        return self.order_name

    class Meta():
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')  # CASCADE значит, что при удалении заказа комментарий тоже удалится
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text

    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

