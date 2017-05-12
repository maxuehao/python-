import requests

#�޲�������
headers = {'user-agent': 'my-app/0.0.1'}#��������ͷ
r = requests.get('https://github.com/timeline.json', headers=headers)
r.encoding = 'utf-8' #��������
r.text #�ı�����
r.content #�ֽڵķ�ʽ����������Ӧ�壬���ڷ��ı�����


#���� URL GET ����
payload = {'key1': 'value1', 'key2': ['value2', 'value3']} #��һ���б���Ϊֵ����
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
>>http://httpbin.org/get?key1=value1&key2=value2&key2=value3

payload = {'key1': 'value1', 'key2': 'value2'} #�������
r = requests.get("http://httpbin.org/get", params=payload) 


#POST ����
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)


#JSON ��Ӧ����
r = requests.get('https://github.com/timeline.json')
r.json()


#��Ӧ״̬��
r = requests.get('http://httpbin.org/get')
r.status_code


#���ĳ����Ӧ�а���һЩ cookie������Կ��ٷ������ǣ�
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']


#Ҫ�뷢�����cookies��������������ʹ�� cookies ������
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text
