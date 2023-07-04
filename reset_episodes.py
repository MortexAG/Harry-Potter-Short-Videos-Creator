import os
import shutil
import glob

os.remove("episodes.db")
os.remove("stored_spells.db")

for databases in glob.glob("./databases/*"):
    shutil.copy("./databases/episodes.db", "../")
    shutil.copy("./databases/stored_spells.db", "../")