from django.test import TestCase
import pytz
from datetime import datetime
if __name__ == '__main__':
    timezone = pytz.timezone('Europe/Athens')
    now = datetime.now(timezone)
    print(now)
