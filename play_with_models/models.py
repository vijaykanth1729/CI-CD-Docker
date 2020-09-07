from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_address = models.TextField(help_text="Provide address of a company")
    company_started = models.DateTimeField(auto_now_add=True, auto_now=False)
    company_ended = models.DateTimeField(null=True)
    company_profit = models.FloatField()


    def __str__(self):
        return self.company_name

class Employee(models.Model):
    GENDER_CHOICE  = (
        ('m' , 'Male'),
        ('f', 'Female'),
        ('t', 'Transgender')
    )
    employee_name = models.CharField(max_length=100, help_text="Provide employee Name")
    employee_id = models.IntegerField(primary_key=True)
    employee_gender = models.CharField(max_length=2, choices=GENDER_CHOICE)
    employee_salary = models.DecimalField(max_digits=10, decimal_places=2)
    employee_address = models.TextField(help_text='Please provide address', null=True)


    def __str__(self):
        return self.employee_name

class Department(models.Model):
    DEPARTMENTS = (
        ('cse', 'Computer science Engineering'),
        ('ece', 'Electronics and communication engineering'),
    )
    department_name = models.CharField(max_length=30, choices=DEPARTMENTS)

    def __str__(self):
        return self.department_name
