# scrapy-proxy-
爬取西刺代理网站的高匿代理ip并存储到mysql数据库为之后爬虫使用。 地址：http://www.xicidaili.com/nn/
#我的运行环境
* linux
* virtualenv
* python 2.7.5
* scrapy1.0.3  


# 依赖条件
## 1. 安装mysql的python扩展
```
(python2.7-env01) [root@vagrant-centos65 crawler]#pip install mysql-python
```
安装完成后还需执行：

```
(python2.7-env01) [root@vagrant-centos65 crawler]# find / -name 'libmysqlclient.so.18' -print
/alidata/server/mysql/lib/libmysqlclient.so.18
```
设置软连接：

```
(python2.7-env01) [root@vagrant-centos65 crawler]# ln -s /alidata/server/mysql/lib/libmysqlclient.so.18   /usr/lib/libmysqlclient.so.18
```
重启系统的动态链接库：

```
# ldconfig
```
## 2. mysql导入dy_proxy.sql文件

# 执行爬虫
## 开发阶段
debug模式执行
```
(python2.7-env01) [root@vagrant-centos65 crawler]#scrapy  crawl  xici   -s LOG_LEVEL=DEBUG
```
## 生产环境
实际运行爬虫需考虑到爬虫可能遇到意外（网络故障等）而中断，暂停爬虫并与稍后恢复而不是重新开始会很有用，scrapy内置了对暂停与恢复爬取的支持，要开启该功能，只需要定义保存爬虫当前状态的目录：

```
(python2.7-env01) [root@vagrant-centos65 crawler]# scrapy  crawl  xici  -s JOBDIR=status/xici
```
# 排错
1. 使用scrapy   shell 排错
2. 查看scrapy  log日志


