from django.contrib import admin
from django.utils.html import format_html
from .models import Tag, Device, Located, Sensor

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'code', 'description')

@admin.register(Located)
class LocatedAdmin(admin.ModelAdmin):
    list_display = ('display_enterprise', 'slug','name', 'display_sensors')
    search_fields = ('enterprise__name', 'name')
    list_filter = ('enterprise__name', )

    @admin.display(description="Empresa")
    def display_enterprise(self, obj):
        return obj.enterprise
    
    @admin.display(description='Sensores')
    def display_sensors(self, obj):
        sensors = obj.sensor_located.all()
        output = ""
        if sensors:
            output = '<ul>'
            for sensor in sensors:
                output += f'<li>{sensor.code}</li>'
            output += '</ul>'
        else:
            message = 'No existen sensores'
            output = '<ul>' + f'<li>{message.upper()}</li>' + '</ul>'
        
        return format_html(output)


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('display_enterprise', 'display_enterprise_locate', 'code', 'display_sensor_model')
    readonly_fields = ('code', )
    list_filter = ('located__name',)
    search_fields = ('located__enterprise__name', )
    autocomplete_fields = ('located', )

    @admin.display(description="Empresa")
    def display_enterprise(self, obj):
        return obj.located.enterprise

    @admin.display(description="Ubicación")
    def display_enterprise_locate(self, obj):
        return obj.located.name
    
    @admin.display(description="Detalle")
    def display_sensor_model(self, obj):
        return obj.device