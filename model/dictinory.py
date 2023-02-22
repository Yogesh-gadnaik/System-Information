import platform
import psutil
import wmi
import pythoncom


def init_dictionary():
    pythoncom.CoInitialize()
    object_wmi = wmi.WMI()
    my_system = object_wmi.Win32_ComputerSystem()[0]
    # crete empty dictionary
    dictinory = {}

    # inserting all info in dictionary from both platform and psutil module
    dictinory['system'] = platform.system()
    dictinory['node'] = platform.node()
    dictinory['release'] = platform.release()
    dictinory['version'] = platform.version()
    dictinory['machine'] = platform.machine()
    dictinory['processor'] = platform.processor()
    dictinory['architecture_details'] = platform.architecture()
    dictinory['platform_details'] = platform.platform()
    dictinory['virtual_memory'] = psutil.virtual_memory()
    dictinory['physical_core'] = psutil.cpu_count(logical=False)
    dictinory['logical_core'] = psutil.cpu_count(logical=True)
    dictinory['cpu_frequency'] = psutil.cpu_freq().current
    dictinory['min_frequency'] = psutil.cpu_freq().min
    dictinory['max_frequency'] = psutil.cpu_freq().max
    dictinory['cpu_utilization'] = psutil.cpu_percent(interval=1)
    dictinory['per_cpu_utilization'] = psutil.cpu_percent(
        interval=1, percpu=True)
    dictinory['manufacturer'] = my_system.Manufacturer
    dictinory['model'] = my_system. Model
    dictinory['sysname'] = my_system.Name
    dictinory['no_processors'] = my_system.NumberOfProcessors
    dictinory['systemtype'] = my_system.SystemType
    dictinory['systemfamily'] = my_system.SystemFamily
    return dictinory
