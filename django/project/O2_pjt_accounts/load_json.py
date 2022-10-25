import requests

key = "6e2592277619abca4da5a340bc99bd77"

fin_grp_list = [
    '020000',    # 은행
    '030200',    # 여신전문
    '030300',    # 저축은행
    '050000',    # 보험회사
    '060000',    # 금융투자
]

# 1. 금융회사 API
# 금융회사 API 상세
company_search_url = f"http://finlife.fss.or.kr/finlifeapi/companySearch.json"
# http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth=6e2592277619abca4da5a340bc99bd77&topFinGrpNo=020000&pageNo=1

params = {
    "auth" : key,
    "topFinGrpNo" : "020000",
    "pageNo" : "1"
}

# response = requests.get(company_search_url, params=params).json()
# print(response)

# 2. 정기예금 API


deposit_product_url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"

params = {
    "auth" : key,
    "topFinGrpNo" : "020000",
    "pageNo" : "1"
}

response = requests.get(deposit_product_url, params=params).json()

# open api에서 전달하는 자료의페이지는 항상 한 장인 것 같다.
# pprint(response['result']['max_page_no'])
# pprint(response['result']['baseList'])
deposit_products = response['result']['baseList'] # 상품 리스트가 담겨있다.
print(len(deposit_products))
'''
[
{
dcls_month: "202210",
fin_co_no: "0010001",
fin_prdt_cd: "WR0001A",
kor_co_nm: "우리은행",
fin_prdt_nm: "우리 SUPER정기예금",
join_way: "영업점,인터넷,스마트폰,전화(텔레뱅킹)",
mtrt_int: "만기 후
- 1개월이내 : 만기시점약정이율×50%
- 1개월초과 6개월이내: 만기시점약정이율×30%
- 6개월초과 : 만기시점약정이율×20%

※ 만기시점 약정이율 : 일반정기예금 금리",
spcl_cnd: "해당사항 없음",
join_deny: "1",
join_member: "실명의 개인",
etc_note: "- 만기일을 일,월 단위로 자유롭게 선택 가능
- 10년까지 자동재예치가 가능",
max_limit: null,
dcls_strt_day: "20221020",
dcls_end_day: null,
fin_co_subm_day: "202210211541"
},...]
'''
# for product in deposit_products:
    


# 3. 적금 API

# 4. 연금저축 API


# 5. 주택담보대출 API

# 6. 전세자금대출 API

# 7. 개인신용대출 API

