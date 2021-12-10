import numpy as np
import random

# 增大numpy的行限制
np.set_printoptions(linewidth=200)

# 初始化矩阵
Q = np.zeros((11, 11))
Q = np.matrix(Q)

# 回报矩阵R
R = np.matrix([[0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 6, 0, 3, 0, 0, 0, 0, 0, 0],
               [0, 8, 0, 9, 0, 5, 0, 0, 0, 0, 0],
               [0, 0, 6, 0, 0, 0, 4, 0, 0, 0, 0],
               [0, 8, 0, 0, 0, 5, 0, 7, 0, 0, 0],
               [0, 0, 6, 0, 3, 0, 4, 0, 9, 0, 0],
               [0, 0, 0, 9, 0, 5, 0, 0, 0, 8, 0],
               [0, 0, 0, 0, 3, 0, 0, 0, 9, 0, 0],
               [0, 0, 0, 0, 0, 5, 0, 7, 0, 5, 0],
               [0, 0, 0, 0, 0, 0, 4, 0, 9, 0, 100],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]])

# 设立学习参数
γ = 0.8


# 训练Q
for i in range(3000):
    # 对每一个训练,随机选择一种状态
    state = 0
    while True:
        # 选择当前状态下的所有可能动作
        r_pos_action = []
        for action in range(11):
            if R[state, action] > 0:
                r_pos_action.append(action)
        next_state = r_pos_action[random.randint(0, len(r_pos_action) - 1)]
        Q[state, next_state] = R[state, next_state] + γ * (Q[next_state]).max()  # 更新
        state = next_state
        # 状态4位最优库存状态
        if state == 10:
            break
print(Q)


# 输出最优路径
state = 0
step = 1
while True:
    r_pos_action = []
    for action in range(11):
        if Q[state, action] == Q[state].max():
            print("Step%s [%s -> %s]" % (step, state, action))
            state = action
            break
    if state == 10:
        break
