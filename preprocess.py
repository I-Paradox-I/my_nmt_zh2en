# from nltk.tokenize import word_tokenize as en_tokenizer
# from transformers import BertTokenizer 
# ch_tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

# en_words = en_tokenizer("To be or not be be, this is a question.")
# ch_words = ch_tokenizer.tokenize("我想要做一个测试，来测测他能不能正常识别中文分词。")

# print(en_words, "\n", ch_words)




import os
import jieba
import nltk

input_dir = '/data2/users/liuyx/Paradox/MY_NMT/data'  # 替换为你的输入目录路径
output_dir = '/data2/users/liuyx/Paradox/MY_NMT/data2'  # 替换为你的输出目录路径

# 创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历输入目录下的所有文件
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith("ch.txt"):  # 仅处理以"ch.txt"结尾的文件
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_dir, file)

            with open(input_file_path, 'r', encoding='utf-8') as input_file, \
                    open(output_file_path, 'w', encoding='utf-8') as output_file:
                for line in input_file:
                    line = line.strip()  # 去除首尾空白字符
                    if line:
                        seg_list = jieba.cut(line)
                        result = " ".join(seg_list)
                        output_file.write(result + '\n')
        if file.endswith("en.txt"):  # 仅处理以 "en.txt" 结尾的文件
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_dir, file)

            with open(input_file_path, 'r', encoding='utf-8') as input_file, \
                    open(output_file_path, 'w', encoding='utf-8') as output_file:
                for line in input_file:
                    line = line.strip()  # 去除首尾空白字符
                    if line:
                        tokens = nltk.word_tokenize(line)
                        result = " ".join(tokens)
                        output_file.write(result + '\n')

