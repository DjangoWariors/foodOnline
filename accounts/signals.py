from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

from .models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('create the user profile')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            #create profile if not exist
            UserProfile.objects.create(user=instance)
        print('create the user profile IF not exist')

@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs): 
    print(instance.username,'this user is being saved')


#post_save.connect(post_save_create_profile, sender=User)
