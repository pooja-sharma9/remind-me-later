from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder

        # Use '__all__' to automatically include all fields defined in the model.
        # This will serialize every field, including new ones such as 'created_at', 'updated_at'.
        # Caution: While convenient, this may expose sensitive fields (e.g., passwords) unintentionally.
        
        # fields = '__all__'

        # Only the following fields will be included in the model:
        # This approach gives you control over which fields are exposed to the client.
        # If you add more fields in your model (e.g., created_at, updated_at),
        # you'll need to manually add them here as well.
        # Good for API security
        fields = ['id', 'date', 'time', 'message', 'reminder_method']
