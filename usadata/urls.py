from django.urls import path
from usadata.views import *

urlpatterns = [
    path('api/states', StateList.as_view(), name='state-list-create'),
    path('api/states/<int:pk>/', StateDetail.as_view(), name='state-update-delete' ),
    path('api/people', PeopleList.as_view(), name='people-list-create'),
    path('api/people/<int:pk>/', PeopleDetail.as_view(), name='people-update-delete' )
]