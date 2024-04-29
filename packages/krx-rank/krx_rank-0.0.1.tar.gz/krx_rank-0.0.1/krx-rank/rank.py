import requests
import json
import pandas as pd
from etc import *

# 주가 등락률 상위 50종목
# 최대 조회기간은 2년
# market='KOSPI', 'KOSDAQ', 'ALL'(KOSPI+KOSDAQ) 중 선택가능
# 입력하지 않으면 'ALL'로 적용

def price_fluctuation_high(start_date, end_date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01501'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('itmTpCd2', '1'),
                ('strtDd', str(start_date)),
                ('endDd', str(end_date)),
                ('stkprcTpCd', 'Y')]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[5]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def price_fluctuation_low(start_date, end_date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01501'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('itmTpCd2', '2'),
                ('strtDd', str(start_date)),
                ('endDd', str(end_date)),
                ('stkprcTpCd', 'Y')]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[5]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df


# 거래대금 상하위 50종목
# 최대 조회기간은 2년
# market='KOSPI', 'KOSDAQ', 'ALL'(KOSPI+KOSDAQ) 중 선택가능
# 입력하지 않으면 'ALL'로 적용

def trading_value_high(start_date, end_date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [
            ('bld', 'dbms/MDC/EASY/ranking/MDCEASY01601'),
            ('locale', 'ko_KR'),
            ('mktId', str(mk)),
            ('itmTpCd3', '2'),
            ('itmTpCd2', '1'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date)),
            ('stkprcTpCd', 'Y')]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[7]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def trading_value_low(start_date, end_date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01601'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('itmTpCd3', '2'),
                ('itmTpCd2', '2'),
                ('strtDd', str(start_date)),
                ('endDd', str(end_date)),
                ('stkprcTpCd', 'Y')]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[7]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# 거래량 상하위 50종목
# 최대 조회기간은 2년
# market='KOSPI', 'KOSDAQ', 'ALL'(KOSPI+KOSDAQ) 중 선택가능
# 입력하지 않으면 'ALL'로 적용

def trading_volume_high(start_date, end_date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01601'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('itmTpCd3', '1'), # 1이 거래량 2가 거래대금
                ('itmTpCd2', '1'),
                ('strtDd', str(start_date)),
                ('endDd', str(end_date)),
                ('stkprcTpCd', 'Y')]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[6]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def trading_volume_low(start_date, end_date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01601'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('itmTpCd3', '1'), # 1이 거래량 2가 거래대금
                ('itmTpCd2', '2'),
                ('strtDd', str(start_date)),
                ('endDd', str(end_date)),
                ('stkprcTpCd', 'Y')]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[6]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# 시가총액 상하위 50종목
# market='KOSPI', 'KOSDAQ', 'ALL'(KOSPI+KOSDAQ) 중 선택가능
# 입력하지 않으면 'ALL'로 적용

def market_cap_high(date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01701'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('itmTpCd', '1'),
                ('trdDd', str(date)),
                ('stkprcTpCd', 'Y')]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '시가총액', '시가총액비중', '상장주식수']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[3]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def market_cap_low(date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01701'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('itmTpCd', '2'),
                ('trdDd', str(date)),
                ('stkprcTpCd', 'Y')]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    print(df_list)
    col = ['종목코드', '종목명', '시장구분', '시가총액', '시가총액비중', '상장주식수']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[3]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# 최대 조회기간은 2년
# market='KOSPI', 'KOSDAQ', 'ALL'(KOSPI+KOSDAQ) 중 선택가능
# 입력하지 않으면 'ALL'로 적용

def upper_limit(date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01801'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('flucTpCd', '4'),
                ('trdDd', str(date))]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '시', '저', '종', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[6]), reverse=True)
    df = pd.DataFrame(df, columns=col, index=[i for i in range(1, len(df)+1, 1)])
    return df

def lower_limit(date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01801'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('flucTpCd', '5'),
                ('trdDd', str(date))]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '시', '고', '종', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[6]), reverse=False)
    df = pd.DataFrame(df, columns=col, index=[i for i in range(1, len(df)+1, 1)])
    return df

# 최대 조회기간은 2년
# market='KOSPI', 'KOSDAQ', 'ALL'(KOSPI+KOSDAQ) 중 선택가능
# 입력하지 않으면 'ALL'로 적용

def convert_price_high(date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY01901'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('trdDd', str(date))
                ]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시장구분', '종', '환산주가', '액면가', '시가총액']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[4]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def turnover_high(date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02001'),
                ('locale', 'ko_KR'),
                ('mktId', str(mk)),
                ('trdDd', str(date))]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    print(df_list)
    col = ['종목코드', '종목명', '시장구분', '종', '등락률', '회전율', '상장주식수', '거래량']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[5]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# 외국인 지분율 & 한도소진율 상위 50종목
