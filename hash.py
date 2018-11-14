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
    def __init__(self, play, idx):
        self.chain = dict()
        self.chain[play] = idx

    def __insert__(self, play, idx):
        self.chain[play] = idx if play not in self.chain else None

    def __sum__(self):
        return sum(i for i in self.chain)

    def __max__(self):
        res = list()
        _max = 0
        _sec = 0
        for i in self.chain:
            if _max < i:
                _sec = _max
                _max = i
            elif _sec < i:
                _sec = i
        res.append(self.chain[_max])
        if _sec > 0:
            res.append(self.chain[_sec])
        return res


def best_album():
    # genres = ["classic", "pop", "classic", "classic", "pop"]
    # plays = [500, 600, 150, 800, 2500]
    # genres = ["classic", "pop", "classic", "classic", "pop", "rock"]
    # plays = [500, 600, 150, 800, 2500, 1800]
    genres = ["rock", "rock", "rock", "rock", "rock", "rock"]
    plays = [500, 600, 150, 800, 2500, 180]

    # 1. 장르별 play수가 가장 많은 장르부터 수록
    # 2. play수가 가장 많은 장르 내에 가장 많이 재생된 노래 먼저 수록
    # 3. 장르내 재생 횟수가 같은 노래중 고유번호가 낮은 노래부터 수록
    # 4. 한 장르에 값이 한개만 있는 경우, 두 장르의 total이 같을 경우, 장르 자체가 한개만 있을 경우

    unique = dict()
    unique_list = list()
    for idx, val in enumerate(genres):
        if val in unique:
            unique[val].__insert__(plays[idx], idx)
        else:
            unique[val] = Album(plays[idx], idx)
            unique_list.append(val)

    max = 0
    max_idx = ""
    sec = 0
    sec_idx = ""

    for i in unique_list:
        if max < unique[i].__sum__():
            sec = max
            sec_idx = max_idx
            max = unique[i].__sum__()
            max_idx = i
        elif sec < unique[i].__sum__():
            sec = unique[i].__sum__()
            sec_idx = i

    res = unique[max_idx].__max__()
    if sec > 0:
        res += unique[sec_idx].__max__()

    print(res)

















