import os
import sys
from app import application     # NOQA

 #1. Add current directory to path, if isn't already
cmd_folder = os.path.dirname(os.path.abspath(__file__))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
