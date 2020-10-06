from django.urls import path
from functional_App import views


urlpatterns=[
        path('', views.BookDetaiView.as_view(),name="user_book")
]