__author__ = 'sky'

from sqlalchemy import Column, String, Integer, Float, Date
from app.models.base import Base
from app.models.elevatorBasic import ElevatorBasic, ElevatorRoomMachine


class ElevatorRoom(ElevatorBasic, ElevatorRoomMachine):
    __tablename__ = 'elevator_room'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 数据编号


class ElevatorNoRoom(ElevatorBasic):
    __tablename__ = 'elevator_no_room'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 数据编号


class Escalator(ElevatorBasic):
    __tablename__ = 'escalator'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 数据编号


class PassengerConveyor(ElevatorBasic):
    __tablename__ = 'passenger_conveyor'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 数据编号


class DumbWaiter(ElevatorBasic):
    __tablename__ = 'dumb_waiter'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 数据编号


def lift_class_choose(deviceName):
    if deviceName == '曳引驱动乘客电梯':
        elevator = ElevatorRoom()
        return elevator
    if deviceName == '曳引驱动乘客电梯(无机房)':
        elevator = ElevatorNoRoom()
        return elevator
    if deviceName == '自动扶梯':
        elevator = Escalator()
        return elevator
    if deviceName == '自动人行道':
        elevator = PassengerConveyor()
        return elevator
    if deviceName == '杂物电梯':
        elevator = DumbWaiter()
        return elevator


def lift_html_choose(deviceName):
    if deviceName == '曳引驱动乘客电梯':
        html_name = ['elevatorRoom_basic.html', 'elevatorRoom_machine.html']
        return html_name

    if deviceName == '曳引驱动乘客电梯(无机房)':
        html_name = ['elevatorNoRoom_basic.html', 'elevatorNoRoom_machine.html']
        return html_name

    if deviceName == '自动扶梯':
        html_name = ['elevatorRoom_basic.html', 'elevatorRoom_machine.html']
        return html_name

    if deviceName == '自动人行道':
        html_name = ['elevatorRoom_basic.html', 'elevatorRoom_machine.html']
        return html_name

    if deviceName == '杂物电梯':
        html_name = ['elevatorRoom_basic.html', 'elevatorRoom_machine.html']
        return html_name
