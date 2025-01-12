class HotelReservationSystem:
    def __init__(self):
        self.rooms = {
            101: {'type': 'Single', 'price': 100, 'status': 'Available'},
            102: {'type': 'Single', 'price': 100, 'status': 'Available'},
            201: {'type': 'Double', 'price': 150, 'status': 'Available'},
            202: {'type': 'Double', 'price': 150, 'status': 'Available'},
            301: {'type': 'Suite', 'price': 250, 'status': 'Available'},
        }
        self.reservations = []

    def show_available_rooms(self):
        print("\nAvailable Rooms:")
        for room_no, details in self.rooms.items():
            if details['status'] == 'Available':
                print(f"Room {room_no}: {details['type']} - ${details['price']} per night")

    def book_room(self, room_no, guest_name, nights):
        if room_no in self.rooms and self.rooms[room_no]['status'] == 'Available':
            self.rooms[room_no]['status'] = 'Booked'
            total_price = self.rooms[room_no]['price'] * nights
            reservation = {
                'room_no': room_no,
                'guest_name': guest_name,
                'nights': nights,
                'total_price': total_price
            }
            self.reservations.append(reservation)
            print(f"\nRoom {room_no} successfully booked for {guest_name} for {nights} nights.")
            print(f"Total Price: ${total_price}")
        else:
            print(f"\nRoom {room_no} is not available for booking.")

    def view_reservations(self):
        if not self.reservations:
            print("\nNo reservations yet.")
        else:
            print("\nCurrent Reservations:")
            for res in self.reservations:
                print(f"Room {res['room_no']} - Guest: {res['guest_name']} - Nights: {res['nights']} - Total: ${res['total_price']}")

    def cancel_reservation(self, room_no):
        for res in self.reservations:
            if res['room_no'] == room_no:
                self.reservations.remove(res)
                self.rooms[room_no]['status'] = 'Available'
                print(f"\nReservation for Room {room_no} has been canceled.")
                return
        print(f"\nNo reservation found for Room {room_no}.")


def main():
    system = HotelReservationSystem()

    while True:
        print("\nHotel Reservation System")
        print("1. Show Available Rooms")
        print("2. Book a Room")
        print("3. View Reservations")
        print("4. Cancel a Reservation")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.show_available_rooms()
        elif choice == '2':
            try:
                room_no = int(input("Enter Room Number to Book: "))
                guest_name = input("Enter Guest Name: ")
                nights = int(input("Enter Number of Nights: "))
                system.book_room(room_no, guest_name, nights)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == '3':
            system.view_reservations()
        elif choice == '4':
            try:
                room_no = int(input("Enter Room Number to Cancel: "))
                system.cancel_reservation(room_no)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == '5':
            print("\nThank you for using the Hotel Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
