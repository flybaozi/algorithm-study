s = "aabb"
s.capitalize()  # 首字母大写
s.upper()  # 全部大写
s.lower()  # 全部小写
s.swapcase()  # 大小写翻转
s.title()  # 多词组首字母大写
s.center()  # 总长度居中  可加填充物例如 #

s.find()  # 找不到返回-1
s.index()  # 找不到抛出异常
s.strip()  # 去掉空格
s.strip('*@@')  # 删头去尾  字符串中间不能处理
s.count('')  # 数有多少个字符

s.split()
# 分割 一分为二

# format
s = '我{},你好{}'.format('18', 36)

s.replace()  # 默认全部替换  第三个参数控制替换的变量

s = "abcdefg"
s10 = s[0:5:2]
# 首 尾 步长
