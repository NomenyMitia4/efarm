from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, default="Jean Pierre")
    contact = models.CharField(max_length=20, default="123456789")
    email = models.EmailField(max_length=100, default="email@gmail.com")
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=128, default="0000")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        # Hash password only if it hasn't already been hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name