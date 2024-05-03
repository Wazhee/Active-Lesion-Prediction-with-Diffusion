import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import csv 
import pandas as pd
from scipy import ndimage
import scipy.ndimage.morphology as morpho

class ImageEvaluator:
    def __init__(self, exp_path, dim, version, mask_path):
        self.exp_path = exp_path
        self.dim = dim
        self.version = version
        self.mask_path = mask_path
        self.thresholds = {"gt": 148, "pred": 140}
        self.mask_arr = []
        self.gt_arr = []
        self.pred_arr = []
        self.id_arr = []
        self.dice_scores = {}

    def load_images(self):
        res = self.dim[0]
        # might need to change according to actual project structure
        path2directory = self.exp_path
        maskpath = self.mask_path

        for folder in os.listdir(path2directory):
            try:
                names = os.listdir(f'{path2directory}{folder}/test_sample/')
                names.sort()
                id = names[-3].split(')_')[0][2:-2]
                self.gt_arr.append(np.array(Image.open(f'{path2directory}{folder}/test_sample/{names[1]}').convert('L')))
                self.pred_arr.append(np.array(Image.open(f'{path2directory}{folder}/test_sample/{names[-3]}').convert('L')))
                print(f'{maskpath}v{self.version}/{id}.png')
                # self.mask_arr.append(np.array(Image.open(f'{maskpath}/v{self.version}/{id}.png').convert('L')))
                mask = np.array(Image.open(f'{maskpath}v{self.version}/{id}.png').convert('L'))
                self.mask_arr.append(cv2.resize(mask, (self.dim[0], self.dim[0]), interpolation = cv2.INTER_LANCZOS4))
                self.id_arr.append(id)
            except:
                print("invalid path")

    def evaluate_all_images(self):
        for idx in range(len(self.mask_arr)):
            mask, gt, pred = self.mask_arr[idx] > 0, self.gt_arr[idx], self.pred_arr[idx]
#             print("pred shape:", pred.shape)
            print("mask shape:", mask.shape)
#             print("gt shape:", gt.shape)
            pfinal, gfinal = (pred > self.thresholds['pred']) * (mask), (gt > self.thresholds['gt']) * (mask)
            print(pfinal, gfinal)
            self.dice_scores[self.id_arr[idx]] = self.dice(pfinal, gfinal)

        for id in self.id_arr:
            print(id, self.dice_scores[id])

    def evaluate_single_image(self, idx):
        mask, gt, pred = self.mask_arr[idx] > 0, self.gt_arr[idx], self.pred_arr[idx]
        pfinal, gfinal = (pred > self.thresholds['pred']) * (mask), (gt > self.thresholds['gt']) * (mask)

        return f'{self.id_arr[idx]}: {self.dice(pfinal, gfinal)}'

    def dice(self, y_true, y_pred):
        y_true, y_pred = y_true > 0, y_pred > 0
        # print(y_true, y_pred)
        intersection = np.sum(y_true * y_pred)
        # print(intersection)
        return (2. * intersection) / (np.sum(y_true) + np.sum(y_pred))


class Menu:
    def __init__(self):
        self.choice = -1

    def display_menu(self):
        menu = [
            "   Please choose from the following options:  ",
            "   (1) evaluate all images   ",
            "   (2) evaluate a single slice  ",
            "   (3) Change version  ",
            "   (4) save results  "
        ]
        width = int(60)
        print('+-' + '-' * width + '-+')
        for item in menu:
            line = "|" + item
            ending = width - len(line) + 3
            print(line + " " * ending + "|")
        print('+-' + '-' * (width) + '-+')
        self.choice = int(input("Enter Choice: "))

    def get_choice(self):
        return self.choice


def main():
    exp_path = "./results/Augmentation Ablation/"
    dim = [256, 256]
    version = 1
    evaluator = ImageEvaluator(exp_path, dim, version)
    menu = Menu()

    while(menu.get_choice() < 5):
        menu.display_menu()

        if menu.choice == 1:
            evaluator.load_images()
            evaluator.evaluate_all_images()

        elif menu.choice == 2:
            if not evaluator.mask_arr:
                evaluator.load_images()
            idx = int(input("Which image would you like to evaluate?: "))
            print(evaluator.evaluate_single_image(idx))

        elif menu.choice == 3:
            if version == 4:
                version = 1
            else:
                version += 1
            evaluator.version = version
            evaluator.mask_arr = []
            evaluator.gt_arr = []
            evaluator.pred_arr = []
            evaluator.id_arr = []

        elif menu.choice == 4:
            try:
                evaluator.create_csv(evaluator.dice_scores, dim[0], version)
                subject_scores = {}
                for id in evaluator.id_arr:
                    subject = id.split('_')[0]
                    if subject in subject_scores:
                        subject_scores[subject].append(evaluator.dice_scores[id])
                    else:
                        subject_scores[subject] = [evaluator.dice_scores[id]]

                for subject in subject_scores:
                    subject_scores[subject] = sum(subject_scores[subject]) / len(subject_scores[subject])
                evaluator.create_csv(subject_scores, dim[0], version * 10)
            except:
                print("Please ensure all variables are defined first")
            break


if __name__ == "__main__":
    main()
