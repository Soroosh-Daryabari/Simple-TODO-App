from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Accounts(AbstractUser):
    account_id = models.SlugField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_("Account ID"),
    )
    about_user = models.TextField(null=True, blank=True, verbose_name=_("About user"))
    first_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name=_("First name"),
    )
    last_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name=_("Last name"),
    )
    email_active_code = models.CharField(
        max_length=100,
        verbose_name=_("Email activate code"),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.get_full_name()
