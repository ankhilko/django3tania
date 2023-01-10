from django.urls import path
from registration.views import SignInView, ProfileView, LogoutView, RegisterCreateView

from .views import SubjectListView, IndexTemplateView, StudentListView, TeacherListView, PersonListView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path('students/', StudentListView.as_view(), name='students'),
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('userprofile/', PersonListView.as_view(), name='userprofile'),
    path('registration/signin/', SignInView.as_view(), name='signin'),
    path('registration/signup/', RegisterCreateView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
