from django.views.generic import TemplateView
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

# github
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView

# from django.contrib.auth.models import  User
from .models import Person
from .serializers import UsersSerializer

# from decouple import config


# index view


class IndexView(TemplateView):
    template_name = 'index.html'


class Ipay_fail(TemplateView):
    template_name = 'ipay_fail.html'


class Ipay_success(TemplateView):
    template_name = 'ipay_succuess.html'


class PersonApi(generics.ListAPIView, generics.CreateAPIView,
                generics.RetrieveAPIView, generics.UpdateAPIView,
                generics.DestroyAPIView):

    serializer_class = UsersSerializer
    queryset = Person.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk=None):
        permission_classes = [IsAdminUser]
        if pk:
            # return the person
            return self.retrieve(request, pk)

        else:
            # all persons
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    # def relationship(self,relationship=None):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     # name ='sister'
    #     return Person.objects.filter(relationship=relationship)


# github
class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'CALLBACK_URL_YOU_SET_ON_GITHUB'
    client_class = OAuth2Client
