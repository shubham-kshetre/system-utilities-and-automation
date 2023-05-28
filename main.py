import psutil

# Conversion into HH:MM:SS format
def convert_to_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def write_to_file():
    global cpu_usage, idle_time 
    cpu_usage, idle_time = cpu_info()
    total_memory, available_memory, used_memory, free_memory, cached_memory = memory_info()
    total_swap_memory, used_swap_memory = swap_memory_info()


    with open("system_utilities.txt", "w") as f:
        f.write("CPU Details:\n")
        f.write(f"idle time of CPU {convert_to_time(idle_time)}\n")
        f.write(f"CPU usage: {cpu_usage}\n\n")

        f.write("Virtual Memory Details:\n")
        f.write(f"Total virtual memory: {total_memory} MB\n")
        f.write(f"Available virtual memory: {available_memory} MB\n")
        f.write(f"Used virtual memory: {used_memory} MB\n")
        f.write(f"Free virtual memory: {free_memory} MB\n")
        f.write(f"Cached virtual memory: {cached_memory} MB\n\n")

        f.write("Swap memory Details\n")
        f.write(f"Total Swap memory: {total_swap_memory} MB\n")
        f.write(f"Used swap memory: {used_swap_memory} MB\n\n")

        partitions = disk_space_info()
        for partition in partitions:
            f.write(f"Device: {partition.device}\n")
            f.write(f"Mountpoint: {partition.mountpoint}\n")
            f.write(f"File System Type: {partition.fstype}\n")
            f.write(f"Options: {partition.opts}\n\n")

        disk_usage_dict = get_disk_usage('/')
        # f.write(f"Total size of the disk: {}")
        for i, j in disk_usage_dict.items():
            f.write(f"{i}: {j}\n")
        
def read_file():
    try:
        with open("system_utilities.txt", "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("File not Found!")
    except IOError:
        print("File reading error")

def cpu_info():
    cpu_usage = psutil.cpu_percent()
    idle_time = psutil.cpu_times().idle

    return cpu_usage, idle_time

def memory_info():
    global total_memory, available_memory, used_memory, free_memory, cached_memory
    # Get the system memory information
    memory_info = psutil.virtual_memory()

    # Calculate the virtual memory usage information
    total_memory = round(memory_info.total / (1024 * 1024), 2)
    available_memory = round(memory_info.available / (1024 * 1024), 2)
    used_memory = round(memory_info.used / (1024 * 1024), 2)
    free_memory = round(memory_info.free / (1024 * 1024), 2)
    cached_memory = round(memory_info.cached / (1024 * 1024), 2)

    return total_memory, available_memory, used_memory, free_memory, cached_memory

def swap_memory_info():
    global total_swap_memory, used_swap_memory
    # Get the swap memory information
    swap_info = psutil.swap_memory() 

    # Calculate the swap memory usage information
    total_swap_memory = round(swap_info.total / (1024 * 1024), 2)
    used_swap_memory = round(swap_info.used / (1024 * 1024), 2)

    return total_swap_memory, used_swap_memory

def disk_space_info():

    return psutil.disk_partitions()

def get_disk_usage(path):
    disk_usage = psutil.disk_usage(path)
    total_size = disk_usage.total
    used_size = disk_usage.used
    free_size = disk_usage.free
    usage_percent = disk_usage.percent

    return {
        'total size': total_size,
        'used size': used_size,
        'free size': free_size,
        'disk usage percent': usage_percent
    }

if __name__=="__main__":
    write_to_file()
    read_file()