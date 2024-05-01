import cv2
import torch
import numpy as np
from ultralytics import YOLO
import requests
import zipfile
import os
import pickle

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)


def find_polygon_center_for_parking(points):
    """Find the center of a polygon given its points."""
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    center_x = int(sum(x_coords) / len(points))
    center_y = int(sum(y_coords) / len(points))
    return (center_x, center_y)


def save_object_for_parking(poligon):
    """Save the polygon object to a file."""
    with open("object/poligon.obj", "wb") as f:
        pickle.dump(poligon, f)


def load_object_for_parking():
    """Load the polygon object from a file."""
    try:
        with open("object/poligon.obj", "rb") as f:
            return pickle.load(f)
    except:
        save_object_for_parking([])

        with open("object/poligon.obj", "rb") as f:
            return pickle.load(f)


def is_point_in_polygon_for_parking(point, polygon):
    """Check if a point is inside a polygon."""
    x, y = point
    poly_points = [(x, y) for x, y in polygon]
    n = len(poly_points)
    inside = False

    p1x, p1y = poly_points[0]
    for i in range(n + 1):
        p2x, p2y = poly_points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


def get_label_name_for_parking(n):
    """Return the label names."""
    label = {
        0: "pedestrian",
        1: "people",
        2: "bicycle",
        3: "car",
        4: "van",
        5: "truck",
        6: "tricycle",
        7: "awning-tricycle",
        8: "bus",
        9: "motor",
    }
    return label[n]


def parking_space_counter(video_path=""):
    ''' 
    This function is used to count the number of parking spaces available in a parking lot.
    if video_path is not provided, the function will try to find the camera and use it as the video source.
    '''
    try:
        model = YOLO("Models/yolov8m mAp 48/weights/best.pt")
        print("Model loaded successfully.")
    except:
        # Specify the URL of the zip file
        url = "https://github.com/shukur-alom/parking-counter/releases/download/v1.0.0/Models.zip"

        # Send HTTP request to URL
        r = requests.get(url, stream=True)

        # Check if the request is successful
        if r.status_code == 200:
            print("Downloading the file...")
            # Open the file in write-binary mode and write the content of the response to it in chunks
            with open("largefile.zip", "wb") as f:
                for chunk in r.iter_content(chunk_size=1023):
                    if chunk:
                        f.write(chunk)

            # Use the zipfile library to extract the zip file
            with zipfile.ZipFile("largefile.zip", 'r') as zip_ref:
                zip_ref.extractall("")

            # Delete the zip file as it's no longer needed
            os.remove("largefile.zip")
            print("File downloaded successfully.")
            model = YOLO("Models/yolov8m mAp 48/weights/best.pt")
            print("Model loaded successfully.")

        else:
            print("Failed to retrieve the file. Check internet connection")

    # List to store points
    try:
        polygon_data = load_object_for_parking()
    except:
        os.makedirs("object", exist_ok=True)
        polygon_data = load_object_for_parking()
    print("Polygon data loaded successfully.")
    points = []

    # mouse callback function

    def draw_polygon(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            points.append((x, y))

    # Create a black image, a window and bind the function to window
    if video_path != "":
        cap = cv2.VideoCapture(video_path)
    else:
        for i in range(10):
            temp_cap = cv2.VideoCapture(i)
            # Check if the video capture object was opened successfully
            if temp_cap.isOpened():
                cap = temp_cap
                print(f"Camera found at index {i}")
                break
            else:
                temp_cap.release()

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", draw_polygon)

    while 1:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (1280, 720))

        mask_1 = np.zeros_like(frame)
        mask_2 = np.zeros_like(frame)

        results = model(frame, device=0)[0]

        polygon_data_copy = polygon_data.copy()

        for detection in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            label_name = get_label_name_for_parking(class_id)
            if label_name == "bicycle" or label_name == "car" or label_name == "van" or label_name == "truck" or label_name == "tricycle" or label_name == "awning-tricycle" or label_name == "bus" or label_name == "motor":

                car_polygon = [(int(x1), int(y1)), (int(x1), int(
                    y2)), (int(x2), int(y2)), (int(x2), int(y1))]

                for cou, i in enumerate(polygon_data_copy):
                    poligon_center = find_polygon_center_for_parking(i)

                    # cemter point of polygon
                    frame = cv2.circle(frame, poligon_center,
                                       1, (255, 0, 255), 3)

                    is_present = is_point_in_polygon_for_parking(
                        poligon_center, car_polygon)

                    if is_present == True:
                        cv2.fillPoly(mask_1, [np.array(i)], (0, 0, 255))
                        polygon_data_copy.remove(i)

        cv2.putText(frame,
                    f'Total space : {len(polygon_data)}',
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (8, 210, 255),
                    2,
                    cv2.LINE_4)

        cv2.putText(frame,
                    f'Free space : {len(polygon_data_copy)}',
                    (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (8, 210, 90),
                    3,
                    cv2.LINE_4)

        for i in polygon_data_copy:
            cv2.fillPoly(mask_2, [np.array(i)], (0, 255, 255))
        # polygon_data_copy.remove(i)
        print(len(polygon_data_copy))

        frame = cv2.addWeighted(mask_1, 0.2, frame, 1, 0)
        frame = cv2.addWeighted(mask_2, 0.2, frame, 1, 0)

        for x, y in points:
            cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)

        cv2.imshow("image", frame)

        wail_key = cv2.waitKey(1)

        if wail_key == ord("s") or wail_key == ord("S"):
            if len(points) > 0:
                polygon_data.append(points)
                points = []
                save_object_for_parking(polygon_data)

        elif wail_key == ord("r") or wail_key == ord("R"):
            try:
                polygon_data.pop()
                save_object_for_parking(polygon_data)
            except:
                pass
        elif wail_key & 0xFF == ord("q") or wail_key & 0xFF == ord("Q"):
            break
    cap.release()
    cv2.destroyAllWindows()
