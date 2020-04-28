from rest_framework import  viewsets
from .serializers import usersSerializer
from rest_framework import  generics
from rest_framework import mixins
from  rest_framework.permissions import  IsAuthenticated,IsAdminUser
# from django.contrib.auth.models import  User
from  .models import Person

# github
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView

class UsersViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = usersSerializer
    permission_classes = [IsAuthenticated,]


class ListUsersApi(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class = usersSerializer
    queryset = Person.objects.all()
    
    def get(self,requst):
        return self.list(requst)
    
class NewListUsersApi(generics.ListAPIView):
    serializer_class = usersSerializer
    queryset = Person.objects.filter()
    permission_classes = [IsAuthenticated,]

    def get(self,requst):
      
        return self.list(requst)

class PostApiview(generics.CreateAPIView):
    # queryset = User.objects.filter(is_superuser=True)
    serializer_class =usersSerializer
    def post(self,requst):
        print(requst)
       
        return self.create(requst)

class UpdateApiView(generics.UpdateAPIView):
    serializer_class = usersSerializer
    def put(self,requst):
        return self.update(requst)


class DelateApiView(generics.DestroyAPIView):
    serializer_class = usersSerializer
    def post(self,requst):
        return self.delete(requst)  

    


# github
class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'CALLBACK_URL_YOU_SET_ON_GITHUB'
    client_class = OAuth2Client