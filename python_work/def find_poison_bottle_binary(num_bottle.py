import random
import math

def find_poison_bottle_binary(num_bottles):
    # 随机生成毒药瓶编号
    poison_bottle = random.randint(1, num_bottles)
    print(f"毒药瓶编号是: {poison_bottle}（为了测试目的，这里显示实际编号）")
    
    # 计算所需的小白鼠数量
    num_mice = math.ceil(math.log2(num_bottles))
    print(f"所需小白鼠数量: {num_mice}")
    
    # 初始化变量
    bottles = list(range(1, num_bottles + 1))
    mice_dead = [False] * num_mice
    iterations = 0

    while len(bottles) > 1 and iterations < num_mice:
        iterations += 1
        mid = len(bottles) // 2
        group1 = bottles[:mid]
        group2 = bottles[mid:]

        # 假设第一个组喂给当前迭代的小白鼠，第二组喂给下一迭代的小白鼠
        if poison_bottle in group1:
            bottles = group1
            mice_dead[iterations - 1] = True
        else:
            bottles = group2
            mice_dead[iterations - 1] = False

    # 输出调试信息
    if iterations > num_mice:
        print(f"迭代次数超出预期: {iterations}次。这不应该发生。")

    return bottles[0], mice_dead, iterations

# 测试总瓶数大于1024的情况
num_bottles = 2000
result, mice_dead, iterations = find_poison_bottle_binary(num_bottles)
print(f"找到毒药瓶是: {result}, 小白鼠死亡状态: {mice_dead}, 迭代次数: {iterations}")
