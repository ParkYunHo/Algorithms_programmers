def marathon1(participant, completion):
    p_dict = dict()
    res = ''
    for i in completion:
        if i in p_dict:
            p_dict[i] += 1
        else:
            p_dict[i] = 1

    for i in participant:
        if i in p_dict:
            if p_dict[i] <= 0:
                res = i
                break
            else:
                p_dict[i] -= 1
        else:
            res = i
            break
    return res


# participant가 completion보다 무조건 1명만 더 많을때 사용가능
def marathon2(participant, completion):
    p = sorted(participant)
    c = sorted(completion)

    for i in range(len(completion)):
        if p[i] != c[i]:
            return p[i]

    return p[len(p)-1]


def phone_num1(list):
    for idx1, val1 in enumerate(list):
        for idx2, val2 in enumerate(list):
            if idx1 == idx2:
                continue
            if val1 == val2[0:len(val1)]:
                return False
    return True


def phone_num2(list):
    list = sorted(list)

    for i, j in zip(list, list[1:]):
        if i == j[0:len(i)]:
            return False
    return True


def phone_num3(list):
    list = sorted(list)

    for i, j in zip(list, list[1:]):
        if j.startswith(i):  # j 문자열에 첫부분에 i가 속해있는지 확인하는 함수
            return False
    return True


class Clothes:
    def __init__(self, category):
        self.category = category
        self.chain = []

    def __insert__(self, clothes):
        self.chain.append(clothes)

    def __length__(self):
        return len(self.chain)

    def __getChain__(self):
        return self.chain


def spy_combine1(clothes):
    category = dict()
    category_list = []

    for i in clothes:
        if i[1] in category_list:
            category[i[1]].__insert__(i[0])
        else:
            category[i[1]] = Clothes(i[1])
            category_list.append(i[1])
            category[i[1]].__insert__(i[0])

    res = 1
    for i in category_list:
        res *= (category[i].__length__()+1)

    return res-1


def spy_combine2(clothes):
    from collections import Counter
    from functools import reduce

    cnt = Counter([kind for name, kind in clothes])
    res = reduce(lambda x,y : x*(y+1), cnt.values(), 1)-1
    return res


class Album:
    chain = dict()

    def __init__(self, play, idx):
        self.chain[play] = idx

    def __insert__(self, play, idx):
        if play not in self.chain:
            self.chain[play] = idx

    def __sum__(self):
        total = 0
        for i in self.chain:
            total += i
        return total

    def __max__(self):
        _max = 0
        for i in self.chain:
            if _max < i:
                _max = i
        return self.chain[_max]


def best_album():
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]

    # 1. 장르별 play수가 가장 많은 장르부터 수록
    # 2. play수가 가장 많은 장르 내에 가장 많이 재생된 노래 먼저 수록
    # 3. 장르내 재생 횟수가 같은 노래중 고유번호가 낮은 노래부터 수록

    unique = dict()
    unique_list = list()
    for idx, val in enumerate(genres):
        if val in unique:
            unique[val].__insert__(plays[idx], idx)
        else:
            unique[val] = Album(plays[idx], idx)
            unique_list.append(val)

    for i in unique_list:
        print(unique[i])
    print(unique_list)

















