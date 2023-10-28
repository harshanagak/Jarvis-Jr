import tkinter
import subprocess

class CLIWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('CLI')

        self.text_box = tkinter.Text(self)
        self.text_box.pack()

        self.button = tkinter.Button(self, text='Create File', command=self.create_file)
        self.button.pack()

    def create_file(self):
        command = "echo. > s.txt"  # Command to create the file 's.txt' using 'echo.' on Windows
        # For Unix-based systems, use: 'touch s.txt'

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()

        if output:
            self.text_box.insert('end', f"Output: {output}\n")
        if error:
            self.text_box.insert('end', f"Error: {error}\n")

if __name__ == '__main__':
    window = CLIWindow()
    window.mainloop()
