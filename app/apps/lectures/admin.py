from django.contrib import admin
from .models import Measures

@admin.register(Measures)
class MeasuresAdmin(admin.ModelAdmin):
    list_display = ('created', 'aventage_volts_mono', 'aventage_volts_tri', 'Ia', 'Ib', 'Ic', 'Pa', 'Pb', 'Pc', 'energy', 'FP', 'Hz') 
    autocomplete_fields = ('sensor', )

    @admin.display(description='Prom. Volts Mono')
    def aventage_volts_mono(self, obj):
        volts_mono = [obj.Va, obj.Vb, obj.Vc]
        return round(sum(volts_mono) / len(volts_mono), 2)
    
    @admin.display(description='Prom. Volts Tri')
    def aventage_volts_tri(self, obj):
        volts_tri = [obj.Vca, obj.Vab, obj.Vbc]
        return round(sum(volts_tri) / len(volts_tri), 2)
    

