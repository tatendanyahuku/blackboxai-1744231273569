from django.contrib import admin
from .models import Consultation

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'scheduled_time', 'status')
    list_filter = ('status', 'doctor', 'patient')
    search_fields = ('patient__username', 'doctor__username', 'symptoms')
    date_hierarchy = 'scheduled_time'
    ordering = ('-scheduled_time',)

admin.site.register(Consultation, ConsultationAdmin)
