import os 

path="./Kfold/"
for i in range(10):
    # clean split folder
    fullpath = f"{path}{i}/"
    if(os.path.exists(f"{fullpath}.DS_Store")):
        os.remove(f"{fullpath}.DS_Store")

    # clean train test val folders
    traindepth2=f"{fullpath}train/"
    if(os.path.exists(f"{traindepth2}.DS_Store")):
       os.remove(f"{traindepth2}.DS_Store")
    testdepth2=f"{fullpath}test/"
    if(os.path.exists(f"{testdepth2}.DS_Store")):
       os.remove(f"{testdepth2}.DS_Store")
    valdepth2=f"{fullpath}val/"
    if(os.path.exists(f"{valdepth2}.DS_Store")):
       os.remove(f"{valdepth2}.DS_Store")
   
    # clean train A B folders
    A=f"{traindepth2}A/"
    if(os.path.exists(f"{A}.DS_Store")):
       os.remove(f"{fullpath}.DS_Store")
    B=f"{traindepth2}B/"
    if(os.path.exists(f"{B}.DS_Store")):
       os.remove(f"{fullpath}.DS_Store")
    # clean test A B folders
    A=f"{testdepth2}A/"
    if(os.path.exists(f"{A}.DS_Store")):
       os.remove(f"{A}.DS_Store")
    B=f"{testdepth2}B/"
    if(os.path.exists(f"{B}.DS_Store")):
       os.remove(f"{B}.DS_Store")
    # clean val A B folders
    A=f"{valdepth2}A/"
    if(os.path.exists(f"{A}.DS_Store")):
       os.remove(f"{A}.DS_Store")
    B=f"{valdepth2}B/"
    if(os.path.exists(f"{B}.DS_Store")):
       os.remove(f"{B}.DS_Store")
    
