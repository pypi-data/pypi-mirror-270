<!--
 * @Description: aka.zhp
 * @Version: 0.0.1
 * @Author: aka.zhp
 * @Date: 2024-01-04 23:38:05
 * @LastEditTime: 2024-04-23 10:43:14
-->
## 项目说明

我的NLP瑞士军刀，含各种趁手常用工具。

## 功能清单

- [x] 日志
- [x] 计时
- [x] 网页搜索(用于RAG)
- [x] 抽取器
- [x] 评测器
- [ ] 消息工具
- [x] 数据库Helper
- [x] 算法服务模版

## 安装与部署
### 在线安装

```shell
pip install nlpknife
```
### 源码安装

```shell
python setup.py install
```

要求:setuptools=58.2.0


## FAQ

**Q:**  ModuleNotFoundError: No module named 'zope.event'

**A:**
```
pip3 install --force-reinstall zope.event
```