print("AWS Re-Start: Lab-15")

import os
import subprocess

print("---> Example os.system(): ")
os.system("ls")

print("---------------------------")

print("---> Example subprocess.run(): ")
subprocess.run(["ls"])

print("---------------------------")

print("---> Example subprocess.run([]): ")

subprocess.run(["ls","-l"])

print("---------------------------")

print("---> Example subprocess.run([README.md]): ")

subprocess.run(["ls","-l","README.md"])

print("###########################")

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

