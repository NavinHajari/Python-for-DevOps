import subprocess

def exec_cmd(command) :
    process = subprocess.run(command,
                             shell=True,
                             check=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                            )

    return process.stdout.decode()

print(exec_cmd("ls"))

