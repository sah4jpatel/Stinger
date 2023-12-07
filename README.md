# Stinger
Automated Mechatronic Golf Putting Robot


1. Introduction

The STINGER Robot is a automated, self putting robot that uses off the shelf parts to distance map from a starting point and computationally processes the distance via USB camera and sets the correct voltage needed to strike the golf ball. It is autonomous and it is able to calibrate and calculate the exact distance of the flag positioning from a single camera and image processing algorithms. 

2. Table of Requirements

| Requirements | Threshold |
| --- | --- |
| System will use sensors to align itself to the ball | Visual Approval |
| System will input data from LiDAR module or Camera for vision | 1 ms response time |
| System will reach a steady state PID response within threshold | 0.25 to 1.5 |
| System should have a distance calibration process | True/False |
| System will be able to control ball firing distance for distance control | True/False |
| Estimate distance to pin/cup with either Camera or LiDAR | True/False |
| Ability to extract the pin/cup in an image to mark "target location" | True/False |
| Ability to compute and visualize attempted trajectory | True/False |
| Predict or Calculate launch power and direction corresponding to trajectory path | True/False |
| Must be able to putt varying distances | 3 to 9 ft |
| Accuracy threshold of getting the ball to the pin/cup based on trajectory | 2 ft radius |
| Provide ability to fine-tune performance based on results from previous launches | True/False |

3. Requirements Decision-making

As a Team, the requirements were chosen to closely mimic the process a golfer takes on the putting green to hit a ball into the hole and translated that for the process necessary a robot to engage and conduct a similar action. The only method of distance approximation in a real setting is based on the golfers sight and intuitive prediction. A typical putt that in a golf putting setting is between 1-9 ft must be able to be done in one stroke or it be comes costly to game performance, accuracy was of the most utmost importance, not sheer distance traveled. The advance vision system is necessary to undergo all the steps of processing the image algorithm to give an exact calculation of the actuation system necessary. 


4. VIdeo Demonstration

Link to all videos and demonstation results can be found [here]().

5. Design and Process Challenges

Some challenges that were encountered were in the actors behavior. The motor was unable to be controlled bidirectionally and therefore was required to complete one full revolution. Another significant challenge was in the physical limitations of the robot. The Car Chassis had a max payload weight of 1500g, and our system exceeded the payload weight, causing inconsistencies in the rotation and alignment stage of the robot. It was also unbalanced meaning the weight was front heavy, causing a additional instability when the swing and rotation was in motion. That caused some inconsistency in the hitting alignment of the ball. 

6. Conclusions

From the conclusion of the project, the team has become familiar with image processing and distance mapping needed for computer vision applications. It was a great project for us to learn and understand the complicated algorithms and steps necessary for computer vision and using the toolboxes for potential applications in the future.

The Team also learned much about mechanical design, and how to use motors and actuators to conduct motions necessary for repetitive tasks. Simply understanding the theoretics of motors and actuators were important when creating initial design, but working with the motors and actuators, we gained much experience on troubleshooting and tuning the motor for the performance necessary. 

As for potential next steps, would be to further improve the vision algorithm to track over a much further distance. Also redesigning the system to be less from heavy and to be able to endure the finer control of motors for both the swing and rotation. Potentially the use of Machine Learning to train the visual algorithms to be able to be used without the flag would be the future directions that could be considered for the project. 

7. Project Code, Files, Etc.

All code is uploaded to the github repo found [here](https://github.com/sah4jpatel/Stinger/).
