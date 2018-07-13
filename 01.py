# 和尚吃馒头(中国古题)
# 大和尚每人吃4个，小和尚4人吃1个。有大小和尚100人，共吃了100个馒头。大、小和尚各几人？各吃 多少馒头？
#coding:utf-8
def HSMT():
    XH=0
    for DH in range(1,101):
        XH=100-DH
        if DH*4+XH/4==100 and int(XH/4)==XH/4:
            return('大和尚有'+str(DH)+'人，小和尚有'+str(XH)+'人时，满足条件！')

def XiWan():
#公鸡每只值5元， 母鸡每只值3元，小鸡每三只值1元。现在用100元钱买100只鸡。问这100只鸡中，公鸡、母鸡、小鸡各有多少只？
    for g in range(1,101):
        x=0
        for m in range(1,101):
            x=100-m-g
            if g*5+3*m+1/3*x==100 and g+m+x==100:
                return('公鸡:'+str(g)+'只，母鸡:'+str(m)+'只，小鸡:'+str(x)+'只')

def lsdd():
# 有垛厚五尺（旧制长度单位，1尺=10寸）的墙壁， 大小两只老鼠同时从墙的两面，沿一直线相对打洞。大鼠第一天打进1尺，以后每天的进度为前一天的2倍；小鼠第一天也打进1尺，以后每天的进度是前一天的一半。它们几天可以相遇？相遇时各打进了多少？\
    bigl=10
    smaill=10
    print('===第1天，大老鼠打进了'+str(bigl)+',小老鼠打进了'+str(smaill))
    for bigmouse in range(2,100):
        bigl=1
        bigl=bigl+(bigmouse-1)*20
        smaill=smaill+1/(smaill*2)
        print('===第'+str(bigmouse)+'天，大老鼠打进了'+str(bigl)+',小老鼠打进了'+str(smaill))
        if bigl+smaill==50:
            return ('它们'+str(bigmouse)+'天可以相遇,相遇时大老鼠打进了'+str(bigl)+',小老鼠打进了'+str(smaill))

print(lsdd())