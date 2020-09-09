#### 基于STM32的嵌入式智能家居远程控制系统说明文档

##### 软件安装

 - 安装Visual Studio Code运行《代码》文件夹下AISmartHome_SWIFT文件的代码。详细安装教程参照链接：[https://code.visualstudio.com/download]
 - 安装《代码》文件夹内的MicroPython File Uploader.exe，运行MQTT文件的代码。

##### 环境配置

- 安装Python 3.0 以上的版本，详细安装教程参照链接：[https://www.python.org/downloads/]

- 成功安装Python后再安装Django，详细安装教程参照链接：[https://www.djangoproject.com/download/]

##### 运行代码

1. 打开MicroPython File Uploader软件，将MQTT文件夹内的*.py文件都导入进去，然后点击“send”发送，程序运行成功后进入下一步。

2. 打开Visual Studio Code，首先在终端输入命令，查看电脑此时的IP地址，打开科大讯飞的网址后，输入账号密码，将电脑的IP地址添加进科大讯飞语音识别的白名单当中。

3. 在Visual Studio Code终端中，输入命令python manage.py runserver，进入相应网址，启动项目完成。


