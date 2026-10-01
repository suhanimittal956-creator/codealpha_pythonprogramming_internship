


def bot(ui):
    ui=ui.strip().lower()
    if ui=="hello" or ui=="hii" or ui=="hey":
        return"hii"
    elif ui=="how are you":
        return"i'm fine thanks!"
    elif ui=="bye" or ui=="goodbye" or ui=="exit":
        return"goodbye"
    elif ui=="whats your name":
       
        return"i am basic bot and i can answer some of your basic questions"
    elif ui=="do mathematical task":
        print("main menu")
        print("+\n-\n*\n/\n%\n**")
        a=int(input("enter the first nember:"))
        b=int(input("enter the secound number:"))
        c=input("enter the operation to be performed")
        if c=='+':
            return(a+b)
        elif c=="-":
            return(a-b)
        elif c=="*":
            return(a*b)
        elif c=="/":
            return(a/b)
        elif c=="%":
            return(a%b)
        elif c=="**":
            return(a**b)
        else:
            return"I cannot do the complex tasks you can give me basic mathematical tasks"

    else:
        return"sorry but i don not understand you can ask something different"

def run():
        print("="*20)
        print("welcome to the basic chatbot:")
        print("type bye or exit to exit")
        print("for giving the mathematical task type'do mathematical task' ")
        print("="*20)
            
        while True:
            um=input("you:")
            br=bot(um)
            print(f"bot:{br}")
            if um.strip().lower( ) in ["bye","exit","goodbye"]:
                break
if __name__=="__main__":
    run( )
