#request库测试服务端
import  requests,pprint
'''
response = requests.get('http://192.168.0.105:4999/api/mgr/customers?action=list_customer')

pprint.pprint(response.json())
'''
payload={
    'username':'vezzzingQAQ',
    'password':'3r1zxz321212'
}
response=requests.post('http://192.168.0.105:4999/api/mgr/signin',data=payload)
pprint.pprint(response.json())