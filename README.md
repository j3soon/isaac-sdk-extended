# ISAAC SDK Extended

> This repo will not be further updated, please refer to <https://github.com/j3soon/isaac-extended> instead.

Provide some Isaac SDK examples and notes not included in the toolkit.

Isaac SDK documentation: https://docs.nvidia.com/isaac/isaac/doc/index.html

> Note: If you are a developer in the NVIDIA Isaac SDK team and find the examples/notes useful, feel free to include them in the next Isaac SDK release.

## Installation

Download Isaac SDK here: https://developer.nvidia.com/isaac/downloads

Extract the file (`isaac-sdk-20201201-427971df2.tar.xz`)'s content into `~/isaac` directory. After extraction, the `~/isaac/sdk` directory should exist.

```sh
git clone https://github.com/j3soon/isaac-sdk-extended.git
cd isaac-sdk-extended
```

Copy all files in this repo into the `~/isaac` directory (Overwrite existing files). After copying, the `~/isaac/ros` directory should exist.

## Examples

All examples are tested in Isaac SDK 2020.2.2 (`isaac-sdk-20201201-427971df2`).

Before running the examples, please `cd` into the `sdk` directory.

### Stereo Dummy (IN SDK)

> No external hardware device required.

```sh
bazel build //apps/samples/stereo_dummy
bazel run //apps/samples/stereo_dummy
```

You should be able to run this example without any error.

If you encountered the following error:

```
ERROR: /home/ubuntu/.cache/bazel/_bazel_ubuntu/1ba3ee7ca57033cab08e8bbae375337a/external/redis/BUILD.bazel:77:1: Couldn't build file external/redis/_objs/redis-server-lib/ae.o: undeclared inclusion(s) in rule '@redis//:redis-server-lib':
this rule is missing dependency declarations for the following files included by 'external/redis/src/ae.c':
  '/usr/lib/gcc/x86_64-linux-gnu/9/include/stddef.h'
  '/usr/lib/gcc/x86_64-linux-gnu/9/include/stdarg.h'
  '/usr/lib/gcc/x86_64-linux-gnu/9/include/stdint.h'
```

