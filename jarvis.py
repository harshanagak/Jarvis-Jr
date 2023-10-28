import tkinter
import subprocess


class CLIWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('CLI')

        self.text_box = tkinter.Text(self)
        self.text_box.pack()

        self.entry = tkinter.Entry(self)
        
        self.entry.pack()

        self.button = tkinter.Button(self, text='Run Command', command=self.run_command)
        self.button.pack()

    def run_command(self):
        
        command = self.entry.get()  # Get the command entered by the user
        # print(command)


        if command:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate()

            if output:
                self.text_box.insert('end', f"Output: {output}\n")
            if error:
                self.text_box.insert('end', f"Error: {error}\n")

if __name__ == '__main__':
    window = CLIWindow()
    window.mainloop()
