// 电梯数据初始值
var dics = {
    'userEntityName': '特检院',
    'userEntityCode': '111111',
    'locationOfUse': 'sydd',
    'numberOfUse': 'L1',
    'regCode': '123456789012345678',
};

function fonfocus(the_object, defaultValue) {
    if (the_object.value == dic[defaultValue][1])
       the_object.value = '';
}

function fblur(the_object, defaultValue) {
    if (the_object.value == '')
       the_object.value = dic[defaultValue][1];
}

