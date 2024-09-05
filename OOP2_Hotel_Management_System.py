class HotelManagement:
    def __init__(self):
        self.rooms = {} # Dictionary to store room status with room_number as key

    def add_room(self, room_number):
        if room_number in self.rooms:
            print(f"Room {room_number} already exists.")
        else:
            self.rooms[room_number] = 'available'
            print(f"Room {room_number} has been added.")

    def check_in(self, room_number):
        """Check-in to a room (mark it as reserved)."""
        if room_number in self.rooms:
            if self.rooms[room_number] == 'available':
                self.rooms[room_number] = 'reserved'
                print(f"Checked in to room {room_number}.")
            else:
                print(f"Room {room_number} is already reserved.")
        else:
            print(f"Room {room_number} does not exist.")

    def check_out(self, room_number):
        """Check-out from a room (mark it as available)."""
        if room_number in self.rooms:
            if self.rooms[room_number] == 'reserved':
                self.rooms[room_number] = 'available'
                print(f"Checked out from room {room_number}.")
            else:
                print(f"Room {room_number} is already available.")
        else:
            print(f"Room {room_number} does not exist.")

    def status(self, room_number):
        """Check the status of a room."""
        if room_number in self.rooms:
            print(f"Room {room_number} is {self.rooms[room_number]}.")
        else:
            print(f"Room {room_number} does not exist.")

# Example usage
hotel = HotelManagement()
hotel.add_room(11)
hotel.add_room(12)

hotel.check_in(11)
hotel.status(11)

hotel.check_out(11)
hotel.status(11)

hotel.check_out(12)  # Should say room does not exist
