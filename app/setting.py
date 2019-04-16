import os

# 每页显示的条数
PER_PAGE = 15

# 获取当前项目的绝对路径
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 保存报告基础文件夹
DOCXFILE_DIR = os.path.join(BASE_DIR, 'static/reportdocx')
