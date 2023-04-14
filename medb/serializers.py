from rest_framework import serializers
from .models import Users, UserPerscriptionPill, Alarm, Pills, Comment
from datetime import datetime


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
    prescription_pills = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'imgSrc', 'prescription_pills']

    def get_prescription_pills(self, obj):
        current_time = datetime.now().time()
        pills = {}
        for user_pill in UserPerscriptionPill.objects.filter(user=obj):
            alarm = Alarm.objects.filter(user_prescription_pill=user_pill, time__gt=current_time).order_by('time').first()
            if alarm:
                pills[user_pill.per_pill.name] = alarm.time
        return pills

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
    id = serializers.IntegerField()
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

    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'gender', 'description', 'imgSrc', 'prescription_pills']

    def to_representation(self, instance):
        user_data = super().to_representation(instance)
        user_data['full_name'] = f"{user_data['first_name']} {user_data['last_name']}"
        user_data.pop('first_name')
        user_data.pop('last_name')
        return user_data

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
