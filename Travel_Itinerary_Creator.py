print("Welcome to the Travel Itinerary Creator!")
    
    ###### User detail #####
name = input("Enter your name: ")
age = int(input("Enter your age: "))
destination = input("Where are you traveling to? :-")
budget = float(input("What's your total travel budget? :- "))
    
    #### Hotel details####
print("Choose a hotel type:")
print("1. taj Hotel (5000 per night)")
print("2. oyo Hotel (1000 per night)")
print("3. Luxury Hotel (2000 per night)")
hotel_choice = int(input("Enter the number of your choice: "))
    
if hotel_choice == 1:
    hotel_cost =5000
    hotel_type ="Budget Hotel"
elif hotel_choice== 2:
    hotel_cost =1000
    hotel_type="Standard Hotel"
elif hotel_choice ==3:
    hotel_cost =2000
    hotel_type ="Luxury Hotel"
else:
    print("Invalid choice. Defaulting to Budget Hotel.")
    hotel_cost =1000
    hotel_type ="Budget Hotel"
    
    ##### Number of nights#####
nights = int(input("How many nights will you stay? "))
total_hotel_cost = hotel_cost * nights
    
remaining_budget=budget -total_hotel_cost
    
print("--- Travel Budget Summary ---")
print("Name",name)
print("Age:",age)
print("Destination: ",destination)
print("Hotel Type: ",hotel_type)
print("Number of Nights: ",nights)
print("Total Hotel Cost: ",total_hotel_cost)
    
if remaining_budget >= 0:
    print("Remaining Budget: ",remaining_budget)
    print("You are within your budget.")
else:
    print("Over Budget by: ",remaining_budget)
    print("You need to adjust your budget.")
    
