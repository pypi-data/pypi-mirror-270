import uuid
from django.db import models


class ComusDisModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'comus_model'


class ComusCtrlParsModel(models.Model):
    comus_dis_uuid = models.UUIDField(unique=True)
    num_layer = models.IntegerField(default=1)
    num_row = models.IntegerField(default=1)
    num_col = models.IntegerField(default=1)
    dim_unit = models.CharField(max_length=10, default="m")
    time_unit = models.CharField(max_length=10, default="day")
    x_coord = models.FloatField(default=0)
    y_coord = models.FloatField(default=0)
    sim_mtd = models.IntegerField(default=1)
    sim_type = models.IntegerField(default=2)
    acc_lambda = models.FloatField(default=-1)
    intblkm = models.IntegerField(default=1)
    solve = models.IntegerField(default=2)
    max_iter = models.IntegerField(default=200)
    damp = models.FloatField(default=1)
    h_close = models.FloatField(default=0.0001)
    r_close = models.FloatField(default=0.001)
    relax = models.IntegerField(default=0)
    theta = models.FloatField(default=0.7)
    gamma = models.FloatField(default=3)
    akappa = models.FloatField(default=0.001)
    n_iter = models.IntegerField(default=5)
    hno_flo = models.FloatField(default=-1E+30)
    ch_flg = models.IntegerField(default=0)
    wd_flg = models.IntegerField(default=0)
    wet_fct = models.FloatField(default=0.1)
    newt_iter = models.IntegerField(default=1)
    hd_wet = models.IntegerField(default=1)
    reg_sta = models.IntegerField(default=0)
    mul_td = models.IntegerField(default=0)
    num_td = models.IntegerField(default=-1)

    class Meta:
        db_table = 'comus_ctrl_pars'

class ComusOutParsModel(models.Model):
    comus_dis_uuid = models.UUIDField(unique=True)
    gdw_bd = models.IntegerField(default=1)
    lyr_bd = models.IntegerField(default=1)
    cell_bd = models.IntegerField(default=1)
    cell_hh = models.IntegerField(default=1)
    cell_dd = models.IntegerField(default=1)
    cell_flo = models.IntegerField(default=1)
    lak_bd = models.IntegerField(default=1)
    segm_bd = models.IntegerField(default=1)
    rech_bd = models.IntegerField(default=1)
    ibs = models.IntegerField(default=1)
    sub = models.IntegerField(default=1)
    ndb = models.IntegerField(default=1)
    db = models.IntegerField(default=1)
    reg_bd = models.IntegerField(default=1)

    class Meta:
        db_table = 'comus_out_pars'
