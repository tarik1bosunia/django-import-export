from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    monthly_salary = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
