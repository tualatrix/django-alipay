# -*- coding:utf-8 -*-

import urllib
import urllib2

from django import forms

from alipay import conf
from alipay.widgets import ValueHiddenInput
from alipay.forms import AlipaySignableForm
from alipay.helpers import make_sign, get_form_data, urldecode

class AlipaySendGoodsForm(AlipaySignableForm):
    """
    Alipay Send Goods confirm by platform
    """
    service = forms.CharField(widget=ValueHiddenInput(), initial=conf.SERVICE[2])

    trade_no = forms.CharField(widget=ValueHiddenInput(), max_length=64)
        # 担保交易 物流
    logistics_name = forms.CharField(widget=ValueHiddenInput(), max_length=64)
    invoice_no = forms.CharField(widget=ValueHiddenInput(), max_length=32)
    transport_type = forms.CharField(widget=ValueHiddenInput(), max_length=32)
    create_transport_type = forms.CharField(widget=ValueHiddenInput(), max_length=32)
    seller_ip = forms.CharField(widget=ValueHiddenInput(), max_length=15)

    def submit(self):
        response = urllib2.urlopen(self.get_action(), urllib.urlencode(get_form_data(self)))
        return response.read()
