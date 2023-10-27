# # import subprocess

# # # Run a command and capture the output
# # result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, text=True)
# # output = result.stdout

# # # Process the output
# # print(output)
# import subprocess
# from subprocess import Popen, PIPE

# cmd = 'ls'
# p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
# stdout, stderr = p.communicate()
# stdout.splitlines() 
import subprocess
file_path = "C:\\Users\\DHEERAJ KUMAR N\\OneDrive\\Desktop\\Chatgpt_01\\blank.py"
result = subprocess.run(["python",file_path], capture_output=True, text=True)

print(result.stdout)