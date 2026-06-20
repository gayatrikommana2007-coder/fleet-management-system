class Robot:
    def __init__(self, robot_id, name):
        self.robot_id = robot_id
        self.name = name
        self.busy = False
        self.current_task = None

    def assign_task(self, task):
        if self.busy:
            print(f"{self.name} is busy and cannot take a new task.")
        else:
            self.busy = True
            self.current_task = task
            print(f"{self.name} assigned task: {task}")

    def complete_task(self):
        if self.busy:
            print(f"{self.name} completed task: {self.current_task}")
            self.busy = False
            self.current_task = None
        else:
            print(f"{self.name} has no task to complete.")

    def status(self):
        if self.busy:
            return f"BUSY - {self.current_task}"
        else:
            return "AVAILABLE"


class FleetManager:
    def __init__(self):
        self.robots = {}

    def register_robot(self, robot):
        self.robots[robot.robot_id] = robot
        print(f"Robot Registered: {robot.robot_id} - {robot.name}")

    def assign_task(self, robot_id, task):
        if robot_id in self.robots:
            self.robots[robot_id].assign_task(task)
        else:
            print("Robot not found!")

    def complete_task(self, robot_id):
        if robot_id in self.robots:
            self.robots[robot_id].complete_task()
        else:
            print("Robot not found!")

    def show_status(self):
        print("\n----- FLEET STATUS -----")
        for robot in self.robots.values():
            print(
                f"ID: {robot.robot_id} | Name: {robot.name} | Status: {robot.status()}"
            )
        print("------------------------")


# Main Program
fleet = FleetManager()

# Register Robots
r1 = Robot("R001", "Robot Alpha")
r2 = Robot("R002", "Robot Beta")
r3 = Robot("R003", "Robot Gamma")

fleet.register_robot(r1)
fleet.register_robot(r2)
fleet.register_robot(r3)

# Show Initial Status
fleet.show_status()

# Assign Tasks
fleet.assign_task("R001", "Pick Item")
fleet.assign_task("R002", "Deliver Package")
fleet.assign_task("R003", "Scan Inventory")

# Show Status
fleet.show_status()

# Complete Tasks
fleet.complete_task("R001")
fleet.complete_task("R002")
fleet.complete_task("R003")

# Final Status
fleet.show_status()