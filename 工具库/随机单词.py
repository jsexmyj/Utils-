import os
import random
import pandas as pd

# 如果工作目录不正确，可以通过以下代码切换到脚本所在目录
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
# print("切换后的工作目录:", os.getcwd())
df = pd.read_excel('单词表.xlsx')
words = df['单词'].tolist()

def get_random(words,num):
    return random.sample(words,num)

num = int(input('请输入要随机生成的数量：'))
# print(pd.read_excel('单词表.xlsx'))
print(get_random(words,num))