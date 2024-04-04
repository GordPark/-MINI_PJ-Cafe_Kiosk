from django.db import models

# Create your models here.
# 메뉴 카테고리 : coffe / tea / Beverages
class Menu_Category(models.Model):
    category = models.CharField(verbose_name="category",max_length=20)
    
    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.category

# 메뉴 : 카테고리[Coffe / Tea / Beverage / ] - 메뉴[Americano/Espresso/Latte/Cappuccino/...]
class Menu(models.Model):
    menu_name = models.CharField(max_length=20)
    category = models.ForeignKey(Menu_Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    best = models.BooleanField(default=True)
    # 품절처리
    disabled = models.BooleanField(default=True)
    
    
    class Meta:
        ordering = ('category',)
    
    def __str__(self):
        return self.menu_name
    
# 옵션: Hot / Iced / Only Iced
class Menu_Option(models.Model):
    Option = models.CharField(max_length=20)
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    

# 장바구니
class Shopping_Cart(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# 주문 
class Order:
    menu_name = models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE)
    order_dt = models.DateTimeField(auto_now_add=True)  
    wait_id = models.IntegerField()

# 결제
class Charge(models.Model):
    pass