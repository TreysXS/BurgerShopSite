from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    """Model User profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, verbose_name='Информация о пользователе')
    img = models.ImageField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('user-profile', args=[str(self.id)])

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Creating a model profile when registering a user.
        """
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """
        Update model profile.
        """
        instance.profile.save()
