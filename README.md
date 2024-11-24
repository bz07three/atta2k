# atta2k
:::
本项目基于whoisavicii师傅的Masscan2Httpx2Nuclei-Xray项目上开发（原项目地址：https://github.com/whoisavicii/Masscan2Httpx2Nuclei-Xray）
实现功能：
masscan全端口扫描==>httpx探测WEB服务==>nuclei&xray漏洞扫描
新增功能：
爬取所有接口将流量导入xray，最大限度发挥xray
代理功能，基于deadpool项目，隐匿流量
钉钉提醒，任务完成钉钉会进行提醒
优化项目输出
:::
## 环境准备
linux服务器
masscan（添加至环境变量）
httpx
nuclei
xray
rad（需要安装chrome）
