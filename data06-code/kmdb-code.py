import requests

# 1. 기본 URL
url = "http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp"

# 2. 요청 파라미터 (쿼리스트링)
params = {
    "collection": "kmdb_new2",
    "nation": "대한민국",
    "ServiceKey": "R71XD4VMIF4UV7I452XI",  # 발급받은 키
    "val001": "2018",  # 상영년도
    "val002": "01"     # 상영월ㅏㅡ유
}

# 3. GET 요청 보내기
response = requests.get(url, params=params)

# 4. 결과 출력
print("Status:", response.status_code)
print("Headers:", dict(response.headers))
print("Body:", response.text)


