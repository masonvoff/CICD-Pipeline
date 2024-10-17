# CI/CD Pipeline: Elevator Ride to the 5th Floor

class ElevatorRide:
    
    def __init__(self):
        self.current_floor = 1
        self.person_in_elevator = False
        self.button_pressed = False
        self.is_used = False
        self.doors_open = False

    def check_elevator_status(self):
        # Check if the elevator is available
        print("Checking elevator status...")
        if(self.is_used == False):
            print("Elevator available")
        else:
            print("Elevator unavailable")
        return self.is_used
    
    def call_elevator(self,floor):
        if not self.check_elevator_status():
            self.move_elevator_to(floor)

    def enter_elevator(self):
        # Simulate the person entering the elevator
        print("Person enters the elevator.")
        self.person_in_elevator = True

    def press_button(self, floor):
        # Simulate pressing the button for the desired floor
        print(f"Button for floor {floor} is pressed.")
        self.button_pressed = True

    def move_elevator_to(self, floor):
        if not self.button_pressed:
            print(f"Error: No button pressed for floor {floor}. Elevator not moving.")
            return
        # Simulate the elevator moving to the specified floor
        print(f"Elevator is moving to floor {floor}...")
        self.current_floor = floor
        print(f"Elevator moved to {floor}")
        # Reset button press after movement


    def verify_person_in_elevator(self):
        # Verify that the person is inside the elevator
        if self.person_in_elevator:
            print("Person is inside the elevator.")
        else:
            print("Person is not in the elevator!")
        return self.person_in_elevator
    
    def exit_elevator(self):
        # Simulate the person exiting the elevator
        print("Person exits the elevator.")
        self.person_in_elevator = False
        self.is_used = False  # Elevator is now free
        self.button_pressed = False


    def run_pipeline(self):
        # Step 1: Initialize Pipeline
        print("Starting CI/CD Pipeline: Elevator Ride to the 5th Floor")
        
        # Stage 1: Ground Floor (Start Point)
        print("\nStage 1: Ground Floor")
        if not self.check_elevator_status() and self.current_floor == 1:
            self.enter_elevator()
        else:
            print("Waiting for elevator...")
            self.call_elevator(1)
            self.enter_elevator()
        self.press_button(5)  # Press button for 1st floor
        self.verify_person_in_elevator()

        # Stage 2: Move to the 2nd Floor
        print("\nStage 3: Second Floor")
        self.move_elevator_to(2)

        # Stage 3: Move to the 3rd Floor
        print("\nStage 4: Third Floor")
        self.move_elevator_to(3)

        # Stage 4: Move to the 4th Floor
        print("\nStage 5: Fourth Floor")
        self.move_elevator_to(4)

        # Stage 5: Move to the 5th Floor
        print("\nStage 6: Fifth Floor")
        self.move_elevator_to(5)
        self.exit_elevator()
        print("Person has reached the 5th Floor and exited the elevator.")
 
if __name__ == "__main__":
    elevator_ride = ElevatorRide()
    elevator_ride.run_pipeline()
