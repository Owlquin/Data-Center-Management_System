
# Initialize data center racks
def initialize_racks(servers):

    # Create an empty rack layout
    racks = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    # Assign servers to rack positions
    racks[0][0] = servers[0]
    racks[0][1] = servers[1]
    racks[1][0] = servers[2]

    return racks


# Display data center racks
def display_racks(racks):
    print("================================")
    print("       DATA CENTER RACKS")
    print("================================")

    # Display each rack and its server positions
    for row, rack in enumerate(racks):
        print(f"\n Racks {row + 1}:")

        for column, server in enumerate(rack):
            if server is None:
                print(f"Position {column+1}:")
            else:
                hostname = server.get_host_name()
                print(f"Position {column + 1}: {hostname}")


# Search for a server's rack location
def search_rack_location(racks, hostname):
    server_found = False

    # Search through the rack positions
    for row in range(len(racks)):
        for column in range(len(racks[row])):
            if racks[row][column] is not None:

                server = racks[row][column]

                if server.get_host_name() == hostname:

                    server_found = True

                    # Display server location
                    print("\nServer Location")
                    print("------------------------")
                    print(f"Hostname: {hostname}")
                    print(f"Rack: {row + 1}")
                    print(f"Position: {column + 1}")

                    break

        if server_found:
            break

    # Handle servers that are not found
    if not server_found:
        print("Server not found in any rack.")
