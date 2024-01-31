import os

apath= "/projects/vb21/jiezy/ELEC542/BBDM-256/val/A"
bpath= "/projects/vb21/jiezy/ELEC542/BBDM-256/val/B"
a_images, b_images = os.listdir(apath), os.listdir(bpath)

for x in a_images:
    if(x not in b_images):
        print(x, y, " dont match")

if(".DS_Store" in a_images and ".DS_Store" in b_images):
    print(".DS_Store found BBDM-256 images")


apath= "/projects/vb21/jiezy/ELEC542/BBDM/datasets/BBDM dataset/val/A"
bpath= "/projects/vb21/jiezy/ELEC542/BBDM/datasets/BBDM dataset/val/B"
a_images, b_images = os.listdir(apath), os.listdir(bpath)

for x in a_images:
    if(x not in b_images):
        print(x, y, " dont match")

if(".DS_Store" in a_images and ".DS_Store" in b_images):
    print(".DS_Store found BBDM-256 images")