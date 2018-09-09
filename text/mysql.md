###MySQL迁移数据库方法一（mysqldump）

 #### 一、导出导入所有数据库的数据

1.导出

    mysqldump -u root -p123456 --all-databases > all.sql

2.导入

    mysql -u root -p123456 < "D:\MySQL 5.5\bin\all.sql"

#### 二、导出导入只指定数据库的数据

1.导出

    mysqldump -u root -p123456 test > test.sql

2.导入

    mysql -u root -p123456 test < "D:\MySQL 5.5\bin\test.sql"

#### 三、导入导出指定表的数据

1.导出

    mysqldump -u root -p123456 scistock calcgsdata_once > calcgsdata_once.sql

2.导入

    mysql -u root -p123456 scistock < "D:\MySQL 5.5\bin\calcgsdata_once.sql"

#### 四、导入某张表的数据还可以用的方法（source）

1. 登录MySQL

2. use dbname

3. source D:\\MySQL 5.5\\bin\\calcgsdata_once.sql;

###MySQL迁移数据库方法二

最近有个需求，要把机器a上的一个数据库迁移到机器b上，这个数据库的数据有100多个G。所以，果断抛弃用mysqldump的方法来迁移。这时候想到的就是直接复制文件来做迁移。 
于是我按照网上的说法，步骤如下： 

1.把机器b的mysql停掉。
 
2.把机器a上要迁移的库的整个目录复制到机器b的mysql data目录下。 

3.修改目录权限为700，修改文件权限为660，并修改他们的所属用户和所属组为mysql。 

4.再启动机器b的mysql。 

操作完成后，我进入机器b的mysql，此时，执行show databases可以看到要迁移的数据库。然后执行use databasename,再执行show tables，也可以看到所有的表。但是问题来了，我执行select * from table limit 10，这时候却报错了，提示表不存在。 
所以，我们大致可以指定mysql的工作机制，show databases和show tables时，mysql其实是去目录下扫描，但执行select这些操作的时候，mysql优化器会去information_schema.TABLES 这个表里面获取信息。由于我们是直接复制文件过去，所以，这个表里面是没有信息的，所以就会提示表不存在。 
知道了这点之后，我修改了上述步骤： 

1.在机器b上，创建需要的database 

2.在该database建好所有的表。 

3.把机器b的mysql停掉。 

4.到机器b上，刚才建的那个数据库的目录下，把所有的(.ibd)文件删除掉。 

5.把机器a上，对应数据库目录下所有的(.ibd)文件复制到机器b上，修改文件的权限。 

6.启动机器b的mysql。 

这时候再连接上b的mysql，就可以看到所有的数据了。

　　