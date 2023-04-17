from .models import Alarm, Taken
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
import os
from django.conf import settings

if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')
    settings.configure()



from django.test import Client, TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404

class TakeMedicationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.alarm = Alarm.objects.create(
            quantity=2,
            soundSrc='sound.mp3',
            time='12:00:00',


        )

    def test_take_medication_success(self):
        url = reverse('take_medication', args=[self.alarm.id])
        data = {'taken': 'true'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': True})
        taken = get_object_or_404(Taken, alarm=self.alarm)
        self.assertTrue(taken.taken)

    def test_take_medication_failure(self):
        url = reverse('take_medication', args=[self.alarm.id])
        data = {'taken': 'false'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': True})
        taken = get_object_or_404(Taken, alarm=self.alarm)
        self.assertFalse(taken.taken)
