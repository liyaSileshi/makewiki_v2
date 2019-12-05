
from django.urls import path

from api.views import PageList, PageDetail

urlpatterns = [
    path('pages/', PageList.as_view(), name='page_list'),
    path('pages/<int:pk>', PageDetail.as_view(), name='page_detail')
]