You may be using non-compatible gcc. More discussions can be found [here](https://forums.developer.nvidia.com/t/bazel-could-not-download-grpc/129446/9).

### ZED Camera (IN SDK)

> - Tested with ZED SDK 3.2.2, ZED1 (Camera Firmware 1523, IMU Firmware N/A)

You should set up the ZED camera beforehand, and follow the Isaac documentation here: https://docs.nvidia.com/isaac/isaac/packages/sensors/doc/zedcamera.html

```sh
bazel build //apps/samples/zed_camera
bazel run //apps/samples/zed_camera
```

If you get the following error:

```
[ZED]ERROR: Cannot initialize the camera. Try another resolution
```

You may need to connect your ZED 1 to a USB 3.0 port. You can test which port is using by the [ZED SDK](https://www.stereolabs.com/developers/release/) tools:

```sh
/usr/local/zed/tools/ZED_Diagnostic
```

The command will launch an diagnostic window. If all test has passed, you can rerun the example with no errors.

### ZED Camera Low Resolution (NEW)

File location: (JSON only, No C++/Python)

- [sdk/apps/samples/zed_camera_low_res](https://github.com/j3soon/isaac-sdk-extended/tree/master/sdk/apps/samples/zed_camera_low_res)

> - Tested with ZED SDK 3.2.2, on PC with ZED1 (Camera Firmware 1523, IMU Firmware N/A).
> - Tested with ZED SDK 3.2.2, on PC with ZED2 (Camera Firmware 1523, IMU Firmware 776).
> - Tested with ZED SDK 3.2.2, on Jetson Xavier with ZED1 (Camera Firmware 1523, IMU Firmware N/A).
> - Tested with ZED SDK 3.2.2, on Jetson Xavier with ZED2 (Camera Firmware 1523, IMU Firmware -1).

This sample performs 2 modifications:
- lower the resolution to `672x376` (default `1280x720`) to support USB 2.0, and
- remove the `imu` component since it doesn't seem to be supported on Jetson platform (IMU Firmware shows -1 in `Zed_Explorer`)

> The `enable_imu` option in the json config is changed to `true` due to line 185-186 in `sdk/packages/zed/ZedCamera.cpp`:
> ```c
> // This should be set for ZedImuReader to read the Zed-M and ZED 2 IMU data
> params.sensors_required = !get_enable_imu();
> ```
> Actually I think the `!get_enabled_imu()` here should be changed to `get_enabled_imu()`, I believe it is a bug of the Isaac SDK.

Following the ZED Camera Sample, if you do not have a USB 3.0 port, or you cannot pass the last two tests in the diagnostic window, try the following ZED SDK tool:

```sh
/usr/local/zed/tools/ZED_Explorer
```

If you can see the real-time image of the camera, you are now capable of running the ZED Camera Sample under low resolution.

```sh
bazel build //apps/samples/zed_camera_low_res
bazel run //apps/samples/zed_camera_low_res
```

Open Isaac Sight (http://localhost:3000/) to view the results.

If you can see the camera image, but not in real-time, please verify that the `zed_camera` checkbox on the left side of Isaac Sight is checked.

### ISAAC ROS Bridge Sample (NEW)

File location: (JSON only for Isaac, Python for ROS)

> - Tested on PC

- [ros/isaac_ros_bridge_sample](https://github.com/j3soon/isaac-sdk-extended/tree/master/ros/isaac_ros_bridge_sample)
- [sdk/packages/ros_bridge/apps/ros_to_isaac_to_ros.app.json](https://github.com/j3soon/isaac-sdk-extended/tree/master/sdk/packages/ros_bridge/apps/ros_to_isaac_to_ros.app.json)
- [sdk/packages/ros_bridge/apps/ros_to_isaac_to_ros.subgraph.json](https://github.com/j3soon/isaac-sdk-extended/tree/master/sdk/packages/ros_bridge/apps/ros_to_isaac_to_ros.subgraph.json)

This is a ROS bridge application that does not require any camera.

For running the ROS package, please refer to [the README file](https://github.com/j3soon/isaac-sdk-extended/tree/master/ros/isaac_ros_bridge_sample/README.md)

- A ROS node publisher sends an blue image (topic: `ros/color/image_raw`) that becomes darker/lighter through time.
- A ROS node subscriber directly receive that blue image (topic: `ros/color/image_raw`) through roscore and show it.
- This Isaac app receives (subscribe) the blue image, show it on Isaac Sight, and transmits (publish) it back to ROS (topic: `isaac/color/image_raw`).
- A ROS node subscriber receives that image (topic: `isaac/color/image_raw`) through isaac & roscore and show it.

When ran correctly, there will be 3 slowly blinking blue image showing on Isaac Sight, ros image viewer, isaac image viewer, simultaneously.

### ISAAC ROS Bridge for Zed Camera (NEW)

File location: (JSON only, no C++/Python)

> - Tested on PC

- [sdk/packages/ros_bridge/apps/zed_camera_to_ros.app.json](https://github.com/j3soon/isaac-sdk-extended/tree/master/sdk/packages/ros_bridge/apps/zed_camera_to_ros.app.json)
- [sdk/packages/ros_bridge/apps/zed_camera_to_ros.subgraph.json](https://github.com/j3soon/isaac-sdk-extended/tree/master/sdk/packages/ros_bridge/apps/zed_camera_to_ros.subgraph.json)

This Isaac application reads the image from zed camera, show it on Isaac Sight, and send it to ROS (roscore), with topic `/rgb`.

### ROS Bridge (IN SDK)

The following is a brief graph of how Isaac communicates with ROS. Please note that Isaac has 2 independent channels for Isaac Sight and Other Isaac Apps respectively. Isaac Sight can receive data from C++ `show` and JSON `ImageViewer`. Other Isaac Apps can receive data through C++ `ISAAC_PROTO_TX`/`ISAAC_PROTO_RX` and JSON `edges`.

![ros_bridge](sdk/packages/ros_bridge/ros_bridge.png)

# ISAAC SDK

> This is the default README file of the Isaac SDK.

The Isaac SDK is the main software toolkit for NVIDIA robotics, and is comprised of the following:
1. Isaac Robotics Engine: A framework which allows you to easily write modular applications and
deploy them on your robots. Found in the top-level folder engine.
2. Isaac GEMs: A collection of robotics algorithms from planning to perception, most of them GPU-
accelerated. gems are found in the top-level folder packages and in engine/gems.
3. Applications: Various example applications from basic samples which show specific features to
applications that facilitate complicated robotics use cases. Applications can currently be found in
the top-level folder apps or inside packages.

## Documentation

The Isaac SDK documentation will get you started and provide details about the robotics engine, the
packages, and the message API for the ISAAC software development kit.

The documentation is available at [http://docs.nvidia.com/isaac/index.html](http://docs.nvidia.com/isaac/index.html).

## Copyright and License

Copyright (c) 2018-2019, NVIDIA CORPORATION. All rights reserved.

This project is released under the software license agreement for NVIDIA software development kits.
See the `LICENSE` file.
