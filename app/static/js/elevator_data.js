var dic = {
    'sydwmc': ['#sydwmc', '特检院'],
    'sydwdm': ['#sydwdm', '111111'],
    'sbm': ['#sbm', '111111'],
    'sydd': ['#sydd', 'sydd'],
    'sybh': ['#sybh', 'L1'],
    'zcdm': ['#zcdm', '12345678901234567890'],
    'xh': ['#xh', 'HD'],
    'ccbh': ['#ccbh'],

};

$(document).ready(function () {
    $(dic['sydwmc'][0]).val(dic['sydwmc'][1])

});


function fonfocus(the_object, defaultValue) {
    if (the_object.value == dic[defaultValue][1])
       the_object.value = '';
}

function fblur(the_object, defaultValue) {
    if (the_object.value == '')
       the_object.value = dic[defaultValue][1];
}