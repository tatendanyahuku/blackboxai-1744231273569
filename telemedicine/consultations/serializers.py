from rest_framework import serializers
from .models import Consultation
from users.models import CustomUser

class ConsultationSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
        slug_field='username',
        queryset=CustomUser.objects.filter(user_type='PATIENT')
    )
    doctor = serializers.SlugRelatedField(
        slug_field='username', 
        queryset=CustomUser.objects.filter(user_type='DOCTOR')
    )

    class Meta:
        model = Consultation
        fields = '__all__'
        read_only_fields = ('room_id', 'started_at', 'ended_at', 'call_duration', 'created_at', 'updated_at', 'status')
