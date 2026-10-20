from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):  # sirve para personalizar la forma en que se muestran los modelos en el panel de administración
    # Mostrar campos de solo lectura
    readonly_fields = ('created_at', 'updated_at')
admin.site.register(Article, ArticleAdmin)
# Registrar los modelos.

admin.site.register(Category)   #site actúa como el objeto encargado de registrar, organizar y mostrar tus modelos (como Article y Category) dentro de la interfaz gráfica del panel de administración de Django

# Configurar el titulo del panel
admin.site.site_header = "Django ADSO - SENA"
admin.site.site_title = "Django ADSO - SENA"
admin.site.index_title = "Panel de Gestión"