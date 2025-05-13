from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

# POST - Create a new reminder
class ReminderCreateView(generics.CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

# GET - List all reminders
class ReminderListView(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

