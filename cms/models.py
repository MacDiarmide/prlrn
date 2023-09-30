from django.db import models

class CmsSlider(models.Model):  # обычно каждое приложение имеет свою веб-страницу
    cms_img = models.ImageField(upload_to='sliderimg/')  # можем добавлять изображения с помощью админ-панели, в папке media на моем ПК создастся папка sliderimg
    cms_title = models.CharField(max_length=40, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=100, verbose_name='Текст')
    cms_css = models.CharField(max_length=100, null=True, default='-', verbose_name='CSS-класс')  # CSS-класс теперь можно прописать в админке. Нужно написать там active, чтобы карусель заработала корректно. После добавления нового поля надо опять делать миграцию

    def __str__(self):  # все, что ниже, нужно исключительно для изменения отображения в админке
        return self.cms_title

    class Meta():
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'