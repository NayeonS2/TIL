# 1단계 데이터 스키마 확인
# 코드 실행에 필요한 모듈 import하기
import pprint
import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

# API 요청 결과를 확인하기 위해 테스트로 호출하기 위한 코드
key = "6e2592277619abca4da5a340bc99bd77"
url = f"https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.xml?auth={key}&topFinGrpNo=020000&pageNo=1"

response = requests.get(url).content.decode('euc-kr')

# pprint.pprint(response)

# 요청결과를 일별한 결과
# <products>태그 하위에 복수의 <product>태그가 내포되어 있고,
# <product>태그는 개별 적금 상품들의 정보 지님
'''
'초록세상적금</fin_prdt_nm> \n'
 '<join_way>영업점,인터넷,스마트폰</join_way> \n'
 '<mtrt_int>만기후 1년 이내 : 만기시점 계약기간별 기본금리의 1/2\n'
 '만기후 1년 초과 : 보통예금 금리</mtrt_int> \n'
 '<spcl_cnd>※ 우대금리 최대한도 : 1.0%p(연%, 세전)\n'
 '1. 온실가스 줄이기 실천서약서 동의 : 0.1%p\n'
 '2. 통장미발급 : 0.3%p\n'
 '3. 손하나로인증 서비스 등록 : 0.2%p\n'
 '4. 대중교통이용 : 0.2%p\n'
 '5. NH내가Green초록세상예금 동시 보유 : 0.2%p</spcl_cnd> \n'
 '<join_deny>3</join_deny> \n'
 '<join_member>개인</join_member> \n'
 '<etc_note>초입금5만원 이상 및 매회 1만원 이상, 매월50만원이내\n'
 '(단, 만기일 전 3개월 이내에는 이전 적립금 합계액을 초과하여 입금불가)\n'    
 '\n'
 '※자세한 사항은 상품설명서 참조</etc_note> \n'
 '<max_limit>500000</max_limit> \n'
 '<dcls_strt_day>20220926</dcls_strt_day> \n'
 '<dcls_end_day></dcls_end_day> \n'
 '<fin_co_subm_day>202209260940</fin_co_subm_day> \n'
 '\t\t\t</baseinfo>  \n'
 '\t\t\t<options>  \n'
 '\t\t\t\t<option>  \n'
 '<intr_rate_type>S</intr_rate_type> \n'
 '<intr_rate_type_nm>단리</intr_rate_type_nm> \n'
 '<rsrv_type>F</rsrv_type> \n'
 '<rsrv_type_nm>자유적립식</rsrv_type_nm> \n'
 '<save_trm>12</save_trm> \n'
 '<intr_rate>2.6</intr_rate> \n'
 '<intr_rate2>3.6</intr_rate2> \n'
 '\t\t\t\t</option>  \n'
 '\t\t\t\t<option>  \n'
 '<intr_rate_type>S</intr_rate_type> \n'
 '<intr_rate_type_nm>단리</intr_rate_type_nm> \n'
 '<rsrv_type>F</rsrv_type> \n'
 '<rsrv_type_nm>자유적립식</rsrv_type_nm> \n'
 '<save_trm>24</save_trm> \n'
 '<intr_rate>2.65</intr_rate> \n'
 '<intr_rate2>3.65</intr_rate2> \n'
 '\t\t\t\t</option>  \n'
 '\t\t\t\t<option>  \n'
 '<intr_rate_type>S</intr_rate_type> \n'
 '<intr_rate_type_nm>단리</intr_rate_type_nm> \n'
 '<rsrv_type>F</rsrv_type> \n'
 '<rsrv_type_nm>자유적립식</rsrv_type_nm> \n'
 '<save_trm>36</save_trm> \n'
 '<intr_rate>2.9</intr_rate> \n'
 '<intr_rate2>3.9</intr_rate2> \n'
 '\t\t\t\t</option>  \n'
 '\t\t\t</options>  \n'
 '\t\t</product>  \n'
 '\t\t<product>  \n'
 '\t\t\t<baseinfo>  \n'
 '<dcls_month>202209</dcls_month> \n'
 '<fin_co_no>0013175</fin_co_no> \n'
 '<kor_co_nm>농협은행주식회사</kor_co_nm> \n'
 '<fin_prdt_cd>10-059-1228-0004</fin_prdt_cd> \n'
 '<fin_prdt_nm>법사랑플러스적금</fin_prdt_nm> \n'
 '<join_way>영업점</join_way> \n'
 '<mtrt_int>만기후 3개월 이내 : 만기시점 국고채 1년물 금리\n'
 '만기후 1년 이내 : 만기시점 채움적금 계약기간별 고시금리의 50%\n'
 '만기후 1년 초과 : 만기시점 보통예금 금리</mtrt_int> \n'
 '<spcl_cnd>1. NH채움카드 이용실적 월평균 10만원 이상 : 0.1%p\n'
 '2. 주택청약종합저축 가입하고, 6개월 이상 보유 : 0.1%p\n'
 '3. 이 적금 가입일이 당행 고객정보 최초등록일과 동일한 경우 : 0.1%p\n'       
 '4. 법사랑 사이버랜드 회원 : 0.1%p</spcl_cnd> \n'
 '<join_deny>1</join_deny> \n'
 '<join_member>개인</join_member> \n'
 '<etc_note>초입금 5만원 이상 및 매회  1만원 이상, 매월 5백만원 이내(1인당),  총불입액 1억8천만원이내(1인당) 자유적립\n'
 '(단,계약기간 3/4 경과 후 적립할 수 있는 금액은 이전 적립누계액의 1/2이내)</etc_note> \n'
 '<max_limit>5000000</max_limit> \n'
 '<dcls_strt_day>20220926</dcls_strt_day> \n'
 '<dcls_end_day></dcls_end_day> \n'
 '<fin_co_subm_day>202209260940</fin_co_subm_day> \n'
 '\t\t\t</baseinfo>  \n'
 '\t\t\t<options>  \n'
 '\t\t\t\t<option>  \n'
 '<intr_rate_type>S</intr_rate_type> \n'
 '<intr_rate_type_nm>단리</intr_rate_type_nm> \n'
 '<rsrv_type>F</rsrv_type> \n'
 '<rsrv_type_nm>자유적립식</rsrv_type_nm> \n'
 '<save_trm>36</save_trm> \n'
 '<intr_rate>3.62</intr_rate> \n'
 '<intr_rate2>4.02</intr_rate2> \n'
 '\t\t\t\t</option>  \n'
 '\t\t\t\t<option>  \n'
 '<intr_rate_type>S</intr_rate_type> \n'
 '<intr_rate_type_nm>단리</intr_rate_type_nm> \n'
 '<rsrv_type>F</rsrv_type> \n'
 '<rsrv_type_nm>자유적립식</rsrv_type_nm> \n'
 '<save_trm>24</save_trm> \n'
 '<intr_rate>3.41</intr_rate> \n'
 '<intr_rate2>3.81</intr_rate2> \n'
 '\t\t\t\t</option>  \n'
 '\t\t\t\t<option>  \n'
 '<intr_rate_type>S</intr_rate_type> \n'
 '<intr_rate_type_nm>단리</intr_rate_type_nm> \n'
 '<rsrv_type>F</rsrv_type> \n'
 '<rsrv_type_nm>자유적립식</rsrv_type_nm> \n'
 '<save_trm>12</save_trm> \n'
 '<intr_rate>3.26</intr_rate> \n'
 '<intr_rate2>3.66</intr_rate2> \n'
 '\t\t\t\t</option>  \n'
 '\t\t\t</options>  \n'
 '\t\t</product>  \n'
 ...
'''

