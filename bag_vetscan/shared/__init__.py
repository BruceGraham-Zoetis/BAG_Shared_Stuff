import os
import sys

# have to do this so connexion backend finds the channel files
# https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
sys.path.append(os.path.dirname(__file__))

