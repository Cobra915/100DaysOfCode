logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

def print_ascii_art(loss_count):
    loss_map = {
        0 : 
            '''
            +---+
            |   |
                |
                |
                |
                |
         ==============        
        ''',
        1 : 
        '''
            +---+
            |   |
            0   |
                |
                |
                |
         ==============        
        ''',
        2 : 
        '''
            +---+
            |   |
            0   |
            |   |
                |
                |
         ==============        
        ''',
        3 : 
        '''
            +---+
            |   |
            0   |
           /|   |
                |
                |
         ==============        
        ''',
        4 : 
        '''
            +---+
            |   |
            0   |
           /|\  |
                |
                |
         ==============        
        ''',
        5 : 
        '''
            +---+
            |   |
            0   |
           /|\  |
           /    |
                |
         ==============        
        ''',
        6 : 
        '''
            +---+
            |   |
            0   |
           /|\  |
           / \  |
                |
         ==============        
        '''
    }
    print(loss_map[loss_count])