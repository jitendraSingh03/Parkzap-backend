from django.db import models

class contact_info(models.Model):
    contact_id=models.AutoField(primary_key=True)
    contact_fname=models.CharField(max_length=20)
    contact_lname=models.CharField(max_length=20)
    contact_dob=models.CharField(max_length=20,default="")
    contact_phone=models.CharField(max_length=15)
    contact_email=models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.contact_fname}---{self.contact_id}"