# 개별 상품 정보가 내포되어 있는 <product>태그를 모두 추출하여 list로 만들기
# 개별 상품정보를 뜻하는 <product>태그를 달고 있는 데이터 모두 추출 :  findAll 함수
xml_obj = BeautifulSoup(response, 'html.parser') # html이나 xml파싱할 때
# html.parser(lxml-xml t사용해도 무방)
rows = xml_obj.findAll('product') # <product>에 nested된 정보 추출
# print(rows)
'''
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>2.65</intr_rate>
<intr_rate2>6.15</intr_rate2>
</option>
</options>
</product>, <product>
<baseinfo>
<dcls_month>202209</dcls_month>
<fin_co_no>0013175</fin_co_no>
<kor_co_nm>농협은행주식회사</kor_co_nm>
<fin_prdt_cd>10-047-1381-0001</fin_prdt_cd>
<fin_prdt_nm>NH내가Green
초록세상적금</fin_prdt_nm>
<join_way>영업점,인터넷,스마트폰</join_way>
<mtrt_int>만기후 1년 이내 : 만기시점 계약기간별 기본금리의 1/2
만기후 1년 초과 : 보통예금 금리</mtrt_int>
<spcl_cnd>※ 우대금리 최대한도 : 1.0%p(연%, 세전)
1. 온실가스 줄이기 실천서약서 동의 : 0.1%p
2. 통장미발급 : 0.3%p
3. 손하나로인증 서비스 등록 : 0.2%p
4. 대중교통이용 : 0.2%p
5. NH내가Green초록세상예금 동시 보유 : 0.2%p</spcl_cnd>
<join_deny>3</join_deny>
<join_member>개인</join_member>
<etc_note>초입금5만원 이상 및 매회 1만원 이상, 매월50만원이내
(단, 만기일 전 3개월 이내에는 이전 적립금 합계액을 초과하여 입금불가)

※자세한 사항은 상품설명서 참조</etc_note>
<max_limit>500000</max_limit>
<dcls_strt_day>20220926</dcls_strt_day>
<dcls_end_day></dcls_end_day>
<fin_co_subm_day>202209260940</fin_co_subm_day>
</baseinfo>
<options>
<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>12</save_trm>
<intr_rate>2.6</intr_rate>
<intr_rate2>3.6</intr_rate2>
</option>
<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>24</save_trm>
<intr_rate>2.65</intr_rate>
<intr_rate2>3.65</intr_rate2>
</option>
<option>
<intr_rate_type>S</intr_rate_type>
<intr_rate_type_nm>단리</intr_rate_type_nm>
<rsrv_type>F</rsrv_type>
<rsrv_type_nm>자유적립식</rsrv_type_nm>
<save_trm>36</save_trm>
<intr_rate>2.9</intr_rate>
<intr_rate2>3.9</intr_rate2>
</option>
</options>
</product>, 
...

'''

