import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 370558433 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = proportions_ztest(count = [x_success,y_success], nobs = [x_cnt,y_cnt], alternative='larger')
    ans = True if pval < 0.9 else False
    return ans # Ваш ответ, True или False
