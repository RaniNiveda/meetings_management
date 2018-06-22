#from django.urls import include, path
#from django.conf.urls import patterns

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from  .views import UserListView,EmployeeView,SalaryView

router=DefaultRouter()
router.register('register_user',UserListView,base_name='register_user')
router.register('employee_details',EmployeeView,base_name='employee_details')
router.register('salary_details',SalaryView,base_name='salary_details')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token, name='token')
]