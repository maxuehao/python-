import requests

#无参数请求
headers = {'user-agent': 'my-app/0.0.1'}#构建请求头
r = requests.get('https://github.com/timeline.json', headers=headers)
r.encoding = 'utf-8' #编码问题
r.text #文本请求
r.content #字节的方式访问请求响应体，对于非文本请求


#传递 URL GET 参数
payload = {'key1': 'value1', 'key2': ['value2', 'value3']} #将一个列表作为值传入
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
>>http://httpbin.org/get?key1=value1&key2=value2&key2=value3

payload = {'key1': 'value1', 'key2': 'value2'} #请求参数
r = requests.get("http://httpbin.org/get", params=payload) 


#POST 请求
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)


#JSON 响应内容
r = requests.get('https://github.com/timeline.json')
r.json()


#响应状态码
r = requests.get('http://httpbin.org/get')
r.status_code


#如果某个响应中包含一些 cookie，你可以快速访问它们：
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']


#要想发送你的cookies到服务器，可以使用 cookies 参数：
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text
