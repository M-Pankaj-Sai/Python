# taking input 
a = input() #input is taken as string single char or entire line

a = int(input()) # int input

a = float(input()) # float input

a,b = input().split() # giving two string or char with space as seperator 

a,b = map(int,input.split()) # taking two int as input with space as seperator

a = input("you can pass a prompt : ")

a = list(map(int,input().split())) 

a,*l = input().split() # if we give 'hello world' then a = 'hello' , l = ['world']

a,*l = input().split() # if we give 'hello world this is pankaj' then a = 'hello' , b=['world'.'this','is','pankaj']

