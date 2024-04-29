import pymysql
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler

def preprocess(data) :
    data.dropna(inplace=True)
    data.set_index('data_time',inplace=True)
    data.index = pd.to_datetime(data.index)
    data.info()

    columns_to_scale = ['ma_q']
    scaler = StandardScaler()
    scaler2 = StandardScaler()
    data_scaled = scaler.fit_transform(data[columns_to_scale])
    target_scaled = scaler2.fit_transform(data['ma_q'].values.reshape(-1, 1))
    
    # 스케일링된 열을 포함한 DataFrame 생성
    data_scaled_df = pd.DataFrame(data_scaled, columns=columns_to_scale)
    data_scaled_df = data_scaled_df.set_index(data.index)
    data_scaled_df.rename(columns={'ma_q':'learningma_q'},inplace=True)
    
    # 'ma_Q' 열을 추가하여 원본 DataFrame과 병합
    data_scaled_df['ma_q'] = data_scaled_df['learningma_q']
    data_scaled_df.drop('learningma_q',axis=1, inplace=True)

    features = data_scaled_df.values
    
    return features, scaler2

def getLatestDate():
    # 최종학습날짜 확인
    directory = "./example/trainedModels/js/"
    with open(directory+'latest_train_date.txt', 'r' ) as f:
        lines = f.readlines() 
        saved_date = lines[0].strip()

    return str(saved_date)

def correction(data):
    saved_date = getLatestDate()
    df = pd.DataFrame(data)
    df['data_time'] = pd.to_numeric(df['data_time'])
    cor_df = df[df['data_time'] > int(saved_date)]
    isna = cor_df.isna().sum()
    cols = cor_df.columns

    for i in range(len(isna)):
        if isna[i] > 0:
            df[cols[i]].fillna(0, inplace=True)
    
    zeroInd = cor_df[cor_df['ma_q'] == 0]['data_time']
    cor_df['correction'] = 0
    cor_df['ma_pcode'] = '210601'
    
    if(len(zeroInd) > 0):
        for i in range(len(zeroInd)):
            dt = zeroInd.iloc[i]
            cor_df.loc[cor_df['data_time'] == dt,'ma_q'] = df.loc[(df.ma_q != 0) & (df.data_time%10000 == zeroInd.iloc[i]%10000)]['ma_q'].mean()
            cor_df.loc[cor_df['data_time'] == dt, 'correction'] = 1
    
    cor_df['data_time'] = cor_df['data_time'].astype('str')
    insertDB(cor_df, 'flowdata')
    
    cor_df.drop("correction",axis=1, inplace=True)
    cor_df.drop("ma_pcode",axis=1, inplace=True)
    result = cor_df.to_dict('records')

    cor_df.drop("temp", axis=1, inplace=True)
    cor_df.drop("humodity", axis=1, inplace=True)
    cor_df.drop("atmo", axis=1, inplace=True)
    cor_df.drop("floor", axis=1, inplace=True)
    cor_df.drop("hr", axis=1, inplace=True)
    result2 = cor_df.to_dict('records')

    return result, result2

def calStrDate(date):
    list_date = list(date)
    str_month = int(list_date[4]+list_date[5])-1
    if str_month < 1:
        str_month = 12
        list_date[3] = str(int(list_date[3])-1)
    
    list_date[4] = str(str_month//10)
    list_date[5] = str(str_month%10)
    
    start_date = datetime.strptime(''.join(list_date), "%Y%m%d%H%M")

    return start_date
    
def calEndDate(date, monthVal):
    list_date = list(date)
    end_month = int(list_date[4] + list_date[5])+monthVal
    if end_month > 12:
        end_month -= 12
        list_date[3] = str(int(list_date[3])+1)
        
    list_date[5] = str(end_month)
    end_date = datetime.strptime(''.join(list_date), "%Y%m%d%H%M")

    return end_date

def insertDB(df, tb_name):
    engine = create_engine("mysql+pymysql://root:manhattancafe@127.0.0.1:3306/scmsdb011")
    conn = engine.connect()
    df.to_sql(name=tb_name, con=engine, if_exists='append', index=False)