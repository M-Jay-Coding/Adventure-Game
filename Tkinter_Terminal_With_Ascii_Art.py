import time
import sys
import tkinter as tk

Initial_Script ="""

          _                                                                                 _                                                                           
        _(_)_                                                                              (_)                                                                          
      _(_) (_)_        _               _        _  _  _             _  _  _  _           _ (_) _  _          _         _          _       _  _           _  _  _        
    _(_)     (_)_     (_)_           _(_)      (_)(_)(_) _         (_)(_)(_)(_)_        (_)(_)(_)(_)        (_)       (_)        (_)_  _ (_)(_)         (_)(_)(_) _     
   (_) _  _  _ (_)      (_)_       _(_)         _  _  _ (_)        (_)        (_)          (_)              (_)       (_)          (_)(_)                _  _  _ (_)    
   (_)(_)(_)(_)(_)        (_)_   _(_)         _(_)(_)(_)(_)        (_)        (_)          (_)     _        (_)       (_)          (_)                 _(_)(_)(_)(_)    
   (_)         (_)          (_)_(_)          (_)_  _  _ (_)_       (_)        (_)          (_)_  _(_)       (_)_  _  _(_)_         (_)                (_)_  _  _ (_)_   
   (_)         (_)            (_)              (_)(_)(_)  (_)      (_)        (_)            (_)(_)           (_)(_)(_) (_)        (_)                  (_)(_)(_)  (_)  
                                                                                                                                                                        
                                                                                                                                                                                                                                                                      


    |''||''| '||                    /.\          ||`                          ||                              .|'''''|                           
       ||     ||                   // \\         ||                           ||                              || .                               
       ||     ||''|, .|''|,       //...\\    .|''||  \\  // .|''|, `||''|,  ''||''  '||  ||` '||''| .|''|,    || |''||  '''|.  '||),,(|,  .|''|, 
       ||     ||  || ||..||      //     \\   ||  ||   \\//  ||..||  ||  ||    ||     ||  ||   ||    ||..||    ||    || .|''||   || || ||  ||..|| 
      .||.   .||  || `|...     .//       \\. `|..||.   \/   `|...  .||  ||.   `|..'  `|..'|. .||.   `|...     `|....|' `|..||. .||    ||. `|...  
                                                                                                                                                 
                                                                                                                                             


"""


class TerminalGUI:
    def type_printA( text, delay=0.01): #This is the first Version of type print which prints in the kernel
        for char in text: #This one iterates on each character in a line 
            sys.stdout.write(char) # This part makes sure that the character prints
            sys.stdout.flush() #This one just refreshes fast enough so it prints
            time.sleep(delay) # This causes the delay in printing and the delay parameter is the time it delays for
        print()  # Move to the next line after printing
    # Example usage
    type_printA("Hello, World!")
    type_printA("Your Terminal is starting Up")
    
    def slow_print(self, text, delay = 0.05): #(THE DELAY VALUE NEEDS TO BE HIGHER This is the first Version of SLOW_print which prints in the kernel
    
        self.output_area.insert('end','')
        for char in text: #This one iterates on each character in a line 
            self.output_area.insert('end',char) # This part makes sure that the character prints Into the terminal. Remember to use 'end' as a parameter for insert's index
            self.output_area.update() #This one just refreshes fast enough so it prints
            time.sleep(delay) # This causes the delay in printing and the delay parameter is the time it delays for
        print()  # Move to the next line after printing

    def fast_print(self, text, space=""): #space means do you want new lines \n or not ? 
        if (space=='n'):
            self.output_area.insert('end',text)
        else:
            self.output_area.insert('end',text +'\n')
    def __init__(self, master):
        self.master = master
        master.title("Terminal")
        master.configure(bg='#222222')  # Set the window background color to dark grey

        # Create the text area to display output
        self.output_area = tk.Text(master, height=40, width=192, bg='#000000', fg='#FFFF00')  # Set the text area background to black and text color to yellow
        self.output_area.pack(pady=10)

        # Create the input area
        self.input_area = tk.Entry(master, width=80, bg='#000000', fg='#FFFF00')  # Set the input area background to black and text color to yellow
        self.input_area.pack(pady=10)
        self.input_area.bind('<Return>', self.process_input)
        
        
    # Example usage
    
    def process_input(self):
        # getting  the user input
        user_input = self.input_area.get()
        
        # on this line we clear the input area
        self.input_area.delete(0, tk.END)

        # Process the user input
        self.process_command(user_input)
        
        # Add a new prompt
        self.output_area.insert(tk.END, "\n>>> ", 'prompt' )
        return user_input
    def process_command(self, command):
        # Here, you can implement the logic to process the user's command
        # and generate the output to be displayed in the output area
        
        output = f"{command}"
        self.slow_print(output + '\n')
        
        ##self.output_area.insert(tk.END,  + '\n')
        self.output_area.tag_config('prompt', foreground='#FFFF00')  # Set the prompt text color to yellow
        # Start with an initial script
    def ter_initial_script(self): 
        
        self.slow_print("Initialising")
        self.slow_print("\n Welcome to Avantura : The Interactive adventure experience by 21188146 ")
        self.slow_print(Initial_Script,0.000001)
    

root = tk.Tk()
terminal = TerminalGUI(root)
terminal.ter_initial_script()
root.mainloop()
