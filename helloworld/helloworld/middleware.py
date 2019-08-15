# ~*~ coding: utf-8 ~*~

import os
import re
# import pytz
from django.shortcuts import HttpResponse
# from django.conf import settings
# from django.utils import timezone
# 
# from .utils import set_current_request

class DemoMiddleware:
    DEMO_MODE_ENABLED = os.environ.get("DEMO_MODE", "") in ("1", "ok", "True")
    SAFE_URL_PATTERN = re.compile(
        r'^/users/login|'
        r'^/api/terminal/v1/.*|'
        r'^/api/terminal/.*|'
        r'^/api/users/v1/auth/|'
        r'^/api/users/v1/profile/'
    )
    SAFE_METHOD = ("GET", "HEAD")

    def __init__(self, get_response):
        self.get_response = get_response

        if self.DEMO_MODE_ENABLED:
            print("Demo mode enabled, reject unsafe method and url")

    def __call__(self, request):
        if self.DEMO_MODE_ENABLED and request.method not in self.SAFE_METHOD \
                and not self.SAFE_URL_PATTERN.match(request.path):
            return HttpResponse("Demo mode, only safe request accepted", status=403)
        else:
            response = self.get_response(request)
            return response

    # # 改成下面这种的话,那么就会什么页面都访问不了了。
    # def __call__(self, request):
    #     return HttpResponse("Demo mode, only safe request accepted", status=403)
