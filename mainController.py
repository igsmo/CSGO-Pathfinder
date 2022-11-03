

import time
from helpers import pathfindingManager as pfm
from helpers import botMovementController as bmc

class Controller():
    def __init__(self) -> None:
        self.pathfindingManager = pfm.PathfindingManager()
        self.movementController = bmc.MovementController()

        self.waypoints_df = self.pathfindingManager.waypoints_df

    def moveToWaypoint(self, waypoint_id: int, position_tolerance=1, time_tolerance=2):
        current_path = self.pathfindingManager.findPathFromCurrentPosition(waypoint_id)
    
        # print(current_path)

        i = 0
        while True:
            
            self.movementController.toggleForwardWalk(state="OFF")
            time.sleep(0.2)
            print(i)
            waypoint = current_path[i]

            destination = self.waypoints_df[['x', 'y', 'z']].iloc[waypoint]
            destination_coordinates = [destination['x'], destination['y'], destination['z']]

            self.movementController.orientateTowardsPoint(destination_coordinates)

            self.movementController.toggleForwardWalk(state="ON")

            current_position = self.movementController.getCurrentPosition()

            # print(f"Walking to {waypoint}...")
            # print(f"Current position is {current_position} and target {destination_coordinates}")

            # print(abs(current_position[0]-destination['x']))

            start_time = time.time()
            # Wait until the destination is within tolerance
            while (abs(current_position[0]-destination['x']) >= position_tolerance) \
                and (abs(current_position[1]-destination['y']) >= position_tolerance):
                current_position = self.movementController.getCurrentPosition()

                if time.time() - start_time >= time_tolerance:
                    current_path = self.pathfindingManager.findPathFromCurrentPosition(waypoint_id)
                    i = 0
                
            i += 1

            if i == len(current_path): break

        self.movementController.toggleForwardWalk(state="OFF")



def main():
    bot = Controller()
    bot.moveToWaypoint(44)


if __name__ == "__main__":
    main()