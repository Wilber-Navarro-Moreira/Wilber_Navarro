import psutil

# Uso de CPU
print(f"Uso actual de CPU: {psutil.cpu_percent(interval=1)}%")

# Uso de memoria
memory = psutil.virtual_memory()
print(f"Uso de memoria: {memory.percent}%")
