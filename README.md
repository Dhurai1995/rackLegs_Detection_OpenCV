# Set up

1. Install pyCharm.
1. Open the folder "detection_MoveAI

# Set up for the code
1. Install opencv module.
1. open and run the "mainFile.py".
1. Tune the parameters in the trackbar if required.

# Reasons
First I have used a "cvtColor" to split out the orange rack, since the objective was to track the legs of the Orange rack. 

Now the rack is split, the next object to find out the contour so that the legs are identified. For this part "canny" is used.

From the contour, I extract all the rectangles. Then I use two limits: area and height greater than width (since the heigh of leg is higher than the width). This was to identify the legs and also reduce the noise.

# Issues

1. Continous Tracking is not so good.
2. Variable tuning would help in object tracking at certain situation or also use a some different optimization algorithms to tune those parameters.

