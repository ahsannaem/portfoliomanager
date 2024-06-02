from django.contrib import admin
from .models import StockHolding,Portfolio,User,RiskProfile
# Register your models here.
admin.site.register(StockHolding)
admin.site.register(Portfolio)
admin.site.register(RiskProfile)