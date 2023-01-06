print(''' ************** SPEED/TIME/DISTANCE CALCULATOR ************** ''')

while(True):
    calculator_options = int(input("\nEnter the 0 for Speed Calculator, 1 for Time Calculator & 2 Distance Calculator : "))

    if calculator_options==0:
        hours = int(input("Enter the Hours : "))
        minutes = int(input("Enter the Minutes : "))/60
        distance = float(input("Enter the distance in KM : "))

        time = hours+minutes
        speed = distance/time

        print("\nThe Average Speed of the vehicle in the travel is", round(speed), "KM/H")
        break


    elif calculator_options==1:
        distance = float(input("Enter the distance in KM : "))
        speed = float(input("Enter the speed in KM/H : "))

        time = distance/speed
        hours = int(time)
        minutes = round((time%1)*60)

        print(f"\nThe Time take by vehicle in the travel is {hours} Hours and {minutes} Minutes")
        break


    elif calculator_options==2  :
        hours = int(input("Enter the Hours : "))
        minutes = int(input("Enter the Minutes : "))/60
        speed = float(input("Enter the speed in KM/H : "))

        time = hours+minutes
        distance = round(speed*time, 1)

        print(f"\nThe Distance traveled by vehicle is {distance} KM")
        break
    

    else:
        print("You Entered Wrong Number Please Enter 0, 1 or 2 for calculating speed, time and distance respectively. Try Again!!")

