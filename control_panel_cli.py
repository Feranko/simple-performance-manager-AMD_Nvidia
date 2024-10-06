import subprocess
import psutil

def cpu_temp():
    return f"Temp: {list(psutil.sensors_temperatures()['acpitz'][0])[1]}°C"

def cpu_usage():
    return f"Usage: {psutil.cpu_percent()}%"

def ram_usage():
    return f"Usage: {psutil.virtual_memory().percent}%"

def get_amd_igpu_vram():
    try:
        # Run radeontop and capture the output
        output = subprocess.check_output(["radeontop", "-d", "-b", "1000", "-l", "1"], stderr=subprocess.DEVNULL)
        output = output.decode('utf-8')
        for line in output.splitlines():
            if "vram" in line.lower():
                vram = line.split()[line.split().index("vram")+2]
                file_size = ["mb", "gb", "tb"]
                for element in file_size:
                    if element in vram :
                        temp = element
                        args = vram.replace(element, "")
                        args = args.replace(",", "")

                return f"{round(float(args), 0)}{temp}"
        return "N/A"
    except subprocess.CalledProcessError:
        return "N/A"

def get_amd_igpu_usage():
    try:
            # Run radeontop and capture the output
        output = subprocess.check_output(["radeontop", "-d", "-b", "1000", "-l", "1"], stderr=subprocess.DEVNULL)
        output = output.decode('utf-8')
        for line in output.splitlines():
            if "gpu" in line.lower():
                usage = line.split()[4]
                return f"{usage}"
        return "N/A"
    except subprocess.CalledProcessErroir:
        return "N/A"

def get_gpu_usage():
    try:
        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=utilization.gpu,temperature.gpu,memory.used,memory.total",
                "--format=csv,noheader,nounits"
            ],
            encoding="utf-8")

        gpu_usage, temp, mem_used, mem_total = output.strip().split(", ")
        vram_usage = (int(mem_used) / int(mem_total)) * 100

        return f"{gpu_usage}% | {temp}°C | {vram_usage:.2f}%"
    except subprocess.CalledProcessError:
        return "N/A"

cpu_stat = [cpu_temp(), cpu_usage()]
ram_stat = [ram_usage()]
amd_stat = [get_amd_igpu_vram(), get_amd_igpu_usage()]

import time as t
import os

while True:
    print(f"\033[31m CPU = {cpu_stat[0]}, {cpu_stat[1]}")
    print(f"\033[34m RAM = {ram_stat[0]}")
    print(f"\033[33m iGPU = {amd_stat[0]}, {amd_stat[1]}")
    print(f"\033[32m dGPU = {get_gpu_usage()}")
    print(f"\033[37m")
    t.sleep(0.5)
    os.system("clear")

