import cv2

def get_available_cameras():
    available_cameras = []
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            available_cameras.append(index)
        cap.release()
        index += 1
    return available_cameras

# Call the function to get the list of available cameras
cameras = get_available_cameras()

# Print the list of available cameras
print("Available cameras:", cameras)