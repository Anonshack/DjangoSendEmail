from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home')
]

# myset = {1, 2, 3, 4, 5, 6}
# myset.discard(2)
# print(myset)