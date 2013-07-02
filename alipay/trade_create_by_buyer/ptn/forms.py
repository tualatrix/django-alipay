# -*- coding:utf-8 -*-

from django import forms

from alipay.helpers import make_sign
from alipay.trade_create_by_buyer.ptn.models import AlipayPTN
from alipay.forms import AlipayBaseForm

class AlipayPTNForm(AlipayBaseForm):
    """
    Alipay Partner Trade Notify Form
    """
    class Meta:
        model = AlipayPTN


