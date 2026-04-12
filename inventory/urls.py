from django.urls import path
from inventory import views

urlpatterns = [
    # Workstation
    path('workstations/', views.WorkStationList.as_view(), name='workstation-list'),
    path('workstations/<int:pk>/', views.WorkStationDetail.as_view(), name='workstation-detail'),
    path('workstations/create/', views.WorkStationCreate.as_view(), name='workstation-create'),
    path('workstations/<int:pk>/update/', views.WorkStationUpdate.as_view(), name='workstation-update'),
    path('workstations/<int:pk>/delete/', views.WorkStationDelete.as_view(), name='workstation-delete'),

    # supply
    path('supplies/', views.list_supplies, name='supplies-list'),
    path('supplies/create/', views.create_supply, name='supplies-create'),
    path('supplies/<slug:slug>/', views.supply_detail, name='supplies-detail'),
    path('supplies/<slug:slug>/update/', views.update_supply, name='supplies-update'),
    path('supplies/<slug:slug>/delete/', views.delete_supply, name='supplies-delete'),
]
