from django.shortcuts import render
import requests
from .models import SavingDeposit
from .serializers import SavingDepositSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def save_deposit(request):
    key = "6e2592277619abca4da5a340bc99bd77"

    fin_grp_list = [
    '020000',    # 은행
    '030200',    # 여신전문
    '030300',    # 저축은행
    '050000',    # 보험회사
    '060000',    # 금융투자
    ]
    
    deposit_product_url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"

    for fin_grp in fin_grp_list:
        params = {
            "auth" : key,
            "topFinGrpNo" : fin_grp,
            "pageNo" : "1"
        }
        # fin_grp별 open api 데이터 받아오기
        response = requests.get(deposit_product_url, params=params).json()
        deposit_products = response['result']['baseList']
        
        for product in deposit_products:
            serializer = SavingDepositSerializer(data=product)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        return Response({'RESULT': 'OPEN API RECEIVED SUCCESSFUL!'}, status=status.HTTP_200_OK)
        

'''
            savedeposit = SavingDeposit()

            savedeposit.dcls_month = product.get("dcls_month")
            savedeposit.fin_co_no = product.get("fin_co_no")
            savedeposit.fin_prdt_cd = product.get("fin_prdt_cd")
            savedeposit.kor_co_nm = product.get("kor_co_nm")
            savedeposit.fin_prdt_nm = product.get("fin_prdt_nm")
            savedeposit.join_way = product.get("join_way")
            savedeposit.mtrt_int = product.get("mtrt_int")
            # 만기시점 약정이율 : 일반정기예금 금리",
            savedeposit.spcl_cnd = product.get("spcl_cnd")
            savedeposit.join_deny = product.get("join_deny")
            savedeposit.join_member = product.get("join_member")
            savedeposit.etc_note = product.get("etc_note")
            savedeposit.max_limit = product.get("max_limit")
            savedeposit.dcls_strt_day = product.get("dcls_end_day")
            savedeposit.dcls_end_day = product.get("dcls_end_day")
            savedeposit.fin_co_subm_day = product.get("fin_co_subm_day")


'''