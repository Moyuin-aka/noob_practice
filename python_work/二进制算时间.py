import random
import math
import time

def find_poison_bottle_binary_encoding(num_bottles):
    # 随机生成毒药瓶编号
    poison_bottle = random.randint(1, num_bottles)
    print(f"毒药瓶编号是: {poison_bottle}（为了测试目的，这里显示实际编号）")
    
    # 计算所需的小白鼠数量
    num_mice = math.ceil(math.log2(num_bottles))
    print(f"所需小白鼠数量: {num_mice}")
    
    mice_states = [0] * num_mice
    num_bottles = 1000

    # 为每一瓶液体分配二进制编号，并模拟小白鼠喂食
    for i in range(1, num_bottles + 1):
        binary_code = list(bin(i)[2:].zfill(num_mice))
        for j in range(num_mice):
            if binary_code[j] == '1' and i == poison_bottle:
                mice_states[j] = 1

    # 通过小白鼠的状态来确定毒药瓶
    binary_result = ''.join(map(str, mice_states))
    result_bottle = int(binary_result, 2)

    return result_bottle, mice_states

start_time = time.time()
result, mice_states = find_poison_bottle_binary_encoding (num_bottles=1000 )
end_time = time.time()
print(f"找到毒药瓶是: {result}, 小白鼠状态: {mice_states}")
print(f"二进制法计算时间: {end_time - start_time:.6f} 秒")
