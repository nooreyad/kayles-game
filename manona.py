player=1
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b=['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']

print(a)
while a!=b:
   if (player==1):
      print("player one's will play")
      print("choose one or two numbers")
      the_number=int(input())
      if the_number==1:
         print("choose the number from",a)
         a[(int(input())) - 1]='*'
         print(a)
      elif the_number ==2:
           print("choose the two numbers from",a)
           print("choose the first number")
           a[(int(input())) - 1] ='*'
           print("choose the second number")
           a[(int(input())) - 1]='*'
           print(a)

           if(a==b):
            print("player one win")
           
      player=2
           
   if (player==2) :
      print("player two's will play")
      print("choose one or two numbers")
      the_number=int(input())
      if the_number==1:
           print("choose the number from",a)
           a[(int(input()))]='*'
           print(a)
      elif the_number==2:
            print("choose the two numbers from",a)
            print("choose the first number")
            a[(int(input()))]='*'
            print("choose the second number")
            a[(int(input()))]='*'
            print(a)
            if(a==b):
               print("player two win")
            
      player=1
print("the game end")
