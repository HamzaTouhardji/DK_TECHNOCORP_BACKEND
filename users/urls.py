from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, Users

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('<int:pk>', Users.as_view(), name="user"),
    path('logout/blacklist', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
