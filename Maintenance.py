
# Add a maintenance record
def add_maintenance_record(servers, maintenance_records):
    while True:
        print("==============================")
        print("     ADD MAINTENANCE RECORD")
        print("==============================")

        hostname = input("Enter server hostname: ")

        # Check if server exists
        server_found = False

        while not server_found:
            for server in servers:
                if server.get_host_name() == hostname:
                    server_found = True
                    break

            if not server_found:
                print("Host not found.")

                retry = input("Would you like to try again? (y/n): ").lower()

                if retry == "y":
                    hostname = input("Enter server hostname: ")
                else:
                    print("Returning to main menu.")
                    return

        # Collect maintenance information
        maintenance_date = input("Enter maintenance date (MM/DD/YYYY): ")
        description = input("Enter maintenance description: ")

        # Create maintenance record
        record = {
            "hostname": hostname,
            "date": maintenance_date,
            "description": description
        }

        # Add record to maintenance list
        maintenance_records.append(record)

        print("\nMaintenance record successfully added!")

        # Ask whether to add another record
        another_record = input(
            "\nWould you like to add another maintenance record? (y/n): "
        ).lower()

        if another_record != "y":
            print("Returning to main menu.")
            break


# Display all maintenance records
def display_maintenance_records(maintenance_records):
    print("==============================")
    print("     MAINTENANCE RECORDS")
    print("==============================")

    if len(maintenance_records) == 0:
        print("No maintenance records found.")
        return

    # Display maintenance records
    for record in maintenance_records:
        print("\n------------------------------")
        print(f"Hostname: {record['hostname']}")
        print(f"Date: {record['date']}")
        print(f"Description: {record['description']}")


# Search maintenance records
def search_maintenance_records(servers, maintenance_records):
    print("==============================")
    print("   SEARCH MAINTENANCE RECORDS")
    print("==============================")

    while True:
        hostname = input("Enter server hostname: ")

        # Check if server exists
        server_found = False

        for server in servers:
            if server.get_host_name() == hostname:
                server_found = True
                break

        if not server_found:
            print("Server not found.")

            retry = input("Would you like to try again? (y/n): ").lower()

            if retry == "y":
                continue
            else:
                print("Returning to main menu.")
                return

        # Search for maintenance records
        record_found = False

        for record in maintenance_records:
            if record["hostname"] == hostname:
                record_found = True

                print("\n------------------------------")
                print(f"Hostname: {record['hostname']}")
                print(f"Date: {record['date']}")
                print(f"Description: {record['description']}")

        # Handle servers without maintenance records
        if not record_found:
            print("No maintenance records found for this server.")

        retry = input(
            "\nWould you like to search for another server? (y/n): "
        ).lower()

        if retry != "y":
            print("Returning to main menu.")
            return
