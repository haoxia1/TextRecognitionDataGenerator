inPath = 'vocab_AND_zipin_AND_gbk_PLUS_gb2312.txt'
outPath = 'vocab_AND_zipin_AND_gbk_PLUS_gb2312_column.txt'

# 将inPath的txt文件（单行）读入然后转为单列（即每行一个汉字）
def convert_to_single_column(inPath, outPath):
    try:
        # 读取txt文件内容
        with open(inPath, 'r', encoding='utf-8') as inFile:
            content = inFile.read()

        # 去除文本中的空格和换行符，并将每个汉字放入列表
        characters = [char for char in content if char != ' ' and char != '\n']

        # 将单列汉字写入新的txt文件
        with open(outPath, 'w', encoding='utf-8') as outFile:
            for char in characters:
                outFile.write(char + '\n')

        print(f"成功将{inPath}的内容转换为单列，保存在{outPath}中。")
    except Exception as e:
        print(f"出现错误：{e}")


convert_to_single_column(inPath, outPath)
