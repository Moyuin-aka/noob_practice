import random
def game():
  num=int(random.randint(0,101))
  print("来玩猜数字游戏吧！数字在0-100之间！")
  while True:
      guess=int(input("请输入一个你猜测的数字："))
      if guess<num:
        print("小了哦！再猜一个吧")
        continue
      elif guess>num:
        print("大了哦！再猜一个吧")
        continue
      else:
        print("你真棒！猜对了！")
        break
while True:
    game()
    while True:
        again_check=input("还想再次来一局么？(是/否)")
        if again_check=="是":
            print('感谢你的支持！') 
            break
        elif again_check=="否":
            print("好的！祝你天天开心！")
            exit()
        else:
            print("请用“是”或者“否”回答><")
            continue  