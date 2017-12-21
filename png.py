#coding:utf-8
import os
import time

def nsfile(s):
    b = os.path.exists("C:\\Users\\jiaotao\\Desktop\\text\\")
    if b:
        print("文件夹已存在")
    else:
        os.mkdir("C:\\Users\\jiaotao\\Desktop\\text\\")

    for i in range(1,s+1):
        localtime = time.strftime("%Y%m%d-%H%M%S",time.localtime())
        filename = "C:\\Users\\jiaotao\\Desktop\\text\\"+localtime+".txt"
        f = open(filename,'ab')
        testnote = 'hello world!'
        f.write(testnote.encode("utf-8"))
        f.close()
        print("file"+" "+str(i)+":"+str(localtime)+".txt")
        time.sleep(1)
    print("ALL Down")
    time.sleep(1)

if __name__ == '__main__':
    s = int(input("需要生成的文件数：\n"))
    nsfile(s)
