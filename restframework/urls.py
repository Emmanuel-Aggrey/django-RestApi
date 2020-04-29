from django.urls import path, include
from rest_framework import routers
from .import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # all objects
    path('persons/',views.PersonApi.as_view()),

    # action on http: [POST,PUT,DELETE]
    path('person/<int:pk>/',views.PersonApi.as_view()),
    
    # get user token
    path('get_auth_token/', obtain_auth_token, name='get_auth_token'),

    # registration and confirmation
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # basic authentications
    path('rest-auth/', include('rest_auth.urls')),

    # github
    path('rest-auth/github/', views.GithubLogin.as_view(), name='github_login'),

]
