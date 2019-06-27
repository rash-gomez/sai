from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [

    path('<name>/profile/', views.UserProfile.as_view(), name='profile'),
    path('profile/update/', views.profile, name='profile_update'),

    # path('base/', views.BaseIndexView.as_view(), name='base_dashbaord'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<name>/profile/', views.UserProfile.as_view(), name='profile'),
    # path('profile/update/', views.profile, name='profile_update'),

    # pharmacy create
    # path('pharmacy_create/', views.PharmacyRegister.as_view(), name='pharmacy_create'),

    # list of pharmacy users in my pharmacy
    path('users/list/', views.UserList.as_view(), name='user_list'),
    path('is_school_staff/', views.staff_add, name='staff_add'),
]
