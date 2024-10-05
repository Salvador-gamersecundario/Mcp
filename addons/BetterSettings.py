def replace_line(line_number, new_text):

    try:
        
        with open("servidor_minecraft/server.properties", 'r') as f:
            lines = f.readlines()
        
        if line_number > len(lines):
            print(f"The line {line_number} don't exist.")
            return
        
        lines[line_number - 1] = new_text + '\n'
        
        with open("servidor_minecraft/server.properties", 'w') as f:
            f.writelines(lines)
        
    except FileNotFoundError:
        print(f"The file don't exist.")
    except Exception as e:
        print(f"A erorr ocurred: {e}")

def nombreservidor():
    servername = input("")
    new_text="motd=" + servername
    replace_line(32, new_text)
    
def premium():
        nopremium = int(input(""))
        if nopremium == 1:
            new_text="online-mode=false"
            replace_line(34, new_text)
            
        if nopremium == 2:
            new_text="online-mode=true"
            replace_line(34, new_text)
        
def dificultad():
    difficulty = int(input(""))
    if difficulty == 1:
        new_text="difficulty=peaceful"
        replace_line(7, new_text)
        
    if difficulty == 2:
            new_text="difficulty=easy"
            replace_line(7, new_text)
            
    if difficulty == 3:
        new_text="difficulty=normal"
        replace_line(7, new_text)
        
    if difficulty == 4:
        new_text="difficulty=hard"
        replace_line(7, new_text)
        

def modopvp():
    pvp = int(input(""))
    if pvp == 1: 
            new_text="pvp=true"
            replace_line(38, new_text)
            
    if pvp == 2: 
            new_text="pvp=false"
            replace_line(38, new_text)
        
def modoharcore():
    hardcore = int(input(""))   
    if hardcore == 1:
        new_text="hardcore=true"
        replace_line(21, new_text)
                
    if hardcore == 2:
        new_text="hardcore=false"
        replace_line(21, new_text)