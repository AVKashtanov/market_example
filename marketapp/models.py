from django.db import models

class Tovar(models.Model):
	code = models.PositiveIntegerField(unique=True, verbose_name='Код товара')
	name = models.CharField(max_length=100, verbose_name='Наименование')
	price = models.PositiveIntegerField(default=0, verbose_name='Цена')

	class Meta:
		verbose_name='Товар'
		verbose_name_plural='Товары'

	def __str__(self):
		return str(self.code)

class Sklad(models.Model):
	code = models.OneToOneField(Tovar, on_delete=models.CASCADE, unique=True, verbose_name='Товар')
	count = models.PositiveIntegerField(default=0, verbose_name='Количество')

	class Meta:
		verbose_name='Склад'
		verbose_name_plural='Склад'

	def __str__(self):
		return str(self.code)

class Postavschik(models.Model):
	ogrn = models.PositiveIntegerField(unique=True, verbose_name='ОГРН')
	name = models.CharField(max_length=100, verbose_name='Организация')
	phone = models.CharField(max_length=100, verbose_name='Телефон')

	class Meta: 
		verbose_name='Поставщик'
		verbose_name_plural='Поставщики'

	def __str__(self):
		return str(self.ogrn)
		
class Postavka(models.Model):
	date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
	count_post = models.CharField(max_length=100, verbose_name='Количество товара')
	code = models.ForeignKey(Tovar, on_delete=models.CASCADE, verbose_name='Товар')
	postavschik = models.ForeignKey(Postavschik, on_delete=models.CASCADE, verbose_name='Поставщик')

	class Meta:
		verbose_name='Поставка'
		verbose_name_plural='Поставки'

	def __str__(self):
		return str(self.date)



		
		