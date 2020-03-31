import imageio
import numpy as np
import matplotlib.colors as colors

class USmap():
    """Class to generate a state map.  
    Forground is the forground color.
    Background is the background color
    Colors can be any valid (r,g,b) or a string:
     'b': (0, 0, 1),
     'g': (0, 0.5, 0),
     'r': (1, 0, 0),
     'c': (0, 0.75, 0.75),
     'm': (0.75, 0, 0.75),
     'y': (0.75, 0.75, 0),
     'k': (0, 0, 0),
     'w': (1, 1, 1)}

    """
    stateindex = {'Background': 0,
        'AL': 1,
        'AK': 2,
        'AZ': 3,
        'AR': 4,
        'CA': 5,
        'CO': 6,
        'CT': 7,
        'DE': 8,
        'FL': 9,
        'GA': 10,
        'HI': 11,
        'ID': 12,
        'IL': 13,
        'IN': 14,
        'IA': 15,
        'KS': 16,
        'KY': 17,
        'LA': 18,
        'ME': 19,
        'MD': 20,
        'MA': 21,
        'MI': 22,
        'MN': 23,
        'MS': 24,
        'MO': 25,
        'MT': 26,
        'NE': 27,
        'NV': 28,
        'NH': 29,
        'NJ': 30,
        'NM': 31,
        'NY': 32,
        'NC': 33,
        'ND': 34,
        'OH': 35,
        'OK': 36,
        'OR': 37,
        'PA': 38,
        'RI': 39,
        'SC': 40,
        'SD': 41,
        'TN': 42,
        'TX': 43,
        'UT': 44,
        'VT': 45,
        'VA': 46,
        'WA': 47,
        'WV': 48,
        'WI': 49,
        'WY': 50}    
    
    def setcolor(self, state, color='r'):
        """sets the color of the map key. Colors can be single charicter (b,g,r,c,m,y,k,w) passed as a string
        or a tuple of (red,green,blue)"""
        
        # loop though state if dictionary
        if isinstance(state, dict):
            for k in state:
                self.setcolor(k,state[k])
        
        index = state
        if isinstance(index, str):
            index = self.stateindex[index]
        if isinstance(color, str):
            color = colors.BASE_COLORS[color]
        self.im[self.iim == index,:] = color
    
    def makeimage(self, statecolors = {}, forground='w', background='b' ):
        """Make an image with a dictionary with key representing state code and value representing color.
        Optional values for forground (default state color) and background color"""
        self.im = np.zeros([self.iim.shape[0], self.iim.shape[1], 3])
        if isinstance(forground, str):
            forground = colors.BASE_COLORS[forground]
        self.im[:,:] = forground
        self.setcolor('Background', background)
        self.setcolor(statecolors)
        
        return self.im

    def __init__(self, statecolors = {}, forground = 'w', background = 'b'):
        """create an instance of a USmap with default forground color white and background color blue"""
        self.iim = imageio.imread('states.png')
        self.makeimage(statecolors=statecolors, forground=forground, background=background)