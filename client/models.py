from django.db import models


class token(models.Model):
    token = models.CharField(max_length=50)

    def __str__(self):
        return str(self.token)


class user(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))

    # VERIFIED = 'verified'
    # UNVERIFIED = 'unverified'
    # INPROGRESS = 'inprogress'
    # PROFILE_STATUS_CHOICES = ((VERIFIED,'verified'),(UNVERIFIED,'unverified'),(INPROGRESS,'InProgress'))

    phone_number = models.CharField(max_length=13)
    last_name = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default=MALE)
    # profile_status = models.CharField(max_length=20,choices=PROFILE_STATUS_CHOICES,default=UNVERIFIED)
    token = models.OneToOneField(token, models.CASCADE, unique=True)
    orders_made_count = models.PositiveIntegerField(default=0)
    user_rating = models.FloatField(default=0.0)
    push_id = models.CharField(max_length=20, blank=True)
    account_balance = models.DecimalField(
        max_digits=10, blank=True, null=True, decimal_places=2)
    profile_photo = models.ImageField(
        upload_to='profile_photos_client/', blank=True, null=True)
    # id_card_photo = models.ImageField(upload_to='id_card_photos_client/',blank=True , null =True)
    id_number = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return str(self.phone_number)


class clientComments(models.Model):
    comment = models.CharField(max_length=300, blank=True)
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    to = models.ForeignKey('provider.provider', on_delete=models.CASCADE)


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
    price = models.DecimalField(decimal_places=3, max_digits=10)
    image = models.ImageField(
        verbose_name='item_image', upload_to='subCategoryService_images/en/', blank=True)

    # image_arabic = models.ImageField(verbose_name='item_image_arabic',upload_to='subCategoryService_images/ar/',blank=True)

    def __str__(self):
        return self.title


class service(models.Model):
    title_preview = models.CharField(max_length=30)
    title_preview_arabic = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    title_arabic = models.CharField(max_length=30)
    description = models.TextField(max_length=2500, blank=True)
    description_arabic = models.TextField(max_length=2500, blank=True)
    image = models.ImageField(verbose_name='item_image', upload_to='service_images/en/',
                              help_text='this is the image for service to be viewed on order page', blank=True)
    image_arabic = models.ImageField(verbose_name='item_image_arabic', upload_to='service_images/ar/',
                                     help_text='this is the image for service to be viewed on order page', blank=True)
    minimum_cost = models.DecimalField(
        max_digits=10, blank=True, null=True, decimal_places=2)
    category = models.ForeignKey(subServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_preview


class service_tip_text(models.Model):
    tip = models.TextField(max_length=200, blank=True)
    tip_arabic = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return '{}'.format(self.tip)


class service_tip(models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    tip = models.ForeignKey(service_tip_text, on_delete=models.CASCADE)

    def __str__(self):
        return '{},{}'.format(self.service, self.tip)


class warninig_text(models.Model):
    text = models.TextField(max_length=300,
                            help_text='this is warning text for specific service, enter just single warning')

    def __str__(self):
        return '{}'.format(self.text)


class warninig(models.Model):
    service = models.ForeignKey(
        service, on_delete=models.CASCADE, help_text='associated service for this warning')
    warninig = models.ForeignKey(warninig_text, on_delete=models.CASCADE)

    def __str__(self):
        return '{} , {}'.format(self.warninig, self.service)


class availableService(models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE,
                                help_text='associeted service ')
    description = models.CharField(
        max_length=30, help_text='description for associeted service')


class serviceList(models.Model):
    title = models.CharField(max_length=40)
    service = models.ForeignKey(
        service, on_delete=models.CASCADE, related_name='services')
    cost = models.DecimalField(
        max_digits=10, blank=True, null=True, decimal_places=2)

    def __str__(self):
        return self.title


class order(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    COMPANY = 'C'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'), (COMPANY, 'Company'))
    COMPLETED = 'CM'
    UNCERTAIN = 'UN'
    SUSPENDED = 'SUS'
    INPROGRESS = 'IP'
    ONLINE = 'O'
    INPLACE = 'INP'
    SERVICE_PAMENT_METHOD_CHOICES = (
        (ONLINE, 'Online'), (INPLACE, 'inPlace'))
    SERVICE_STATUS_CHOICES = (
        (COMPLETED, 'Completed'), (UNCERTAIN, 'Uncertain'), (SUSPENDED, 'Suspended'), (INPROGRESS, 'InProgress'))
    service = models.TextField(max_length=1200)
    dateTime = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default=MALE)
    orderNumber = models.CharField(max_length=12, unique=True)
    location_coordinates_or_address = models.TextField(max_length=1000)
    client = models.ForeignKey(user, on_delete=models.CASCADE)
    serviceProvider = models.ForeignKey(
        'provider.provider', on_delete=models.CASCADE, blank=True, null=True)
    service_status = models.CharField(
        max_length=3, choices=SERVICE_STATUS_CHOICES, default=UNCERTAIN)
    cost = models.DecimalField(
        max_digits=10, blank=True, null=True, decimal_places=2)
    paymentMethod = models.CharField(
        max_length=3, choices=SERVICE_PAMENT_METHOD_CHOICES, default=ONLINE)

    def __str__(self):
        return self.service


class orderTag(models.Model):
    tag_name = models.ForeignKey('provider.skillTag', on_delete=models.CASCADE)
    order = models.ForeignKey(order, on_delete=models.CASCADE)


class ordered_service(models.Model):
    service = models.ForeignKey(serviceList, on_delete=models.CASCADE)
    _order = models.ForeignKey(order, on_delete=models.CASCADE)


# class bidd(models.Model):
#     owner = models.ForeignKey('serviceProvider.provider',on_delete=models.CASCADE)
#     order = models.ForeignKey(order,on_delete=models.CASCADE)
#     bidd_content = models.TextField(max_length=300)

class comments(models.Model):
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)


class address(models.Model):
    address = models.TextField(max_length=10000)
    owner = models.ForeignKey(user, on_delete=models.CASCADE)


class serviceDate(models.Model):
    _date = models.DateField()

    def __str__(self):
        return '{}'.format(self._date)


class serviceTime(models.Model):
    _time = models.TimeField()

    def __str__(self):
        return '{}'.format(self._time)


class availableDateTimeService(models.Model):
    service = models.ForeignKey(serviceCategory, on_delete=models.CASCADE)
    time = models.ForeignKey(serviceTime, on_delete=models.CASCADE)
    date = models.ForeignKey(serviceDate, on_delete=models.CASCADE)
