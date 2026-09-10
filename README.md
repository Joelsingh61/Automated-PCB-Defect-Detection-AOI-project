# Automated PCB Defect Detection & AOI

An AI-based **Automated Optical Inspection (AOI)** system for detecting and classifying common Printed Circuit Board (PCB) manufacturing defects using **YOLO26n** and computer vision.

##  Project Overview

Manual PCB inspection can be time-consuming and may be affected by human fatigue and inconsistency.

This project develops an automated PCB inspection system that analyzes PCB images and detects manufacturing defects using a trained YOLO object-detection model.

### Inspection Pipeline

```text
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

🎯 Objectives
Automate PCB visual inspection using computer vision
Detect common PCB manufacturing defects
Classify defects into different categories
Localize defects using bounding boxes
Measure model performance using precision, recall and mAP
Demonstrate the use of AI in electronics manufacturing quality inspection
🧠 Defects Detected

The model detects six PCB defect classes:

Class	Defect
0	Open
1	Short
2	Mousebite
3	Spur
4	Pin-hole
5	Spurious Copper
📊 Dataset

The project uses the DeepPCB dataset.

Dataset	Images
Training	1,200
Validation	150
Testing	150
Total	1,500

The test set contains 1,005 annotated defect instances.

🤖 Model
YOLO26n

A lightweight YOLO26n object-detection model was trained to detect and classify PCB defects.

The model provides:

Defect classification
Defect localization
Confidence scores
Multiple defect detection in a single PCB image
📈 Model Performance

The trained model was evaluated on 150 previously unseen test images.

Metric	Result
Precision	96.4%
Recall	92.6%
mAP@50	97.9%
mAP@50–95	74.6%
Test Images	150
Defect Instances	1,005
Per-Class Performance
Defect	Precision	Recall	mAP@50	mAP@50–95
Open	96.0%	95.2%	98.3%	66.2%
Short	98.0%	89.8%	96.8%	66.0%
Mousebite	96.6%	90.6%	97.9%	72.6%
Spur	90.2%	90.3%	96.2%	70.9%
Pin-hole	99.7%	95.3%	99.2%	88.4%
Spurious Copper	97.9%	94.3%	98.9%	83.7%
📉 Training Results

Training and evaluation results are available in the defect_detector-3 directory.

Training Results

Confusion Matrix

Normalized Confusion Matrix

Precision-Recall Curve

F1 Curve

🔎 Sample Detection

The trained model was tested on the complete 150-image test set.

Example output:

PCB Image
    ↓
YOLO26n
    ↓
1 Open
1 Short
3 Mousebites
3 Spurs

Another example:

PCB Image
    ↓
YOLO26n
    ↓
2 Opens
3 Shorts
1 Mousebite
1 Spur
2 Pin-holes

The system provides:

Defect type
Bounding-box location
Detection confidence
Number of detected defects
⚙️ Technology Stack
Programming
Python
Machine Learning
YOLO26n
Ultralytics
PyTorch
Computer Vision
OpenCV
Pillow
Data Analysis
Pandas
Matplotlib
Development
Kaggle GPU
Git
GitHub
🏗️ System Architecture
                 PCB IMAGE
                     │
                     ▼
          ┌───────────────────┐
          │ Image Processing  │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │     YOLO26n       │
          │ Object Detection  │
          └─────────┬─────────┘
                    │
             ┌──────┴──────┐
             ▼             ▼
       Defect Class    Bounding Box
             │             │
             └──────┬──────┘
                    ▼
           Confidence Score
                    │
                    ▼
            Quality Decision
                    │
             ┌──────┴──────┐
             ▼             ▼
           PASS           FAIL
                           │
                           ▼
                   Defect Information
