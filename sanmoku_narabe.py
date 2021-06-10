import copy


def view_node(node):
    print(node[0:3])
    print(node[3:6])
    print(node[6:9])
    print()


def turn_node(node):
    turned_node = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    indexs = [2, 5, 8, 
             1, 4, 7,
             0, 3, 6]
    for i, index in enumerate(indexs):
        turned_node[i] = node[index]
    return turned_node


def symmetry_node_yoko(node):
    symmetric_node = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    indexs = [2, 1, 0,
              5, 4, 3,
              8, 7, 6]
    for i, index in enumerate(indexs):
        symmetric_node[i] = node[index]
    return symmetric_node


def symmetry_node_tate(node):
    symmetric_node = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    indexs = [6, 7, 8,
              3, 4, 5,
              0, 1, 2]
    for i, index in enumerate(indexs):
        symmetric_node[i] = node[index]
    return symmetric_node


def symmetry_node_naname1(node):
    symmetric_node = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    indexs = [0, 3, 6,
              1, 4, 7,
              2, 5, 8]
    for i, index in enumerate(indexs):
        symmetric_node[i] = node[index]
    return symmetric_node


def symmetry_node_naname2(node):
    symmetric_node = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    indexs = [8, 5, 2,
              7, 4, 1,
              6, 3, 0]
    for i, index in enumerate(indexs):
        symmetric_node[i] = node[index]
    return symmetric_node


def check_node_exist(new_node, nodes):
    for node in nodes:
        for i in range(4):
            new_node = turn_node(new_node)
            if(node == new_node):
                return score_dict[str(node)]
        if(node == symmetry_node_yoko(new_node)):
            return score_dict[str(node)]
        if(node == symmetry_node_tate(new_node)):
            return score_dict[str(node)]
        if(node == symmetry_node_naname1(new_node)):
            return score_dict[str(node)]
        if(node == symmetry_node_naname2(new_node)):
            return score_dict[str(node)]
    return 2


def judge_node(node):
    # 3: 途中
    # 1: 先攻勝利
    # -1: 後攻勝利
    # 0: 引き分け
    indexs = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
              [0, 3, 6], [1, 4, 7], [2, 5, 8],
              [0, 4, 8], [2, 4, 6]]
    for index in indexs:
        if(node[index[0]] == 1 and node[index[1]] == 1 and node[index[2]] == 1):
            return 1
    for index in indexs:
        if(node[index[0]] == 2 and node[index[1]] == 2 and node[index[2]] == 2):
            return -1
    for i in node:
        if(i==0):
            return 3
    return 0


def search_newNode(node, depth):
    turn = depth % 2 + 1
    new_scores = []

    if(judge_node(node) != 3):
        score_dict[str(node)] = judge_node(node)
        return

    for i in range(9):
        new_node = copy.deepcopy(node)
        if(node[i]==0):
            new_node[i] = turn
            new_score = check_node_exist(new_node, all_nodes)
            if(new_score == 2):
                all_nodes.append(new_node)
                all_judge.append(judge_node(new_node))
                search_newNode(new_node, depth + 1)
                new_score = score_dict[str(new_node)]
            new_scores.append(new_score)
    if(turn == 1):
        score_dict[str(node)] = max(new_scores)
    elif(turn == 2):
        score_dict[str(node)] = min(new_scores)

    if(depth < 3):
        print("-----")
        print("turn" + str(depth))
        print("score : " + str(score_dict[str(node)]))
        view_node(node)


# main
all_nodes = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
all_judge = [3]
score_dict = {}
first_node = [0,0,0,0,0,0,0,0,0]
depth = 0

search_newNode(first_node, depth)

print("-------------------------------------------")

end_node_count = 0
sente = 0
koute = 0
draw  = 0

for i, judge in enumerate(all_judge):
    if(judge==1):
        sente += 1
    if(judge==-1):
        koute += 1
    if(judge==0):
        draw  += 1
        view_node(all_nodes[i])

print("all_kyokumen : " + str(len(all_nodes)))
print("end_kyokumen : " + str(sente + koute + draw))
print("sente_win : " + str(sente))
print("koute_win : " + str(koute))
print("draw : " + str(draw))
