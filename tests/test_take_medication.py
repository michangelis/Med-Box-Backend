from django.test import Client, TestCase
from django.urls import reverse
from medb.models import Alarm, Taken


class TakeMedicationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.alarm = Alarm.objects.create(
            pill_name="Acetaminophen",
            alarm_time="13:00:00",
            full_name="John Smith",

        )

    def test_take_medication(self):
        url = reverse('take_medication', args=[self.alarm.id])
        response = self.client.post(url, {'taken': 'true'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Taken.objects.count(), 1)
        taken = Taken.objects.first()
        self.assertEqual(taken.taken, True)
        self.assertEqual(taken.alarm, self.alarm)
