from django.db import models


class token(models.Model):
    token = models.CharField(max_length=50)

    def __str__(self):
        return str(self.token)


class user(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))
    phone_number = models.CharField(max_length=13)
    last_name = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default=MALE)
    token = models.OneToOneField(token, models.CASCADE, unique=True)
    orders_made_count = models.PositiveIntegerField(default=0)
    user_rating = models.FloatField(default=0.0)
    push_id = models.CharField(max_length=20, blank=True)
    account_balance = models.DecimalField(
        max_digits=10, blank=True, null=True, decimal_places=2)
    profile_photo = models.ImageField(
        upload_to='profile_photos_client/', blank=True, null=True)
    id_number = models.CharField(max_length=11, blank=True)

    def __str__(self):
        
        return str(self.phone_number)


class bannerSlider(models.Model):
    name = models.CharField(max_length=30, blank=True)
    # name_arabic = models.CharField(max_length=30,blank=True)
    # description = models.CharField(max_length=500,blank=True)
    # description_arabic = models.CharField(max_length=500)
    phone = models.CharField(max_length=12, blank=True)
    location = models.CharField(max_length=30, blank=True)
    webURL = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='slider_images/en/', blank=True)

    # image_arabic = models.ImageField(upload_to='slider_images/ar/',blank=True)

    def __str__(self):
        return self.name


# TODO : remove blank=True for title_arabic
class serviceCategory(models.Model):
    title = models.CharField(max_length=200)
    title_arabic = models.CharField(max_length=200, blank=True)
    image = models.FileField(verbose_name='cat_Image',
                             upload_to='categoryService_images/', blank=True)
    image_selected = models.FileField(verbose_name='cat_Image_selected', upload_to='categoryService_images/',
                                      blank=True)

    def __str__(self):
        return self.title


class subServiceCategory(models.Model):
    category = models.ForeignKey(
        serviceCategory, models.CASCADE, related_name='service')
    title = models.CharField(max_length=30)
    title_arabic = models.CharField(max_length=30)
    image = models.ImageField(
        verbose_name='item_image', upload_to='subCategoryService_images/en/', blank=True)

    def __str__(self):
        return self.title


class serviceDate(models.Model):
    _date = models.DateField()

    def __str__(self):
        return '{}'.format(self._date)


class serviceTime(models.Model):
    _time = models.TimeField()

    def __str__(self):
        return '{}'.format(self._time)


class availableDateTimeService(models.Model):
    time = models.ForeignKey(serviceTime, on_delete=models.CASCADE)
    date = models.ForeignKey(serviceDate, on_delete=models.CASCADE)

    def __str__(self):
        return '{},{}'.format(self.date, self.time)


class order(models.Model):

    COMPLETED = 'CM'
    SUSPENDED = 'SUS'
    INPROGRESS = 'IP'
    SERVICE_STATUS_CHOICES = (
        (COMPLETED, 'Completed'), (SUSPENDED, 'Suspended'), (INPROGRESS, 'InProgress'))
    services = models.TextField(max_length=10000, default='')
    dateTime = models.CharField(max_length=40)
    orderNumber = models.CharField(max_length=20, unique=True)
    location = models.TextField(max_length=1000)
    client = models.ForeignKey(user, on_delete=models.CASCADE)
    provider = models.ForeignKey(
        'provider.provider', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3, choices=SERVICE_STATUS_CHOICES, default=INPROGRESS)
    total_cost = models.CharField(max_length=30)
    description = models.TextField(max_length=270,blank=True)
    qrCode = models.ImageField(upload_to='orders/qrcodes/', default='')

    # def __str__(self):
    # return '{}'.format(self.services)


class address(models.Model):
    address = models.TextField(max_length=1000)
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
