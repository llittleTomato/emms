#### 1.flask-wtf 的目的
Flask-WTF（http://pythonhosted.org/Flask-WTF/）扩展可以把处理 Web 表单的过程变成一种愉悦的体验。
这个扩展对独立的 WTForms（http://wtforms.simplecodes.com）包进行了包装，方便集成到 Flask 程序中。

#### 2.跨站请求伪造保护
Flask-WTF 使用这个密钥生成加密令牌，
再用令牌验证请求中表单数据的真伪。
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hard to guess string'

SECRET_KEY 配置变量是通用密钥，
可在 Flask 和多个第三方扩展中使用。

#### 3.表单结构
使用 Flask-WTF 时，每个 Web 表单都由一个继承自 Form 的类表示。
这个类定义表单中的一组字段，每个字段都用对象表示。
字段对象可附属一个或多个验证函数。验证函数用来验证用户提交的输入值是否符合要求。
表单类只需将表单的字段定义为类属性即可。

一个简单的表单类
    
    from flask_wtf import FlaskForm  # 0.13开始不推荐原书的Form
    from wtforms import StringField, SubmitField
    from wtforms.validators import DataRequired  # 原书是Required，官网最新示例为DataRequired
 
    class NameForm(Form):
        name = StringField('What is your name?', validators=[DataRequired()])
        submit = SubmitField('Submit')

