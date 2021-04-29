#!/usr/bin/env python
import sys
import time
import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image

def main(args):
    FPS = 60
    B = 0
    dir = 1

    # Init ROS node
    rospy.init_node('image_publisher', anonymous=True)
    pub = rospy.Publisher("/ros/color/image_raw", Image, queue_size=1)

    rate = rospy.Rate(FPS)
    print("Begin Publishing")
    count = 0
    ts_start = time.perf_counter()
    IMG_WIDTH = 640
    IMG_HEIGHT = 480
    while not rospy.is_shutdown():
        image_np = np.zeros((IMG_HEIGHT, IMG_WIDTH, 3), dtype=np.uint8)
        B += 1 * dir
        if B == 255:
            dir = -1
        elif B == 0:
            dir = 1
        image_np[:,:,0] = B
        # Create Image
        image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
        msg = Image()
        msg.header.stamp = rospy.Time.now()
        msg.height = image_np.shape[0]
        msg.width = image_np.shape[1]
        msg.encoding = "rgb8"
        # "bgr8" is not supported by Isaac SDK
        msg.data = image_np.tostring()
        # Publish new image
        pub.publish(msg)
        count += 1
        delta = time.perf_counter() - ts_start
        # Log
        print("Sent", count, "images in",
            round(delta), "seconds with",
            round(count / delta, 2), "FPS")
        rate.sleep()

if __name__ == '__main__':
    main(sys.argv)
