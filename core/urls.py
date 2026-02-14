# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from projects.views import ProjectViewSet

# router = DefaultRouter()
# router.register(r'projects', ProjectViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]


# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns += [
#     path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
# ]


# #this were it look like but we need to add the jwt token views
# # from django.contrib import admin



from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from projects.views import ProjectViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    # API Routes
    path('api/', include(router.urls)),

    # JWT Authentication Routes
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
