# 小工具

- common
    - exceptions: 异常处理
    - ftp: FTP上传下载
    - logger: 日志打印
    - mail: 邮件发送
    - retry_decorator: 重试装饰器
    - setqueue: 去重队列，有序去重队列
- db
    - mysql
    - redis
- spider 爬虫基类
    - basespider
    - selenium_spider

### 0.3.6
  ```
  由于新版将会弃用直接传executable_path，更新了 
  service = Service(executable_path=executable_path)
  browser = webdriver.Chrome(service=service, options=chrome_options)
  ```


```shell
# 安装
pip install -i https://pypi.org/simple/ wise-utils

- mac 打包
  python3 -m build
  python3 -m twine upload --repository testpypi dist/*
  python3 -m twine upload --repository pypi dist/*
- win 打包
  python setup.py sdist
  python setup.py install
  twine upload dist/*
```
