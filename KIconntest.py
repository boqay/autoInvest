import mojito
import pprint

with open("./koreainvestment.key") as f:
    lines = f.readlines()

key = lines[0].strip()
secret = lines[1].strip()
acc_no=lines[2].strip()

broker = mojito.KoreaInvestment(
    api_key=key,
    api_secret=secret,
    acc_no=acc_no,
    mock=True
)
resp = broker.fetch_price("005930")
print("시가:  ", resp['output']['stck_oprc'])
print("고가 : ", resp['output']['stck_hgpr']) 
print("저가  : ", resp['output']['stck_lwpr'])
print("종가: ", resp['output']['stck_prpr'])
pprint.pprint(resp)