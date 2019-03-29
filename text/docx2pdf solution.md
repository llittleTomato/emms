1.使用libreoffice，将docx文件转换为pdf文件，转换时间较长，代码如下。
```
    import subprocess
    # 在终端可以执行以下命令，进行文件转化
    # libreoffice --convert-to pdf elevator_room.docx
    # 在python中
    output = subprocess.check_output(['libreoffice', '--convert-to', 'pdf', 'app/static/reportpdf/test.docx', '--outdir', 'app/static/reportpdf/'])
```
此外安装完libreoffice后，需要有JVM环境
是否有此环境，可用指令查看，若没有，根据提示安装即可
```
    java --version
```

2.用纯python代码转化pdf文件，速度相差不大，暂用第一种方式。