#coding:utf-8
import os
import time
import argparse
import requests
import json

class DingTalk_Base:
    def __init__(self, name):
        self.name = name
        self.__headers = {'Content-Type': 'application/json;charset=utf-8'}
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=XXXXXXXXXX'

    def send_msg(self):
        json_text = {
            "msgtype": "text",
            "text": {
                "content": "目标“{}”扫描已接近尾声，请及时查看".format(self.name)
            },
            "at": {
                "atMobiles": [""],
                "isAtAll": False
            }
        }
        response = requests.post(self.url, json=json_text, headers=self.__headers)
        return response.content

def biaoti():
    splash1 = """
        +----------------------------------+
        | Masscan2Httpx2Nuclei             |
        +----------------------------------+
        | by mbskter &  bzz                |
        +----------------------------------+
    """
    print(splash1)

def args():
    parser = argparse.ArgumentParser(description='Masscan2Httpx2Nuclei')
    parser.add_argument('-i', '--input', help='参考masscan -iL', required=True)
    parser.add_argument('-p', '--port',help='参考masscan -p', required=True)
    parser.add_argument('-rate','--rate', help='参考masscan速率rate', required=True)
    parser.add_argument('-name','--name', help='项目名称', required=True)
    args = parser.parse_args()
    return args

def update():
    splash00 = """
        +----------------------------------+
        | nucle检查更新ing
        +----------------------------------+
    """
    print(splash00)
    os.system('./nuclei/nuclei -update')
    splash03 = """
        +----------------------------------+
        | 检查完毕，开扫
        +----------------------------------+
    """
    print(splash03)


def check_args(args):
    if not os.path.exists(args.input):
        print('ip文件不存在')
        exit()
    if not args.port:
        print('请输入端口参数')
        exit()
    if not args.rate:
        print('请输入扫描速率(例：-rate 2000)')
        exit()
    if not args.name:
        print('请输入项目名称(例：edu)')
        exit()
    return args

def masscan2httpx2nuclei(args):
    args = check_args(args)
    input_file = args.input
    port = args.port
    rate = args.rate
    name=args.name
    dirname="result/{}".format(name)
    try:
        os.makedirs(dirname, exist_ok=True)  # exist_ok=True表示如果目录已存在，不会抛出异常
        print(f"结果输出目录 {dirname} 创建成功。")
    except Exception as e:
        print(f"创建目录时出错：{e}")
    os.system('masscan -iL ' + input_file + ' -p' + port +" --rate "+rate+' -oL result/{}/{}_portscan.txt'.format(name,name))

def masscan2httpx2nuclei_main(args):
    args = check_args(args)
    name = args.name
    portname='result/{}/{}_portscan.txt'.format(name,name)
    portconvert = 'result/{}/{}_portconvert.txt'.format(name,name)
    httpxname='result/{}/{}_httpx_scan.txt'.format(name,name)
    nucleiname='result/{}/{}_nuclei_scan.txt'.format(name,name)
    while True:
        if os.path.exists(portname):
            break
        else:
            time.sleep(1)
    if os.path.getsize(portname) == 0:
        splash3 = """
            +----------------------------------+
            | 无端口开放，程序已退出!
            +----------------------------------+
        """
        print(splash3)
        exit()
    else :
        splash4 = """
            +----------------------------------+
            | Masscan扫描结果解析并调用httpx
            +----------------------------------+
        """
        print(splash4)
        masscanfile = open(portname, "r")
        masscanfile.seek(0)
        for line in masscanfile:
            if line.startswith("#"):
                continue
            if line.startswith("open"):
                line = line.split(" ")
                with open(portconvert, "a") as f:
                    f.write(line[3]+":"+line[2]+"\n")
                    f.close()
        masscanfile.close()
    if os.path.exists(portname):
        os.system('./httpx/httpx -l {} -nc -o {}'.format(portconvert,httpxname))
        splash2 = """
            +----------------------------------+
            | Httpx is done !
            +----------------------------------+
        """
        print(splash2)
    else:
        splash5 = """
            +----------------------------------+
            | 未发现解析后的masscan端口结果
            +----------------------------------+
        """
        print(splash5)
        exit()
    if os.path.getsize(httpxname)!=0:
        os.system('./nuclei/nuclei -l {} -s medium,high,critical -timeout 5 -p socks5://127.0.0.1:10086 -o {}'.format(httpxname,nucleiname))
        os.system('./rad/rad -uf {} -http-proxy 127.0.0.1:7777'.format(httpxname))
    else:
        print("扫描结果未发现http协议")
        exit()
    if os.path.getsize(nucleiname)!=0:
        splash6 = """
            +----------------------------------+
            | 扫描完成。请在结果输出目录查看
            +----------------------------------+
        """
        print(splash6)
    else:
        splash7 = """
            +----------------------------------+
            | nuclei未发现中高危漏洞
            +----------------------------------+
        """
        print(splash7)

    splash8 = """
            +----------------------------------+
            | xray正在扫描，详情请查看xray面板
            +----------------------------------+
        """
    print(splash8)
    dingding = DingTalk_Base(name)
    dingding.send_msg()
    exit()


def main():
    biaoti()
    update()
    masscan2httpx2nuclei(args())
    masscan2httpx2nuclei_main(args())

if __name__ == '__main__':

    main()
    exit()
