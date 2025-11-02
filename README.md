# Custom DWA Local Planner for ROS2

## Overview
This github repo focuses on implementing a **DYNAMIC WINDOW APPROACH (DWA) local planner** in ROS2 Humble that utilises the Turtlebot3 and Gazebo packages and without the usage of **nav2_dwb_controller**. 
The goal for this algorithm is to navigate the turtlebot to a goal, while avoiding the obstacles it faces in the environment.


## Features
- Samples velocity commands within dynamic constraints.
- Predicts trajectories based on sampled velocities.
- Evaluates trajectories using a cost function (goal distance, obstacle avoidance, and smoothness).
- Selects the best trajectory and publishes velocity commands (`/cmd_vel`).
- Subscribes to **Odometry (`/odom`)** and **LaserScan (`/scan`)**.
- Uses **RViz Markers** to visualize sampled trajectories.
- Works in **Gazebo** with obstacles for real-world testing.

## Installation & Setup
### 1. Install ROS2 Humble and TurtleBot3 Simulation
Ensure you have **ROS2 Humble** installed:
```sh
sudo apt update
sudo apt install ros-humble-desktop
```

### 2. Creating your workspace
A.) Create your ROS2 workspace and clone the Turtlebot3 packages. 

```sh
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git -b humble
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git -b humble
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git -b humble
```

B.) Navigate to your ROS2 'src' workspace and clone the custom DWA repository:
```sh
cd ~/src
git clone https://github.com/ProEvolution03/dwa-local-path-planner.git
```

### 3. Build the Package
Open a new terminal and run the following:
```sh
cd ~/ros2_ws/src
colcon build --packages-select dwa_nav_pkg
source install/setup.bash
```

### 4. Launch the Simulation
**Gazebo Simulation**: In the 1st Terminal, start the Gazebo environment with TurtleBot3:
```sh
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

In the 2nd Terminal, run the custom DWA local planner for goal selection:
```sh
ros2 run dwa_nav_pkg run_dwa
```

**RViz Visualization:**: In a 3rd Terminal, launch RViz by running:
```sh
ros2 run rviz2 rviz2
```

NOTES :
- In **RViz**, click **Add → By Topic** and select **visual_paths** to view the planned trajectories.
- The robot will attempt to navigate to a goal while avoiding obstacles.
- Debugging logs will show velocity sampling, trajectory scores, and decision-making steps.
- **RViz** will display sampled trajectories and the selected path.
- The code prompts for user input, and one of the only few integer values of **XY coordinates** that works is **(2,1)**, so it is highly recommended to use that.

