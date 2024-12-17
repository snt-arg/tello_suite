# 🚁 Tello Suite

> [!IMPORTANT]
> This project is still a work in progress, so expect some bugs!  
> If you encounter any, please open an issue or submit a PR with a fix.

Tello Suite is a collection of ROS2 packages designed to enhance the intelligence of the DJI Tello drone. The suite leverages plugins (additional ROS2 packages) with distinct functionalities to expand the drone's capabilities.

At its core is `tello_bt`, a behavior tree that orchestrates all components by defining behaviors. This makes the system more robust, allowing you to control which plugins should run and making it more reliable in case of unexpected events.

The suite also includes a `Dockerfile` for easy setup without needing local installation. For more information, see the [Docker](#docker) section.

---

## 📑 Table of Contents

- [🔧 Structure](#structure)
- [⚙️ Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Dependencies](#dependencies)
- [🤝 How to Contribute](#how-to-contribute)
    - [Creating a New Plugin](#creating-a-new-plugin)
    - [Creating a New Suite Package](#creating-a-new-suite-package)
- [🐋 Docker](#docker)

---

## 🔧 Structure <a id="structure"></a>

- **[tello_driver](./tello_driver)**: A complete Tello driver package for controlling the drone, publishing image data, and tracking status like battery life.
- **[tello_msgs](./tello_msgs)**: Contains custom message and service definitions.
- **[tello_bringup](./tello_bringup)**: A bring-up package that helps launch the various components. Includes `system_launch.py`, which launches everything with the `hand_gestures` plugin.
- **[plugin_server_base](./plugin_server_base)**: A base class for developing plugins. It acts as a bridge between a plugin and the `tello_bt` package.
- **[tello_bt](./tello_bt)**: Implements the behavior tree that orchestrates all components.
- **[tello_control_station](./tello_control_station)**: An interface for controlling the Tello via keyboard and joystick, and for interacting with plugins. (**Note**: This package will soon be deprecated in favor of `tello_app`.)
- **[tello_plugins](./tello_plugins)**: Contains various plugins. Check each plugin package for details on its functionality.
- **[tello_nav](./tello_nav)**: Enables the Tello to localize itself and build maps using VSLAM technology. (**Not yet implemented: potential BSP**)
- **[tello_app](./tello_app)**: A web-based application that will eventually replace `tello_control_station`. (**Partially implemented in another repository**)

---

## ⚙️ Installation <a id="installation"></a>

### Prerequisites

- ROS2 Humble or later (only tested with Humble)
- Ubuntu 22.04

### Dependencies

- `tellopy` (must be installed from source)
- `av`
- `pillow`
- `py-trees`
- `pygame`
- `mediapipe`

To simplify the setup, we provide a `bootstrap.sh` script that installs all dependencies. Run the following command:

```sh
./bootstrap.sh
```

Alternatively, if you prefer manual installation, ensure each of the dependencies above is installed.

## 🤝 How to Contribute <a id="how-to-contribute"></a>

### Creating a New Plugin

1. Create a package in the plugins directory with your plugin's name.
2. Develop your plugin using the plugin_server_base methodology.
3. Update tello_bt to integrate your plugin. Detailed instructions are available in tello_bt.

### Creating a New Suite Package

> [!NOTE]
> To be done!

## 🐋 Docker <a id="docker"></a>

A `Dockerfile` is provided for using this suite within Docker. Follow these steps:

1. Build the docker image

```sh
docker build -t tello_suite .
```

3. Create container

```sh
docker run --name tello_suite --privileged --net=host tello_suite
```

4. Start the container

```sh
docker exed -t tello_suite bash
```

5. Once inside the container, launch the system using:

```sh
tello
```

A test
