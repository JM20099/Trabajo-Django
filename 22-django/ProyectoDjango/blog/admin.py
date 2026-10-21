from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)  #readonly_fields: campos de solo lectura, no se pueden modificar desde el panel de administración

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:  #Si el objeto no tiene usuario asignado, asignamos el usuario que esta logueado
            obj.user_id = request.user.id  #Asignamos el usuario que esta logueado al campo user del modelo Article
        obj.save()  #Guardamos el objeto
       

# Register your models here.
admin.site.register(Category , CategoryAdmin)
admin.site.register(Article, ArticleAdmin)