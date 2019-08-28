import psutil
 
total_mem = psutil.virtual_memory().total
used_mem = psutil.virtual_memory().used
used_percent = psutil.virtual_memory().percent

print("Total Mem:{}" .format(int(total_mem /1000 ** 3)))
print("Used Mem:{}" .format(int(used_mem / 1000 ** 3)))

