import cv2
import numpy as np

# Load the image
image_path = 'path_to_your_image.jpg'  # Replace with the actual path to your image
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve star detection
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Detect stars using the HoughCircles method
circles = cv2.HoughCircles(
    blurred_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0
)

if circles is not None:
    # Convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

    # Loop over the detected circles and draw them on the image
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # Display the number of detected stars
    num_stars = len(circles)
    cv2.putText(image, f"Stars: {num_stars}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the image
    cv2.imshow("Detected Stars", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No stars detected in the image.")
