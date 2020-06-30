from django.urls import path
from .views import DailyListView,DailyDetailView,DailyCreateView,DailyUpdateView,DailyDeleteView,UserDailyListView
from . import views

urlpatterns = [
    path('', DailyListView.as_view(), name='myapp-home'),
    path('about/', views.about, name='myapp-about'),
    path('user/<str:username>', UserDailyListView.as_view(), name='user-dailys'),
    path('daily/<int:pk>/', DailyDetailView.as_view(), name='daily-detail'),
    path('daily/new/', DailyCreateView.as_view(), name='daily-create'),
    path('daily/<int:pk>/update/', DailyUpdateView.as_view(), name='daily-update'),
    path('daily/<int:pk>/delete/', DailyDeleteView.as_view(), name='daily-delete'),

]