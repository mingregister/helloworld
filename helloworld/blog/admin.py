from django.contrib import admin

# from django.contrib.auth.models import User
from accounts.models import User
from .models import Blog

# Register your models here.

# 这个方法可以实现选择blogger时，自动选择当前用户。
# 但是：仅限于在admin页面下.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    date_hierarchy = 'modified_time'
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'blogger':
            kwargs['initial'] = request.user.id
        # # 限制可选项
        # if db_field.name == 'blogger':
        #     kwargs['queryset'] = User.objects.filter(id=request.user.id)
        return super(BlogAdmin, self).formfield_for_foreignkey(
                    db_field, request, **kwargs)

