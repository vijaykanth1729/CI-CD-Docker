from django.urls import path
from .views import *
app_name = 'student_app'

# including only class based views...
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('create/', CreateStudentView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteStudentView.as_view(), name='delete'),
    path('send_mail/', sendEmail, name='send'),
]
