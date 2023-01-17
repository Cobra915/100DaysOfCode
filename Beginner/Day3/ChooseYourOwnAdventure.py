print("Welcome to the choose your own adventure-motron")
Character_Name = input("Please Enter the name of your Character: ")
Origin_City = input(f"From where do thou hail, {Character_Name}? ")

print(f'Well, {Character_Name} from {Origin_City}, are you ready to embark on an epic adventure where the simplest choice will kill you for no raisen? (Choose "Yes" or "No")')

def Acquire_Inputs():
    BillTotal_Input_Str = input("What was the total Bill? " )
    
    if '$' in BillTotal_Input_Str:
        BillTotal_Input = float(BillTotal_Input_Str.strip('$'))
    else:
        BillTotal_Input = float(BillTotal_Input_Str)

    Party_Input = int(input("How many people are in your party? "))
    Tip_Input = int(input("What percentage would you like to give? 10, 12, 15 or 20? "))
    Tip_Factor = Tip_Input/100
    return BillTotal_Input, Party_Input, Tip_Factor
    

def Calculate_Individual_Bill(Bill, Size, Tip):
    Total_Tip = Bill * Tip
    Total_Bill = Bill + Total_Tip
    Ind_Bill = round(((Total_Bill)/Size), 2)
    Ind_Bill_Str = "{:.2f}".format(Ind_Bill)
    return Ind_Bill_Str
    
# Main function:
if __name__ == "__main__":
    print("Welcome to the tip calculator!")
    Inputs = Acquire_Inputs()
    BillTotal = Inputs[0]
    Party_Size = Inputs[1]
    Tip_Factor = Inputs[2]

    Ind_Bill = Calculate_Individual_Bill(BillTotal, Party_Size, Tip_Factor)

    print(f"Your individual bill is ${Ind_Bill}")