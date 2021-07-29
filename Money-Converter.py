def dollars():  
    usd=float(input("Please Enter US Dollars To Be Converted Into IND Rupees: "))
    usd_to_rup = usd*72.67
    print(f"{usd} $ in Rs are {usd_to_rup:.3f} Rs")

def rupee():
    rup=float(input("Please Enter IND Rupees To Be Converted Into US Dollars: "))
    rup_to_usd = rup/72.67
    print(f"{rup} Rs in $ are {rup_to_usd:.3f} $")
   
if __name__ == "__main__":
    while True:
        print()
        print("Welcome To Money Converter")
        print()
        ans=str(input("Please Type (U) to convert from US Dollars To IND Rupee OR Type (R) to convert from IND Rupee to US Dollars OR type (Q) to quit: "))

        if ans=='U':
            dollars()
        
        elif ans=='R':
            rupee()

        elif ans=="Q":
            quit()    
        
        else:
            print("Please Type Either (U) OR (R) OR (Q)")    


