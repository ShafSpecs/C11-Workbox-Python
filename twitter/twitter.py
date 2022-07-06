from utils import *
from colors import yellow, reset

welcome_message()
command = input(f"{yellow}>>> {reset}")

command_engine(command)
