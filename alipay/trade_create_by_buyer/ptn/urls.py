
from django.conf.urls.defaults import *

urlpatterns = patterns('alipay.trade_create_by_buyer.ptn.views',
    url(r'^$', 'ptn', {'item_check_callable':None}, name='alipay-ptn'),
)

