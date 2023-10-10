# Running the Turtlesim Program

## Prerequisites
Before running the Turtlesim program, make sure you have ROS (Robot Operating System) installed on your system.

## Steps for Execution

1. Start ROS in the terminal using the following command:

    ```
    $ roscore
    ```

   This command initializes the ROS core.

2. Open a new terminal and start the Turtlesim node:

    ```
    $ rosrun turtlesim turtlesim_node
    ```

   This command launches the Turtlesim simulator.

3. Now, execute the Turtlesim program using the following command:

    ```
    $ rosrun my_package turtlesim.py 2.0
    ```

   Replace `my_package` with the name of your ROS package if it's different.

4. The Turtlesim program will now run, and you should see a turtle moving in the Turtlesim window.

Enjoy exploring and controlling the turtle using your Python script!

## Additional Information
- Ensure that you have all the necessary dependencies and packages installed in your ROS workspace to run your custom Turtlesim script successfully.
- Make sure your Python script (`turtlesim.py`) is located in the appropriate directory within your ROS package.
