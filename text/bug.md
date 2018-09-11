##### 1. bootstrap-datepicker插件bug
（1）使用bootstrap-datepicker时必须使用jQuery2.0版本，bootstrap3.0以上版本与jQuery3.0以上版本冲突，导致时间选择框无法弹出

（2）bootstrap-datepicker是在jQuery2.0下开发，因此使用时必须引用jQuery2.0的版本

##### 2. 出现错误ModuleNotFoundError: No module named 'flask_sqlalchemy'
解决方法：

设置SQLALCHEMY_TRACK_MODIFICATIONS 为True或False

在flask_sqlalchemy的__init__.py文件中找到

```
   track_modifications = app.config.setdefault(
          'SQLALCHEMY_TRACK_MODIFICATIONS', True #这里，一开始是None需要改变为True or Flase
   )
```

改动后保存，退出虚拟环境，重新进入运行即可修复。