# 은행별 코드와 코드명 매칭
fin_co_no = xml_obj.findAll('fin_co_no')
kor_co_nm = xml_obj.findAll('kor_co_nm')
for i in range(len(fin_co_no)):
    fin_co_no[i] = str(fin_co_no[i]).strip('</fin_co_no>')
    kor_co_nm[i] = str(kor_co_nm[i]).strip('</kor_co_nm>')
co_nm_set = set((zip(fin_co_no, kor_co_nm)))

# 2. API를 호출하여 데이터를 리스트로 변환하는 함수 정의
def get_product(KEY, FINGROUP, PAGE):
    # 파이썬에서 인터넷을 연결하기 위해 urllib 패키지 사용.
    # urlopen함수는 지정한 url과 소켓 통신할 수 있도록 자동 연결해줌
    import requests
    from bs4 import BeautifulSoup
    from lxml import html
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode, quote_plus, unquote
    
    url = f"https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.xml?auth={KEY}&topFinGrpNo={FINGROUP}&pageNo={PAGE}"
    response = requests.get(url).content.decode('euc-kr')    

    # html을 파싱할 때는 html.parser를,
    # xml을 파싱할 때는 lxml.parser 사용
    xml_obj = BeautifulSoup(response, 'html.parser')
    rows = xml_obj.findAll('product')
    return rows

