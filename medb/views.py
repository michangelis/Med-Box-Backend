from django.db.models import Q, Count
from rest_framework import status
from .models import Users, UserPerscriptionPill, Alarm, Pills, Comment, Taken
from .serializers import UserPerscriptionPillSerializer, UsrSerializer, NextUserSerializer, \
    UserSer, UserSerlzr, UserSerlzer, PillsSerializer, PillSerializer, CommentSerializer, \
    TakenSerializer, CreateUserProfileSerializer, CreatePillSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pytz
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import Users, Pills, UserPerscriptionPill
from playsound import playsound
import threading




@api_view(['POST'])
def create_pill(request):
    serializer = CreatePillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_user(request):
    print(request.data)
    serializer = CreateUserProfileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    birth_date = validated_data.get('birth_date')
    if birth_date:
        validated_data['birth_date'] = birth_date.strftime('%Y-%m-%d')
    gender = validated_data.get('gender')
    if gender:
        if gender == Users.MALE:
            validated_data['imgSrc'] = './users/user1.jpg'
        elif gender == Users.FEMALE:
            validated_data['imgSrc'] = './users/user2.jpg'
        elif gender == Users.OTHER:
            validated_data['imgSrc'] = './users/user3.jpg'
    user = Users.objects.create(**validated_data)
    response_data = {
        "user": CreateUserProfileSerializer(user, context=serializer.context).data,
    }
    return Response(response_data)


@api_view(['POST'])
def take_medication(request, alarm_id):
    alarm = get_object_or_404(Alarm, pk=alarm_id)
    taken = request.data.get('taken')

    if taken is None:
        return Response({'error': 'taken field is required'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = TakenSerializer(data={'taken': taken, 'alarm': alarm.id})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def user_list(request):
    query_set = Users.objects.values('id', 'first_name', 'last_name', 'description')
    return Response(query_set)

@api_view()
def get_user_pills(request):
    query_set = Users.objects.select_related('userperscriptionpill').all()
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
            'alarm_id': next_alarm.id,
            'first_name': serialized_user.data['first_name'],
            'last_name': serialized_user.data['last_name'],
            'pill_name': pill.name,
            'alarm_time': next_alarm.time
        })
        return Response(serialized_next_user.data)

    return Response({'full_name': 'No one for today'})


@api_view()
def getUserCards(request):
    timezone = pytz.timezone('Europe/Athens')
    now = datetime.now(timezone)
    current_day = now.strftime('%A')
    current_time = now.strftime('%H:%M:%S')

    users = []
    for user in Users.objects.all():
        next_pill = {}
        for user_pill in UserPerscriptionPill.objects.filter(user=user):
            alarm = Alarm.objects.filter(user_prescription_pill=user_pill, time__gt=current_time,
                                         day__day=current_day).order_by('time').first()
            if alarm:
                if not next_pill or alarm.time < next_pill['time']:
                    next_pill = {
                        'id': user_pill.per_pill.id,
                        'name': user_pill.per_pill.name,
                        'time': alarm.time
                    }

        user_dict = UserSer(user).data
        user_dict['prescription_pill'] = next_pill
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


@api_view()
def get_user_p(request):
    users = []
    for user in Users.objects.all():
        pills = []
        for user_pill in UserPerscriptionPill.objects.filter(user=user):
            pill_data = {
                'id': user_pill.per_pill.id,
                'name': user_pill.per_pill.name,
            }
            pills.append(pill_data)

        user_dict = UserSerlzer(user).data
        user_dict['prescription_pills'] = pills
        users.append(user_dict)

    return Response(users)


@api_view()
def get_user(request, user_id):
    try:
        user = Users.objects.get(id=user_id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    pills = []
    for user_pill in UserPerscriptionPill.objects.filter(user=user):
        pill_data = {
            'id': user_pill.per_pill.id,
            'name': user_pill.per_pill.name
        }
        pills.append(pill_data)

    user_data = UserSerlzer(user).data
    user_data['prescription_pills'] = pills

    return Response(user_data)


@api_view()
def get_per_pills(request):
    pills = Pills.objects.filter(perscription=False)
    serializer = PillsSerializer(pills, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def get_pills(request):
    pills = Pills.objects.all()
    serializer = PillsSerializer(pills, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def get_pill(request, pill_id):
    try:
        pill = Pills.objects.get(id=pill_id)
    except Pills.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PillSerializer(pill)
    return Response(serializer.data)


@api_view()
def get_comments(request, pill_id):
    try:
        pill = Pills.objects.get(id=pill_id)
    except Pills.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comments = Comment.objects.filter(pill=pill)
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)