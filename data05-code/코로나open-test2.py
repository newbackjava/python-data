# Python3 샘플 코드 #


import requests

url = 'http://apis.data.go.kr/1262000/CountryCovid19SafetyServiceNew/getCountrySafetyNewsListNew'
params ={'serviceKey' : '서비스키', 'returnType' : 'JSON', 'numOfRows' : '10', 'pageNo' : '1', 'cond[country_nm::EQ]' : '가나', 'cond[country_iso_alp2::EQ]' : 'GH' }

response = requests.get(url, params=params)
print(response.content)