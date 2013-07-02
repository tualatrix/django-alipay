# -*- coding: utf-8 -*-

from django.contrib import admin
from alipay.trade_create_by_buyer.ptn.models import AlipayPTN

class AlipayPTNAdmin(admin.ModelAdmin):
    date_hierarchy = 'gmt_payment'
    list_display = [
        "out_trade_no", "flag", "flag_info", "trade_no", "trade_status", "created_at"
    ]
    search_fields = ["out_trade_no", "trade_no"]


admin.site.register(AlipayPTN, AlipayPTNAdmin)
