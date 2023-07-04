import os
import shutil
import glob

os.remove("episodes.db")
os.remove("stored_spells.db")

shutil.copy("./databases/episodes.db", "./")
shutil.copy("./databases/stored_spells.db", "./")