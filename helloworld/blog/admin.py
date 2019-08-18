from django.contrib import admin

# Register your models here.

# 1.你可以通过重写ModelAdmin的get_form方法来做到这一点。

# 2.now, the blow way can not be work.
class BlogModelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'blogger':
            kwargs['initial'] = request.user.id
        return super(BlogModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )
