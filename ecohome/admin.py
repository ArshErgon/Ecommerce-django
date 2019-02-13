from django.contrib import admin


from .models import BannerProduct, HomeProductDisplay, UserDetail

admin.site.register(HomeProductDisplay)
admin.site.register(BannerProduct)
admin.site.register(UserDetail)