# 3. 금융기관별 적금 정보(상품명, 가입방법, 이자율, 한도, 우대금리) 수집
# - API 호출에 필요한 파라미터
# - 금융기관별 코드 list : 데이터 명세 참고
fin_grp_list = [
    '020000',    # 은행
    '030200',    # 여신전문
    '030300',    # 저축은행
    '050000',    # 보험회사
    '060000',    # 금융투자
]

# API 호출에 필요한 파라미터(필수)
KEY = "6e2592277619abca4da5a340bc99bd77"# 발급받은 인증키
PAGE = 1 # 조회하고자 하는 페이지 번호

# 수집할 상품 스펙 태그명 list = 데이터 명세 참고
item_list = [
    'dcls_month',       # 공시제출월
    'kor_co_nm',        # 금융회사명
    'fin_prdt_nm',      # 금융상품명
    'join_way',         # 가입방법
    'mtrt_cnd',         # 만기 후 이자율
    'spcl_cnd',         # 우대조건
    'join_deny',        # 가입제한 1" 제한X, 2:서민전용, 3: 일부제한
    'join_member',      # 가입대상
    'max_limit',        # 최고한도
    'intr_rate_type_nm',# 저축 금리 유형명
    'rsrv_type_nm',     # 적립 유형명
    'save_tm',          # 저축 기간
    'intr_rate',        # 저축금
    'intr_rate2',       # 최고 우대금리
]

# 스크래핑한 데이터를 담을 빈 list 정의
bank_savings_list = list()

# 금융기관별로 상품 정보를 호출한 후 의도한 스펙을 스크래핑하는 for-loop문
for grp in fin_grp_list:
    products = get_product(KEY, grp, PAGE)
    for p in range(len(products)):
        savings_product_list = list()
        for i in item_list:
            try:
                # 특정 스펙을 수집하는 과정에서 어떤 종류든 error발생 시
                savings_info = products[p].find(i).text
            except:
                savings_info = ''
            savings_product_list.append(savings_info)
        bank_savings_list.append(savings_product_list)
# print(bank_savings_list)

# import pandas
import pandas as pd
from pandas import DataFrame
from datetime import datetime

# 위 과정의 결과물은 list이기 때문에 이것을  dataframe으로 변형
# DF로 변형하면서 컬럼명을 국문으로 지정
bank_savings_df = DataFrame(bank_savings_list, columns=[
    '공시제출월',
    '금융회사명',
    '금융상품명',
    '가입방법',
    '만기 후 이자율',
    '우대조건',
    '가입제한', # 1" 제한X, 2:서민전용, 3: 일부제한
    '가입대상',
    '최고한도',
    '저축 금리 유형명',
    '적립 유형명',
    '저축 기간',
    '저축금',
    '최고 우대금리'
])

# print(bank_savings_df.head())
'''
    공시제출월        금융회사명               금융상품명  ... 저축 기간   저축금 최고 우대금리
0  202209         우리은행        우리SUPER주거래적금  ...        2.15    4.05
1  202209         우리은행               WON적금  ...         3.4     3.6
2  202209  한국스탠다드차타드은행             퍼스트가계적금  ...        2.95    2.95
3  202209         대구은행  자유적금\n(내가만든　보너스적금)  ...        2.96    3.51
4  202209         대구은행            마이(my)적금  ...        2.96    3.86

[5 rows x 14 columns]

'''

# # 4. 데이터 프레임 엑셀로 저장
date = datetime.today().strftime('%Y-%m-%d')
bank_savings_df.to_excel(date + '_savings interest_3.xlsx', index=False)