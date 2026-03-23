cmake_minimum_required(VERSION 3.8)
project(abb_crb15000_12_127_moveit_config)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config launch DESTINATION share/${PROJECT_NAME})

ament_package()
