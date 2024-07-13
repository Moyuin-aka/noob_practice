import random
#简单打招呼输入名字
guest_name = input("Your name:")
guest_name = guest_name.strip()
for_example=f"{guest_name}".title()
print(f"Hello,{for_example}!\nGlad to see you!")

#构建随机谚语库
proverbs = ["Absence makes the heart grow fonder.",
            "Actions speak louder than words.",
            "A journey of a thousand miles begins with a single step.",
            "All good things must come to an end.",
            "A picture is worth a thousand words",
            "A watched pot never boils.",
            "Beggars can’t be choosers.",
            "Beauty is in the eye of the beholder.",
            "Better late than never.",
            "Birds of a feather flock together."]#我之后研究研究怎么从网页直接导入库

everyday_saying_check=input("Do you wanna some common proverbs to embrace the brand new day?(yes/no)")
while True:
  if everyday_saying_check.lower()==("yes"):
    print(random.choice(proverbs).title())#获取随机谚语
    #只有这个能循环，虽然有点小bug，循环到上一句有点烦
  elif everyday_saying_check.lower() == ("no"):
    print("Alright.Have a good day!")
    break
  else:
    message='please answer it with "yes" or "no",thanks.' 
    print(message)
  if everyday_saying_check.lower() == ("no"):
      print("Alright.Have a good day!")
      break
  else:
      message='please answer it with "yes" or "no",thanks.' 
      print(message)
#免得大伙抖机灵乱答

  continue_check = input("Do you wanna get more?(yes/no)").strip().lower()
  if continue_check =="no":
   print("goodbye!")
   break



