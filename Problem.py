import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import string

browser=webdriver.Edge()
browser.maximize_window()
browser.get('http://m.shqszx.com/preview/762645/?url=http%3A%2F%2Fm.shqszx.com%2Fapp-afstudy%2Fquestion_view.html')
time.sleep(2)
iframe = browser.find_element_by_tag_name('iframe')
browser.switch_to.frame(iframe)
username=browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section[1]/section[2]/section[2]/section[2]/section[1]/section[2]/section[2]/section[1]/section/section/div/section/input')
username.send_keys("13580113806")
userpassword=browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section[1]/section[2]/section[2]/section[2]/section[2]/section[2]/section[2]/section[1]/section/section/div/section/input')
userpassword.send_keys("19880107")
login = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section[1]/section[2]/section[2]/section[2]/section[3]/section[1]/section/section')
login.click()
time.sleep(2)
browser.get('http://m.shqszx.com/preview/762645/?url=http%3A%2F%2Fm.shqszx.com%2Fapp-afstudy%2Fquestion_view.html')

iframe = browser.find_element_by_xpath('/html/body/div/div/div[1]/div/iframe')
browser.switch_to.frame(iframe)
answer = []
tempproblem = ""
for i in range(1614):
    fw = open("题库答案.txt","a")
    flag=0
    pt = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[1]/div[1]').text
    problem = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[1]/div[2]').text
    if tempproblem == problem:#说明重复了
        i-=1
        print(problem,"====>重复")  ##爬标题
        continue
    else:
        print(problem)##爬标题
        fw.write(problem.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "\n")
        # iframe = browser.find_element_by_tag_name('iframe')
        # browser.switch_to.frame(iframe)
        #判断多个选项哪个被选中
        noA = False
        noB = False
        noC = False
        noD = False
        noE = False
        noF = False
        noG = False
        try:
            A = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[1]/input')
            Ac = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[1]/div/label').text
        except:
            noA = True

        try:
            B = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[2]/input')
            Bc = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[2]/div/label').text
        except:
            noB = True

        try:
            C = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[3]/input')
            Cc = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[3]/div/label').text
        except:
            noC = True

        try:
            D = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[4]/input')
            Dc = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[4]/div/label').text
        except:
            noD = True
        try:
            E = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[5]/input')
            Ec =browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[5]/div/label').text
        except:
            noE = True
        try:
            F = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[6]/input')
            Fc =browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[6]/div/label').text
        except:
            noF = True
        try:
            G = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[7]/input')
            Gc =browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[1]/section[2]/section/section[1]/section/section/div/div/div[2]/div/ul/li[7]/div/label').text
        except:
            noG = True

        if noA:
            fw.write("There is no A!!!\n")
        else:
            if A.is_selected():
                print(Ac,"==yes")
                fw.write(Ac.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->yes\n")
                if flag:#判断是否是多选题
                    answer[-1]+=" A"
                else:
                    answer.append('A')
                    flag=1
            else:
                print(Ac,"==no")
                fw.write(Ac.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->no\n")
        if noB:
            fw.write("There is no B!!!\n")
        else:
            if B.is_selected():
                print(Bc, "==yes")
                fw.write(Bc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->yes\n")
                if flag:
                    answer[-1] += " B"
                else:
                    answer.append('B')
                    flag = 1
            else:
                print(Bc,"==no")
                fw.write(Bc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->no\n")
        if noC:
            fw.write("There is no C!!!\n")
        else:
            if C.is_selected():
                print(Cc,"==yes")
                fw.write(Cc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->yes\n")
                if flag:
                    answer[-1] += " C"
                else:
                    answer.append('C')
                    flag = 1
            else:
                print(Cc,"==no")
                fw.write(Cc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->no\n")
        if noD:
            fw.write("There is no D!!!\n")
        else:
            if D.is_selected():
                print(Dc,"==yes")
                fw.write(Dc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->yes\n")
                if flag:
                    answer[-1] += " D"
                else:
                    answer.append('D')
                    flag = 1
            else:
                print(Dc,"==no")
                fw.write(Dc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->no\n")
        if noE:
            fw.write("There is no E!!!\n")
        else:
            if E.is_selected():
                print(Ec,"==yes")
                fw.write(Ec.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->yes\n")
                if flag:
                    answer[-1] += " E"
                else:
                    answer.append('E')
                    flag = 1
            else:
                print(Ec,"==no")
                fw.write(Ec.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->no\n")
        if noF:
            fw.write("There is no F!!!\n")
        else:
            if F.is_selected():
                print(Ec,"==yes")
                fw.write(Fc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->yes\n")
                if flag:
                    answer[-1] += " F"
                else:
                    answer.append('F')
                    flag = 1
            else:
                print(Fc,"==no")
                fw.write(Fc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->no\n")
        if noG:
            fw.write("There is no G!!!\n")
        else:
            if G.is_selected():
                print(Gc,"==yes")
                fw.write(Gc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->yes\n")
                if flag:
                    answer[-1] += " G"
                else:
                    answer.append('G')
                    flag = 1
            else:
                print(Gc,"==no")
                fw.write(Gc.encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8') + "   -->no\n")

        fw.write(answer[-1]+"\n")
        fw.write("\n")
        fw.close()
        tempproblem = problem
        nextproblem = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/section/section/section[2]/section/section/section/section[2]/section[2]/section[2]/section[4]/section[2]/section/section[2]/section[3]/section[1]/section/section')
        nextproblem.click()
        time.sleep(1)
fw = open("题库答案.txt","a")
print("完美运行结束")

