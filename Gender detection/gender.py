import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Load the pre-trained model
gender_model = cv2.dnn.readNetFromCaffe('gender_deploy.prototxt', 'gender_net.caffemodel')

# Load the image
image = cv2.imread('your_image.jpg')

# Perform face detection
faces, confidences = cv.detect_face(image)

# Loop through detected faces
for face in faces:
    # Get the coordinates of the face
    (startX, startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]
    
    # Extract the face region of interest
    face_crop = np.copy(image[startY:endY, startX:endX])
    
    # Preprocess the face crop for gender classification
    face_crop = cv2.resize(face_crop, (96, 96))
    face_crop = face_crop.astype('float') / 255.0
    face_blob = cv2.dnn.blobFromImage(face_crop, 1.0, (96, 96), (0, 0, 0), swapRB=True, crop=False)
    
    # Perform gender classification
    gender_model.setInput(face_blob)
    gender_preds = gender_model.forward()
    
    # Get the gender label
    gender_label = ['Male', 'Female'][np.argmax(gender_preds)]
    
    # Draw bounding box and gender label on the image
    label = f'{gender_label}: {max(gender_preds[0]) * 100:.2f}%'
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
    cv2.putText(image, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Display the output image
cv2.imshow('Gender Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
