# _*_ encoding:utf-8 _*_
__author__ = 'hsurich'
__date__ = '2018/12/3 21:52'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, PageBanner

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlabalSetting(object):
    site_title = "徐超慕学网后台管理系统"
    site_footer = "诺娃网络科技有限公司"
    menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email','send_type','send_time']
    search_fields = ['code', 'email','send_type']
    list_filter = ['code', 'email','send_type','send_time']

class PageBannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(PageBanner, PageBannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlabalSetting)



