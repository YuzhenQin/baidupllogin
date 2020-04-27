# -*- coding: UTF-8 -*-
import requests

def dvgen():
    os.system('.\\nodejs\\node.exe .\\dvgen.js | .\\dvsave.exe')
    time.sleep(0.1)
    dv = open('.\\temp\\dv.txt','r')
    ret = dv.read()
    dv.close()
    return ret
def gidgen():
    os.system('.\\nodejs\\node.exe .\\gidgen.js | .\\gidsave.exe')
    time.sleep(0.1)
    gid = open('.\\temp\\gid.txt','r')
    ret = gid.read()
    gid.close()
    return ret

def login(username,password,proxy):
    dv = dvgen()
    gid = gidgen()
    proxies = {'http':proxy}
    r1 = requests.get('https://www.baidu.com',headers=headers,proxies=proxies)#获取BaiduID（cookie中）
    r2 = requests.get('https://passport.baidu.com/v2/api/?getapi&tpl=tb&apiver=v3&tt='+time.time()+'&class=login&gid='+str(gid)+'&loginversion=\
    v4&logintype=dialogLogin&traceid=&callback=',headers=headers,cookies=r1.cookies,proxies=proxies)#获取token
    token = r2.json
    token = token["data"]["token"]
    r3 = requests.get('https://passport.baidu.com/v2/api/?logincheck&token='+str(token)+'&tpl=tb&apiver=v3&tt='+time.time()+'&sub_source=\
    leadsetpwd&username='+username+'&loginversion=v4&dv='+dv+'&traceid=&callback=',headers=headers,cookies=r2.cookies,proxies=proxies)#模拟登陆时失去焦点
    loginret = r3.json
    verify = ''
    if loginret["data"]["codeString"] == '':
        nothing()#无验证码
    else:
        nothing()#有验证码 没写
    #r4 = requests.get('https://passport.baidu.com/v2/getpublickey/?token='+token+'&tpl=tb&apiver=v3&tt='+time.time()+'&gid='+rsagid+'&loginversion=v4\
    #&traceid='+rsatrace+'&callback=',headers=headers,cookies=r3.cookies,proxies=proxies)#获取RSA密钥
    #r5 = requests.get('https://passport.baidu.com/viewlog?ak=1e3f2dd1c81f2075171a547893391274&as=2283e880&fs='+use_js.fsgen+'&v='+v+'&callback=\
    #',headers=headers,cookies=r4.cookies,proxies=proxies)#提交轨迹                                                                                             这些居然是扯蛋的，我枯了
    r4 = requests.get('https://passport.baidu.com/v2/api/?login&staticpage=http://www.baidu.com/cache/user/html/v3Jump.html&charset=UTF-8\
    &token='+token+'&tpl=mn&apiver=v3&tt='+time.time()+'&codestring=&isPhone=false&safeflg=0&u=http://www.baidu.com&quick_user=0&usernamelogin=1&\
    splogin=rate&username='+username+'&password='+password+'&verifycode='+verify+'&mem_pass=on&ppui_logintime=5000&callback=',headers=headers,cookies=r3.cookies,proxies=proxies)
    ret = []
    ret.append(r4.cookies)
    ret.append(r4.json)
    return ret