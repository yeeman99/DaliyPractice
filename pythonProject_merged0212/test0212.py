# import os
# # 设置目录和目标文件名
#
# directory = './file'  # 当前目录，替换为你的文件路径
# output_file = 'merged_file01.md'
#
# # 获取所有md文件，并按文件名排序
# md_files = sorted([f for f in os.listdir(directory) if f.endswith('.md')], key=lambda x: int(x.split('.')[0]))
#
# # 合并文件
# with open(output_file, 'w') as outfile:
#     for md_file in md_files:
#         with open(os.path.join(directory, md_file), 'r') as infile:
#             outfile.write(infile.read())
#             outfile.write("\n\n")  # 可选，添加换行作为文件间分隔符
#
# print(f'Files merged into {output_file}')
'''
re 模块是 Python 的标准库之一，提供了对 正则表达式（Regular Expressions） 的支持。
正则表达式是一种强大的模式匹配工具，可以用来在字符串中查找、替换、分割或提取数据。
re 模块允许你使用正则表达式来执行这些操作。
'''
import os
import re

# 设置目录和目标文件名
directory = './file'  # 当前目录，替换为你的文件路径
output_file = 'merged_file02.md'

# 获取所有md文件，并提取文件名中的数字部分排序
def extract_number(filename):
    match = re.search(r'(\d+)', filename)  # 提取文件名中的数字部分
    return int(match.group(1)) if match else float('inf')  # 如果没有找到数字，返回无穷大，确保排到最后

md_files = sorted([f for f in os.listdir(directory) if f.endswith('.md')], key=extract_number)

# 合并文件
with open(output_file, 'w', encoding='utf-8') as outfile:
    for md_file in md_files:
        file_number = extract_number(md_file)  # 获取文件中的数字序号
        outfile.write(f"### 从这行开始是 {file_number} {md_file}\n\n")  # 添加分隔信息
        with open(os.path.join(directory, md_file), 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
            outfile.write("\n\n")  # 可选，添加换行作为文件间分隔符

print(f'Files merged into {output_file}')
