# facing postions
# 0 up, 1 right, 2 down, 3 left
# robot initial ps (0,0)

# {(1,2): 2, (0,2): 2, (-1,2): 1, (0,1): 2,(-1,1): 1, (0,0) : 2, (-1, 0): 1, (0, -1): 1}


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# dfs, backtrancing to the recursion
class Solution:

    def changeDirection(self, actual_orientation, wanted_orientation, robot):
        offset = (wanted_orientation - actual_orientation)
    
        turn_right = True if offset > 0 else False 
        
        for i in range(abs(offset)):
            if turn_right:
                robot.turnRight()
            else:
                robot.turnLeft()
                

            
    # 0 up, 1 right, 2 down, 3 left
    def new_position(self, position, orientation):
        if orientation == 0:
            position = (position[0]-1, position[1])
        elif orientation == 1:
            position = (position[0], position[1]+1)
        elif orientation == 2:
            position = (position[0]+1, position[1])
        elif orientation == 3:
            position = (position[0], position[1]-1)
        return position
    
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        position_to_val = set()
        
        
        def dfs_exploration(original_orientation, position):
            # 0 up, 1, right, 2 down, 3 left
            robot.clean()
            position_to_val.add(position)
            
            curr_orientation = original_orientation
        
            for mv in [0, 1, 2, 3]:
                new_position = self.new_position(position, mv)
                if new_position not in position_to_val: 
            
                    self.changeDirection(curr_orientation, mv, robot)
                    curr_orientation = mv
                    
                    if robot.move():
                        dfs_exploration(mv, new_position)
                    else: 
                        position_to_val.add(new_position) 
            
            self.changeDirection(curr_orientation, original_orientation, robot)
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight() 
            
        dfs_exploration(0, (0,0))
            
        
                
                
                

        
        
        