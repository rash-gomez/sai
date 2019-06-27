from django.urls import path
from apply import views

app_name = 'apply'

urlpatterns = [
    # path('', views.student_application, name='create'),
    path('new/', views.StudentNewApplication.as_view(), name="application_new"),
    path('old/', views.StudentOldApplication.as_view(), name="application_old"),
    path('list/', views.ApplicationList.as_view(), name="list_application"),
    path('details/<pk>/', views.ApplicationDetails.as_view(),
         name="detail_application"),
    path('update/<pk>/', views.ApplicationEdit.as_view(), name="edit_application"),
    path('delete/<pk>/', views.ApplicationDelete.as_view(),
         name="delete_application"),

    path('print/', views.GeneratePdf.as_view(), name="print_applicants"),
]
