from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('python', views.python_view, name='python'),
    path('git', views.git_view, name='git'),
    path('solidity', views.solidity_view, name='solidity'),
    path('js', views.js_view, name='js'),
    path('ruby', views.ruby_view, name='ruby'),
    path('rust', views.rust_view, name='rust'),
    path('linux', views.linux_view, name='linux'),
    path('nodejs', views.nodejs_view, name='nodejs'),
]