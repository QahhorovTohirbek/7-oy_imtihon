from django.urls import path, include
from . import views
from dashboard.views import log_in

app_name = 'main'

urlpatterns = [
    path('', log_in),
    path('api/', include('api.urls'))
]
