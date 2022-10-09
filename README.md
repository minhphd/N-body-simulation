# N-body-simulation
A python program that simulate the interaction between multiple bodies in zero-g environment. This program used Barnes-Hutt algorithm to help with simulating large number of particles. Tkinter is used for GUI.
The default parameters for rendering bodies are similar to the parameters in the solar system.

| Variable name |     Value     |
| ------------- | ------------- |
| G  | 67408e-11  |
| Object Density  | 600  |
| initialLightestBodyMass  | 1.0224e+22  |
| initialHeaviestBodyMass  | 2.1469e+24  |
| initialMinBodySpeed  | 241.02  |
| initialMaxBodySpeed  | 4075.8  |

The radius of each body is calculated from the mass using spherical volumne equation

## Usage
- Git clone the repo to your local folder and cd into N-Body-simulation
- Download all the required libraries
  - vpython (for vector operation)
  - tkinter (for GUI)
  - pyautogui (for screensize)

- run Animation.py
```
python3 Animate.py
```

The program will then ask you to input the number of bodies, time step, and show or hide quadtree gridlines before rendering. 

![](https://github.com/minhphd/N-body-simulation/blob/main/media/terminalInput.gif)

After click enter, the simulation will run full screen based on your input. Sit back and enjoy!

![](https://github.com/minhphd/N-body-simulation/blob/main/media/withGrid.png)

![](https://github.com/minhphd/N-body-simulation/blob/main/media/without.png)

