# DALP: Diffusion based Active Lesion Prediction Model

## Short Description:
```
Diffusion probabilistic models are generative AI models, capable of generating high fidelity images. By gradually adding noise to the input data (forward diffusion), and learning to generate the input
from noise (reverse diffusion), DPMs have achieved state of the art performance in image generation. We used a DPM to predict active MS lesions similar to subtract pre-and post contrast T1 weighted
images (ground truth). We performed leave one out K-fold cross validation for training and validation of DPM. To measure the overlap between predicted and ground truth active lesions, we used Dice
Similarity (DS). 
```


## Image-to-Image Translation
<img width="866" alt="Screenshot 2024-01-31 at 2 45 55 PM" src="https://github.com/Wazhee/Active-Lesion-Prediction-with-Diffusion/assets/34732790/11798bc7-577c-41b9-9eb3-5718fe1b6b92">

## Example Results
<p align="center">
  <img width="599" alt="Screenshot 2024-01-31 at 2 48 59 PM" src="https://github.com/Wazhee/Active-Lesion-Prediction-with-Diffusion/assets/34732790/af01a4b3-c398-4a9d-9da2-e9dac11e51eb">
</p>


## Training DALP Model
```yaml
python main.py --train --config ./configs/configfilename.yaml --result_path ./save/directory/ --gpu_ids 0
```

## Testing DALP Model
```yaml
python main.py --config ./configs/configfilename.yaml --result_path ./save/directory/ --resume_model ./save/directory/BrownianBridge/checkpoint/checkpoint_name.pth --gpu_ids 0
```

## Evaluating DALP Model
```yaml
python main.py --evaluate --maskpath path/to/annotations/ --config ./configs/configfilename.yaml --result_path ./save/directory/ --resume_model ./save/directory/BrownianBridge/checkpoint/checkpoint_name.pth --gpu_ids 0
```

For datasets that have paired image data, the path should be formatted as:
```yaml
your_dataset_path/train/A  # training reference
your_dataset_path/train/B  # training ground truth
your_dataset_path/val/A  # validating reference
your_dataset_path/val/B  # validating ground truth
your_dataset_path/test/A  # testing reference
your_dataset_path/test/B  # testing ground truth
```


We used Diffusion Probabilistic Model proposed by Bo Li et al 2023, referenced below



```
@inproceedings{li2023bbdm,
  title={BBDM: Image-to-image translation with Brownian bridge diffusion models},
  author={Li, Bo and Xue, Kaitao and Liu, Bin and Lai, Yu-Kun},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={1952--1961},
  year={2023}
}
```
