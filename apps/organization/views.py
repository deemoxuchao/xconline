# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg, CityDict


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        """

        :type request: object
        """
        #课程机构
        all_orgs = CourseOrg.objects.all()
        #课程数量
        org_nums = all_orgs.count()
        #城市
        all_cities = CityDict.objects.all()

        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        #5---代表一页显示5个
        p = Paginator(all_orgs, 5, request=request)

        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs":orgs,
            "all_cities":all_cities,
            "org_nums": org_nums,
        })