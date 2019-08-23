# -*- coding:utf-8 -*- 


# from django.contrib.auth.models import User
from accounts.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    '''
    create random users
    '''

    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

        # Optional argument
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            random_string = get_random_string()
            random_email = '@'.join([random_string,'qq.com'])
            User.objects.create_user(username=get_random_string(), email=random_email, password='123')
