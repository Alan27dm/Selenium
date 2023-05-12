优化了导入`Unit`测试类，自动导入测试类
删除了`all_class_name`方法
添加浏览器启动全局配置

用法：
`test_case` 下面存放每一个单独的用例
类名开头大写和文件名一致
baidu.py => Baidu
tencentCompany => TencentCompany

运行单个 `UnitTest`
`cd baiduTest`
then
`python -m test_case.baidu`

or

`python run.py baidu`
```
输出 >>>
modules: ['baidu', 'taobao', 'tencent', 'wangyi']
sys.argv: ['baidu']
Selected module: <class 'test_case.baidu.Baidu'>
test_Baidu (test_case.baidu.Baidu)
Baidu搜索验证 ... ok

----------------------------------------------------------------------
Ran 1 test in 8.154s

OK
```