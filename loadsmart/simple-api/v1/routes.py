# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.healthcheck import Healthcheck
from .api.elb_elbName import ElbElbname


routes = [
    dict(resource=Healthcheck, urls=['/healthcheck'], endpoint='healthcheck'),
    dict(resource=ElbElbname, urls=['/elb/<elbName>'], endpoint='elb_elbName'),
]