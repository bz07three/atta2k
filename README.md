# atta2k

  本项目基于whoisavicii师傅的Masscan2Httpx2Nuclei-Xray项目上开发
  
  (原项目地址：https://github.com/whoisavicii/Masscan2Httpx2Nuclei-Xray)

## 实现功能：

  masscan全端口扫描==>httpx探测WEB服务==>nuclei&xray漏洞扫描\n

  新增功能：

  爬取所有接口将流量导入xray，最大限度发挥xray

  代理功能，基于deadpool项目，隐匿流量

  钉钉提醒，任务完成钉钉会进行提醒

  优化项目输出

## 环境准备

  linux服务器

  masscan（添加至环境变量）

  httpx

  nuclei

  xray

  rad（需要安装chrome）
## 使用方法

  参数：
  
  ```
  -i    指定目标ip集合，如-i ip.txt
  -p    指定扫描端口，如 -p 80 或 -p 1-1000
  -rate 指定扫描速率，如 -rate 1000或-rate 10000
  -n    指定项目名称，如 -n test
  ```
  
  1，配置代理和钉钉webhook，将目标ip放入ip.txt
  2，启动xray
  ```
  cd xray
  chmod +x start.sh 
  sh start.sh test
  ```
  ![image](https://github.com/user-attachments/assets/67d0d638-3884-474c-88e5-8c319da1b1c8)

  3，启动attack.py
  
  ```
  python3 attack.py -i ip.txt -p 1-1000 -rate 2000 -n test
  ```
  ![image](https://github.com/user-attachments/assets/364f040a-d04d-414a-873f-ede4e7237b97)

  
  4，结束后结果放在result目录，钉钉会有提醒
  
  ![9bec8ea84db4efe8df5e97cd5f5d302](https://github.com/user-attachments/assets/2e9f1236-44bc-4ea3-8e65-b837a6eb4a85)



