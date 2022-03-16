import requests


def upload(cookies):
    r = requests.request(
        method='POST',
        url='https://xxcapp.xidian.edu.cn/ncov/wap/default/save',
        data={
            'sfzx': '1',
            'tw': '1',
            'sfcyglq': '0',
            'sfyzz': '0',
            'ymtys': '0',
            'qtqk': '',
            'area': '广东省 广州市 黄埔区',
            'city': '广州市',
            'province': '广东省',
            'address': '广东省广州市黄埔区九佛街道中新广州知识城',
            'geo_api_info': {
                'type': 'complete',
                'position': {
                    'Q': '23.321510687935',
                    'R': '113.54531738281298',
                    'lng': '113.545317',
                    'lat': '23.321511',
                },
                'location_type': 'html5',
                'accuracy': '153',
                'isConverted': 'true',
                'status': '1',
                'addressComponent': {
                    'citycode': '020',
                    'adcode': '440112',
                    'businessAreas': [],
                    'neighborhoodType': '',
                    'neighborhood': '',
                    'building': '',
                    'buildingType': '',
                    'street': '峻岚街',
                    'streetNumber': '7号',
                    'country': '中国',
                    'province': '广东省',
                    'city': '广州市',
                    'district': '黄埔区',
                    'towncode': '440112019000',
                    'township': '九佛街道',
                },
                'formattedAddress': '广东省广州市黄埔区九佛街道凤湖中路广州绿地城',
                'roads': [],
                'crosses': [],
                'pois': [],
                'info': 'SUCCESS',
            },
        },
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
        },
        cookies=cookies)

    if r.status_code != 200:
        raise RuntimeError('填写失败，状态码为：{}'.format(r.status_code))
    body = r.json()
    if body['e'] != 0:
        raise RuntimeError('填写失败，错误信息为：{}'.format(body['m']))
    print('填写成功')
