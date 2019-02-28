#coding=utf-8
import time,subprocess,sys

class TimeoutError(Exception):
    pass


def command(cmd, timeout=60):
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    t_beginning = time.time()
    seconds_passed = 0
    while True:
        if p.poll() is not None:
            break
        seconds_passed = time.time() - t_beginning
        if timeout and seconds_passed > timeout:
            p.terminate()
            raise TimeoutError(cmd, timeout)
        time.sleep(0.1) 
    return p.stdout.read()

def getIP():
    with open('ip.txt','r') as f:
        res = [i.strip() for i in f.readlines()]
    return res

if __name__ == '__main__':
    res = getIP()
    for index,ip in enumerate(res):
        cmd = 'python dbscan.py -t 1000 '+ip
        print str(index)+'   '+cmd
        try:
            print command(cmd,120)
        except Exception,e:
            pass
