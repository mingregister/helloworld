import uuid 

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import ugettext_lazy as _


# Create your models here.

class RoleMixin:
    ROLE_ADMIN = 'Admin'
    ROLE_USER = 'User'
    ROLE_APP = 'App'
    ROLE_AUDITOR = 'Auditor'

    ROLE_CHOICES = (
        (ROLE_ADMIN, _('Administrator')),
        (ROLE_USER, _('User')),
        (ROLE_APP, _('Application')),
        (ROLE_AUDITOR, _("Auditor"))
    )
    role = ROLE_USER

class User(RoleMixin, AbstractUser):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    username = models.CharField(
        max_length=128, unique=True, verbose_name=_('Username')
    )

    name = models.CharField(max_length=128, verbose_name=_('Name'))

    email = models.EmailField(
        max_length=128, unique=True, verbose_name=_('Email')
    )

    # groups = models.ManyToManyField(
    #     'users.UserGroup', related_name='users',
    #     blank=True, verbose_name=_('User group')
    # )

    role = models.CharField(
        choices=RoleMixin.ROLE_CHOICES, default='User', max_length=10,
        blank=True, verbose_name=_('Role')
    )

    avatar = models.ImageField(
        upload_to="avatar", null=True, verbose_name=_('Avatar')
    )

    wechat = models.CharField(
        max_length=128, blank=True, verbose_name=_('Wechat')
    )

    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_('Phone')
    )

    comment = models.TextField(
        blank=True, null=True, verbose_name=_('Comment')
    )

    is_first_login = models.BooleanField(default=True)

    # date_expired = models.DateTimeField(
    #     default=date_expired_default, blank=True, null=True,
    #     db_index=True, verbose_name=_('Date expired')
    # )

    created_by = models.CharField(
        max_length=30, default='', verbose_name=_('Created by')
    )

    date_password_last_updated = models.DateTimeField(
        auto_now_add=True, blank=True, null=True,
        verbose_name=_('Date password last updated')
    )

    user_cache_key_prefix = '_User_{}'

    def __str__(self):
        return '{0.name}({0.username})'.format(self)

    def get_absolute_url(self):
        return reverse('users:user-detail', args=(self.id,))

    @property
    def groups_display(self):
        return ' '.join([group.name for group in self.groups.all()])

    @property
    def source_display(self):
        return self.get_source_display()

    @property
    def is_expired(self):
        if self.date_expired and self.date_expired < timezone.now():
            return True
        else:
            return False

    @property
    def expired_remain_days(self):
        date_remain = self.date_expired - timezone.now()
        return date_remain.days

    @property
    def will_expired(self):
        if 0 <= self.expired_remain_days < 5:
            return True
        else:
            return False

    @property
    def is_valid(self):
        if self.is_active and not self.is_expired:
            return True
        return False

    @property
    def is_local(self):
        return self.source == self.SOURCE_LOCAL

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.username
        if self.username == 'admin':
            self.role = 'Admin'
            self.is_active = True
        super().save(*args, **kwargs)

    def is_member_of(self, user_group):
        if user_group in self.groups.all():
            return True
        return False

    def avatar_url(self):
        admin_default = settings.STATIC_URL + "img/avatar/admin.png"
        user_default = settings.STATIC_URL + "img/avatar/user.png"
        if self.avatar:
            return self.avatar.url
        if self.is_superuser:
            return admin_default
        else:
            return user_default

    def delete(self, using=None, keep_parents=False):
        if self.pk == 1 or self.username == 'admin':
            return
        return super(User, self).delete()

    class Meta:
        ordering = ['username']
        verbose_name = _("User")
