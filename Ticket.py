
# Create a support ticket
def create_ticket(servers, tickets):
    while True:
        print("==============================")
        print("       CREATE SUPPORT TICKET")
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

        # Collect ticket information
        description = input("Enter ticket description: ")

        # Create ticket
        ticket = {
            "ticket_id": len(tickets) + 1,
            "hostname": hostname,
            "description": description,
            "status": "Open"
        }

        # Add ticket to list
        tickets.append(ticket)

        print("\nSupport ticket successfully created!")
        print(f"Ticket ID: {ticket['ticket_id']}")

        # Ask whether to create another ticket
        another_ticket = input(
            "\nWould you like to create another ticket? (y/n): "
        ).lower()

        if another_ticket != "y":
            print("Returning to main menu.")
            break


# Display all support tickets
def display_tickets(tickets):
    print("==============================")
    print("       SUPPORT TICKETS")
    print("==============================")

    if len(tickets) == 0:
        print("No support tickets found.")
        return

    # Display ticket information
    for ticket in tickets:
        print("\n------------------------------")
        print(f"Ticket ID: {ticket['ticket_id']}")
        print(f"Hostname: {ticket['hostname']}")
        print(f"Description: {ticket['description']}")
        print(f"Status: {ticket['status']}")


# Search support tickets
def search_tickets(servers, tickets):
    print("==============================")
    print("     SEARCH SUPPORT TICKETS")
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

        # Search for matching tickets
        ticket_found = False

        for ticket in tickets:
            if ticket["hostname"] == hostname:
                ticket_found = True

                print("\n------------------------------")
                print(f"Ticket ID: {ticket['ticket_id']}")
                print(f"Hostname: {ticket['hostname']}")
                print(f"Description: {ticket['description']}")
                print(f"Status: {ticket['status']}")

        # Handle servers without support tickets
        if not ticket_found:
            print("No support tickets found for this server.")

        retry = input(
            "\nWould you like to search for another server? (y/n): "
        ).lower()

        if retry != "y":
            print("Returning to main menu.")
            return

# Update support ticket status


def update_ticket_status(tickets):
    while True:
        print("==============================")
        print("     UPDATE TICKET STATUS")
        print("==============================")

        if len(tickets) == 0:
            print("No support tickets available.")
            return

        ticket_id = input("Enter ticket ID: ")

        # Search for the selected ticket
        ticket_found = False

        for ticket in tickets:
            # Compare ticket IDs as strings
            if str(ticket["ticket_id"]) == ticket_id:

                ticket_found = True

                print("\nCurrent Ticket Status:", ticket["status"])
                print("\nAvailable Statuses:")
                print("1. Open")
                print("2. In Progress")
                print("3. Resolved")

                choice = input("Select new status: ")

                if choice == "1":
                    ticket["status"] = "Open"

                elif choice == "2":
                    ticket["status"] = "In Progress"

                elif choice == "3":
                    ticket["status"] = "Resolved"

                else:
                    print("Invalid status selection.")
                    break

                print("\nTicket status successfully updated!")
                print(f"New Status: {ticket['status']}")
                break

        # Handle tickets that are not found
        if not ticket_found:
            print("Ticket ID not found.")

        # Ask whether to update another ticket
        another_ticket = input(
            "\nWould you like to update another ticket? (y/n): "
        ).lower()

        if another_ticket != "y":
            print("Returning to main menu.")
            break