# 최대 조회기간은 2년
# market='KOSPI', 'KOSDAQ', 'ALL'(KOSPI+KOSDAQ) 중 선택가능
# 입력하지 않으면 'ALL'로 적용

def foreigner_share_high(date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02101'),
                ('locale', 'ko_KR'),
                ('itmTpCd', '1'),
                ('mktId', str(mk)),
                ('trdDd', str(date))]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    print(df_list)
    col = ['종목코드', '종목명', '상장주식수', '외국인보유수량', '외국인지분율', '외국인한도수량', '외국인한도소진율']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[5]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def foreigner_limit_high(date, market="ALL"):
    df_list = []
    for mk in mktId(market):
        data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02101'),
                ('locale', 'ko_KR'),
                ('itmTpCd', '2'),
                ('mktId', str(mk)),
                ('trdDd', str(date))]
        df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    print(df_list)
    col = ['종목코드', '종목명', '상장주식수', '외국인보유수량', '외국인지분율', '외국인한도수량', '외국인한도소진율']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[6]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# ETF 주가 등락률 상하위 50종목
# 최대 조회기간은 2년

def etf_price_fluctuation_high(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02201'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EF'),
            ('itmTpCd', '1'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[4]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def etf_price_fluctuation_low(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02201'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EF'),
            ('itmTpCd', '2'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[4]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# ETN 주가 등락률 상하위 50종목
# 최대 조회기간은 2년

def etn_price_fluctuation_high(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02201'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EN'),
            ('itmTpCd', '1'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[4]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def etn_price_fluctuation_low(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02201'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EN'),
            ('itmTpCd', '2'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[4]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# ETF 거래량 상하위 50종목
# 최대 조회기간은 2년

def etf_trading_volume_high(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02301'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EF'),
            ('itmTpCd1', '1'),
            ('itmTpCd2', '1'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[5]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def etf_trading_volume_low(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02301'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EF'),
            ('itmTpCd1', '1'),
            ('itmTpCd2', '2'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[5]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# ETN 거래량 상하위 50종목
# 최대 조회기간은 2년

def etn_trading_volume_high(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02301'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EN'),
            ('itmTpCd1', '1'),
            ('itmTpCd2', '1'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[5]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def etn_trading_volume_low(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02301'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EN'),
            ('itmTpCd1', '1'),
            ('itmTpCd2', '2'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[5]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# ETF 거래대금 상하위 50종목
# 최대 조회기간은 2년

def etf_trading_value_high(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02301'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EF'),
            ('itmTpCd1', '2'),
            ('itmTpCd2', '1'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[6]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def etf_trading_value_low(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02301'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EF'),
            ('itmTpCd1', '2'),
            ('itmTpCd2', '2'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[6]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# ETN 거래대금 상하위 50종목
# 최대 조회기간은 2년

def etn_trading_value_high(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02301'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EN'),
            ('itmTpCd1', '2'),
            ('itmTpCd2', '1'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[6]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def etn_trading_value_low(start_date, end_date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02301'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EN'),
            ('itmTpCd1', '2'),
            ('itmTpCd2', '2'),
            ('strtDd', str(start_date)),
            ('endDd', str(end_date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    col = ['종목코드', '종목명', '시가', '종가', '등락률', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[6]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# ETF NAV 상하위 50종목
# 최대 조회기간은 2년

def etf_net_asset_value_high(date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02401'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EF'),
            ('itmTpCd', '1'),
            ('trdDd', str(date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    print(df_list)
    col = ['종목코드', '종목명', '종', '등락률', '추정NAV', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[4]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def etf_net_asset_value_low(date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02401'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EF'),
            ('itmTpCd', '2'),
            ('trdDd', str(date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    print(df_list)
    col = ['종목코드', '종목명', '종', '등락률', '추정NAV', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[4]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

# ETN NAV 상하위 50종목
# 최대 조회기간은 2년

def etn_net_asset_value_high(date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02401'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EN'),
            ('itmTpCd', '1'),
            ('trdDd', str(date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    print(df_list)
    col = ['종목코드', '종목명', '종', '등락률', '추정NAV', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[4]), reverse=True)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df

def etn_net_asset_value_low(date):
    df_list = []
    data = [('bld', 'dbms/MDC/EASY/ranking/MDCEASY02401'),
            ('locale', 'ko_KR'),
            ('secugrpId', 'EN'),
            ('itmTpCd', '2'),
            ('trdDd', str(date))]
    df_list.append(json.loads(requests.post(BASE_URL, headers=headers, data=data).text)['OutBlock_1'])
    print(df_list)
    col = ['종목코드', '종목명', '종', '등락률', '추정NAV', '거래량', '거래대금']
    df = make_dl(list_cb(df_list), col)
    df.sort(key=lambda x: float(x[4]), reverse=False)
    df = pd.DataFrame(df[:50], columns=col, index=[i for i in range(1, 51, 1)])
    return df