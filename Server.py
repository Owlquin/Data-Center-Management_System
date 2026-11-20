# This is the server

class Server:
    def __init__(self, hostname, operatingSystem, cpuCores, ram, storage, status):
        self.__hostname = str(hostname)
        self.__operatingSystem = str(operatingSystem)
        self.__cpuCores = int(cpuCores)
        self.__ram = int(ram)
        self.__storage = int(storage)
        self.__status = str(status)

    def get_host_name(self):
        return self.__hostname

    def set_hostname(self, hostname):
        self.__hostname = str(hostname)

    def get_operating_system(self):
        return self.__operatingSystem

    def set_operating_system(self, operatingSystem):
        self.__operatingSystem = str(operatingSystem)

    def get_cpu_cores(self):
        return self.__cpuCores

    def get_ram(self):
        return self.__ram

    def get_storage(self):
        return self.__storage

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = str(status)
