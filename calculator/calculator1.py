import itertools


gain_dist={6:10000,7:36,8:720,9:360,10:80,11:252,12:108,13:72,14:54,15:180,
           16:72,17:180,18:119,19:36,20:306,21:1080,22:144,23:1800,24:3600}
gd = gain_dist
allowed_line = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),
                (1,5,9),(3,5,7)]

def list_sub(lst, Max=9):
    res = []
    for i in range(1,Max+1):
        if i not in lst:
            res.append(i)
    return res
        
def argmax(dic,flag=0):
    n = len(dic)
    maxvalue = -9999
    maxkey = None
    for key in dic:
        if dic[key] > maxvalue:
            maxvalue = dic[key]
            maxkey = key
    if flag == 0:
        return [maxkey, maxvalue]
    else:
        return [maxkey+10, maxvalue]

def expt3(a,b,c,unum):
    unknown = 0
    current = a + b + c
    if a == 0:
        unknown += 1
    if b == 0:
        unknown += 1
    if c == 0:
        unknown += 1
    if unknown == 0:
        return gd[current]

    possible_list = []
    for tup in itertools.combinations(unum,unknown):
        possible_list.append(gd[current + sum(tup)])
    return sum(possible_list)/len(possible_list)
    
    

class Step():
    def __init__(self,status):
        self.status = status
        self.appeared = len(status)
        self.cplace = [x for x in status]
        self.uplace = list_sub([x for x in status])
        self.cnum = [status[x] for x in status]
        self.unum = list_sub([status[x] for x in status])
        self.status_all = status.copy()
        for i in range(1,10):
            if i not in self.status_all:
                self.status_all[i] = 0
        self.next = None

    def show(self):
        show_list = []
        for i in range(1,10):
            if i in self.status:
                show_list.append(str(self.status[i]))
            else:
                show_list.append('?')
        sl = show_list
        show_str = "{} {} {}\n{} {} {}\n{} {} {}".format(sl[0],sl[1],sl[2],
                                                         sl[3],sl[4],sl[5],
                                                         sl[6],sl[7],sl[8])
        print(show_str)

    def expt_direct(self):
        expt_of_lines = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
        sta = self.status_all
        for i in range(8):
            a,b,c = allowed_line[i]
            expt_of_lines[i] = expt3(sta[a],sta[b],sta[c],self.unum)
        return argmax(expt_of_lines)
            

    def expt(self):
        assert len(self.uplace) == len(self.unum)
        if len(self.cplace) >= 4:
            return self.expt_direct()
        n = len(self.uplace)
        expt_dict = {}
        for p in self.uplace:
            t_expt = 0
            for d in self.unum:
                new_status = self.status.copy()
                new_status[p] = d
                add = Step(new_status).expt()[1]
                t_expt += add/len(self.unum)
            expt_dict[p] = t_expt
        return argmax(expt_dict)

    def expt_print(self):
        assert len(self.uplace) == len(self.unum)
        if len(self.cplace) >= 4:
            return self.expt_direct()
        n = len(self.uplace)
        expt_dict = {}
        for p in self.uplace:
            t_expt = 0
            for d in self.unum:
                new_status = self.status.copy()
                new_status[p] = d
                add = Step(new_status).expt()[1]
                t_expt += add/len(self.unum)
            expt_dict[p] = t_expt
        print(expt_dict)
        return argmax(expt_dict)
            
            
def mini_helper():
    print("=========================================================================")
    print("??????????????????1.0??????")
    print("????????????????????????5:3????????????????????????5????????????3????????????7:1???????????????????????????7????????????1???")
    print("?????????????????????????????????????????????????????????????????????????????????????????????")
    print("??????r??????????????????")
    print("=========================================================================")
    while True:
        inputstr = input("????????????????????????")
        if 'r' in inputstr:
            return 0
        try:
            p1 = int(inputstr[0])
            d1 = int(inputstr[2])
            assert 1 <= p1 <= 9 and 1 <= d1 <= 9
            break
        except:
            print("??????????????????")
            pass

    a1 = Step({p1:d1})
    a1.show()
    best1,expt1 = a1.expt()
    print("Bestplace =", best1)
    print("Expectation =", round(expt1,2))

    while True:
        inputstr = input("?????????????????????????????????")
        if 'r' in inputstr:
            return 0
        try:
            p2 = int(inputstr[0])
            d2 = int(inputstr[2])
            assert 1 <= p2 <= 9 and 1 <= d2 <= 9
            break
        except:
            print("??????????????????")
            pass
    a2 = Step({p1:d1,p2:d2})
    a2.show()
    best2,expt2 = a2.expt()
    print("Bestplace =", best2)
    print("Expectation =", round(expt2,2))

    while True:
        inputstr = input("?????????????????????????????????")
        if 'r' in inputstr:
            return 0
        try:
            p3 = int(inputstr[0])
            d3 = int(inputstr[2])
            assert 1 <= p3 <= 9 and 1 <= d3 <= 9
            break
        except:
            print("??????????????????")
            pass
    a3 = Step({p1:d1,p2:d2,p3:d3})
    a3.show()
    best3,expt3 = a3.expt()
    print("Bestplace =", best3)
    print("Expectation =", round(expt3,2))

    while True:
        inputstr = input("?????????????????????????????????")
        if 'r' in inputstr:
            return 0
        try:
            p4 = int(inputstr[0])
            d4 = int(inputstr[2])
            assert 1 <= p4 <= 9 and 1 <= d4 <= 9
            break
        except:
            print("??????????????????")
            pass
    a4 = Step({p1:d1,p2:d2,p3:d3,p4:d4})
    a4.show()
    bestline,expt4 = a4.expt()
    print("Best Line =", allowed_line[bestline])
    print("Expectation =", round(expt4,2))
    input("????????????????????????????????????")

while True:
    mini_helper()


