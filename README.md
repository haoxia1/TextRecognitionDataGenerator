fork from [link](https://github.com/Belval/TextRecognitionDataGenerator)

生成100*num_char个字典为trdg/vocab_AND_zipin_AND_gbk_PLUS_gb2312.txt，ttf选自trdg/fonts/cn，背景选自trdg/images的字体

Inplement process:

two method: 
1. (5,5,5,5) 无裁剪 line 297
2. (10,10,10,10) 裁剪(字更小); 
为了命名一致，需要修改data_generator line 259 TODO str(index) += 80w-1

first:
设置run.py各参数
注释run.py line 503, 505
注释data_generator.py line 260
修改run.py line 297(5,5,5,5) 300(False)
python run.py 

second:
取消注释以上
修改run.py line 503 505 297(10,10,10,10) 300(True)
注释data_generator.py line 259
python run.py
> 总共2253403字符 2253403/(200*16802) = 67%
> label.txt是齐全的 图片由于某些ttf没有该字符只有67%
> out image已被移出