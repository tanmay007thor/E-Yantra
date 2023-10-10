'''
# Team ID:          eYRC#HB#2281
# Theme:            Hologlyph Bots (HB)
# Author List:      Tanmay Rathod , Rushal Choksi , Hirva Patel , Savsani Dhanvi 
# Filename:         ROS.py
# Functions:        Hologlyph Bots
# Global variables: None
'''

import rclpy
from rclpy.node import Node
import turtle

class DrawEightNode(Node):
    def __init__(self):
        super().__init__('draw_eight')
        
        # Initialize the Turtle graphics window
        self.turtle_screen = turtle.Screen()
        self.turtle_screen.title('ROS 2 Turtle Drawing')
        
        # Create a Turtle object
        self.turtle = turtle.Turtle()

        # Draw the number "8"
        self.draw_eight()

    def draw_eight(self):
        '''
        Purpose:
        ---
        Draws the number "8" using Turtle graphics.
        
        Input Arguments:
        ---
        None
        
        Returns:
        ---
        None
        '''
        self.turtle.speed(1)
        
        # Draw the upper circle
        self.turtle.circle(100)
        
        # Move to the lower circle position
        self.turtle.penup()
        self.turtle.goto(0, -100)
        self.turtle.pendown()
        
        # Draw the lower circle
        self.turtle.circle(100)
        
        # Close the Turtle graphics window when done
        self.turtle_screen.mainloop()

def main():
    '''
    Purpose:
    ---
    Initializes and runs the ROS 2 node for drawing the number "8" using Turtle graphics.
    
    Input Arguments:
    ---
    None
    
    Returns:
    ---
    None
    '''
    rclpy.init()
    draw_eight_node = DrawEightNode()
    rclpy.spin(draw_eight_node)
    draw_eight_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
