from django.urls import path
from .views import ReminderCreateView, ReminderListView

urlpatterns = [
    path('reminders/', ReminderCreateView.as_view(), name='reminder-create'),
    path('reminders/all/', ReminderListView.as_view(), name='reminder-list'),
]

