#!/usr/bin/env python
import sys
import time
import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image

def callback(ros_data):
    global count, ts_start
    # print(ros_data.height, ros_data.width, ros_data.encoding)
    # print(len(ros_data.data))
    image_np = np.ndarray(shape=(ros_data.height, ros_data.width, 3), dtype=np.uint8, buffer=ros_data.data)
    image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    cv2.imshow('isaac_image_viewer', image_np)
    key = cv2.waitKey(5)
    if key == ord('q'):
        rospy.signal_shutdown("User exit.")
        return
    count += 1
    delta = time.perf_counter() - ts_start
    # Log
    print("Received", count, "images in",
        round(delta), "seconds with",
        round(count / delta, 2), "FPS and Latency",
        round((rospy.Time.now() - ros_data.header.stamp).to_sec(), 2), "seconds")

def main(args):
    global count, ts_start
    # Init ROS node
    rospy.init_node('isaac_image_viewer', anonymous=True)
    sub = rospy.Subscriber("/isaac/color/image_raw",
        Image, callback, queue_size=1)
    count = 0
    ts_start = time.perf_counter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down ROS Image Viewer module")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
