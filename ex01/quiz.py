from random import randint, random
def main():
    a=(shutudai())
    kaito(a)
def shutudai():
    r=random.randint(0,2)
    if r==0:
        k={"q":"サザエの旦那の名前は？","a":{"マスオ","ますお"}}
        s=(k[r]["q"])
        print(k[r]["q"])
        return s
    elif r==1:
        k={"q":"カツオの妹は？","a":{"ワカメ","わかめ"}}
        s=(k[r]["q"])
        print(k[r]["q"])
        return s
    else:
        k={"q":"タラオはカツオから見てどんな関係？","a":{"甥","おい","甥っ子","おいっこ"}}
        s=(k[r]["q"])
        print(k[r]["q"])
        return s
def kaito(a):
    ans=input("答えるんだ:")
    if ans==a :
        print("正解")
    else:
        print("出直してこい")

if __name__=="main":
    main()