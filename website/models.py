from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50)
    KRA_PIN = models.CharField(max_length=50)
    Account_Number = models.DecimalField(max_digits=20, unique=True, decimal_places=0)
    Phone_Number = models.CharField(max_length=10, unique=True, validators=[RegexValidator(
                                                                                           regex=r"^0\d{9}$", 
                                                                                           message='Phone number should have 10 digits and start with 0 e.g. 0xxxxxxxxx', 
                                                                                           code='invalid_phone_number'
                                                                                        )], )

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")

        # return(f"{self.first_name} {self.last_name} {self.KRA_PIN} {self.Acount_Number}")
    


    

