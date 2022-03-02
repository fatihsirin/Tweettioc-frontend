from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)
#router.register(r'api/tweets', views.TweetsViewSet_day)
router.register(r'api/tweets/day', views.TweetsViewSet_day)
router.register(r'api/tweets/week', views.TweetsViewSet_week)





# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path(r'api/tweets/<str:user_id>/', views.TodoListApiView.as_view()),
]