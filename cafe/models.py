from django.db import models

# Create your models here.
# 메뉴 카테고리 : coffe / tea / Beverages
class Menu_Category(models.Model):
    category = models.CharField(max_length=20)
# 메뉴 : 카테고리[Coffe / Tea / Beverage / ] - 메뉴[Americano/Espresso/Latte/Cappuccino/...]
class Menu(models.Model):
    menu_text = models.CharField(max_length=20)
# 옵션: Hot / Iced / Only Iced
class Menu_Option(models.Model):
    pass