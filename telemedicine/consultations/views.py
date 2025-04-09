from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Consultation
from .serializers import ConsultationSerializer
from rest_framework.permissions import IsAuthenticated

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'DOCTOR':
            return Consultation.objects.filter(doctor=user)
        elif user.user_type == 'PATIENT':
            return Consultation.objects.filter(patient=user)
        return Consultation.objects.all()

    @action(detail=True, methods=['post'])
    def start_call(self, request, pk=None):
        consultation = self.get_object()
        if consultation.status != 'CONFIRMED':
            return Response(
                {'error': 'Consultation must be confirmed to start'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        consultation.status = 'ACTIVE'
        consultation.started_at = timezone.now()
        consultation.save()
        return Response({'status': 'call started', 'room_id': str(consultation.room_id)})

    @action(detail=True, methods=['post'])
    def end_call(self, request, pk=None):
        consultation = self.get_object()
        if consultation.status != 'ACTIVE':
            return Response(
                {'error': 'No active call to end'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        consultation.status = 'COMPLETED'
        consultation.ended_at = timezone.now()
        consultation.call_duration = (consultation.ended_at - consultation.started_at).seconds
        consultation.save()
        return Response({
            'status': 'call ended', 
            'duration': consultation.call_duration,
            'start_time': consultation.started_at,
            'end_time': consultation.ended_at
        })
