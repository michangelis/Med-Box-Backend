from django.db.models import Q, Count
from .models import Users, UserPerscriptionPill, Alarm
from .serializers import UserPerscriptionPillSerializer, UsrSerializer, NextUserSerializer, UserSer, UserSerlzr
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pytz
from datetime import datetime

@api_view()
def user_list(request):
    query_set = Users.objects.values('id', 'first_name', 'last_name', 'description')
    return Response(query_set)

@api_view()
def get_user_pills(request):
    query_set = UserPerscriptionPill.objects.select_related('user').all()
    serializer = UserPerscriptionPillSerializer(query_set, many=True)
    return Response(serializer.data)


@api_view()
def get_next_user(request):
    user_serializer_class = UsrSerializer
    next_user_serializer_class = NextUserSerializer
    timezone = pytz.timezone('Europe/Athens')
    now = datetime.now(timezone)
    current_day = now.strftime('%A')
    current_time = now.strftime('%H:%M:%S')

    next_alarm = Alarm.objects.filter(day__day=current_day, time__gt=current_time).order_by('time').first()

    if next_alarm:
        user_pill = next_alarm.user_prescription_pill
        next_user = user_pill.user
        pill = user_pill.per_pill
        serialized_user = user_serializer_class(next_user)
        serialized_next_user = next_user_serializer_class({
            'id': serialized_user.data['id'],
            'first_name': serialized_user.data['first_name'],
            'last_name': serialized_user.data['last_name'],
            'pill_name': pill.name,
            'alarm_time': next_alarm.time
        })
        return Response(serialized_next_user.data)

    return Response({'message': 'No next user found.'})

@api_view()
def getUserCards(request):
    current_time = datetime.now().time()

    users = []
    for user in Users.objects.all():
        pills = {}
        for user_pill in UserPerscriptionPill.objects.filter(user=user):
            alarm = Alarm.objects.filter(user_prescription_pill=user_pill, time__gt=current_time).order_by('time').first()
            if alarm:
                pills['id'] = user_pill.per_pill.id
                pills['name'] = user_pill.per_pill.name
                pills['time'] = alarm.time

        user_dict = UserSer(user).data
        user_dict['prescription_pills'] = pills
        users.append(user_dict)

    return Response(users)

@api_view()
def count_taken(request):
    # Query the database to count the number of false taken values and associate them with the appropriate user
    users = Users.objects.annotate(taken_count=Count('userperscriptionpill__alarm__taken__taken', filter=Q(userperscriptionpill__alarm__taken__taken=False)))
    # Serialize the data
    serializer = UserSerlzr(users, many=True)

    # Return the serialized data through the response object
    return Response(serializer.data)



