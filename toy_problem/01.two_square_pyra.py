"""
input 16
1
2 3
4 5 6 7
8 9 10 11 12 13 14 15
16

input 10
1
2 3
4 5 6 7
8 9 10
"""
class Two_square_pyra():

    def __init__(self, input_num):
        self.input_num = input_num
        self.sqr_cnt = 0
        self.enterarry =[]
        self.numarry= list(range(1, input_num+1))

    def make_enter_cnt(self):
        result = 0
        while 1 :
            result = int(self.input_num/2)
            self.input_num = result
            self.enterarry.append(pow(2, self.sqr_cnt)-1)
            self.sqr_cnt +=1
            if result < 1 : break

    def prnt_pyramid(self):
        for value in self.numarry:
            print (value, end="")
            if value in self.enterarry: print("")

obj = Two_square_pyra(2)
obj.make_enter_cnt()
obj.prnt_pyramid()
