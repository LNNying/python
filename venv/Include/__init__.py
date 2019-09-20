tuple = ('runoob', 232)
print(tuple[0]) # 以恶搞
message = "这是一个变量"
msg = 'love'
print(msg.upper())
print(message)
list = ['track','123', '343']
print(list[2])
for lists in list:
    print(lists.title())
listss = [12,23,43]
for listsw in listss:
    squre = listsw ** 2
# age = input('你的年龄')
# age = int(age)
# if age >= 20:
#     print("你太大了")
# meddling = ""
# while meddling != '1':
#     meddling = input(message)
#     print(meddling)

def greet_user(value = "lNN"):
    print("Hello" + value)

greet_user()


# 同样用set() 去掉重复值
# 数据 也可用对象数组
# for循环 可以不用指定下标
# input 用于获取用户输入的值
# while 与for 一样 ：不可丢掉
# 函数 关键词 def :不可丢掉
# title()方法为首字母大写
# *top 为空元组 可变的 与前端多参数方法一样
# **user 多参数字典数据
# import 指定文件名 （as 别名）
# from 文件名 import 函数名 （*） 引入全部函数
# from 文件名 import 函数名 as 别名

# class 定义类 不能丢掉：
# 构造方法 def __init__ (self,参数): self 必有
# 实例化 变量名 = 类名
# 继承 Car1(Car)
class Car() :
    def __init__(self, make, model):
        self.make = make
        self.model = model
car = Car('1','2')
print(car.model)

# 输入输出
# rstrip 删除末尾空白
# readlines() 获取行数
# 参数 a 与 w 追加写入
# write() 写入文件
# try :
# except ZeroDivisionError:

# HttpResponseRedirect reverse('模板名'， args()参数) 重置路由
# 模板 在每一个app 文件中都一个templates文件夹 用于存放html文件 在setting配置文件中配置INSTALLED_APPS 添加新建的挨app文件
# render(request,模板名) 加载模板
# 求和 annotate(avg_s=Avg('score'))

# 启动项目
# python manage.py runserver 9000
# 新建app
# python manage.py startapp name
# 同步数据库表
# python manage.py makemigrations
# python manage.py migrate
# 数据迁移
# python manage.py dumpdata [app name] > [json 文件名]

# beautifulsoup 使用方法
# soup = Beautifulsoup(html,'lxml')
# 获取标签
# soup.title 等 可以获取标签里的内容 返回第一个标签
# scoup.title.name 获取标签名称
# scoup.title.attr[''] 获取属性
# scoup.title.string 获取内容
# scoup.p.contents 获取子节点返回列表 或 .children 通过 返回迭代器
# for i,child in enumerate(scoup.p.children)
# scoup.p.descendants 获取子孙节点
# .parent 获取夫节点
# .parents 获取所有父节点
# .next_silblings .previous_siblings 获取兄弟节点
# find_all(name,attrs,recursive,text,**kwargs) 可根据标签名属性内容查找文档

# 数组转化成字符串 ','.join(str(i) for i in 数组)
# 字符串转化为数组 .split(',')
# replace 用于字符串的替换

# 安装 pip3 install beautifulsoup4  pip3 install lxml
# requests 需要安装  pip install requests

# 用HttpResponse 返回json 数据 json.dunmps(data), content_type="application/json" 在network可见接口
# json.dumps 将python对象编码成json字符串
# json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)v
# json.loads 将以编码的json字符串解码成json对象

# 爬接口
# 需要导入
# import requests
# from urllib.parse import urlencode
# from urllib import request

# post
# 1. 封装请求数据
# 2. url 
# 3. 根据页面请求封装headers
# 4. urlencode(uploads).encode('utf-8') 编码数据
# 5. req = request.Request(url, data=data, headers=headers) 发送请求
# reponse = request.urlopen(req)
# print(reponse.read().decode("utf-8"))

# 在往文件写内容的时候，如果出现编码问题 可以open('myJS', 'w+', encoding='utf-8')

# 内置chrome插件爬虫
# 安装chromedriver  需要在chrome下拷贝一份以及在python36 下 路径为 print(sys.path) 可得

# 常用查找元素
# find_element_by_id # ID
# find_elements_by_class_name # class
# find_elements_by_tag_name # 标签名
# find_elements_by_name # name
# find_elements_by_link_text # a标签中的text查找（精确匹配）
# find_elements_by_partial_link_text #a标签中的text查找（部分匹配即可）
# find_elements_by_css_selector # css选择器查找
# find_elements_by_xpath # find_elements_by_xpath("//input")，请翻阅文档

#driver = webdriver.Chrome() 获取浏览器本地驱动
#driver.get(路径) 打开网页地址
# driver.page_source 获取网页代码
# 1.通过上面查找元素
# 2.By -- find_element(By.ID,'a') 获取元素 多元素elements
# driver.execute_script() 执行JavaScript
# driver.implicitly_wait(10) 等待时间 隐式 未发现元素就等待 ，超出等待时间为发现 就抛出异常

# 显示等待 见 网页
# WebDriverWait(driver,5)是实例化WebDriverWait类，等待是显示等待，时间是5秒
# .until是实例化的类调用类的方法
# expected_conditions是个模块.py,后面的.visibility_of_element_located是模块调用他的各个方法

# driver.back()/forward() 前进后退
# driver.add_cookies/.get_cookies/.delete_all_cookies  操作cookie
# .send_keys() 模拟输入框输入值
# .click() 模拟按钮点击
# .get_attribute('class') 获取属性
# .text 获取文本
# .id/.location/tag_name/.size  获取id/位置/标签名/宽高
# driver.close() 关闭网页

# impot  time   time.sleep() 睡眠秒数

# 异常 TimeoutException NoSuchElementException 不存在元素

# 从A跳转到B页面需要重定向 driver.switch_to_window(driver.window_handles[1])

# requsets 中Session .get /.post 请求页面 self.session.post(self.login_url, data=request_obj, headers=self.HEADERS, timeout=5) 通过close() 关闭
# 通过 requests.utils.dict_from_cookiejar(self.session.cookies) 获取登录的cookie值
# utils.dict_from_cookiejar cookie形式转变为字典形式
# utils.cookiejar_from_dict 字典形式转化为cookie形式 requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)

# not 相当于! if not x: / if x is not none: / if nor x is none:  最好用第二种  第一种必须了解空元组，{}等无影响

# 正则匹配获取内容
# dome = re.findall(r"/data_files.*?'",str)