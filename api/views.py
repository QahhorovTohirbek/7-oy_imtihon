from main import models 
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone


@api_view(['GET'])
def staff_list(request):
    staff=models.Staff.objects.all()
    serializer_date = serializers.StaffSerializerList(staff, many=True)

    return Response(serializer_date.data)


@api_view(['POST'])
def attendance_create(request):
    serializer_data = serializers.AttendanceSerializer(data=request.data)
    if serializer_data.is_valid():
        staff = serializer_data.validated_data.get('staff')
        enter_time = serializer_data.validated_data.get('enter_time')
        exit_time = serializer_data.validated_data.get('exit_time')

        if not enter_time:
            enter_time = timezone.now()
            serializer_data.validated_data['enter_time'] = enter_time 

        last_attendance = models.Attendance.objects.filter(staff=staff).last()

        if last_attendance and not exit_time:
            last_attendance.exit_time = enter_time
            last_attendance.save()
        else:
            serializer_data.save()

        return Response({'success': True})
    return Response({'success': False})