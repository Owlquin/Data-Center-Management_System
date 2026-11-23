
# Display data center statistics
def display_statistics(servers):

    # Initialize statistics
    total_servers = len(servers)

    online_servers = 0
    offline_servers = 0
    maintenance_servers = 0
    decommissioned_servers = 0
    total_cpu_cores = 0
    total_ram = 0
    total_storage = 0

    # Count servers and calculate hardware totals
    for server in servers:
        if server.get_status() == "Online":
            online_servers += 1

        elif server.get_status() == "Offline":
            offline_servers += 1

        elif server.get_status() == "Maintenance":
            maintenance_servers += 1

        elif server.get_status() == "Decommissioned":
            decommissioned_servers += 1

        total_cpu_cores += server.get_cpu_cores()
        total_ram += server.get_ram()
        total_storage += server.get_storage()

    # Calculate server status percentages
    if total_servers > 0:
        online_percentage = (online_servers / total_servers) * 100
        offline_percentage = (offline_servers / total_servers) * 100
        maintenance_percentage = (maintenance_servers / total_servers) * 100
    else:
        online_percentage = 0
        offline_percentage = 0
        maintenance_percentage = 0

    # Display statistics
    print("==============================")
    print("     DATA CENTER STATISTICS")
    print("==============================")

    print(f"Total Servers: {total_servers}")
    print(f"Online Servers: {online_servers}")
    print(f"Offline Servers: {offline_servers}")
    print(f"Maintenance Servers: {maintenance_servers}")
    print(f"Decommissioned Servers: {decommissioned_servers}")

    print(f"Total CPU Cores: {total_cpu_cores}")
    print(f"Total RAM: {total_ram} GB")
    print(f"Total Storage: {total_storage} GB")

    print(f"Online Percentage: {online_percentage:.2f}%")
    print(f"Offline Percentage: {offline_percentage:.2f}%")
    print(f"Maintenance Percentage: {maintenance_percentage:.2f}%")
