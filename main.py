import requests
import json

def get_data():

    cookies = {
        '__lhash_': '89e493ff21ee2c17901c57b5aea0c871',
        'MVID_AB_PERSONAL_RECOMMENDS': 'true',
        'MVID_AB_UPSALE': 'true',
        'MVID_ACCESSORIES_PDP_BY_RANK': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_CASCADE_CMN': 'true',
        'MVID_CATALOG_NEW': 'true',
        'MVID_CHAT_VERSION': '6.6.0',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_DIGITAL': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_DISPLAY_ACCRUED_BR': 'true',
        'MVID_DISPLAY_PERS_DISCOUNT': 'true',
        'MVID_EMPLOYEE_DISCOUNT': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_NEW_CHAT_PDP': 'true',
        'MVID_NEW_GET_SHOPPING_CART_HIT_PRODUCTS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_POST_SHOPPING_CART_AUTHORIZE': 'true',
        'MVID_NEW_POST_SHOPPING_CART_USEFUL_PRODUCTS': 'true',
        'MVID_PODELI_PDP': 'true',
        'MVID_PROMO_PAGES_ON_2': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICE_AVLB': 'true',
        'MVID_SINGLE_CHECKOUT': 'true',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod1',
        'mindboxDeviceUUID': '1cc65070-ab60-42b2-8692-eea6929f4e5a',
        'directCrm-session': '%7B%22deviceGuid%22%3A%221cc65070-ab60-42b2-8692-eea6929f4e5a%22%7D',
        '_ym_uid': '170932042623785005',
        '_ym_d': '1709320426',
        '_ga': 'GA1.1.985081463.1709320426',
        'admitad_uid': 'mvideo',
        'utm_term': 'mvideo',
        '__SourceTracker': 'yandex__cpc',
        'admitad_deduplication_cookie': 'yandex__cpc',
        '__cpatrack': 'yandex_cpc',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '62db3ab5ace2e91fa254f3dd95bbee38',
        'tmr_lvidTS': '1709320428501',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'f52f3e99-2999-424d-be10-a06c76e1e7da',
        'advcake_track_id': '01966146-8e23-4e59-c659-7fe6fc5a1de9',
        'advcake_session_id': '79d1046b-af5b-2231-f695-2f99261a75c6',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Fpid%3Dyandexdirect_int%26c%3Dmg_image_name_p_msk%26af_siteid%3Dsearch_none%26af_c_id%3D81880841%26af_adset_id%3D5107952449%26af_ad_id%3D13283626504%26af_ad%3Dmvideo%26af_sub1%3D%26af_sub2%3D1%26is_retargeting%3Dtrue%26clickid%3D3474376258296741887%26idfa%3D%26google_aid%3D%26android_id%3D%26oaid%3D%26af_reengagement_window%3D7d%26af_force_deeplink%3Dtrue%26af_click_lookback%3D7d%26utm_medium%3Dcpc%26utm_source%3Dyandex%26utm_campaign%3Dcn%3Amg_image_name_p_msk%7Ccid%3A81880841%26utm_term%3Dmvideo%26utm_content%3Dph%3A42727574045%7Cre%3A42727574045%7Ccid%3A81880841%7Cgid%3A5107952449%7Caid%3A13283626504%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A213%7C%25D0%259C%25D0%25BE%25D1%2581%25D0%25BA%25D0%25B2%25D0%25B0%26yclid%3D3474376258296741887',
        'advcake_utm_partner': 'cn%3Amg_image_name_p_msk%7Ccid%3A81880841',
        'advcake_utm_webmaster': 'ph%3A42727574045%7Cre%3A42727574045%7Ccid%3A81880841%7Cgid%3A5107952449%7Caid%3A13283626504%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A213%7C%25D0%259C%25D0%25BE%25D1%2581%25D0%25BA%25D0%25B2%25D0%25B0',
        'advcake_click_id': '',
        'uxs_uid': 'd50f5c10-d7ff-11ee-9e50-85d2a1a2d361',
        'flocktory-uuid': '65ef7f12-7382-4dcf-9db3-e8dcb9dc20f7-2',
        'customer_email': 'null',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1157946378.20480.0000',
        'bIPs': '-1178626581',
        '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
        'afUserId': '123aa2fa-66c7-470a-99cd-ba3ed78d133f-p',
        'AF_SYNC': '1709320429416',
        'adid': '170932042947024',
        '__hash_': 'f2036355be794482376bb97d8f6c8f64',
        '_sp_ses.d61c': '*',
        '_ym_isad': '2',
        '_sp_id.d61c': 'ab42f880-f341-4aca-91b8-59805680a55f.1709320426.2.1709393608.1709321203.9476bc70-06ac-41c7-88fc-6bdadc2c9d99.16d8fc07-02b1-423c-bda2-da69c1f51491.95620fa3-b1d2-4366-9a7b-b9a2454c60c8.1709393598453.7',
        'tmr_detect': '0%7C1709393610166',
        '_gp100025D5': '{"hits":1,"vc":1,"ac":1}',
        'gsscgib-w-mvideo': '3BfOtMqagKx1kI5TwcLnB5xae+NV3gdpZtNsO5dYaLcbRZYuPINLflPs/ZF7PZ9StMolAETq/KjXzOurmMCGGmgXPoaOGWD/WOJbSFmINp+7Zdh1DL889qZ19vLrDNm5L0gX3uW76jY9amQVeOZdRo08GhgKeD5UovMe9449L//9o4CyFSmV0L3f82knPaD46qDH/NUqDSEMQPordQrIxGZGIaXpvZ9tlHeo/YgTqIcL3FeS7ms5Opl0lqYrhQ==',
        'gsscgib-w-mvideo': '3BfOtMqagKx1kI5TwcLnB5xae+NV3gdpZtNsO5dYaLcbRZYuPINLflPs/ZF7PZ9StMolAETq/KjXzOurmMCGGmgXPoaOGWD/WOJbSFmINp+7Zdh1DL889qZ19vLrDNm5L0gX3uW76jY9amQVeOZdRo08GhgKeD5UovMe9449L//9o4CyFSmV0L3f82knPaD46qDH/NUqDSEMQPordQrIxGZGIaXpvZ9tlHeo/YgTqIcL3FeS7ms5Opl0lqYrhQ==',
        'fgsscgib-w-mvideo': 'IO7bc3bb0ff4a946863b0e042638a81564b1003b',
        'fgsscgib-w-mvideo': 'IO7bc3bb0ff4a946863b0e042638a81564b1003b',
        'gsscgib-w-mvideo': 'SjOgBZngfMoZj8By13/161knbIOX0tR/g1IvTFI7oFgG/cuTLGEbdbFkAggfKj1v4FMcGl+HRpvkaY7caCGchROz/wwH33Bg1kpY4kxOK/2g97yqfnYRfo1mg7PPkIXyBsgNKbUwqx1xGsp1SG0A5430QNqKKL9zhaKq2DC/z8dod1i9qsSw0b6YYfqMSgPoULCDfj7oLhbu6g5TZU0UcokB/GIl5fIMmmqE+ScyieKBoPEeUZbGwQXtzjiRPg==',
        'cfidsgib-w-mvideo': 'VMJTXLKENhX6rOzbecoatGOG7Cdh0DzP9vh5LTZK0KzMFNmbubJu62mminQ6oLOPgLiV8Rc5azJX3LwyRQQAGVR1VE32myxM6k1t2w3tStiVdUOutVpVQajNzMLvbc1D4SL790FVyvRWXGq8nKnJCCOBRxaIQ7nCAEobbGU=',
        '_ga_BNX5WPP3YK': 'GS1.1.1709393598.2.1.1709393951.60.0.0',
        '_ga_CFMZTSS5FM': 'GS1.1.1709393598.2.1.1709393951.0.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'baggage': 'sentry-environment=production,sentry-release=release_24_2_5(6094),sentry-public_key=ae7d267743424249bfeeaa2e347f4260,sentry-trace_id=fc709970c8a0480c8e9ca6c256b41035,sentry-sample_rate=0.5,sentry-transaction=%2F**%2F,sentry-sampled=false',
        'cache-control': 'no-cache',
        # 'cookie': '__lhash_=89e493ff21ee2c17901c57b5aea0c871; MVID_AB_PERSONAL_RECOMMENDS=true; MVID_AB_UPSALE=true; MVID_ACCESSORIES_PDP_BY_RANK=true; MVID_ALFA_PODELI_NEW=true; MVID_CASCADE_CMN=true; MVID_CATALOG_NEW=true; MVID_CHAT_VERSION=6.6.0; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_DISPLAY_ACCRUED_BR=true; MVID_DISPLAY_PERS_DISCOUNT=true; MVID_EMPLOYEE_DISCOUNT=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_NEW_CHAT_PDP=true; MVID_NEW_GET_SHOPPING_CART_HIT_PRODUCTS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_POST_SHOPPING_CART_AUTHORIZE=true; MVID_NEW_POST_SHOPPING_CART_USEFUL_PRODUCTS=true; MVID_PODELI_PDP=true; MVID_PROMO_PAGES_ON_2=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICE_AVLB=true; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod1; mindboxDeviceUUID=1cc65070-ab60-42b2-8692-eea6929f4e5a; directCrm-session=%7B%22deviceGuid%22%3A%221cc65070-ab60-42b2-8692-eea6929f4e5a%22%7D; _ym_uid=170932042623785005; _ym_d=1709320426; _ga=GA1.1.985081463.1709320426; admitad_uid=mvideo; utm_term=mvideo; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; SMSError=; authError=; tmr_lvid=62db3ab5ace2e91fa254f3dd95bbee38; tmr_lvidTS=1709320428501; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=f52f3e99-2999-424d-be10-a06c76e1e7da; advcake_track_id=01966146-8e23-4e59-c659-7fe6fc5a1de9; advcake_session_id=79d1046b-af5b-2231-f695-2f99261a75c6; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Fpid%3Dyandexdirect_int%26c%3Dmg_image_name_p_msk%26af_siteid%3Dsearch_none%26af_c_id%3D81880841%26af_adset_id%3D5107952449%26af_ad_id%3D13283626504%26af_ad%3Dmvideo%26af_sub1%3D%26af_sub2%3D1%26is_retargeting%3Dtrue%26clickid%3D3474376258296741887%26idfa%3D%26google_aid%3D%26android_id%3D%26oaid%3D%26af_reengagement_window%3D7d%26af_force_deeplink%3Dtrue%26af_click_lookback%3D7d%26utm_medium%3Dcpc%26utm_source%3Dyandex%26utm_campaign%3Dcn%3Amg_image_name_p_msk%7Ccid%3A81880841%26utm_term%3Dmvideo%26utm_content%3Dph%3A42727574045%7Cre%3A42727574045%7Ccid%3A81880841%7Cgid%3A5107952449%7Caid%3A13283626504%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A213%7C%25D0%259C%25D0%25BE%25D1%2581%25D0%25BA%25D0%25B2%25D0%25B0%26yclid%3D3474376258296741887; advcake_utm_partner=cn%3Amg_image_name_p_msk%7Ccid%3A81880841; advcake_utm_webmaster=ph%3A42727574045%7Cre%3A42727574045%7Ccid%3A81880841%7Cgid%3A5107952449%7Caid%3A13283626504%7Cadp%3Ano%7Cpos%3Apremium1%7Csrc%3Asearch_none%7Cdvc%3Adesktop%7Ccoef_goal%3A0%7Cregion%3A213%7C%25D0%259C%25D0%25BE%25D1%2581%25D0%25BA%25D0%25B2%25D0%25B0; advcake_click_id=; uxs_uid=d50f5c10-d7ff-11ee-9e50-85d2a1a2d361; flocktory-uuid=65ef7f12-7382-4dcf-9db3-e8dcb9dc20f7-2; customer_email=null; flacktory=no; BIGipServeratg-ps-prod_tcp80=1157946378.20480.0000; bIPs=-1178626581; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; afUserId=123aa2fa-66c7-470a-99cd-ba3ed78d133f-p; AF_SYNC=1709320429416; adid=170932042947024; __hash_=f2036355be794482376bb97d8f6c8f64; _sp_ses.d61c=*; _ym_isad=2; _sp_id.d61c=ab42f880-f341-4aca-91b8-59805680a55f.1709320426.2.1709393608.1709321203.9476bc70-06ac-41c7-88fc-6bdadc2c9d99.16d8fc07-02b1-423c-bda2-da69c1f51491.95620fa3-b1d2-4366-9a7b-b9a2454c60c8.1709393598453.7; tmr_detect=0%7C1709393610166; _gp100025D5={"hits":1,"vc":1,"ac":1}; gsscgib-w-mvideo=3BfOtMqagKx1kI5TwcLnB5xae+NV3gdpZtNsO5dYaLcbRZYuPINLflPs/ZF7PZ9StMolAETq/KjXzOurmMCGGmgXPoaOGWD/WOJbSFmINp+7Zdh1DL889qZ19vLrDNm5L0gX3uW76jY9amQVeOZdRo08GhgKeD5UovMe9449L//9o4CyFSmV0L3f82knPaD46qDH/NUqDSEMQPordQrIxGZGIaXpvZ9tlHeo/YgTqIcL3FeS7ms5Opl0lqYrhQ==; gsscgib-w-mvideo=3BfOtMqagKx1kI5TwcLnB5xae+NV3gdpZtNsO5dYaLcbRZYuPINLflPs/ZF7PZ9StMolAETq/KjXzOurmMCGGmgXPoaOGWD/WOJbSFmINp+7Zdh1DL889qZ19vLrDNm5L0gX3uW76jY9amQVeOZdRo08GhgKeD5UovMe9449L//9o4CyFSmV0L3f82knPaD46qDH/NUqDSEMQPordQrIxGZGIaXpvZ9tlHeo/YgTqIcL3FeS7ms5Opl0lqYrhQ==; fgsscgib-w-mvideo=IO7bc3bb0ff4a946863b0e042638a81564b1003b; fgsscgib-w-mvideo=IO7bc3bb0ff4a946863b0e042638a81564b1003b; gsscgib-w-mvideo=SjOgBZngfMoZj8By13/161knbIOX0tR/g1IvTFI7oFgG/cuTLGEbdbFkAggfKj1v4FMcGl+HRpvkaY7caCGchROz/wwH33Bg1kpY4kxOK/2g97yqfnYRfo1mg7PPkIXyBsgNKbUwqx1xGsp1SG0A5430QNqKKL9zhaKq2DC/z8dod1i9qsSw0b6YYfqMSgPoULCDfj7oLhbu6g5TZU0UcokB/GIl5fIMmmqE+ScyieKBoPEeUZbGwQXtzjiRPg==; cfidsgib-w-mvideo=VMJTXLKENhX6rOzbecoatGOG7Cdh0DzP9vh5LTZK0KzMFNmbubJu62mminQ6oLOPgLiV8Rc5azJX3LwyRQQAGVR1VE32myxM6k1t2w3tStiVdUOutVpVQajNzMLvbc1D4SL790FVyvRWXGq8nKnJCCOBRxaIQ7nCAEobbGU=; _ga_BNX5WPP3YK=GS1.1.1709393598.2.1.1709393951.60.0.0; _ga_CFMZTSS5FM=GS1.1.1709393598.2.1.1709393951.0.0.0',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/brand=xiaomi?reff=menu_main',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'fc709970c8a0480c8e9ca6c256b41035-a254b2ab83252cd1-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'x-set-application-id': '0cfe56bb-37d5-4155-ad46-c97db608ec93',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJicmFuZCIsIiIsInhpYW9taSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    # print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()