# EasyWebApis-EWA
我的目标是：让数据变得更简单！
## 包含的库
1.easyjson

2.easyurl
## 使用方法
### easyjson 使用
我们现在已经提供了以下几个函数：
```python
easyjson.getjson_local(jsons)               #此函数用于直接输入JSON文本
easyjson.getjson_file(jsons)                #此函数用于获取JSON本地文件
easyjson.getjson_remote()                   #此函数用于获取Internet上的Json文件，推荐用于获取API
easyjson.autojson(jsons , keys , requests)  #此函数用于获取Internet上的Json文件，但是可以支持APi秘钥和请求参数自动获取，目前仍在测试中，不要使用
```
#### easyjson.getjson_local(jsons)
使用jsons，将jsons替换为您的json文本。需要您注意的是，请确保传入的字符为str类型。将会通过此函数返回给您一个字典型文本。
#### easyjson.getjson_file(jsons)
使用此函数，将jsons替换为您的文件路径。通过"\\"代替"\"
#### easyjson.getjson_remote(jsons)
这是主要用于进行WebApi开发的函数，请将jsons替换为您的api地址
#### easyjson.autojson(jsons , keys , requests)
这是新的功能。将jsons替换为webapi地址，将keys替换为您的Api鉴权密钥，将requests替换为您的请求参数和请求内容。由于此功能尚在内测，因此不告知具体的操作方式。

#致谢
感谢您能使用EWA，若有问题，请提交Issues。
本人学业繁忙，不一定会回复。也可以向我发邮件：xhcmli@outlook.com
