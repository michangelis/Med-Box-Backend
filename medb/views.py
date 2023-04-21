from django.db.models import Q, Count
from rest_framework import status
from .models import Users, UserPerscriptionPill, Alarm, Pills, Comment, Taken, Days, Motor
from .serializers import UserPerscriptionPillSerializer, UsrSerializer, NextUserSerializer, \
    UserSer, UserSerlzr, UserSerlzer, PillsSerializer, PillSerializer, CommentSerializer, \
    TakenSerializer, CreateUserProfileSerializer, CreatePillSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pytz
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from .models import Users, Pills, UserPerscriptionPill
from django.http import HttpRequest

@api_view()
def get_box(request):
    print('angelkas cool electician shit')
    box = True
    if box:
        return Response({'message': 'Box is inserted', 'box': True}, status=200)
    else:
        return Response({'message': 'Please insert the box', 'box': False}, status=200)



@api_view()
def get_user_alarms(request: HttpRequest, user_id):
    user = get_object_or_404(Users, pk=user_id)
    user_pills = UserPerscriptionPill.objects.filter(user=user).all()
    alarms = Alarm.objects.filter(user_prescription_pill__in=user_pills).all()

    # Create a list of dictionaries containing the required information
    alarm_list = []
    for alarm in alarms:
        pill_name = alarm.user_prescription_pill.per_pill.name
        alarm_time = alarm.time
        today = datetime.now().date()
        this_weekday = today.weekday()
        target_weekday = alarm.day.id - 1
        days_difference = target_weekday - this_weekday
        target_date = today + timedelta(days=days_difference)
        target_time = datetime.strptime(str(alarm_time), '%H:%M:%S').time()
        target_datetime = datetime.combine(target_date, target_time)

        alarm_data = {
            'id': alarm.id,
            'title': pill_name,
            'start': target_datetime.isoformat(),
        }
        alarm_list.append(alarm_data)

    return Response({'alarms': alarm_list}, status=200)


@api_view()
def get_disable(request, pill_id):
    pill = get_object_or_404(Pills, pk=pill_id)
    if pill.motor is None:
        return Response({'disabled': True}, status=200)
    else:
        return Response({'disabled': False}, status=200)


@api_view(['POST'])
def deload(request):
    print(request.data["pill_id"])
    pill = get_object_or_404(Pills, pk=request.data["pill_id"])
    if pill.motor is not None:
        for i in range(11):
            print(pill.motor.dscript)
        pill.inventory = 0
        pill.motor = None

        pill.save()
        return Response({'message': 'There is a pill in the machine'}, status=200)
    else:
        return Response({'message': 'There is Not a pill in the machine'}, status=200)



@api_view(['POST'])
def take_pill(request):
    pill = Pills.objects.get(pk=request.data["pill_id"])
    if pill.motor is not None:
        new_inv = pill.inventory - 1
        if new_inv > 0:
            print(pill.motor.script)
            pill.inventory = new_inv
            pill.save()
            return Response({'message': 'Here is your pill'}, status=200)
        elif new_inv == 0:
            print(pill.motor.script)
            pill.motor = None
            pill.save()
            return Response({'message': 'Here is your pill but empty'}, status=200)
    else:
        return Response({'message': 'No pills in machine'}, status=200)


@api_view(['POST'])
def post_pill_comment(request):
    user_id = request.data['user_id']
    pill_id = request.data['pill_id']
    comment_text = request.data['commentText']
    user = get_object_or_404(Users, pk=user_id)
    pill = get_object_or_404(Pills, pk=pill_id)
    Comment.objects.create(user=user, pill=pill, commentText=comment_text)

    return Response(data={"message": "Data received"}, status=200)


@api_view(['POST'])
def login(request):
    first_name, last_name = request.data['username'].split()
    try:
        user = Users.objects.get(first_name=first_name, last_name=last_name, password=request.data['password'])
        return Response(data={"message": "received", "img": user.imgSrc, "user_id": user.id}, status=200)
    except Users.DoesNotExist:
        return Response(data={"message": "No user found"}, status=404)



@api_view(['POST'])
def create_alarms(request):
    user_id = request.data.get('user_id')
    pill_id = request.data.get('pill_id')
    user = get_object_or_404(Users, pk=user_id)
    pill = get_object_or_404(Pills, pk=pill_id)
    user_pill = UserPerscriptionPill.objects.filter(user=user, per_pill=pill).first()
    if user_pill is None:
        user_pill = UserPerscriptionPill.objects.create(user=user, per_pill=pill)

    for form in request.data['formValues']:
        time = form.get('time')
        days = form.get('days')
        dosage = form.get('dosage')
        for day in days:
            alarm_day = get_object_or_404(Days, pk=day)
            if dosage is not None:
                alarm = Alarm.objects.create(quantity=dosage, time=time, day=alarm_day, user_prescription_pill=user_pill)
            else:
                alarm = Alarm.objects.create(time=time, day=alarm_day, user_prescription_pill=user_pill)
    return Response(data={"message": "received"}, status=200)


@api_view(['POST'])
def create_pill(request):
    null_values = Pills.objects.exclude(motor__isnull=True).count()
    if null_values < 4:
        empty_motor = Pills.objects.exclude(motor__isnull=False).values_list('id', flat=True).first()
        serializer = CreatePillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(motor_id=empty_motor)
            motor = get_object_or_404(Motor, pk=empty_motor)
            for inv in range(serializer.data["inventory"]):
                print(motor.script)
            return Response({"message": "Created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Something went wrong please try again"}, status=200)
    return Response({"message": "The machine is full"}, status=200)


@api_view(['POST'])
def register_user(request):
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
    full_name = f"{user.first_name}_{user.last_name}"
    print(full_name)
    return Response(response_data)


@api_view()
def verify_user(request, alarm_id):
    alarm = get_object_or_404(Alarm, pk=alarm_id)
    first_name = alarm.user_prescription_pill.user.first_name
    last_name = alarm.user_prescription_pill.user.last_name
    full_name = f"{first_name}_{last_name}"
    print(full_name)
    if full_name is not None:
        return Response({'message': False}, status=200)
    else:
        return Response({'message': True}, status=200)


@api_view(['POST'])
def take_medication(request, alarm_id):
    box = True
    alarm = get_object_or_404(Alarm, pk=alarm_id)
    pill = alarm.user_prescription_pill.per_pill
    if pill.motor is not None:
        if box:
            for quant in range(alarm.quantity):
                new_inv = pill.inventory - 1
                if new_inv > 0:
                    print(pill.motor.script)
                    pill.inventory = new_inv
                    pill.save()
                    message = "Here are your pills"
                elif new_inv == 0:
                    print(pill.motor.script)
                    pill.motor = None
                    pill.save()
                    message = "The pills are empty"
        else:
            return Response({'message': 'Please insert the box'}, status=200)
    else:
        return Response({'message': 'No pills in machine'}, status=200)

    taken = True
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
    pills = Pills.objects.exclude(motor=None).filter(perscription=True)
    serializer = PillsSerializer(pills, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def get_pills(request):
    pills = Pills.objects.filter()
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