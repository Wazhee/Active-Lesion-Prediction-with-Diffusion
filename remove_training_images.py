import shutil
import os

PATH="/projects/vb21/jiezy/ELEC542/BBDM/"

def remove_training_samples(path):
    folders = os.listdir(path)
    folders = [x for x in folders if x != '.DS_Store']
    for folder in folders:
        path_to_samples = f'{path}{folder}/'
        files = os.listdir(f'{path_to_samples}')
        try:
            files.remove('.DS_Store')
        except:
            None
        for file in files:
            if(file != 'val_sample'):
                try:
                    shutil.rmtree(f'{path_to_samples}{file}')
                except:
                    os.remove(f'{path_to_samples}{file}')

image_path = "/pre2post/BrownianBridge/image/"
experiments = os.listdir(PATH)
experiments = [x for x in experiments if "experiment" in x]
for folder in experiments:
    try:
        remove_training_samples(f'{PATH}{folder}{image_path}')
    except:
        None