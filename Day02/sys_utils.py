#A class is like a Blueprint
import os
class Utils:

    def show_disk_space(self):
        print(os.system("df -h"))

    def show_ram(self):
        print(os.system("free -h"))

    def show_system_details(self):
        print(os.uname().sysname)

machine_a = Utils() # object1
machine_a.show_disk_space()

machine_b = Utils() # object2
machine_b.show_ram()

machine_c = Utils() # object3
machine_c.show_system_details()
