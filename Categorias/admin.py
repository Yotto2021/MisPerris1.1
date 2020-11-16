from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'create_at', 'update_at')

    def save_model(self, request, obj, form, change):
        if not obj.User_id:
            obj.User_id = request.User.id
        obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)