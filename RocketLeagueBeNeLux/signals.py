from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer


@receiver(post_save, sender=User)
def customer_profiele(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='klant')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
        )

#post_save.connect(customer_profiele, sender=User)

@receiver(post_save, sender=User)
def update_profiel(sender, instance, created, **kwargs):

    if created == False:
        instance.customer.save()
        print('profiel updated')