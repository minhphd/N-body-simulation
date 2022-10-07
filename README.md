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

gif

After click enter, the simulation will run full screen based on your input. Sit back and enjoy!



MIT License

Copyright (c) 2022  Minh Hoang Pham Dinh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
