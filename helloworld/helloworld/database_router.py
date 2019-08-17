# -*- coding: utf-8 -*-
from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING

class CustomError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo


class MyDatabaseAppsRouter(object):
    """
    # https://code.ziqiangxuetang.com/django/django-multi-database.html
    # https://docs.djangoproject.com/en/2.2/topics/db/multi-db/

    A router to control all database operations on models for different
    databases.
 
    In case an app is not set in settings.DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.
 
    Settings example:
 
    DATABASE_APPS_MAPPING = {'app1': 'db1', 'app2': 'db2'}
    """

    def db_for_read(self, model, **hints):
        """Point all read operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    # Django 1.7 - Django 1.11
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # print("db: {}, app_label: {}, model_name: {}, hints: {}".format(db, app_label, model_name, hints))
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(app_label) == db
        elif app_label in DATABASE_MAPPING:
            return False 
        # raise CustomError('db {} router allow_migrate function return False'.format(db))
        return None

    # # 2.2.2官方文档中没有写函数的示例。
    # # 没有搞懂这个是怎么用的，先放着。
    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     """
    #     All non-auth models end up in this pool.
    #     """
    #     return True

