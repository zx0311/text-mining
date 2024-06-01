
import os
import fitz

# 设置输入文件夹和输出文件夹的路径
input_folder = '/Users/x.zhao/Desktop/ILTA/'
output_folder = '/Users/x.zhao/Desktop/ilta/'

def pdf_to_txt(input_file, output_file):
    doc = fitz.open(input_file)
    num_of_pages = doc.page_count

    full_text = []

    for i in range(num_of_pages):
        page = doc.load_page(i)
        text = page.get_text()
        full_text.append(text)

    full_text_str = '\n'.join(full_text)
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(full_text_str)

def convert_folder_to_txt(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.pdf'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_folder, os.path.splitext(file)[0] + '.txt')
                pdf_to_txt(input_file, output_file)

convert_folder_to_txt(input_folder, output_folder)