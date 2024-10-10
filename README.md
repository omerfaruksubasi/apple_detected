# Apple Detection and Segmentation using YOLOv8

This repository demonstrates **apple detection and segmentation** using the **YOLOv8** model. YOLOv8 is the latest version of the You Only Look Once (YOLO) family of algorithms, which is well-known for its real-time object detection capabilities. In this project, we use YOLOv8 for segmenting apples from images, helping us not only detect their presence but also outline their exact locations.

## What is Image Segmentation?

**Image Segmentation** is a computer vision technique used to partition an image into meaningful parts or regions. It helps identify specific objects in the image by classifying every pixel to a particular label. In this project, the goal is to segment apples from their background, which allows for precise identification and analysis of each individual apple.

Segmentation is useful in several scenarios:
- **Object Localization**: Finding the exact boundary of an object (e.g., an apple).
- **Count Estimation**: Counting the number of objects in an image.
- **Detailed Analysis**: Studying the shape, size, or color of objects more precisely.

There are different types of segmentation:
- **Semantic Segmentation**: Classifies each pixel in the image into a class, treating all objects of the same type as one.
- **Instance Segmentation**: Similar to semantic segmentation but treats each instance of an object independently, allowing differentiation between multiple apples in an image.

In this project, we use instance segmentation to identify and differentiate multiple apples in the image.

## YOLOv8 Overview

**YOLOv8** is the latest version of the YOLO (You Only Look Once) object detection model, released by Ultralytics. YOLOv8 incorporates advancements from previous YOLO models and is designed to improve both accuracy and speed. It supports various tasks, such as:

- **Object Detection**: Identifying objects and drawing bounding boxes around them.
- **Instance Segmentation**: Detecting objects and providing precise masks to segment each object.
- **Pose Estimation**: Estimating key points for human pose analysis.

In this project, YOLOv8 is used for **instance segmentation** to detect apples and generate a mask for each detected apple.

### Key Features of YOLOv8:
1. **Real-Time Performance**: YOLOv8 is optimized for speed and accuracy, making it suitable for real-time applications.
2. **Improved Architecture**: It has a more flexible and lightweight architecture compared to previous versions, resulting in better performance.
3. **Multitasking Capabilities**: YOLOv8 can handle object detection, segmentation, and pose estimation tasks.

## How Does YOLOv8 Perform Segmentation?

YOLOv8 uses an improved network architecture to learn the features of objects at different scales. For segmentation, YOLOv8 adds a **segmentation head** that outputs masks for each detected object. The process can be broken down into several steps:

1. **Object Detection**: YOLOv8 first detects apples in the image, drawing bounding boxes around them.
2. **Mask Prediction**: Once the objects are detected, a segmentation head generates a mask for each bounding box, outlining the precise shape and boundaries of the detected apples.

The output is an image where each apple is not only detected but also segmented, allowing us to distinguish between individual apples.

## Dataset

The dataset used for this project consists of images containing apples in various environments, such as orchards or markets. Each image is labeled with bounding boxes and masks that indicate the presence of apples, allowing the YOLOv8 model to learn how to detect and segment apples effectively.

## Installation

To use this repository and run the code, you'll need to install the necessary dependencies. Follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/omerfaruksubasi/apple_detected.git

3. Navigate to the repository folder:
   
   ```bash
   cd apple_detected

4. Create a virtual environment and activate it:
   
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

5. Install the required packages:
   
   ```bash
   pip install -r requirements.txt

##Running YOLOv8 for Apple Detection
To detect and segment apples using YOLOv8, follow these steps:

1. Training the Model: If you want to train YOLOv8 on your own dataset, you can modify the dataset path in the configuration file and run:

   ```bash
   yolo train model=yolov8-seg.pt data=apple_dataset.yaml epochs=50 imgsz=640
3. Running Inference: To detect apples in an image or video using a pre-trained model, use the following command:

   ```bash
   yolo predict model=best.pt source=apple_images/ save=True
This command will run inference on the images in the apple_images/ directory, and save the results with the detected apples segmented.

## Results
The following image shows an example of apple detection and segmentation using YOLOv8:

!(apple_segmantion_ressult.png)(https://github.com/omerfaruksubasi/apple_detected/blob/main/path_to_save_output.jpg)

In this image, each detected apple is outlined with a mask, allowing for precise identification and localization. The segmentation helps in applications where understanding the exact location and size of the apples is crucial, such as in automated harvesting or quality control.
