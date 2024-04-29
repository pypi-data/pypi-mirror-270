import numpy as np

def create_seq(features, look_back, look_ahead) :
    """
    모델 학습을 위한 Sequence를 생성하는 함수
    """
    X, y = [], []
    for i in range(len(features) - look_back - look_ahead + 1) :
        X.append(features[i : i + look_back])
        # 모든 항목을 target으로
        y.append(features[i + look_back : i + look_back + look_ahead])
    
    return np.array(X), np.array(y)

