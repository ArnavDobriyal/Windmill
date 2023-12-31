# Windmill Corrosion Detection using YOLOv8

## Overview

This repository contains the code for training and deploying a YOLOv8 model for detecting corrosion in windmill images. The model is trained using transfer learning on a dataset annotated using CVAT.ai.

## Dataset

The dataset consists of 641 training images and 60 validation images. The dataset is organized as follows:

dataset/

|-- images/

| |-- train/

| | |-- image1.jpg

| | |-- image2.jpg

| |-- val/

| | |-- image3.jpg

| | |-- image4.jpg

|-- labels/

| |-- train/

| | |-- image1.txt

| | |-- image2.txt

| |-- val/

| | |-- image3.txt

| | |-- image4.txt

## Training

The YOLOv8 model is trained using transfer learning, starting from pre-trained weights. The training script, configuration files, and details can be found in the `train` directory.

## Results

the graphs:

![results](https://github.com/ArnavDobriyal/Windmill/assets/120387628/73481743-901a-4a3f-b3b9-5994015f53fb)

the following is the example image of trainig batch:

![train_batch0](https://github.com/ArnavDobriyal/Windmill/assets/120387628/2cdc5ba6-80dc-496e-a74b-4654ed064054)

the following is the validation batch:

![image](https://github.com/ArnavDobriyal/Windmill/assets/120387628/1731db37-d1d7-4b26-9852-57e24d2cb670)

the following is the predicted batch:

![image](https://github.com/ArnavDobriyal/Windmill/assets/120387628/0d2ef35b-012a-4ed7-a3fc-d5eaf79814bf)

Overall Metrics:

Precision (P): 0.667
Recall (R): 0.344

Class-wise Metrics:

Corrosion:
Precision: 0.817
Recall: 0.195

Cracks:
Precision: 0.611
Recall: 0.17

Normal:
Precision: 0.571
Recall: 0.667


## Potential Improvements

Increased Epochs: Due to computational constraints, the number of epochs was limited. Consider training for more epochs if resources permit.

Enhanced Annotations: Ensure high-quality annotations and refine or add more annotations for improved model accuracy.

Ensembling: Experiment with model ensembling by combining predictions from multiple models for enhanced overall performance.





 
