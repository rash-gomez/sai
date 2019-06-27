from django.urls import path
from search import views


app_name = 'search'

urlpatterns = [
    # path('', views.DrugSearchListView.as_view(), name="list"),
    path('staff_list', views.StaffSearchListView.as_view(),
         name="staff_list"),
]
