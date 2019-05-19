from django.contrib import admin
from . models import About, header, category, numbers

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'reload')
admin.site.register(About, AboutAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'reload')
admin.site.register(category, categoryAdmin)

class headerAdmin(admin.ModelAdmin):
    list_display = ('title', 'reload')
admin.site.register(header, headerAdmin)

class numbersAdmin(admin.ModelAdmin):
    list_display = ('title', 'reload')
admin.site.register(numbers, numbersAdmin)