"""
N개의 자연수로 이루어진 수열과 자연수 s가 주어졌을 때 합이 s보다 같거나 큰 수열의
부분배열(subarry) 중 크기가 가장 작은 부분배열의 크기를 구하는 문제
예를 들어, 수열 5,1,3,5,10,7,4,9,2,8이 주어지고 s가 15라면 [10, 7]이 합이
s보다 같거나 큰 부분배열 중 크기가 가장 작은 부분배열이다 그러므로 답은 2이다

입력
입력의 첫 줄에는 테스트케이스 수 T가 주어진다
각 테스트케이스의 첫줄에는 자연수 N, S가 주어진다 (1<N<100,000, S<10000000000)
주어지는 수는 10,000보다 크지 않다

출력
각 테스트 케이스마다 첫줄에 #testcaseT"를 출력해야 한다 이때 T는 케이스의 번호이다
각 테스트케이스 마다 합이 s보다 같거나 큰 부분배열이 없는 경우 0을 출력하고
존재한다면 가장 작은 부분배열의 크기를 줄로 구분하여 출력한다
"""

class AddTester:

    def __init__(self, list):
        self.list = list
        self.left = 0
        self.right = len(list)-1
        self.testcnt =0



    def list_sort(self, left=None, right=None):

        if left ==None and right == None:
            left = self.left
            right = self.right

        list = self.list
        pivoteindex = left
        lowindex= left+1
        highterindex = right

        if(left >=right):
            return

        while lowindex < highterindex or lowindex != highterindex:

            if list[lowindex] > list[highterindex]:
                list[lowindex] , list[highterindex] =list[highterindex] , list[lowindex]

            if list[pivoteindex] > list[lowindex]:
                lowindex +=1
            if list[pivoteindex] < list[highterindex]:
                highterindex -=1

        list[pivoteindex], list[highterindex] = list[highterindex], list[pivoteindex]



        self.list_sort(left, highterindex-1)
        self.list_sort(highterindex+1, right)

    def get_list(self):
        print(self.list)

    def get_sublist(self, target):
        lenght = len(self.list)-1
        sum = 0

        for i in range(0,lenght):
            sum+=self.list[lenght-i]
            if(sum>=target):
                self.testcnt+=1
                print ("test case ", self.testcnt)
                print ("len is", i+1)
                return




tester = AddTester([5,1,3,6,10,7,4,9,8])
tester.list_sort()
tester.get_list()
tester.get_sublist(30)
