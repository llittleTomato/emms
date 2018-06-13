#### 1.图像设置
    <img src="..." class="img-responsive" alt="响应式图像">
    图像按比例缩放，不超过其父元素的尺寸
    .img-responsive {
        display: block;
        height: auto;
        max-width: 100%;
    }
#### 2.基本的全局显示
Bootstrap 3 使用 body {margin: 0;} 来移除 body 的边距。
    
    body {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;  //字体样式
        font-size: 14px;     //字体大小
        line-height: 1.428571429;  //行高
        color: #333333;   //字体颜色黑色
        background-color: #ffffff;  //白色
    }
##### 3.布局容器
Bootstrap 需要为页面内容和栅格系统包裹一个 .container 容器。
我们提供了两个作此用处的类。注意，由于 padding 等属性的原因，这两种 容器类不能互相嵌套。
.container 类用于固定宽度并支持响应式布局的容器。
   
    <div class="container">
    ...
    </div>
.container-fluid 类用于 100% 宽度，占据全部视口（viewport）的容器。
    
    <div class="container-fluid">
    ...
    </div>
#### 4.表格
为任意 <table> 标签添加 .table 类可以为其赋予基本的样式 — 少量的内补（padding）和水平方向的分隔线。

    基本表格
    <table class="table">
    ...
    </table>
    
    条纹状表格
    通过 .table-striped 类可以给 <tbody> 之内的每一行增加斑马条纹样式。
    <table class="table table-striped">
    ...
    </table>
    
    带边框的表格
    添加 .table-bordered 类为表格和其中的每个单元格增加边框
    <table class="table table-bordered">
    ...
    </table>
    
表格上的鼠标悬停
通过添加 .table-hover 类可以让 <tbody> 中的每一行对鼠标悬停状态作出响应。

    <table class="table table-hover">
    ...
    </table>
    
紧缩表格
通过添加 .table-condensed 类可以让表格更加紧凑，单元格中的内补（padding）均会减半。

    <table class="table table-condensed">
    ...
    </table>    

表格状态
通过这些状态类可以为行或单元格设置颜色。
     
     Class	              描述
    .active  	鼠标悬停在行或单元格上时所设置的颜色
    .success	标识成功或积极的动作
    .info	        标识普通的提示信息或动作
    .warning	标识警告或需要用户注意
    .danger	        标识危险或潜在的带来负面影响的动作
    
    <!-- On rows -->
    <tr class="active">...</tr>
    <tr class="success">...</tr>
    <tr class="warning">...</tr>
    <tr class="danger">...</tr>
    <tr class="info">...</tr>
    
    <!-- On cells (`td` or `th`) -->
    <tr>
      <td class="active">...</td>
      <td class="success">...</td>
      <td class="warning">...</td>
      <td class="danger">...</td>
      <td class="info">...</td>
    </tr>
    
响应式表格
将任何 .table 元素包裹在 .table-responsive 元素内，即可创建响应式表格，其会在小屏幕设备上（小于768px）水平滚动。当屏幕大于 768px 宽度时，水平滚动条消失。
>垂直方向的内容截断

响应式表格使用了 overflow-y: hidden 属性，这样就能将超出表格底部和顶部的内容截断。特别是，也可以截断下拉菜单和其他第三方组件。
    
    <div class="table-responsive">
    <table class="table">
        ...
    </table>
    </div>