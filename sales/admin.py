from django.contrib import admin

from .models import Customer, Product, Bill, Order, Producttype


class OrderInline(admin.TabularInline):
    model = Order
    extra = 1
    fields = ("bill",)
    readonly_fields = ("bill",)
    show_change_link = True


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "newsletter_abo", "email_address", "account")
    list_filter = ("newsletter_abo", "account")
    search_fields = ("name", "email_address")
    inlines = [OrderInline]

    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "email_address"), "classes": ["wide"]}),
        ("Account Information", {"fields": ("account", "newsletter_abo"), "classes": ["collapse"]}),
    )

    @admin.display(ordering="account")
    def account(self, obj):
        return obj.account

    @admin.display(ordering="newsletter_abo", boolean=True, description="Newsletter Abo")
    def newsletter_abo(self, obj):
        return obj.newsletter_abo

    @admin.display(ordering="name", description="Name")
    def name(self, obj):
        return f"{obj.last_name}, {obj.first_name}"


class ProducttypeInline(admin.TabularInline):
    model = Producttype
    extra = 1
    fields = ("product", "type_name")
    show_change_link = True


class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "bill")
    list_filter = ("customer", "bill")
    search_fields = ("customer__first_name", "customer__last_name", "bill__id")

    inlines = [ProducttypeInline]

    fieldsets = ((None, {"fields": ("customer", "bill"), "classes": ["wide"]}),)

    @admin.display(ordering="customer")
    def customer(self, obj):
        return obj.customer

    @admin.display(ordering="products")
    def products(self, obj):
        return obj.products.all()

    @admin.display(ordering="bill")
    def bill(self, obj):
        return obj.bill


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order, OrderAdmin)
admin.site.register(Producttype)
