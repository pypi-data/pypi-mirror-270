from rest_framework import serializers

from .models import ComusDisModel, ComusCtrlParsModel, ComusOutParsModel


class ComusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComusDisModel
        fields = ['user_name', 'project_name']


class ComusCtrlParsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComusCtrlParsModel
        fields = '__all__'

    def validate(self, data):
        sim_mtd = data.get('sim_mtd', 1)
        sim_type = data.get('sim_type', 2)
        acc_lambda = data.get('acc_lambda', -1)
        intblkm = data.get('intblkm', 1)
        solve = data.get('solve', 2)
        max_iter = data.get('max_iter', 200)
        damp = data.get('damp', 1)
        h_close = data.get('h_close', 0.0001)
        r_close = data.get('r_close', 0.001)
        relax = data.get('relax', 0)
        theta = data.get('theta', 0.7)
        gamma = data.get('gamma', 3)
        akappa = data.get('akappa', 0.001)
        n_iter = data.get('n_iter', 5)
        ch_flg = data.get('ch_flg', 0)
        wd_flg = data.get('wd_flg', 0)
        wet_fct = data.get('wet_fct', 0.1)
        newt_iter = data.get('newt_iter', 1)
        hd_wet = data.get('hd_wet', 1)
        reg_sta = data.get('reg_sta', 0)
        mul_td = data.get('mul_td', 0)
        num_td = data.get('num_td', -1)

        if sim_mtd not in [1, 2]:
            raise serializers.ValidationError("The 'sim_mtd' parameter must be 1 or 2. Please check!")

        if sim_type not in [1, 2]:
            raise serializers.ValidationError("The 'sim_type' parameter must be 1 or 2. Please check!")

        if sim_mtd == 1 and sim_type == 1:
            if not (1E-4 <= acc_lambda <= 1E-3) and abs(acc_lambda + 1.0) > 1e-10:
                raise serializers.ValidationError(
                    "The valid range for the 'acc_lambda' parameter is from 0.0001 to 0.001 or it can be -1.0. Please check!")

        if intblkm not in [1, 2]:
            raise serializers.ValidationError("The 'intblkm' parameter must be 1 or 2. Please check!")

        if solve not in [1, 2]:
            raise serializers.ValidationError("The 'solve' parameter must be 1 or 2. Please check!")

        if not (200 <= max_iter <= 1000000):
            raise serializers.ValidationError(
                "The valid range for the 'max_iter' parameter is from 200 to 1000000. Please check!")

        if not (0.0001 <= damp <= 1.0):
            raise serializers.ValidationError(
                "The valid range for the 'damp' parameter is from 0.0001 to 1.0. Please check!")

        if not (1e-8 <= h_close <= 1e-1):
            raise serializers.ValidationError(
                "The valid range for the 'h_close' parameter is from 0.1 to 1e-8. Please check!")

        if solve == 2 and not (1e-8 <= r_close <= 1e-1):
            raise serializers.ValidationError(
                "The valid range for the 'r_close' parameter is from 0.1 to 1e-8. Please check!")

        if relax not in [0, 1]:
            raise serializers.ValidationError("The 'relax' parameter value must be 0 or 1. Please check!")

        if relax == 1:
            if not (0.35 <= theta <= 0.95):
                raise serializers.ValidationError(
                    "The valid range for the 'theta' parameter is from 0.35 to 0.95. Please check!")
            if not (1.0 <= gamma <= 5.0):
                raise serializers.ValidationError(
                    "The valid range for the 'gamma' parameter is from 1.0 to 5.0. Please check!")
            if not (0.0 < akappa <= 0.2):
                raise serializers.ValidationError(
                    "The valid range for the 'akappa' parameter is from 0.0 (exclusive) to 0.2. Please check!")
            if not (0 <= n_iter <= 100):
                raise serializers.ValidationError(
                    "The valid range for the 'n_iter' parameter is from 0 to 100. Please check!")

        if ch_flg not in [0, 1]:
            raise serializers.ValidationError("The 'ch_flg' parameter must be 0 or 1. Please check!")

        if sim_mtd == 2:
            if wd_flg not in [0, 1]:
                raise serializers.ValidationError("The 'wd_flg' parameter must be 0 or 1. Please check!")

            if wd_flg == 1:
                if not (-1.0 <= wet_fct <= 1.0 and wet_fct > 0.0):
                    raise serializers.ValidationError(
                        "The 'wet_fct' parameter should be entered as -1 or a valid value between 0.0 and 1.0 (Note: it should be greater than 0.0 and can be equal to 1.0). Please check!")

                if not (1 <= newt_iter <= 4):
                    raise serializers.ValidationError(
                        "The valid range for the 'newt_iter' parameter is from 1 to 4. Please check!")

                if hd_wet not in [-1, 1, 2]:
                    raise serializers.ValidationError("The 'hd_wet' parameter must be -1, 1, or 2. Please check!")

        if reg_sta not in [0, 1]:
            raise serializers.ValidationError("The 'reg_sta' parameter must be 0 or 1. Please check!")

        if mul_td not in [0, 1]:
            raise serializers.ValidationError("The 'mul_td' parameter must be 0 or 1. Please check!")

        if mul_td == 1:
            if not (-1 <= num_td <= 256 and num_td not in [-1, 0, 1]):
                raise serializers.ValidationError(
                    "The 'num_td' parameter must be either -1 or within the range of 2 to 256. Please check!")

        return data

class ComusOutParsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComusOutParsModel
        fields = '__all__'

    def validate(self, data):
        for field_name, field_value in data.items():
            if field_name != 'comus_dis_uuid' and field_value not in [0, 1, 2]:
                raise serializers.ValidationError(f"The '{field_name}' parameter must be 0, 1, or 2. Please check!")
        return data
