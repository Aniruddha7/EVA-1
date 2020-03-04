**TINY YOLO_V3 USING CUSTOM DATASET**

Here is the implementation of Tiny Yolo_V3 for detecting the object of your own choice. In this age of Data science, Google colaboratory is a boon which gives free access to GPUs and upto 13GB of RAM to anyone having google account but for this project CUDA needs to be installed. Please refer [&lt;this&gt;](https://colab.research.google.com/github/ShimaaElabd/CUDA-GPU-Contrast-Enhancement/blob/master/CUDA_GPU.ipynb#scrollTo=h7lbKJvm-SLG) link for more info 

**The following are the steps to detect the object using Tiny_YoloV3**

Prepare the data by downloading the images of your own choice

Split the dataset into train-test 

Calculate anchor boxes for the data

Modify the configuration(*.cfg*) file according to the number of classes in the dataset (in this implementation, only one class is present to detect)

Make a zip folder of this data and upload to Google drive

In Colab environment, mount Google drive and unzip this folder and train the model

Test the model with predictions.png since DarkNet was not compiled with OpenCV. Hence it cannot display detection directly.

Run this on any video file and save the mp4 format













![Yolo_Ferrari](Ferrari.gif)
