from django.db import models


class Motor(models.Model):
    script = models.SlugField(default='/somepath')
    dscript = models.SlugField(default='/somepath')


class Pills(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    warning = models.TextField(null=True)
    company = models.CharField(max_length=255)
    inventory = models.IntegerField()
    imageSrc = models.SlugField(null=True, default='./pills/Acetaminophen.jpeg')
    weight = models.CharField(max_length=255, null=True)
    perscription = models.BooleanField(default=False)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, null=True)



class UserPerscriptionPill(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    per_pill = models.ForeignKey(Pills, on_delete=models.CASCADE)

    class Meta:
        db_table = 'medb_user_prescription_pill'
        unique_together = (('user', 'per_pill'),)


class Days(models.Model):
    day = models.CharField(max_length=255)


class Alarm(models.Model):
    quantity = models.IntegerField(default=1)
    soundSrc = models.SlugField(default='/Users/Desktop/Alarm.wav')
    time = models.TimeField(default='-')
    day = models.ForeignKey(Days, on_delete=models.PROTECT, default='-')
    user_prescription_pill = models.ForeignKey(UserPerscriptionPill, on_delete=models.CASCADE, default='-')


class Taken(models.Model):
    taken = models.BooleanField()
    taken_date = models.DateField(auto_now_add=True)
    alarm = models.ForeignKey(Alarm, on_delete=models.CASCADE, default='-')


class Users(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default='-')
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE, null=True)
    description = models.TextField(null=True)
    birth_date = models.DateField()
    imgSrc = models.SlugField(null=True)
    prescription_pills = models.ManyToManyField(Pills, through=UserPerscriptionPill, null=True)


class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    pill = models.ForeignKey(Pills, on_delete=models.PROTECT)
    commentText = models.TextField()

