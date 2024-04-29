from .NLinear import NLinear_Model
from .GAILinear import GAILinear_model

from .config import Config
from .create_seq import create_seq
from .train import model_train
from .preprocessing import preprocess

import torch
import torch.nn.functional as F
import torch.optim as optim

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

from sklearn.preprocessing import StandardScaler

import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class AIModelService :

    def __init__ (self,place,feature_num) :        
        # 모델 로드를 위한 Config 정의 ==> 데이터 받아오자 
        
        if feature_num < 2:
            directory = "./example/trainedModels/"+place+"/"
        else:
            directory = "./example/trainedModels/"+place+"_cli/"
        
        with open(directory+'latest_train_date.txt', 'r' ) as f:
            lines = f.readlines()  # 파일의 모든 줄을 읽어옵니다.

            # 첫 번째 행의 날짜와 두 번째 행의 버전 값을 분리
            self.saved_date = datetime.strptime(lines[0].strip(), "%Y%m%d%H%M").strftime('%Y-%m-%d %H:%M')
            self.version = float(lines[1].strip()[1:])

        model_list = os.listdir(directory)
        model_list_pt = [file for file in model_list if file.endswith(".pt")]

        final_model = directory+model_list_pt[-1]

        self.configs = Config(240,2160,feature_num,False)
        if feature_num < 2:
            # 시간 + 유량 모델
            self.model = GAILinear_model(self.configs).cuda()
        else:
            # 추가 데이터 학습 모델
            self.model = NLinear_Model(self.configs).cuda()
        
        # 모델 학습 가중치 .pt 모델 load
        self.model.load_state_dict(torch.load(final_model))
        self.model.eval()
        

    def predict(self,pp_data,scaler,latest_date,input_date,end_date,raw_df,latest_df,start_date=0):

        # 전처리 완료 데이터
        last_sequence = pp_data[-self.configs.seq_len:].astype(np.float32)
        # torch 타입으로 변환
        last_sequence = torch.tensor(last_sequence).unsqueeze(0).to(device)
        # 예측 수행
        prediction = self.model(last_sequence).detach().cpu().numpy()
        # 예측 완료 데이터 역정규화
        prediction = scaler.inverse_transform(prediction[:, :, -1])
        
        # input_date보다 크거나 같은 날짜의 유량 데이터 추출 from all data
        totalHour = 0
        input_date = pd.Timestamp(datetime.strptime(str(input_date), "%Y-%m-%d %H:%M:%S"))

        if start_date != 0:
            date_str = str(start_date)  # 시작 날짜 및 시간 문자열
            str_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")  # 문자열을 datetime 객체로 변환
            end_date = datetime.strptime(str(end_date), "%Y-%m-%d %H:%M:%S")
            totalHour = (end_date - input_date).days * 24 - 24

            #print("Month Predict START DATE : ", str_date)
            temp = raw_df[raw_df.index >= pd.to_datetime(str_date, format='%Y-%m-%d %H:%M')]
            real_ma_Q = temp.loc[temp.index < input_date, 'ma_q'].tolist()
            total_list = real_ma_Q.copy()
            input_date = str_date
        else :
            if(end_date != "2300"):
                end_date = datetime.strptime(str(end_date), "%Y-%m-%d %H:%M:%S")
                totalHour = (end_date - input_date).days * 24 + 24

            total_list = []

        prediction_list = prediction[0].tolist()

        max_value = raw_df['ma_q'].max()
        min_value = raw_df['ma_q'].min()
        # 예측값 최대 최소
        max_pred = max(prediction_list)
        min_pred = min(prediction_list)
        mean_pred = sum(prediction_list)/len(prediction_list)
        chLen = len(raw_df[raw_df.index > self.saved_date])

        if(totalHour > 2160):
                totalHour = 2160

        if totalHour > 0:
            for i in range(totalHour):
                total_list.append(prediction_list[i])
        else :
            for i in range(len(prediction_list)):
                total_list.append(prediction_list[i])

        generated_dates = [input_date + timedelta(hours=i) for i in range(0, len(total_list))]
        
        df = pd.DataFrame({"x": generated_dates, "y": total_list, "last_tr_day": self.saved_date, "last_ver": self.version, "chlen": chLen, "js": latest_df[0]['js'], "jsb":latest_df[0]['jsb'], "osb":latest_df[0]['osb'], "osbp":latest_df[0]['osbp'] })

        return df