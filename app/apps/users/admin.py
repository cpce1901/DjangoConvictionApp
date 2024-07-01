from django.contrib import admin
from django.utils.html import format_html
from .models import User, Enterprise
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_users', 'display_locates')

    @admin.display(description='Usuarios')
    def display_users(self, obj):
        users = obj.user_enterprise.all()
        output = ""
        if users:
            output = '<ul>'
            for users in users:
                output += f'<li>{users.email}</li>'
            output += '</ul>'
        else:
            message = 'No existen usuarios'
            output = '<ul>' + f'<li>{message.upper()}</li>' + '</ul>'
        
        return format_html(output)

    @admin.display(description='Lugares de instalación')
    def display_locates(self, obj):
        locates = obj.located_enterprise.all()
        output = ""
        if locates:
            output = '<ul>'
            for locate in locates:
                output += f'<li>{locate.name}</li>'
            output += '</ul>'
        else:
            message = 'No existen lugares'
            output = '<ul>' + f'<li>{message.upper()}</li>' + '</ul>'
        
        return format_html(output)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'last_name', 'display_enterprise')
    exclude = ('date_joined', 'last_login', 'groups', 'user_permissions')
    list_filter = ('enterprise__name', )
    search_fields = ('name', 'last_name', 'email')

    @admin.display(description='Empresa')
    def display_enterprise(self, obj):
        return  obj.enterprise.name if obj.enterprise else ""

    def save_model(self, request, obj, form, change):
        # Hash the password if it is being set/changed
        if form.cleaned_data['password']:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

    