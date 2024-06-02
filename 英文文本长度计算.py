import os
import csv
import re
from collections import Counter
from nltk.corpus import stopwords

# 设置包含文本文件的目录路径
directory_path = '/Users/x.zhao/Desktop/ilta-txt/'

# 获取nltk的英文停用词列表
stop_words = set(stopwords.words('english'))

# 准备CSV文件写入
csv_file_path = os.path.join(directory_path, 'token_type_counts_with_regex.csv')

# 初始化CSV文件和写入标题
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['文件名', 'Tokens', 'Types'])

    # 循环处理目录中的每个.txt文件
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                # 使用正则表达式匹配单词tokens
                tokens = re.findall(r'\b\w+\b', text)
                # 过滤停用词
                filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words]
                # 计算types
                types = len(set(filtered_tokens))
                # 更新tokens计数
                token_counts = Counter(filtered_tokens)

                # 写入文件名、tokens数量和types数量
                csvwriter.writerow([file_name, len(filtered_tokens), types])

print("去除停用词并使用正则表达式之后的文本tokens和types计数已写入CSV文件。")