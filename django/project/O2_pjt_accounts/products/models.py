from django.db import models

# Create your models here.
class SavingDeposit(models.Model):
    dcls_month = models.CharField(max_length=50) # 공시제출월
    fin_co_no = models.CharField(max_length=50)  # 금융회사 코드
    fin_prdt_cd = models.CharField(max_length=50) # 금융상품 코드
    kor_co_nm = models.CharField(max_length=50) # 금융회사명
    fin_prdt_nm = models.CharField(max_length=50) # 금융상품명
    join_way = models.CharField(max_length=50, null=True) # 가입방법
    mtrt_int = models.CharField(max_length=200, null=True) # 만기 후
    # 만기시점 약정이율 : 일반정기예금 금리",
    spcl_cnd = models.CharField(max_length=50, null=True) # 우대조건
    join_deny = models.CharField(max_length=50, null=True) # 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_member = models.CharField(max_length=50, null=True)
    etc_note = models.CharField(max_length=200, null=True) # 기타 유의사항
    max_limit = models.CharField(max_length=50, null=True) # 최고한도
    dcls_strt_day = models.CharField(max_length=50, null=True) # 공시 시작일
    dcls_end_day = models.CharField(max_length=50, null=True) # 공시 종료일
    fin_co_subm_day = models.CharField(max_length=50, null=True) # 금융회사 제출일
