from django.db import models
# Create your models here.

# class provider(models.Model):
#     MALE = 'M'
#     FEMALE = 'F'
#     COMPANY = 'C'
#     GENDER_CHOICES = ((MALE,'Male'),(FEMALE,'Female'),(COMPANY,'company'))
#     phone_number = models.CharField(max_length=13)
#     first_name = models.CharField(max_length=20,blank=True)
#     last_name = models.CharField(max_length=20,blank=True)
#     gender = models.CharField(max_length=2,choices=GENDER_CHOICES,default=MALE)
#     #personel_id = models.OneToOneField(personel_id,models.CASCADE,unique=True)
#     services_done_count = models.PositiveIntegerField(blank=True,null=True)
#     provider_rating = models.FloatField(blank=True,null=True)
#     push_id = models.CharField(max_length=20,blank=True)
#     token = models.OneToOneField('client.token',models.CASCADE,unique=True,blank=True)
#     profile_description = models.CharField(max_length=300)
#     address = models.TextField(max_length=10000,help_text='json encoded',blank=True)
#     account_balance = models.DecimalField(max_digits=10 , blank=True,null =True,decimal_places=2)
#     profile_photo = models.ImageField(upload_to='profile_photos_provider/',blank=True , null =True)
#     is_activted = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.phone_number)


class provider(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    providing_category = models.ForeignKey(
        'client.serviceCategory', models.CASCADE,related_name='category')
    providing_services = models.ManyToManyField(
        'client.subServiceCategory')

    # def __str__(self):
        # return self.providing_services
# class providerComments(models.Model):
#     comment = models.CharField(max_length = 300 , blank=True)
#     owner = models.ForeignKey(provider,on_delete='')
#     to = models.ForeignKey('client.user',on_delete='')


# class skillTag(models.Model):
#     tag_name = models.CharField(max_length=10)
#     joined_skill = models.ForeignKey(
#         'client.subServiceCategory', on_delete=models.CASCADE)


# class skill(models.Model):
#     skill = models.ForeignKey(skillTag, on_delete=models.CASCADE)
#     provider = models.ForeignKey(provider, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.skill)
