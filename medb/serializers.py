from rest_framework import serializers
from .models import Users, UserPerscriptionPill, Alarm, Pills, Comment, Taken
import pytz
from datetime import datetime, date



#for create_pill
class CreatePillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pills
        fields = '__all__'


#for register_user
class CreateUserProfileSerializer(serializers.ModelSerializer):
    imgSrc = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Users
        exclude = ('prescription_pills',)

    def create(self, validated_data):
        user = Users.objects.create(**validated_data)
        return user

    def get_imgSrc(self, obj):
        gender = obj.gender
        if gender:
            if gender == Users.MALE:
                return './users/user1.jpg'
            elif gender == Users.FEMALE:
                return './users/user2.jpg'
            elif gender == Users.OTHER:
                return './users/user3.jpg'
        return None





#for take_medication
class TakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taken
        fields = '__all__'


#for count_taken
class UserSerlzr(serializers.ModelSerializer):
    missed = serializers.IntegerField(source='taken_count')

    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'email', 'imgSrc', 'missed')

    def to_representation(self, instance):
        user_data = super().to_representation(instance)
        user_data['name'] = f"{user_data['first_name']} {user_data['last_name']}"
        user_data.pop('first_name')
        user_data.pop('last_name')
        return user_data


#for getUserCards
class UserSer(serializers.ModelSerializer):
    prescription_pill = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'imgSrc', 'prescription_pill']

    def get_prescription_pill(self, obj):
        timezone = pytz.timezone('Europe/Athens')
        now = datetime.now(timezone)
        current_day = now.strftime('%A')
        current_time = now.strftime('%H:%M:%S')
        next_pill = {}
        for user_pill in UserPerscriptionPill.objects.filter(user=obj):
            alarm = Alarm.objects.filter(user_prescription_pill=user_pill, time__gt=current_time,
                                         day__day=current_day).order_by('time').first()
            if alarm:
                if not next_pill or alarm.time < next_pill['time']:
                    next_pill = {
                        'name': user_pill.per_pill.name,
                        'time': alarm.time
                    }


        return next_pill

    def to_representation(self, instance):
        user_data = super().to_representation(instance)
        user_data['full_name'] = f"{user_data['first_name']} {user_data['last_name']}"
        user_data.pop('first_name')
        user_data.pop('last_name')
        return user_data

#for get next_user
class UsrSerializer(serializers.ModelSerializer):
    prescription_pills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'prescription_pills']


class NextUserSerializer(serializers.Serializer):
    alarm_id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    pill_name = serializers.CharField()
    alarm_time = serializers.TimeField()

    def to_representation(self, instance):
        user_data = super().to_representation(instance)
        user_data['full_name'] = f"{user_data['first_name']} {user_data['last_name']}"
        user_data.pop('first_name')
        user_data.pop('last_name')
        return user_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name']


#for get_user_pills
class UserPerscriptionPillSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()

    class Meta:
        model = UserPerscriptionPill
        fields = ['id', 'user_id']


class UserSerlzer(serializers.ModelSerializer):
    prescription_pills = serializers.StringRelatedField(many=True)
    gender = serializers.CharField(source='get_gender_display')
    age = serializers.SerializerMethodField()


    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'gender', 'description', 'age', 'imgSrc', 'prescription_pills']

    def to_representation(self, instance):
        user_data = super().to_representation(instance)
        user_data['full_name'] = f"{user_data['first_name']} {user_data['last_name']}"
        user_data.pop('first_name')
        user_data.pop('last_name')
        return user_data

    def get_age(self, obj):
        today = date.today()
        age = today.year - obj.birth_date.year - ((today.month, today.day) < (obj.birth_date.month, obj.birth_date.day))
        return age

class PillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pills
        fields = ['id', 'name', 'description', 'imageSrc']


class PillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pills
        fields = ['id', 'name', 'description', 'warning', 'company', 'inventory', 'imageSrc', 'weight']


class USer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email', 'imgSrc']

    def to_representation(self, instance):
        user_data = super().to_representation(instance)
        user_data['full_name'] = f"{user_data['first_name']} {user_data['last_name']}"
        user_data.pop('first_name')
        user_data.pop('last_name')
        return user_data


class CommentSerializer(serializers.ModelSerializer):
    user = USer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'commentText']
