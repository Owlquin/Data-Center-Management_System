# Data Center Management System
# App will keep track of maintaining a data center with a few servers
# including server inventory, server status management, maintenance records, IT support tickets
from Server import Server


def display_server_info(server):
    print("Server Information")
    print("------------------------")

    print(f"Hostname: {server.get_host_name()}")
    print(f"Operating System: {server.get_operating_system()}")
    print(f"CPU Cores: {server.get_cpu_cores()}")
    print(f"RAM: {server.get_ram()} GB")
    print(f"Storage: {server.get_storage()} GB")
    print(f"Status: {server.get_status()}")


def display_all_servers(servers):
    for server in servers:
        display_server_info(server)


def search_server(servers, hostname):
    for server in servers:
        if server.get_host_name() == hostname:
            display_server_info(server)
            return True
    return False


def update_server_status(servers, hostname, new_status):
    for server in servers:
        if server.get_host_name() == hostname:
            server.set_status(new_status)
            display_server_info(server)
            break


def add_server(servers):
    new_server = input("Would you like to create a new server? (y/n): ")
    if new_server == 'y':
        hostname = input("Enter hostname: ")
        hostname_exists = True
        while hostname_exists:
            hostname_exists = False
            for server in servers:
                if server.get_host_name() == hostname:
                    print("Hostname already exists.")
                    hostname = input("Enter a different hostname: ")
                    hostname_exists = True
                    break
        operating_system = input("Enter operating system: ")
        cpu_cores = int(input("Enter CPU cores: "))
        ram = int(input("Enter RAM (GB): "))
        storage = int(input("Enter storage (GB): "))
        status = input("Enter server status: ")
        new_server_object = Server(
            hostname, operating_system, cpu_cores, ram, storage, status)
        servers.append(new_server_object)
        # display_server_info(new_server_object)
    elif new_server == 'n':
        print("Returning to the main menu")


def delete_server(servers):
    while True:
        hostname = input("Enter hostname of server to delete: ")
        server_found = False

        for server in servers:
            if server.get_host_name() == hostname:
                server_found = True
                print("\nServer found:")
                display_server_info(server)
                confirmation = input(
                    "\nAre you sure you want to delete this server? (y/n): ")
                if confirmation == 'y':
                    servers.remove(server)
                    print(f"Server {hostname} has been deleted.")
                elif confirmation == 'n':
                    print("Deletion cancelled.")
                else:
                    print("Invalid choice. Deletion cancelled.")
                return

        if not server_found:
            print("\nServer not found.")
            retry = input(
                "Would you like to try again? (y/n): ")
            if retry == 'y':
                continue
            elif retry == 'n':
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice. Returning to main menu.")
                break


def main():
    server1 = Server("web-server-01", "Ubuntu", 8, 32, 500, "Online")
    server2 = Server("web-server-02", "Ubuntu", 8, 64, 1000, "Online")
    server3 = Server("web-server-03", "Ubuntu", 16, 32, 750, "Online")

    servers = []
    servers.append(server1)
    servers.append(server2)
    servers.append(server3)

    while True:
        print("================================")
        print(" Data Center Management System")
        print("================================")

        print("1. Display all servers")
        print("2. Search for a server")
        print("3. Update server status")
        print("4. Add a new server")
        print("5. Delete a server")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        print(f"You selected option: {choice}")
        if choice == '1':
            display_all_servers(servers)

        elif choice == '2':
            hostname = input("Enter hostname: ")
            while True:
                if search_server(servers, hostname):
                    retry = input(
                        "Would you like to search for another server? (y/n): ")
                    while retry != 'y' and retry != 'n':
                        retry = input("Invalid choice. Please enter y or n: ")
                    if retry == 'n':
                        print("Returning to main menu.")
                        break
                    hostname = input("Enter hostname: ")
                else:
                    print("Server not found. Please check the hostname.")
                    retry = input("Would you like to try again? (y/n): ")
                    while retry != 'y' and retry != 'n':
                        retry = input("Invalid choice. Please enter y or n: ")
                    if retry == 'n':
                        print("Returning to main menu.")
                        break
                    hostname = input("Enter hostname: ")

        elif choice == '3':
            hostname = input("Enter hostname: ")
            while not search_server(servers, hostname):
                print("Server Not Found. Please check the hostname.")
                retry = input("Would you like to try again? (y/n): ")
                if retry == 'y':
                    hostname = input("Enter hostname: ")
                elif retry == 'n':
                    print("Returning to main menu.")
                    break
                else:
                    print("Invalid choice. Please enter y or n.")

            else:
                new_status = input("Enter new server status: ")
                update_server_status(servers, hostname, new_status)

        elif choice == '4':
            add_server(servers)

        elif choice == '5':
            delete_server(servers)

        elif choice == '6':
            print("Exiting Data Center Management System")
            break

        else:
            print("Invalid choice. Please select 1-5.")

    # add_server(servers)
    # display_all_servers(servers)


main()
