# System Utilities and Automation

This project is a system utility program that collects and provides information about CPU usage, virtual memory, swap memory, disk space, and writes the information to a text file.

## Features

- CPU Details:
  - Idle time of CPU
  - CPU usage

- Virtual Memory Details:
  - Total virtual memory
  - Available virtual memory
  - Used virtual memory
  - Free virtual memory
  - Cached virtual memory

- Swap Memory Details:
  - Total swap memory
  - Used swap memory

- Disk Space Details:
  - Device
  - Mountpoint
  - File System Type
  - Options

- Disk Usage Details:
  - Total size of the disk
  - Used size
  - Free size
  - Disk usage percent

## Usage

1. Run the `main.py` file.
2. The program will collect system information and write it to a file named `system_utilities.txt`.
3. After writing the file, the program will read the file and print its contents.

## Requirements

- Python 3.x
- psutil library

## Installation

1. Clone the repository:

