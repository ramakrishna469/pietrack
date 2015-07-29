from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.conf import settings
from django.template import loader
from django.template.context import Context
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from django.utils import timezone
from django.core import validators
from .helper import Memail


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    email_verified = models.BooleanField(default=False)
    mobile = models.BigIntegerField(default='0', blank=True)
    api_auth_key = models.CharField(max_length=100, default='')
    api_secret_key = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='', blank=True)
    state = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    pincode = models.IntegerField(default='0', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def send_reset_pwd_mail(self):
        uidb64 = urlsafe_base64_encode(str(self.pk))
        token = default_token_generator.make_token(self)

        t = loader.get_template('emails/resetpwd_email.html')
        c = Context({'uidb64': uidb64, 'token': token})
        rendered = t.render(c)
        Memail(settings.DEFAULT_FROM_EMAIL, "Reset your password", rendered, self.email)

    def send_activate_mail(self):

        uidb64 = urlsafe_base64_encode(str(self.pk))
        token = default_token_generator.make_token(self)

        t = loader.get_template('emails/activate_email.html')
        c = Context({'uidb64': uidb64, 'token': token})
        subject = "Activate your account"
        rendered = t.render(c)
        Memail(settings.DEFAULT_FROM_EMAIL, subject, rendered, self.email)