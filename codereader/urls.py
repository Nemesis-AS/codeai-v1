from django.contrib import admin
from django.urls import path, include
from .views import generate_pdf1, profile_analysis, index, user_signin, get_docs

urlpatterns = [
    path('generate_pdf', generate_pdf1, name='generate_pdf1'),
    path('profile_analysis', profile_analysis, name='profile_analysis'),
    path('', index, name='index'),
    path('user_signin', user_signin, name='user_signin'),

    path("get-docs", get_docs)

    # path('result', result,name='result'),
    # path('profile_test', profile_test, name='profile_test')
]

