from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
# import cloudinary modules
from cloudinary.models import CloudinaryField


class Store(models.Model):
    name = models.CharField('name', max_length=100)
    address = models.CharField('Address', max_length=100, null=True, blank=True)
    tel = models.CharField('Phone number', max_length=100, null=True, blank=True)
    description = models.TextField('Description', default="", blank=True)
    # image = models.ImageField(upload_to='images', verbose_name='store image', null=True, blank=True)
    images = CloudinaryField('store_images', null=True, blank=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name='Staff', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, verbose_name='Store', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.store}：{self.user}'


class Booking(models.Model):
    staff = models.ForeignKey(Staff, verbose_name='Staff', on_delete=models.CASCADE)
    first_name = models.CharField('First name', max_length=100, null=True, blank=True)
    last_name = models.CharField('Last name', max_length=100, null=True, blank=True)
    tel = models.CharField('Phone number', max_length=100, null=True, blank=True)
    remarks = models.TextField('remarks', default="", blank=True)
    start = models.DateTimeField('Start time', default=timezone.now)
    end = models.DateTimeField('End time', default=timezone.now)

    def __str__(self):
        start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M')
        end = timezone.localtime(self.end).strftime('%Y/%m/%d %H:%M')
        return f'{self.first_name}{self.last_name} {start} ~ {end} {self.staff}'