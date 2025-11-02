cmake_minimum_required(VERSION 3.8)
project(dwa_nav_pkg_cpp)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)

# Add executable
add_executable(run_dwa_cpp src/dwa_planner.cpp)

# Link dependencies
ament_target_dependencies(run_dwa_cpp
  rclcpp
  geometry_msgs
  nav_msgs
  sensor_msgs
  tf2
  tf2_geometry_msgs
  visualization_msgs
)

# Install target
install(TARGETS run_dwa_cpp DESTINATION lib/${PROJECT_NAME})

# Compiler options
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Enable testing
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)  # Skip copyright check
  set(ament_cmake_cpplint_FOUND TRUE)    # Skip cpplint check
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
