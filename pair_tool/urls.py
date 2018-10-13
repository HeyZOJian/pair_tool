from django.urls import path

from app.views import assign_pair_randomly, user_view
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pair_tool/', assign_pair_randomly),
    path('pair_tool/users/', user_view)

]