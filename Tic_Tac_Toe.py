
chs="y"
while chs=="y":
    A=1
    B=2
    C=3
    D=4
    E=5
    F=6
    G=7
    H=8
    I=9
    ocp1=10
    ocp2=11
    ocp3=13
    ocp4=14
    ocp5=15
    ocp6=16
    ocp7=17
    ocp8=18
    ocp9=19
    w_cond=1
    #draw board
    print("/---WELCOME TO TIC TAC TOE GAME---/")
    def printboard():
        print(A," |",B,"|",C)
        print("___|___|___")
        print(D," |",E,"|",F)
        print("___|___|___")
        print(G," |",H,"|",I)
        print("   |   |")
    player=input("Enter your name: ")
    import random
    #selection of symbole
    print(player,"Enter your symbol x or o")
    icon1=input().upper()
    while icon1.isalpha()is False:
       print("Wrong selection!\nplease choose either X or O: ")
       icon1=input().upper()
    if icon1=="X":
        icon2="O"
    elif icon1=="O":
        icon2="X"
    print(player,"your symbol is",icon1)
    print("Computer's symbol is",icon2)
    printboard()
    count=1
    #toss
    coin=["heads","tails"]
    Toss=random.choice(coin)
    slc=input("for toss\n"+str(player)+" Choose heads or tails: ")
    while slc not in coin:
       print("Wrong selection!\nplease choose either heads or tails")
       slc=input()
    if slc==Toss:
       print("congratulations",player,"WON THE TOSS")
       num=1
    else:
       print("Ooops! ",player,"Loss THE TOSS")
       num=2
    while count<=9:
        if num%2!=0:
           print("      ",player,"\nselect 1 to chose box 1\nselect 2 to chose box 2\nselect 1 to chose box 3\nselect 4 to chose box 4\nselect 5 to chose box 5\nselect 6 to chose box 6\nselect 7 to chose box 7\nselect 8 to chose box 8\nselect 9 to chose box 9 ")
           num1=eval(input())
           while num1==ocp1 or num1==ocp2 or num1==ocp3 or num1==ocp4 or num1==ocp5 or num1==ocp6 or num1==ocp7 or num1==ocp8 or num1==ocp9:
               print("Box ",num1," is already occupied\nselect another box")
               print("      ",plyr,"\nselect 1 to chose box 1\nselect 2 to chose box 2\nselect 1 to chose box 3\nselect 4 to chose box 4\nselect 5 to chose box 5\nselect 6 to chose box 6\nselect 7 to chose box 7\nselect 8 to chose box 8\nselect 9 to chose box 9 ")
               num1=eval(input())
           if num1==1:
              A=icon1
              printboard()
              ocp1=1
           elif num1==2:
              B=icon1
              printboard()
              ocp2=2
           elif num1==3:
              C=icon1
              printboard()
              ocp3=3
           elif num1==4:
              D=icon1
              printboard()
              ocp4=4
           elif num1==5:
              E=icon1
              printboard()
              ocp5=5
           elif num1==6:
              F=icon1
              printboard()
              ocp6=6
           elif num1==7:
              G=icon1
              printboard()
              ocp7=7
           elif num1==8:
              H=icon1
              printboard()
              ocp8=8
           elif num1==9:
              I=icon1
              printboard()
              ocp9=9
        #computer's turn
        elif num%2==0:
           print("Its Computer's turn")
            #winning moves of computer
           #checking first row
           if A==icon2 and B==icon2 and ocp3!=3:
              C=icon2
              printboard()
              ocp3=3
           elif A==icon2 and C==icon2 and ocp2!=2:
              B=icon2
              printboard()
              ocp2=2
           elif B==icon2 and C==icon2 and ocp1!=1:
              A=sym2
              printboard()
              ocp1=1
           #checking second row
           elif D==icon2 and E==icon2 and ocp6!=6:
              F=icon2
              printboard()
              ocp6=6
           elif D==icon2 and F==icon2 and ocp5!=5:
              E=icon2
              printboard()
              ocp5=5
           elif E==icon2 and F==icon2 and ocp4!=4:
              D=icon2
              printboard()
              ocp4=4
           #checking third row
           elif G==icon2 and H==icon2 and ocp9!=9:
              I=icon2
              printboard()
              ocp9=9
           elif G==icon2 and I==icon2 and ocp8!=8:
              H=icon2
              printboard()
              ocp8=8
           elif H==icon2 and I==icon2 and ocp7!=7:
              G=icon2
              printboard()
              ocp7=7

              #checking first column
           elif A==icon2 and D==icon2 and ocp7!=7:
              G=icon2
              printboard()
              ocp7=7
           elif A==icon2 and G==icon2 and ocp4!=4:
              D=icon2
              printboard()
              ocp4=4
           elif D==icon2 and G==icon2 and ocp1!=1:
              A=icon2
              printboard()
              ocp1=1
           #checking second column
           elif B==icon2 and E==icon2 and ocp8!=8:
              H=sym2
              printboard()
              ocp8=8
           elif B==icon2 and H==icon2 and ocp5!=5:
              E=sym2
              printboard()
              ocp5=5
           elif E==icon2 and H==icon2 and ocp2!=2:
              B=icon2
              printboard()
              ocp2=2
           #checking third column
           elif C==icon2 and F==icon2 and ocp9!=9:
              I=icon2
              printboard()
              ocp9=9
           elif C==icon2 and I==icon2 and ocp6!=6:
              F=icon2
              printboard()
              ocp6=6
           elif F==icon2 and I==icon2 and ocp3!=3:
              C=icon2
              printboard()
              ocp3=3
           #checking first diagonal
           elif A==icon2 and E==icon2 and ocp9!=9:
              I= icon2
              printboard()
              ocp9=9
           elif A==icon2 and I==icon2 and ocp5!=5:
              E=icon2
              printboard()
              ocp5=5
           elif E==icon2  and I==icon2  and ocp1!=1:
              A=icon2
              printboard()
              ocp1=1
           #checking second diagonal
           elif G==icon2  and E==icon2  and ocp3!=3:
              C=icon2
              printboard()
              ocp3=3
           elif G==icon2  and C==icon2  and ocp5!=5:
              E=icon2
              printboard()
              ocp5=5
           elif E==icon2  and C==icon2  and ocp7!=7:
              G=icon2
              printboard()
              ocp7=7
           #blocking winnig conditions of player
           #checking first row
           elif A==icon1 and B==icon1 and ocp3!=3:
              C=icon2
              printboard()
              ocp3=3
           elif A==icon1 and C==icon1 and ocp2!=2:
              B=icon2
              printboard()
              ocp2=2
           elif B==icon1 and C==icon1 and ocp1!=1:
              A=icon2
              printboard()
              ocp1=1
           #checking second row
           elif D==icon1 and E==icon1 and ocp6!=6:
              F=sym2
              printboard()
              ocp6=6
           elif D==icon1 and F==icon1 and ocp5!=5:
              E=icon2
              printboard()
              ocp5=5
           elif E==icon1 and F==icon1 and ocp4!=4:
              D=icon2
              printboard()
              ocp4=4
           #checking third row
           elif G==icon1 and H==icon1 and ocp9!=9:
              I=icon2
              printboard()
              ocp9=9
           elif G==icon1 and I==icon1 and ocp8!=8:
              H=sym2
              printboard()
              ocp8=8
           elif H==icon1 and I==icon1 and ocp7!=7:
              G=icon2
              printboard()
              ocp7=7
               #checking first column
           elif A==icon1 and D==icon1 and ocp7!=7:
              G=icon2
              printboard()
              ocp7=7
           elif A==icon1 and G==icon1 and ocp4!=4:
              D=icon2
              printboard()
              ocp4=4
           elif D==icon1 and G==icon1 and ocp1!=1:
              A=icon2
              printboard()
              ocp1=1
           #checking second column
           elif B==icon1 and E==icon1 and ocp8!=8:
              H=icon2
              printboard()
              ocp8=8
           elif B==icon1 and H==icon1 and ocp5!=5:
              E=icon2
              printboard()
              ocp5=5
           elif E==icon1 and H==icon1 and ocp2!=2:
              B=icon2
              printboard()
              ocp2=2
           #checking third column
           elif C==icon1 and F==icon1 and ocp9!=9:
              I=icon2
              printboard()
              ocp9=9
           elif C==icon1 and I==icon1 and ocp6!=6:
              F=icon2
              printboard()
              ocp6=6
           elif F==icon1 and I==icon1 and ocp3!=3:
              C=icon2
              printboard()
              ocp3=3
           #checking first diagonal
           elif A==icon1 and E==icon1 and ocp9!=9:
              I=icon2
              printboard()
              ocp9=9
           elif A==icon1 and I==icon1 and ocp5!=5:
              E=icon2
              printboard()
              ocp5=5
           elif E==icon1 and I==icon1 and ocp1!=1:
              A=icon2
              printboard()
              ocp1=1
           #checking second diagonal
           elif G==icon1 and E==icon1 and ocp3!=3:
              C=icon2
              printboard()
              ocp3=3
           elif G==icon1 and C==icon1 and ocp5!=5:
              E=icon2
              printboard()
              ocp5=5
           elif E==icon1 and C==icon1 and ocp7!=7:
              G=icon2
              printboard()
              ocp7=7
            #initial moves
           elif A==icon1 and ocp9!=9:
               I=icon2
               printboard()
               ocp9=9
           elif A==icon1 and ocp7!=97:
               G=icon2
               printboard()
               ocp7=7
           elif A==icon1 and ocp3!=3:
               C=icon2
               printboard()
               ocp3=3

           elif B==icon1 and ocp8!=8:
               H=icon2
               printboard()
               ocp8=8
           elif B==icon1 and ocp6!=6:
               F=icon2
               printboard()
               ocp6=6
           elif B==icon1 and ocp4!=4:
               D=icon2
               printboard()
               ocp4=4
           elif C==icon1 and ocp3!=3:
               G=icon2
               printboard()
               ocp3=3
           elif C==icon1 and ocp1!=1:
               A=icon2
               printboard()
               ocp1=1
           elif C==icon1 and ocp9!=9:
               I=icon2
               printboard()
               ocp9=9
           elif D==icon1 and ocp6!=6:
               F=icon2
               printboard()
               ocp6=6
           elif D==icon1 and ocp8!=8:
               H=icon2
               printboard()
               ocp8=8
           elif D==icon1 and ocp2!=2:
               B=icon2
               printboard()
               ocp2=2
           elif E==icon1 and ocp1!=1:
               A=icon2
               printboard()
               ocp1=1
           elif E==icon1 and ocp9!=9:
               I=icon2
               printboard()
               ocp9=9
           elif E==icon1 and ocp3!=3:
               C=icon2
               printboard()
               ocp3=3
           elif E==icon1 and ocp7!=7:
               G=icon2
               printboard()
               ocp7=7
           elif F==icon1 and ocp4!=4:
               D=icon2
               printboard()
               ocp4=4
           elif F==icon1 and ocp2!=2:
               B=icon2
               printboard()
               ocp2=2
           elif F==icon1 and ocp8!=8:
               H=icon2
               printboard()
               ocp8=8
           elif G==icon1 and ocp3!=3:
               C=icon2
               printboard()
               ocp3=3
           elif G==icon1 and ocp1!=1:
               A=icon2
               printboard()
               ocp1=1
           elif G==icon1 and ocp9!=9:
               I=icon2
               printboard()
               ocp9=9
           elif H==icon1 and ocp2!=2:
               B=icon2
               printboard()
               ocp2=2
           elif H==icon1 and ocp4!=4:
               D=icon2
               printboard()
               ocp4=4
           elif H==icon1 and ocp6!=6:
               F=icon2
               printboard()
               ocp6=6
           elif I==icon1 and ocp1!=1:
               A=icon2
               printboard()
               ocp1=1
           elif I==icon1 and ocp3!=3:
               C=icon2
               printboard()
               ocp3=3
           elif I==icon1 and ocp7!=7:
               G=icon2
               printboard()
               ocp7=7
           elif A==1 and B==2 and C==3 and D==4 and E==5 and F==6 and G==7 and H==8 and I==9:
               E=icon2
               printboard()
               ocp5=5


        count=count+1
        num=num+1
        if A==B and B==C and A==icon1 or D==E and E==F and D==icon1 or G==H and H==I and G==icon1 or A==D and D==G and A==icon1 or B==E and E==H and B==icon1 or C==F and F==I and C==icon1 or A==E and E==I and A==icon1 or C==E and E==G and C==icon1:
           w_cond="Won the Match"
           print(plyr," ",w_cond)
           break
        elif A==B and B==C and A==icon2 or D==E and E==F and D==icon2 or G==H and H==I and G==icon2 or A==D and D==G and A==icon2 or B==E and E==H and B==icon2 or C==F and F==I and C==icon2 or A==E and E==I and A==icon2 or C==E and E==G and C==icon2:
           w_cond="Won the Match"
           print("Computer ",w_cond)
           break
    if w_cond==1:
       print("Match Draw")
    print("Press y to play again or any other key to exit")
    chs=input()


