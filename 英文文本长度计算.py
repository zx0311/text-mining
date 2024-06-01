import os
import csv

# 设置包含文本文件的目录路径
directory_path = '/Users/x.zhao/Desktop/ilta-txt/'

# 确保只处理文本文件，这里假设所有.txt文件都是我们要处理的文件
file_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith('.txt')]

# 创建CSV文件并写入标题行
csv_file_path = os.path.join(directory_path, 'word_counts.csv')
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['文件名', '词数'])  # 写入标题行

    # 循环读取每个文件
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            # 读取文件内容并转换为小写
            data = f.read().lower()
            # 使用空格分割文本以计算词数，这里假设词之间由空格分隔
            words = data.split()
            # 计算词数
            word_count = len(words)

            # 从文件路径中提取文件名
            file_name = os.path.basename(file_path)

            # 将结果写入CSV文件
            csvwriter.writerow([file_name, word_count])