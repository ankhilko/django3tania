from django.urls import path
from .views import SubjectListView, IndexTemplateView, StudentListView, TeacherListView, PersonListView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path('students/', StudentListView.as_view(), name='students'),
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('userprofile/', PersonListView.as_view(), name='userprofile'),

]
