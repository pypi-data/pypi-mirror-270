from client import EAPIClient


# 创建默认的客户端
def create_client(access_key, secret_key,
                  base_url):  # baseUrl要改成部署后的网关
    client = EAPIClient(access_key, secret_key, base_url)
    return client.call_api({'question': '奥特曼打得过潇洒哥吗'}, 2)

create_client ("dd3724b1b8acf95be5cbf715ffc85fef", "fd9e3b3bf0711ee60ad2174f1e200cbc",'http://192.168.3.5:8090/api/interfaceInfo/invoke')

