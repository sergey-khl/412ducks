import cv2
import numpy as np
from time import sleep


def gst_pipeline_string():
    # Parameters from the camera_node
    # Refer here : https://github.com/duckietown/dt-duckiebot-interface/blob/daffy/packages/camera_driver/config/jetson_nano_camera_node/duckiebot.yaml
    res_w, res_h, fps = 640, 480, 30
    fov = 'full'
    # find best mode
    camera_mode = 3  # 
    # compile gst pipeline
    gst_pipeline = """ nvarguscamerasrc sensor-mode=3 exposuretimerange="100000 80000000" ! video/x-raw(memory:NVMM), width=640, height=480, format=NV12, framerate=30/1 ! nvjpegenc !  appsink"""
    # ---
    print("Using GST pipeline: {}".format(gst_pipeline))
    return gst_pipeline


cap = cv2.VideoCapture()
cap.open(gst_pipeline_string(), cv2.CAP_GSTREAMER)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Put here your code!
    # You can now treat output as a normal numpy array
    # Do your magic here
    print(ret, frame)
    sleep(1)