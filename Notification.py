# Debugging Messages 
def Info(string, end="\n"): print(f"\033[92m{'[INFO]: '}\033[00m{string}", end=end)
def Warning(string, end="\n"): print(f"\033[93m{'[WARN]: '}\033[00m{string}", end=end)
def Error(string, end="\n"): print(f"\033[91m{'[ERROR]: '}\033[00m{string}", end=end)
def User(string, end="\n"): print(f"\033[94m{'[USER]: '}\033[00m{string}", end=end)
def User_input(string): return input(f"\033[94m{'[INPUT]: '}\033[00m{string}")