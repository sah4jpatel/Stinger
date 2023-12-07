import paramiko, os
import numpy as np
import cv2
import time
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def calculate_flag_area(image_path):
    try:
        img = cv2.imread(image_path)
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        combined_mask = cv2.inRange(hsv_img, lower_red, upper_red)

        contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return 0
        
        largest_contour = max(contours, key=cv2.contourArea)
        largest_contour_mask = np.zeros_like(combined_mask)
        cv2.drawContours(largest_contour_mask, [largest_contour], -1, 255, thickness=cv2.FILLED)
        flag_area = cv2.contourArea(largest_contour)

        moments = cv2.moments(largest_contour)
        cx = int(moments['m10']/moments['m00'])
        cy = int(moments['m01']/moments['m00'])

        return np.sqrt(flag_area), cx, cy
    except:
        return 0

def check_file_exists(sftp, remote_file_path):
    try:
        sftp.stat(remote_file_path)
        return True
    except IOError:
        return False
    
def write_string_to_file(file_path, string_data):
    with open(file_path, 'w') as file:
        file.write(string_data)
        print(f"Data written to {file_path}")

def predict_distance(img, a, b, full=True):
    val, cx, cy = calculate_flag_area(img)
    if full:
        predicted_distance = a*np.log(val) + b
        return str(predicted_distance)+"\n"+ str(cx)+","+str(cy)       
    else:
        return str(cx)+","+str(cy)


def get_coefficients(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        data = data.split(",")
        coefficients = [np.float64(x) for x in data]
        return coefficients[0], coefficients[1]

router_ip = "172.22.11.2"
router_username = "admin"
router_password = ""

ssh = paramiko.SSHClient()

ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(router_ip, 
            username=router_username, 
            password=router_password,
            look_for_keys=True )

sftp = ssh.open_sftp()

try:
    while(True):
        if check_file_exists(sftp, "/C/output.png"):
            time.sleep(0.5)
            sftp.get("/C/output.png", "output.png")
            sftp.get("/C/coeffs.txt", "coeffs.txt")

            coefficients, intercept = get_coefficients("coeffs.txt")
            
            sftp.remove("/C/output.png")
            sftp.remove("/C/coeffs.txt")

            predicted_distance = predict_distance("output.png", coefficients, intercept)
            print(predicted_distance)
            write_string_to_file("out_val.txt", predicted_distance)
            os.remove("output.png")
            sftp.put("out_val.txt", "/C/out_val.txt")
            os.remove("out_val.txt")
        if check_file_exists(sftp, "/C/rotation.png"):
            sftp.get("/C/rotation.png", "rotation.png")
            try:
                predicted_distance = predict_distance("rotation.png", [0,0], 0, full=False)
                print(predicted_distance)
                write_string_to_file("center.txt", predicted_distance)
                sftp.put("center.txt", "/C/center.txt")
                os.remove("rotation.png")
            except:
                pass
except KeyboardInterrupt:
    ssh.close()
