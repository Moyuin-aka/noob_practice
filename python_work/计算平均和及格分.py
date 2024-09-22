import numpy as np
np.random.seed(6)
scores = np.random.randint(40,101,size=(10,3))
score = int(input("请输入你的分数："))
mask = scores<=score
print(f"语文，数学，英语三门课在及格线以下的人数分别是：{score,np.sum(mask,axis=0)}")
ab_all=np.sum(np.all(scores>=score,axis=1))
print(f"三门课都及格的人数是：{ab_all}")
average_scores=np.mean(scores,axis=0)
print(f"三门课的平均分数为：{average_scores}")