# Pathfinder for CS:GO

The objective of the project is to find the path to a certain point on a map and walk to it. The points on the map shall be specified manually using tools provided in the package (see below for tutorials).

## How to use
1. Open "helpers/parameters.py" and set desired WAYPOINTS_NAME and your mouse senstivity as SENSITIVITY.
2. Run CS:GO (remember to add -insecure in launch options not to get a VAC ban).
3. Go into a match (ideally kick all the bots and set the round time to 60min).
4. Run "pathfindingGatherData.py" provided in the root folder.
5. Walk around the map and press "/" to add a waypoint.
6. After you are done, press "." to save the file. If a file already exists, it overwrites it.
7. Close "pathfindingGatherData.py".
8. Run "pathfindingConfigureWaypoints.py".
9. Press one point (now, it is saved in memory).
10. Press another point to connect them. You should see a line connecting them.
11. When you are finished, press "." to save the file.
12. Open "mainController.py" and in the main function change the destination point (it is and ID that you saw next to each point in "pathfindingConfigureWaypoints.py").
13. Run "mainController.py" and meanwhile the program is loading quickly focus on CS:GO (shoot/slice your knife).
