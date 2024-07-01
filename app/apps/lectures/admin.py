from django.contrib import admin
from .models import Measures

@admin.register(Measures)
class MeasuresAdmin(admin.ModelAdmin):
    list_display = ('created', 'aventage_volts_mono', 'aventage_volts_tri', 'i1', 'i2', 'i3', 'p1', 'p2', 'p3', 'energy', 'fp', 'hz') 
    autocomplete_fields = ('sensor', )

    @admin.display(description='Prom. Volts Mono')
    def aventage_volts_mono(self, obj):
        volts_mono = [obj.v1, obj.v2, obj.v3]
        return sum(volts_mono) / len(volts_mono)
    
    @admin.display(description='Prom. Volts Tri')
    def aventage_volts_tri(self, obj):
        volts_tri = [obj.v12, obj.v13, obj.v23]
        return sum(volts_tri) / len(volts_tri)