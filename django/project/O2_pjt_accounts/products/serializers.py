from django.forms import CharField
from rest_framework import serializers
from .models import SavingDeposit

class SavingDepositSerializer(serializers.ModelSerializer):
    join_way = serializers.CharField(allow_null=True) # 가입방법
    mtrt_int = serializers.CharField(allow_null=True) # 만기 후
    max_limit = serializers.CharField(allow_null=True)
    spcl_cnd = serializers.CharField(allow_null=True) # 우대조건
    join_deny = serializers.CharField(allow_null=True) # 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_member = serializers.CharField(allow_null=True)
    etc_note = serializers.CharField(allow_null=True) # 기타 유의사항
    max_limit = serializers.CharField(allow_null=True) # 최고한도
    dcls_strt_day = serializers.CharField(allow_null=True) # 공시 시작일
    dcls_end_day = serializers.CharField(allow_null=True) # 공시 종료일
    fin_co_subm_day = serializers.CharField(allow_null=True) # 금융회사 제출일
    
    class Meta:
        model = SavingDeposit
        fields = '__all__'
