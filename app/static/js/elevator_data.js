var dics = {
    'userEntityName': '特检院',
    'userEntityCode': '111111',
    'locationOfUse': 'sydd',
    'numberOfUse': 'L1',
    'regCode': '12345678901234567890',
};

$(document).ready(function () {
    for (var key in dics){
        $('#'+key).val(dics[key]);
    }
});

function fonfocus(the_object, defaultValue) {
    if (the_object.value == dic[defaultValue][1])
       the_object.value = '';
}

function fblur(the_object, defaultValue) {
    if (the_object.value == '')
       the_object.value = dic[defaultValue][1];
}

$('#new_input').click(function () {
    $('#idCode_cp').val('');
    $('form').submit();
});

$("#pre_ele").click(function(){
    if (sessionStorage.getItem('pre_idCode')){
        $('#idCode_cp').val(sessionStorage.getItem('pre_idCode'));
        $('form').submit();
    }
    else{
        alert("这是第一台，请新录入！");
    }
});

$('#cp_bt').click(function () {
    if ($('#idCode_cp').val() == ""){
        alert("请输入复制的电梯识别码");
    }
    else if ($('#idCode_cp').val().length < 6){
        alert("请输入正确的识别码");
    }
    else if (($('#idCode').val() == "") || ($('#model').val() == "")){
        alert("请先输入录入电梯的识别码和型号，并选择设备名称");
    }
    else{
        $('form').submit();
    }
});

$('#close_bt').click(function () {
    $('#idCode_cp').val('');
});