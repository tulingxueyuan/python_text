class GameZiMu():
    # 打印字母A
    def a(self):
        # 控制行
        for i in range(1,6):
            # 判断开始输入的位置
            for k in range(6-i):
                print(' ',end="")
            # 控制列
            for j in range(1,i+1):
                if i==1 or i==3 or j==1 or j==i:
                    print('*',end=" ")
                else:
                    print(' ', end=" ")
            print()
    # 打印字母B
    def b(self):
        for i in range(1,4):
            for j in range(1,4):
                if i==1 or i==4 or j==1:
                    if j<3:
                        print('*',end=" ")
                elif j==3:
                    if i==2 or i==3:
                        print('*', end=" ")
                else:
                    print(' ',end=" ")
            print()
        for i in range(1,5):
            for j in range(1,4):
                if i==1 or i==4 or j==1:
                    if j<3:
                        print('*',end=" ")
                elif j==3:
                    if i==2 or i==3:
                        print('*', end=" ")
                else:
                    print(' ',end=" ")
            print()
    # 打印字母C
    def c(self):
        for i in range(1,5):
            for j in range(1,4):
                if i==1 or i==4:
                    if j==1:
                        print(' ',end=" ")
                    else:
                        print("*", end=" ")
                elif j==1:
                    if i==2 or i==3:
                        print("*", end=" ")
                else:
                    print(' ', end=" ")
            print()

    # 打印字母D
    def d(self):
        for i in range(1,5):
            for j in range(1,4):
                if i==1 or i==4 or j==1:
                    if j<3:
                        print('*',end=" ")
                elif j==3:
                    if i==2 or i==3:
                        print('*', end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母E
    def e(self):
        for m in range(1,8):
            for n in range(1,4):
                if m==1 or m==4 or m==7 or n==1:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母F
    def f(self):
        for m in range(1,8):
            for n in range(1,4):
                if m==1 or m==4 or n==1:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母G
    def g(self):
        for m in range(1,5):
            for n in range(1,5):
                if m==1 or m==4:
                    if n==1:
                        print(' ',end=" ")
                    else:
                        print('*',end=" ")
                elif m==2 and n==1:
                    print("*",end=" ")
                elif m==3:
                    if n==2:
                        print(' ', end=" ")
                    else:
                        print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母H
    def h(self):
        for m in range(1,6):
            for n in range(1,4):
                if m==3 or n==1 or n==3:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母I
    def i(self):
        for m in range(1,6):
            for n in range(1,4):
                if m==1 or m==5 or n==2:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母J
    def j(self):
        for m in range(1,6):
            for n in range(1,5):
                if m==1 or n==3:
                    if m<5:
                        print('*',end=" ")
                elif m==4 and n==1:
                    print('*', end=" ")
                elif m==5 and n==2:
                    print('*', end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母K
    def k(self):
        for m in range(1,3):
            for n in range(m,4):
                if m==1 and n==2:
                    print(' ',end=" ")
                else:
                    print('*',end=" ")
            print()
        for m in range(1,4):
            for n in range(m):
                if n==0 or n==m-1:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母L
    def l(self):
        for m in range(1,6):
            for n in range(1,4):
                if m==5 or n==1:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母M
    def m(self):
        # 控制行
        for i in range(1,6):
            # 判断开始输入的位置
            for k in range(6-i):
                print(' ',end="")
            # 控制列
            for j in range(1,i+1):
                if i==1 or j==1 or j==i:
                    print('*',end=" ")
                else:
                    print(' ', end=" ")


            # 判断开始输入的位置
            for k in range(5-i):
                print(' ',end=" ")
            # 控制列
            for j in range(1,i+1):
                if i==1 or j==1 or j==i:
                    print('*',end=" ")
                else:
                    print(' ', end=" ")
            print()

    # 打印字母N
    def n(self):
        for m in range(1,5):
            for n in range(1,5):
                if n==4 or n==1 or m==n:
                    print('*',end=" ")
                else:
                    print(' ',end=" ")
            print()

