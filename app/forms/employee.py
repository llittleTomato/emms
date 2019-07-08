__author__ = 'sky'

from wtforms import StringField, Form
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from app.models.elevator import ElevatorRoom


class EmployeeForm(Form):
    # 对人员录入信息和更新信息信息进行验证
    # TODO: 以下内容需修改为对员工录入信息的验证
    idCode = StringField('idCode', validators=[DataRequired('请输入电梯识别码'), Length(max=6)])
    maintenanceContractNumber = StringField('maintenanceContractNumber', validators=[DataRequired('请输入电梯维保合同编号')])
    idCode_cp = StringField('idCode_cp', validators=[Length(max=6)])

    # 对电梯识别码验证是否存在
    def validate_idCode(self, field):
        if ElevatorRoom.query.filter_by(idCode=field.data).first():
            raise ValidationError('识别码为' + field.data + '的电梯已经存在!')

    # 验证输入的被复制电梯是否存在，不存在则报错
    def validate_idCode_cp(self, field):
        if field.data != '':
            if not ElevatorRoom.query.filter_by(idCode=field.data).first():
                raise ValidationError('被复制的电梯不存在!')
