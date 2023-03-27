import subprocess
import cpuinfo
import psutil


def grabHardware():
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    memory = str(round(((psutil.virtual_memory().total / 1024) / 1024) / 1024)) + " GB"
    gpu = get_gpu_info()

    return {
        "CPU": cpu,
        "GPU": gpu,
        "RAM": memory
    }


def get_gpu_info():
    cmd = 'nvidia-smi --query-gpu=driver_version,gpu_name --format=csv'
    exit_code, result = run_command(cmd)

    if exit_code != 0:
        return None

    lines = result.splitlines()
    gpu = lines[1].split(", ")[1]

    return gpu


def run_command(cmd, shell=True):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, shell=shell)

    exit_code = None
    line = ''
    stdout = ''
    while exit_code is None or line:
        exit_code = p.poll()
        line = p.stdout.readline().decode('utf-8')
        stdout += line

    return exit_code, stdout

