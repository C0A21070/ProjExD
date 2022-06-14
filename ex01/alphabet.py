import datetime
from random import random
words=10
dwords=2
count=5

def main():
    st=datetime.datetime.now()
    for i in range(count):
        a=shutudai()
        kaitou(a)
        if i==1:
            break
    et=datetime.datetime.now()
    print(f"{(et-st)}秒かかりました")
def shutudai():
    #対象文字
    als=[]
    for c in range(46):
        al=chr(c+65)
        als.append(al)
    all_als=random.sample(als,words)
    print(f"対象文字：{all_als}")

    #欠損文字
    d_al=random.sample(als,dwords)
    
    #表示文字
    o_al=
    print(o_al)

def kaitou(a):
    num=int(input("欠損文字はいくつあるでしょうか？"))
    if num!=dwords:
        print("不正解です。またチャレンジしてください")
        return 0

    else:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        for i in range(dwords):
            j=input(f"{i+1}つ目の文字を入力してください：")
            if j not in a:
                print("不正解です。またチャレンジしてください")
                return 0
            a.remove(j)
        print("正解です。ゲームを終了します")
        return 1

if __name__=="__main__":
    main()