var dic = {
    'sydwmc': ['#sydw', '特检院'],
    'sydwdm': ['#sydwdm', '111111'],
    'sbm': ['#sbm', '111111'],
    'sydd': ['#sydd', 'sydd'],
    'sybh': ['#sybh', 'L1'],
    'zcdm': ['#zcdm', '12345678901234567890'],
    'xh': ['#xh', 'HD'],
    'ccbh': ['#ccbh'],

};

$(document).ready(function () {
    $(dic['sydwmc'][0]).val(dic['sydw'][1])

});

$(dic['sydw'][0]).click(function () {
   if (this.value === dic['sydw'][1])
       this.value = ''
});

$(dic['sydw'][0]).blur(function () {
    if (this.value === '')
        this.value = dic['sydw'][1]
});
