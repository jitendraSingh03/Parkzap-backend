from rest_framework import serializers
from account.models import contact_info

class contact_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = contact_info
        fields = ["contact_id","contact_fname","contact_lname","contact_dob","contact_phone","contact_email"]
    def validate_contact_phone(self, attrs):
        contacts=None
        try:
            contacts=contact_info.objects.get(contact_phone=attrs)
        except:
            pass
        
        print(contacts)
        if contacts:
            raise serializers.ValidationError('all ready exits')
        return attrs