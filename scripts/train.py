# train.py

from models.model import train_model
from data.dataset import fetch_data

# 데이터셋 준비
train_data = fetch_data('https://example.com/train')
eval_data = fetch_data('https://example.com/eval')

# 모델 훈련
train_model(train_data, eval_data)
