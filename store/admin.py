from django.contrib import admin

from .models import Product, Cart, CartItem, Category, Customer, Order, OrderItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Product)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
