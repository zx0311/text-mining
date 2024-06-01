import os
import csv
import re
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import download

# 设置包含文本文件的目录路径
directory_path = '/Users/x.zhao/Desktop/ilta-txt/'

# 准备停用词列表和词形还原器
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# 初始化一个变量来存储所有文档的内容
all_text = ""

# 读取所有文档的内容
for file_path in [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith('.txt')]:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        # 分词并进行词性标注
        tokens = word_tokenize(text)
        pos_tags = nltk.pos_tag(tokens)

        # 词形还原
        lemmatized = []
        for token, tag in pos_tags:
            if tag.startswith('VB'):  # Verb
                lemmatized.append(lemmatizer.lemmatize(token, pos='v'))
            elif tag.startswith('JJ'):  # Adjective
                lemmatized.append(lemmatizer.lemmatize(token, pos='a'))
            elif tag.startswith('NN'):  # Noun
                lemmatized.append(lemmatizer.lemmatize(token, pos='n'))
            else:
                lemmatized.append(lemmatizer.lemmatize(token))

        # 合并词形还原后的词
        all_text += ' '.join(lemmatized) + ' '

# 使用正则表达式分割文本以计算词数
words = re.findall(r'\b\w+\b', all_text)

# 去除停用词
filtered_words = [word for word in words if word not in stop_words]

# 计算词频
word_counts = Counter(filtered_words)

# 获取前50个高频词及其频率
top_50_words = word_counts.most_common(60)

# 创建CSV文件并写入数据
csv_file_path = os.path.join(directory_path, 'top_50_lemmatized_words.csv')
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # 写入标题行
    csvwriter.writerow(['Rank', 'Word', 'Frequency'])

    # 写入前50个高频词及其频率
    for i, (word, count) in enumerate(top_50_words, start=1):
        csvwriter.writerow([i, word, count])

print("高频词及其词频（词形还原后）已写入CSV文件。")
