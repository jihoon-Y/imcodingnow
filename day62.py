# 06. 환전 서비스

prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]

# 조건1 : 원화로 이루어진 위의 리스트를 미국 달러로, 일본 엔화로 환전하는 함수를 사용하라
# 조건2 : 반복문을 통해 리스트 요소들을 변환시켜라

# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000  # 1,000원 당 1달러


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd / 8 * 1000


# 원화(￦)로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
# prices를 원화(￦)에서 달러($)로 변환하기
i = 0
while i < len(prices):
    prices[i] = krw_to_usd(prices[i])
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)로 변환하기
i = 0
while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i += 1

# 엔화(￥)로 각각 얼마인가요?
print("일본 화폐: " + str(prices))