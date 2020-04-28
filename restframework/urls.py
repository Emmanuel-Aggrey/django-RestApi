from django.urls import  path,include
from  rest_framework import routers
from .import views
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register('',views.UsersViewset)


urlpatterns = [
    path('users/',include(router.urls)),
    path('listusers/',views.ListUsersApi.as_view()),
    path('listuser/',views.NewListUsersApi.as_view()),
    path('post/',views.PostApiview.as_view()),
    path('update/<int:pk>/',views.UpdateApiView.as_view()),
    path('delate/<int:pk>/',views.DelateApiView.as_view()),

    # rest view
    path('get_auth_token/', obtain_auth_token, name='get_auth_token'),

    # django_rest_auth
    # path('rest-auth/', include('rest_auth.urls'))


    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('rest-auth/', include('rest_auth.urls')),


    # github
    path('rest-auth/github/',views.GithubLogin.as_view(), name='github_login')




]