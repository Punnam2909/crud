from django.db import models

# Create your models here.


class Surname(models.Model):
    family_name=models.CharField(default=None,max_length=120)
    class Meta:
        verbose_name = "Surname"
        verbose_name_plural = "Surnames"

    def __str__(self):
        return self.family_name

class Member(models.Model):
    initial=models.ForeignKey(Surname,on_delete=models.CASCADE,related_name="Surnames")
    persons_name=models.CharField(max_length=120)
    persons_dob=models.DateField()
    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __str__(self):
        return self.persons_name
