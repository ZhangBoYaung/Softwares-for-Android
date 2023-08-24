import random,time
fuhao = ('+','-')
score = 0
def start(st):
    def zhuangshi():
        global n
        print('第{}题'.format(n+1).center(28,'*'))
        st()
        print('\n')
    return zhuangshi

@start 
def suanshu():
    global weight,score,how_long
    
    a = random.choice(weight)
    b = random.choice(weight)
    x = random.randrange(2)
    
    if a<b and x:
        a,b = b,a
        
    print('%d %s %d = ？'%(a,fuhao[x],b))
    t1 = time.time()
    n = int(input())
    t2 = time.time()
    if t2 - t1 > how_long:
        raise(TypeError('你真是太慢了！'))
        
    right = eval('{}{}{}'.format(a,fuhao[x],b))
    
    if n == right:
        print('正确！')
        score+=1
    else:
        print('错误！',right)


easy = int(input('''
	选择难度：
	1  简单
	2  中等难度
	3  有点难
	4  很难
	'''))

how_long = 0

if easy==1:
    how_long = 15
    weight = [i for i in range(0,11)]
elif easy==2:
    how_long = 25
    weight = [i for i in range(0,21)] + [i for i in range(11,21)]*2
elif easy==3:
    how_long = 35
    weight = [i for i in range(101)] + [i for i in range(21,101)]*2
else :
    how_long = 45
    weight = [i for i in range(501)] + [i for i in range(101,501)]*2


many = int(input('你想算几道数学题？'))

for n in range(many):
    suanshu()
else:
    print('你共算了%d道题，算对了:%d 道题。'%(many,score)) 
    print('得分 ：{:.0f}'.format(score / many * 100))
input()