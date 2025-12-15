FROM osrf/ros:humble-desktop-full

ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=humble

# Update and upgrade (with time sync handling)
RUN apt-get update -o Acquire::Check-Valid-Until=false && apt-get upgrade -y

# Install essential build tools
RUN apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    python3-argcomplete \
    build-essential \
    git vim wget curl \
    bash-completion sudo \
    software-properties-common \
    gnupg lsb-release

# Install locales
RUN apt-get install -y locales && \
    locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8

# Install Gazebo Classic (already included in ros-humble-desktop-full)
# Additional Gazebo Classic tools
RUN apt-get update && apt-get install -y \
    gazebo \
    ros-${ROS_DISTRO}-gazebo-ros-pkgs \
    ros-${ROS_DISTRO}-gazebo-ros

# Install Navigation2 and SLAM dependencies
RUN apt-get install -y \
    ros-${ROS_DISTRO}-navigation2 \
    ros-${ROS_DISTRO}-nav2-bringup \
    ros-${ROS_DISTRO}-cartographer \
    ros-${ROS_DISTRO}-cartographer-ros \
    ros-${ROS_DISTRO}-rmw-cyclonedds-cpp

# Install ROS2 development tools
RUN apt-get install -y \
    ros-${ROS_DISTRO}-rviz2 \
    ros-${ROS_DISTRO}-rqt \
    ros-${ROS_DISTRO}-rqt-common-plugins \
    ros-${ROS_DISTRO}-robot-state-publisher \
    ros-${ROS_DISTRO}-joint-state-publisher \
    ros-${ROS_DISTRO}-joint-state-publisher-gui \
    ros-${ROS_DISTRO}-xacro \
    ros-${ROS_DISTRO}-tf2-ros \
    ros-${ROS_DISTRO}-tf2-tools

# Install teleop tools
RUN apt-get install -y \
    ros-${ROS_DISTRO}-teleop-twist-keyboard \
    ros-${ROS_DISTRO}-teleop-twist-joy

# Install ros2_control packages
RUN apt-get install -y \
    ros-${ROS_DISTRO}-controller-manager \
    ros-${ROS_DISTRO}-ros2-control \
    ros-${ROS_DISTRO}-ros2-controllers || true

# Install OpenGL and Mesa utilities for GUI
RUN apt-get install -y \
    mesa-utils \
    libglx-mesa0 \
    libgl1-mesa-dri \
    mesa-vulkan-drivers \
    x11-apps

# Install Python dependencies
RUN pip3 install --no-cache-dir \
    setuptools numpy transforms3d

# Clean apt cache
RUN rm -rf /var/lib/apt/lists/*

# Create workspace directory (will be accessible by any user)
RUN mkdir -p /workspace/turtlebot3_ws/src

WORKDIR /workspace/turtlebot3_ws

CMD ["/bin/bash"]