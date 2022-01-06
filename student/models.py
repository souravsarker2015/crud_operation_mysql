from django.db import models


class User(models.Model):
    uname = models.CharField(max_length=200)
    uemail = models.EmailField(max_length=200)
    ufname = models.CharField(max_length=200)
    ulname = models.CharField(max_length=200)
    upassword = models.CharField(max_length=200)

    class Meta:
        db_table = "users"
