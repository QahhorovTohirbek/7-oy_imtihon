from django.db import models


class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.first_name
    


class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    enter_time = models.DateTimeField(null=True, blank=True)
    exit_time = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.staff.first_name


            
            

