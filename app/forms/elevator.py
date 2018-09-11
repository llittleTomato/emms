__author__ = 'sky'

from wtforms import StringField, Form
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from app.models.elevator import ElevatorRoom


class ElevatorInitForm(Form):
    # 对输入的电梯信息进行验证
    sbm = StringField('sbm', validators=[DataRequired('请输入电梯识别码'), Length(max=6)])
    xh = StringField('xh', validators=[DataRequired('请输入电梯型号')])
    sbm_cp = StringField('sbm_cp', validators=[Length(max=6)])

    # 对电梯识别码验证是否存在
    def validate_sbm(self, field):
        if ElevatorRoom.query.filter_by(sbm=field.data).first():
            raise ValidationError('识别码为' + field.data + '的电梯已经存在!')