# -*- coding:utf-8 -*-

from django import forms

from alipay import conf
from alipay.widgets import ValueHiddenInput
from alipay.forms import AlipaySignableForm


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
