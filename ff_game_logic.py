# Create a global variable named my_health and set it to 100 
my_health = 100 

# Create a list of 5 legendary loot items 
air_drop = ["groza", "fake item1", "level-4 vest", "fake item2", "Super-medkit"] 

# Use slicing with a step of 2 to skip fake items and extract only the 3 real items 
Extract_real_item = air_drop[::2] 

# Take that sliced 3-item list and unpack it into three separate variables 
gun, vest, heal_item = Extract_real_item 

# Create a function named last_zone_cluth 
def last_zone_cluth(): 
    # 1. Use the global keyword to get permission to modify my_health
    global my_health 
    
    # 2. Print a cool message 
    print("Enemies Spotted! using " + gun + " for the fight!") 
    
    # 3. Enemy hits you! Create damage_taken variable 
    damage_taken = 65.5 
    
    # 4. Subtract damage from my_health 
    my_health = my_health - damage_taken 
    
    # 5. Use heal_item and create heal_amount variable 
    heal_amount = 50.0 
    
    # 6. Add heal_amount to my_health 
    my_health = my_health + heal_amount 

# Call the function 
last_zone_cluth() 

# Outside the function, print the final remaining health 
# Note: Now we are directly printing the global variable 'my_health' with str()
print("BOOYAHHHHHHHhhhhhh....! left with " + str(my_health) + " hp")
# Giving any solid condition
if my_health >= 50:
    print("Your are win but minus -5")

