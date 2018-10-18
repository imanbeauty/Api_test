# _*_coding:utf-8 _*_
import requests
import urllib3
urllib3.disable_warnings()


def Get_token():
    url =  'https://lift.linli580.com.cn/admin/login'
    params =  {
            "user_name":13800138000,
            "password":123456,
            "channel":1
        }
    rqst = requests.post(url=url,data=params,verify=False)
    tokenInfo = rqst.json()['data']['tokenInfo']['token']
    Bearer = 'Bearer '
    token =  Bearer + tokenInfo
    return token


url1 = 'https://lift.linli580.com.cn/index.php/admin/repair/ContractList'
params = {
    "admin_id":"1",
    "organization_id":"9",
    "page":"1",
    "page_size":"20"
}
header = {"Authorization":Get_token()}
re = requests.get(url=url1,params=params,headers = header,verify=False)
rp = re.text
print(rp)