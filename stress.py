import subprocess
import os
import psutil
import time


def run_stress_test(cpu_percentage, ram_percentage, duration):
    # Calculate the number of CPU workers to spawn based on the desired CPU percentage
    cpu_workers = round(os.cpu_count() * cpu_percentage / 100)

    # Calculate the memory size to use based on the desired RAM percentage
    memory_size = round(psutil.virtual_memory().total * ram_percentage / 100)

    # Build the stress-ng command with desired options
    command = [
        'stress-ng',
        '--cpu', str(cpu_workers),
        '--vm', '1',
        '--vm-bytes', f'{memory_size}K',
        '--timeout', f'{duration}s',
        '--metrics-brief'
    ]

    # Start the stress-ng process in a subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        # Wait for the specified duration
        time.sleep(duration)
    finally:
        # Terminate the stress-ng process after the specified duration
        process.terminate()
        process.wait()

if __name__ == "__main__":
    # Define the desired CPU and RAM percentages, and the duration in seconds
    cpu_percentage = 50  # Use 50% of available CPU cores
    ram_percentage = 50  # Use 50% of available RAM
    duration = 10        # Run the stress test for 10 seconds

    run_stress_test(cpu_percentage, ram_percentage, duration)
