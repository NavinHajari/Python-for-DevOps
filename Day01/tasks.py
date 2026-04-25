import os
print(os.uname().sysname)

def check_os():
    if os.uname().sysname == "Darwin":
        print("Switch to Linux")

    elif opsystem == "Linux" or opsystem == "Mac":
        print("You are good to go")


# for i in range(1,2):
    check_os("Darwin")
