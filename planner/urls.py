from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('planner/<int:planner_id>/',views.detail,name='detail'),
    path('planner/new/',views.planner_new,name='new'),
    path('planner/<int:planner_id>/edit/',views.planner_edit,name='edit'),
    path('planner/<int:planner_id>/delete/',views.planner_delete,name='delete'),
]
