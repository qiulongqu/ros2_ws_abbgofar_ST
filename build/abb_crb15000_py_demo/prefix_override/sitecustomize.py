import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yunhao/ros2_ws_abbgofar/install/abb_crb15000_py_demo'
