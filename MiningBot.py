##########################
## Minecraft Mining Bot ##

import pyautogui as pt
import MiningBot_Utilities as MUtil
from time import sleep


'''
Main Object: Mining Bot
'''
class MiningBot:
    def __init__(self) -> None:
        pass

    '''
    Navigates the character to the desired image
    '''
    def _navToImage(self, img, num_clicks= MUtil.NUM_CLICKS, offset_x = MUtil.DEFAULT_OFFSET_X, offset_y = 0):
        position = pt.locateCenterOnScreen(img, confidence=MUtil.CONF_TARGET)

        if position is None:
            print("{0} is not found!".format(str(img))) #TODO: check img datatype
            return 1
        
        else:
            pt.moveTo(position, duration= MUtil.MOUSE_SPEED)
            pt.moveRel(position, offset_x, offset_y)
            pt.click(clicks= num_clicks, interval= MUtil.CLICK_INTERVAL)
    
        return 0
    

    '''
    Moves the character
    TODO = attack
    TODO = place
    '''

    def _moveCharacter(self, key_press, duration, action = 'walking'):
        pt.keyDown(key_press)
        sleep(duration)
        pt.keyUp(key_press)

        print("Moved the character for {} seconds.".format(str(duration)))
        return 0
    
    def _chopTree(self):
        self._moveCharacter('q', 0.5)



        self._moveCharacter('num2', 2)
        self._moveCharacter('q', 0.5)
        self._moveCharacter('num8', 2)
        # self._moveCharacter('w', 0.2)
        

        # self._moveCharacter('num8', 2)
        # self._moveCharacter('q', 0.5)
        # self._moveCharacter('num2', 2)
        
        # self._moveCharacter('num8', 4)
        # self._moveCharacter('q', 3.5)
        # self._moveCharacter('q', 3.5)
        # self._moveCharacter('num2', 4)




    '''
    Turn the character.
    Direction= <'left', 'right', 'up', 'down'>
    Position = <(X, Y)>
    If direction is specified, prioritize direction.
    '''
    def _turn(self, direction = None, position = (100, 0)):
        if direction != None:
            if direction == 'left':
                print('Turning Left')
                self._moveCharacter(MUtil.LK_LFT_KEY, 1)
                #pt.moveRel(100, 100, MUtil.MOUSE_SPEED * 5)






