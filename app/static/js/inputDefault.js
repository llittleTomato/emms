var dic = {
    'sydw': ['#sydw', '特检院'],

};

$(document).ready(function () {
    $(dic['sydw'][0]).val(dic['sydw'][1])
});

$(dic['sydw'][0]).click(function () {
   if (this.value === dic['sydw'][1])
       this.value = ''
});

$(dic['sydw'][0]).blur(function () {
    if (this.value === '')
        this.value = dic['sydw'][1]
});
