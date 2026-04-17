import os
import time

# Khai báo các module
from Services import *
from Config import *
from State import *
from Cache import *
from Utils import *
from CombatEngine import *
from SilentAim import *
from Visuals import *
from LagFixer import *
from FakeLag import *
from MaruUI import *

# Hàm main để cập nhật và vẽ tất cả các phần của dự án
def main():
    # Cập nhật trạng thái của dự án
    update_state()

    # Vẽ tất cả các phần của dự án
    draw_all()

    # Cập nhật và vẽ lại sau một khoảng thời gian
    time.sleep(1 / 60)
    main()

# Chạy hàm main
main()
