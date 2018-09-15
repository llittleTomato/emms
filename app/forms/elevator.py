__author__ = 'sky'

from wtforms import StringField, Form
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from app.models.elevator import ElevatorRoom


class ElevatorInitForm(Form):
    # 对输入的电梯信息进行验证
    idCode = StringField('idCode', validators=[DataRequired('请输入电梯识别码'), Length(max=6)])
    model = StringField('model', validators=[DataRequired('请输入电梯型号')])
    idCode_cp = StringField('idCode_cp', validators=[Length(max=6)])

    # 对电梯识别码验证是否存在
    def validate_idCode(self, field):
        if ElevatorRoom.query.filter_by(idCode=field.data).first():
            raise ValidationError('识别码为' + field.data + '的电梯已经存在!')