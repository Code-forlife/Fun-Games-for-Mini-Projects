def water_jug_problem():
    jug1 = 0  # Initial amount of water in Jug 1
    jug2 = 0  # Initial amount of water in Jug 2
    capacity_jug1 = 4  # Capacity of Jug 1
    capacity_jug2 = 3  # Capacity of Jug 2

    print(f"Jug 1 ({capacity_jug1} liters)   Jug 2 ({capacity_jug2} liters)")

    while True:
        print(f"Current state: Jug 1 ({jug1} liters)   Jug 2 ({jug2} liters)")

        action = input("Enter an action (e.g., 'fill 1', 'fill 2', 'pour 1 to 2', 'pour 2 to 1', 'empty 1', 'empty 2', 'quit'): ").lower()

        if action == 'quit':
            break
        elif action.startswith('fill 1'):
            jug1 = capacity_jug1
        elif action.startswith('fill 2'):
            jug2 = capacity_jug2
        elif action.startswith('pour 1 to 2'):
            amount_to_pour = min(jug1, capacity_jug2 - jug2)
            jug1 -= amount_to_pour
            jug2 += amount_to_pour
        elif action.startswith('pour 2 to 1'):
            amount_to_pour = min(jug2, capacity_jug1 - jug1)
            jug2 -= amount_to_pour
            jug1 += amount_to_pour
        elif action.startswith('empty 1'):
            jug1 = 0
        elif action.startswith('empty 2'):
            jug2 = 0
        else:
            print("Invalid action. Please try again.")

        # Check if Jug 1 or Jug 2 has exactly 2 liters, and if so, the problem is solved.
        if jug1 == 2 or jug2 == 2:
            print('''
            
   _____ _                 _                     _     
  / ____| |               | |                   | |    
 | (___ | |__   __ _  __ _| |__   __ _  __ _ ___| |__  
  \___ \| '_ \ / _` |/ _` | '_ \ / _` |/ _` / __| '_ \ 
  ____) | | | | (_| | (_| | |_) | (_| | (_| \__ \ | | |
 |_____/|_| |_|\__,_|\__,_|_.__/ \__,_|\__,_|___/_| |_|
                                                       
                                                       
                                 
''')
            print("Congratulations! You have exactly 2 liters of water in one of the jugs. Problem solved!")
            break

if __name__ == "__main__":
    print('''
    
 _    _       _                ___              ______          _     _                
| |  | |     | |              |_  |             | ___ \        | |   | |               
| |  | | __ _| |_ ___ _ __      | |_   _  __ _  | |_/ / __ ___ | |__ | | ___ _ __ ___  
| |/\| |/ _` | __/ _ \ '__|     | | | | |/ _` | |  __/ '__/ _ \| '_ \| |/ _ \ '_ ` _ \ 
\  /\  / (_| | ||  __/ |    /\__/ / |_| | (_| | | |  | | | (_) | |_) | |  __/ | | | | |
 \/  \/ \__,_|\__\___|_|    \____/ \__,_|\__, | \_|  |_|  \___/|_.__/|_|\___|_| |_| |_|
                                          __/ |                                        
                                         |___/                                         
    ''')
    print("Get exactly 2 liters of water in either jug.")
    water_jug_problem()
