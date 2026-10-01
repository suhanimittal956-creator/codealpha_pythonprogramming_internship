ia=0
l=[ ]
pr=[]
nu=int(input("in how many different different companies you have invested"))
stocks = {
    "reliance":1257.50,"adaniports":1764.6,"vedanta":263.7,"tatasteel":183,"goldbees":125.12,"silverbees":216.72,"irbinvit":64.16,"powergridinfra":111.99,"modefence":106.73,"metalietf":13.1,"hdfcsensex":85.32,"indiangridtrust":173.9,"vedantaaluminummetal":421.75,"vedantaoilandgas":"36.71"}
for j in stocks:
    print(j.upper( ))
pri=0
for i in range(nu):
        n=input("enter name of the stock :").strip().lower()
        p=int(input ("enter the quantity of the stock:"))
        pr.append(p)
        l.append(n)
while (ia<len(l)):
        price=0
        cs=l[ia]
        if cs in stocks:
               price=price+(stocks[cs]*pr[ia])
               pri=pri+price
           
        print(f"your total investement in {cs} stocks is {price}")
        ia+=1
print(f"your toatal investment is{pri}")
sc=input("enter do you want  to save the summary to a file(y/n)").lower( )
if sc=='y':
       filename="portfolio_summary.txt"
       with open(filename,'w')as file:
              file.write("-"*20+"\n")
              write_idx=0
              while write_idx<len(l):
                     item_stock=l[write_idx]
                     if item_stock in stocks:
                            item_cost=stocks[item_stock]*pr[write_idx]
                            file.write(f"{item_stock}:{pr[write_idx]}shares={item_cost}in ruppes"+"\n")
                     write_idx+=1
              file.write("-"*20+"\n")
              file.write(f"overflow total investement :{pri}"+"\n")
print(f"successfully saved to{filename}") 
