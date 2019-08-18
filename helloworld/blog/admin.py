from django.contrib import admin

from .models import Blog

# Register your models here.

# 这个方法可以实现选择blogger时，自动选择当前用户。
# 但是：仅限于在admin页面下.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'blogger':
            kwargs['initial'] = request.user.id
        return super(BlogAdmin, self).formfield_for_foreignkey(
                    db_field, request, **kwargs)

