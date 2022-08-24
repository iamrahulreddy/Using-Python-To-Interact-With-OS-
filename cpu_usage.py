import psutil
cpu_usage=psutil.cpu_percent(10) #Returns average cpu usage in 100s
print(cpu_usage)
