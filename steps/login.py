import requests


def login(username, password):
    r = requests.request(
        method='POST',
        url='https://xxcapp.xidian.edu.cn/uc/wap/login/check',
        data={
            'username': username,
            'password': password,
        },
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
        })

    if r.status_code != 200:
        raise RuntimeError('登录失败，状态码为：{}'.format(r.status_code))
    body = r.json()
    if body['e'] != 0:
        raise RuntimeError('登录失败，错误信息为：{}'.format(body['m']))
    print('登录成功')
    return r.cookies
