from json_api.models import User1,Activity_period1
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'populate data'

    def handle(self, *args, **kwargs):
       
        u1=User1(UserID='W012A3CDE',Real_name='Egon Spengler',tz='America/Los_Angeles')
        u1.save()
        u2=User1(UserID='W07QCRPA4',Real_name='Glinda Southgood',tz='Asia/Kolkata')
        u2.save()
        r1 = Activity_period1(user=u1,id=None,start_time="Feb 1 2020  1:33PM",end_time= "Feb 1 2020 1:54PM")
        r1.save()

        r2 = Activity_period1(user=u1,id=None ,start_time="Mar 1 2020  11:11AM",end_time= "Mar 1 2020 2:00PM")
        r2.save()

        r3 = Activity_period1(user=u1,id=None , start_time= "Mar 16 2020  5:33PM",end_time= "Mar 16 2020 8:02PM")
        r3.save()

        r4 = Activity_period1(user=u2,id=None,start_time="Feb 1 2020  1:33PM",end_time= "Feb 1 2020 1:54PM")
        r4.save()

        r5 = Activity_period1(user=u2,id=None ,start_time="Mar 1 2020  11:11AM",end_time= "Mar 1 2020 2:00PM")
        r5.save()

        r6 = Activity_period1(user=u2,id=None , start_time= "Mar 16 2020  5:33PM",end_time= "Mar 16 2020 8:02PM")
        r6.save()
        """
       User1.objects.all().delete()
       Activity_period1.objects.all().delete()
        
        """
