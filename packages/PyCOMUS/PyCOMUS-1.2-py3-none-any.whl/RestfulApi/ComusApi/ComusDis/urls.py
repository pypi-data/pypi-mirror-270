from django.urls import path
from . import views
from .views import ComusModelView, ComusCtrlParsView,ComusOutParsView

urlpatterns = [
    path('createModel/', ComusModelView.as_view(), name='create_directory'),
    path('comusCtrlPars/', ComusCtrlParsView.as_view(), name='comus_ctrl_pars'),
    path('comusOutPars/', ComusOutParsView.as_view(), name='comus_output_pars'),
]
