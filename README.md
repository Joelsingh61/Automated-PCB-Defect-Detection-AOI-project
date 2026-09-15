
# Automated PCB Defect Detection & AOI

An AI-based **Automated Optical Inspection (AOI)** system for detecting and classifying common Printed Circuit Board (PCB) manufacturing defects using **YOLO26n** and computer vision.

##  Project Overview

Manual PCB inspection can be time-consuming and may be affected by human fatigue and inconsistency.

This project develops an automated PCB inspection system that analyzes PCB images and detects manufacturing defects using a trained YOLO object-detection model.


##  Inspection Pipeline

PCB Image
    ↓
Image Preprocessing
    ↓
YOLO26n Object Detection
    ↓
Defect Classification
    ↓
Defect Localization
    ↓
Confidence Score
    ↓
Quality Inspection
## Objectives
Automate PCB visual inspection using computer vision
Detect common PCB manufacturing defects
Classify defects into different categories
Localize defects using bounding boxes
Measure model performance using precision, recall and mAP
Demonstrate the use of AI in electronics manufacturing quality inspection
## Defects Detected
The model detects six PCB defect classes:

Class	Defect
0	Open
1	Short
2	Mousebite
3	Spur
4	Pin-hole
5	Spurious Copper
## Dataset
The project uses the DeepPCB dataset.

Dataset	Images
Training	1,200
Validation	150
Testing	150
Total	1,500

The test set contains 1,005 annotated defect instances.
## Model Used
A lightweight YOLO26n object-detection model was trained to detect and classify PCB defects.

The model provides:

Defect classification
Defect localization
Confidence scores
Multiple defect detection in a single PCB image
## Results
The trained model was evaluated on 150 previously unseen test images.

Metric	Result
Precision	96.4%
Recall	92.6%
mAP@50	97.9%
mAP@50–95	74.6%
Test Images	150
Defect Instances	1,005

Confusion Matrix

<img width="3000" height="2250" alt="image" src="https://github.com/user-attachments/assets/2a964a4f-d5f6-4286-8eda-755c66b7f07f" />

