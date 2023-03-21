import cv2
import mediapipe as mp
import numpy as np
import math as m


########################     Variable insialization

########################

# Font type.
font = cv2.FONT_HERSHEY_SIMPLEX
 
# Colors.
blue = (255, 127, 0)
red = (50, 50, 255)
green = (127, 255, 0)
dark_blue = (127, 20, 0)
light_green = (127, 233, 100)
yellow = (0, 255, 255)
pink = (255, 0, 255)
 
# Initialize mediapipe pose class.
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


mPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mPose.Pose()

drawspec1 = mpDraw.DrawingSpec(thickness=2,circle_radius=3,color=(0,0,255))
drawspec2 = mpDraw.DrawingSpec(thickness=3,circle_radius=8,color=(0,255,0))

mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils
temp_image = cv2.imread("project\\assets\\tadasana.png")
###############################

################################ FUNCTIONs

def findAngle(x1, y1, x2, y2):
    try:
        theta = m.acos( (y2 -y1)*(-y1) / (m.sqrt((x2 - x1)**2 + (y2 - y1)**2 ) * y1) )
    except ZeroDivisionError:
        theta = 0
    
    degree = int(180/m.pi)*theta
    return degree

def findDistance(x1, y1, x2, y2):
    dist = m.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist

def sendWarning(x):
    pass



#################################

############################### MAIN STREAMING
def Virabhadrasana():
    cap = cv2.VideoCapture(0)


    while True:
        ###############################################
        ### BASIC SETUP
        success, image = cap.read()
        
        if not success:
            print("Null.Frames")
            break

        h, w = image.shape[:2]
        
        # Convert the BGR image to RGB.
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process the image.
        keypoints = pose.process(image)
        
        # Convert the image back to BGR.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        ###################################
        try:
                
            lm = keypoints.pose_landmarks
            lmPose  = mp_pose.PoseLandmark
            
            #wrist
            l_wrist_x = int(lm.landmark[lmPose.LEFT_WRIST].x * w)
            l_wrist_y = int(lm.landmark[lmPose.LEFT_WRIST].y * h)
            
            r_wrist_x = int(lm.landmark[lmPose.RIGHT_WRIST].x * w)
            r_wrist_y = int(lm.landmark[lmPose.RIGHT_WRIST].y * h)
            
            
            # elbow
            l_elbow_x = int(lm.landmark[lmPose.LEFT_ELBOW].x * w)
            l_elbow_y = int(lm.landmark[lmPose.LEFT_ELBOW].y * h)
            
            r_elbow_x = int(lm.landmark[lmPose.RIGHT_ELBOW].x * w)
            r_elbow_y = int(lm.landmark[lmPose.RIGHT_ELBOW].y * h)
            
            
            # shoulder.
            l_shldr_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
            l_shldr_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
            r_shldr_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
            r_shldr_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)

            #######################################################################################################
            # Here is my code :- Bhavishaya Khandelwal

            # hip
            l_hip_x = int(lm.landmark[lmPose.LEFT_HIP].x * w)
            l_hip_y = int(lm.landmark[lmPose.LEFT_HIP].y * h)
            r_hip_x = int(lm.landmark[lmPose.RIGHT_HIP].x * w)
            r_hip_y = int(lm.landmark[lmPose.RIGHT_HIP].y * h)


            # knee
            l_knee_x = int(lm.landmark[lmPose.LEFT_KNEE].x * w)
            l_knee_y = int(lm.landmark[lmPose.LEFT_KNEE].y * h)
            r_knee_x = int(lm.landmark[lmPose.RIGHT_KNEE].x * w)
            r_knee_y = int(lm.landmark[lmPose.RIGHT_KNEE].y * h)

            
            # ankle
            l_ankle_x = int(lm.landmark[lmPose.LEFT_ANKLE].x * w)
            l_ankle_y = int(lm.landmark[lmPose.LEFT_ANKLE].y * h)
            r_ankle_x = int(lm.landmark[lmPose.RIGHT_ANKLE].x * w)
            r_ankle_y = int(lm.landmark[lmPose.RIGHT_ANKLE].y * h)


            # heel
            l_heel_x = int(lm.landmark[lmPose.LEFT_HEEL].x * w)
            l_heel_y = int(lm.landmark[lmPose.LEFT_HEEL].y * h)
            r_heel_x = int(lm.landmark[lmPose.RIGHT_HEEL].x * w)
            r_heel_y = int(lm.landmark[lmPose.RIGHT_HEEL].y * h)

            ######################################################################################################
            
            
            offset = findDistance(l_shldr_x, l_shldr_y, r_shldr_x, r_shldr_y)
            
            
            if offset < 100:
                cv2.putText(image, str(int(offset)) + ' Aligned', (30, 30), font, 0.9, green, 2)
            else:
                cv2.putText(image, str(int(offset)) + ' Not Aligned', (30, 30), font, 0.9, red, 2)

            
            l_wrist_inclination = findAngle(l_wrist_x, l_wrist_y, l_elbow_x, l_elbow_y,)
            r_wrist_inclination = findAngle(r_wrist_x, r_wrist_y, r_elbow_x, r_elbow_y,)
            
            l_elbow_inclination = findAngle(l_shldr_x, l_shldr_y, l_elbow_x, l_elbow_y)
            r_elbow_inclination = findAngle(r_shldr_x, r_shldr_y, r_elbow_x, r_elbow_y)

            #######################################################################################################
            # Here is my code :- Bhavishaya Khandelwal

            l_knee_inclination = findAngle(l_knee_x, l_knee_y, l_ankle_x, l_ankle_y)
            r_knee_inclination = findAngle(r_knee_x, r_knee_y, r_ankle_x, r_ankle_y)

            l_ankle_inclination = findAngle(l_ankle_x, l_ankle_y, l_heel_x, l_heel_y)
            r_ankle_inclination = findAngle(r_ankle_x, r_ankle_y, r_heel_x, r_heel_y)

            ########################################################################################################

            
            
            cv2.circle(image, (l_shldr_x, l_shldr_y), 7, yellow, -1)
            cv2.circle(image, (r_shldr_x, r_shldr_y), 7, yellow, -1)
            
            cv2.circle(image, (l_wrist_x, l_wrist_y), 7, blue, -1)
            cv2.circle(image, (r_wrist_x, r_wrist_y), 7, blue, -1)
            
            cv2.circle(image, (l_elbow_x, l_elbow_y), 7, pink, -1)
            cv2.circle(image, (r_elbow_x, r_elbow_y), 7, pink, -1)







            ######################################################################################################
            # Here is my code :- Bhavishaya Khandelwal

            # For Hip :-
            cv2.circle(image, (l_hip_x, l_hip_y), 7, blue, -1)
            cv2.circle(image, (r_hip_x, r_hip_y), 7, blue, -1)

            # For Knee :-
            cv2.circle(image, (l_knee_x, l_knee_y), 7, yellow, -1)
            cv2.circle(image, (r_knee_x, r_knee_y), 7, yellow, -1)

            # For Ankle :-
            cv2.circle(image, (l_ankle_x, l_ankle_y), 7, blue, -1)
            cv2.circle(image, (r_ankle_x, r_ankle_y), 7, blue, -1)

            # For Heel :-
            cv2.circle(image, (l_heel_x, l_heel_y), 7, blue, -1)
            cv2.circle(image, (r_heel_x, r_heel_y), 7, blue, -1)

            angle_text_str = 'left knee : ' + str(int(l_knee_inclination)) + ' left ankle : ' + str(int(l_ankle_inclination))
            angle_text_str1 = 'right knee : ' + str(int(r_knee_inclination)) + ' right ankle : ' + str(int(r_ankle_inclination))
            

            if 162 < l_knee_inclination < 175 and 143 < l_ankle_inclination < 159:
                # cv2.putText(image, angle_text_str, (10, 90), font, 0.6, light_green, 2)
                # cv2.putText(image, angle_text_str1, (10, 120), font, 0.6, light_green, 2)
                #Line For Left Hip TO Right Hip
                cv2.line(image, (l_hip_x, l_hip_y), (r_hip_x, r_hip_y), green, 2)
                # Line For Hip To Knee :-
                cv2.line(image, (l_hip_x, l_hip_y), (l_knee_x, l_knee_y), green, 2)
                cv2.line(image, (r_hip_x, r_hip_y), (r_knee_x, r_knee_y), green, 2)

                # Line For Knee To Ankle :-
                cv2.line(image, (l_knee_x, l_knee_y), (l_ankle_x, l_ankle_y), green, 2)
                cv2.line(image, (r_knee_x, r_knee_y), (r_ankle_x, r_ankle_y), green, 2)

                # Line For Ankle To Heel :- 
                cv2.line(image, (l_ankle_x, l_ankle_y), (l_heel_x, l_heel_y), green, 2)
                cv2.line(image, (r_ankle_x, r_ankle_y), (r_heel_x, r_heel_y), green, 2)

            else:
                # cv2.putText(image, angle_text_str, (10, 90), font, 0.6, red, 2)
                # cv2.putText(image, angle_text_str1, (10, 120), font, 0.6, red, 2)
                #Line For Left Hip TO Right Hip
                cv2.line(image, (l_hip_x, l_hip_y), (r_hip_x, r_hip_y), red, 2)
                # Line For Hip To Knee :-
                cv2.line(image, (l_hip_x, l_hip_y), (l_knee_x, l_knee_y), red, 2)
                cv2.line(image, (r_hip_x, r_hip_y), (r_knee_x, r_knee_y), red, 2)

                # Line For Knee To Ankle :-
                cv2.line(image, (l_knee_x, l_knee_y), (l_ankle_x, l_ankle_y), red, 2)
                cv2.line(image, (r_knee_x, r_knee_y), (r_ankle_x, r_ankle_y), red, 2)

                # Line For Ankle To Heel :- 
                cv2.line(image, (l_ankle_x, l_ankle_y), (l_heel_x, l_heel_y), red, 2)
                cv2.line(image, (r_ankle_x, r_ankle_y), (r_heel_x, r_heel_y), red, 2)

            #########################################################################################################



            
            angle_text_string = 'left wrist : ' + str(int(l_wrist_inclination)) + ' left elbow : ' + str(int(l_elbow_inclination))
            angle_text_string1 = 'right wrist : ' + str(int(r_wrist_inclination)) + ' right elbow : ' + str(int(r_elbow_inclination))

            if 80 < l_wrist_inclination < 92 and 80 < l_elbow_inclination < 90:
                # cv2.putText(image, angle_text_string, (10, 30), font, 0.5, light_green, 2)
                # cv2.putText(image, angle_text_string1, (10, 60), font, 0.5, light_green, 2)
                
                cv2.line(image, (l_elbow_x, l_elbow_y), (l_wrist_x, l_wrist_y), green, 2)
                cv2.line(image, (r_elbow_x, r_elbow_y), (r_wrist_x, r_wrist_y), green, 2)
                cv2.line(image, (l_shldr_x, l_shldr_y), (l_elbow_x, l_elbow_y), green, 2)
                cv2.line(image, (r_shldr_x, r_shldr_y), (r_elbow_x, r_elbow_y), green, 2)
            
            else:
                # cv2.putText(image, angle_text_string, (10, 30), font, 0.5, red, 2)
                # cv2.putText(image, angle_text_string1, (10, 60), font, 0.5, red, 2)
                
                cv2.line(image, (l_elbow_x, l_elbow_y), (l_wrist_x, l_wrist_y), red, 2)
                cv2.line(image, (r_elbow_x, r_elbow_y), (r_wrist_x, r_wrist_y), red, 2)
                cv2.line(image, (l_shldr_x, l_shldr_y), (l_elbow_x, l_elbow_y), red, 2)
                cv2.line(image, (r_shldr_x, r_shldr_y), (r_elbow_x, r_elbow_y), red, 2)
                
            #####################################################################################
            #KARAN BASANDANI CODE :-

            
            #  right to left shoulder  
            r_shldr_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
            r_shldr_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
            
            l_shldr_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
            l_shldr_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)

            
            cv2.circle(image, (r_shldr_x, r_shldr_y), 7, yellow, -1)
            cv2.circle(image, (l_shldr_x, l_shldr_y), 7, yellow, -1)
            
            shoulder_inclination = findAngle(l_shldr_x, l_shldr_y, r_shldr_x, r_shldr_y)
            
            angle_text_string1 = 'Shoulder Line : ' + str(int(shoulder_inclination))
            
            if 82 < shoulder_inclination and shoulder_inclination < 88:
                
                #cv2.putText(image, angle_text_string, (10, 30), font, 0.6, green, 2)
                # cv2.putText(image, angle_text_string1, (10,150), font, 0.6, green, 2)
                
                #cv2.line(image, (r_elbow_x, r_elbow_y), (r_shldr_x, r_shldr_y), green, 4)
                cv2.line(image, (l_shldr_x, l_shldr_y), (r_shldr_x, r_shldr_y), green, 2)
            
            else:
                #cv2.putText(image, angle_text_string, (10, 30), font, 0.6,red, 2)
                # cv2.putText(image, angle_text_string1, (10, 150), font, 0.6, red, 2)
                
                #cv2.line(image, (r_elbow_x, r_elbow_y), (r_shldr_x, r_shldr_y), red, 4)
                cv2.line(image, (l_shldr_x, l_shldr_y), (r_shldr_x, r_shldr_y), red, 2)                
                
                
            # left tp right hips  
            r_hip_x = int(lm.landmark[lmPose.RIGHT_HIP].x * w)
            r_hip_y = int(lm.landmark[lmPose.RIGHT_HIP].y * h)
            
            l_hip_x = int(lm.landmark[lmPose.LEFT_HIP].x * w)
            l_hip_y = int(lm.landmark[lmPose.LEFT_HIP].y * h)
            
            
            cv2.circle(image, (r_hip_x, r_hip_y), 7, yellow, -1)
            cv2.circle(image, (l_hip_x, l_hip_y), 7, yellow, -1)
            
            hip_inclination = findAngle(l_hip_x, l_hip_y, r_hip_x, r_hip_y)
            
            angle_text_string1 = 'HIP Line: ' + str(int(shoulder_inclination))
            
            if 76 < hip_inclination and hip_inclination < 86:
                

                # cv2.putText(image, angle_text_string1, (10, 180), font, 0.6, green, 2)
                
                #cv2.line(image, (r_elbow_x, r_elbow_y), (r_shldr_x, r_shldr_y), green, 4)
                cv2.line(image, (l_hip_x, l_hip_y), (r_hip_x, r_hip_y), green, 2)
            
            else:
            
                # cv2.putText(image, angle_text_string1, (10,180), font, 0.6, red, 2)
                
                #cv2.line(image, (r_elbow_x, r_elbow_y), (r_shldr_x, r_shldr_y), red, 4)
                cv2.line(image, (l_hip_x, l_hip_y), (r_hip_x, r_hip_y), red, 2)
                    
                
            # shoulder to hips (left and right)
            
            l_StoH_inclination = findAngle(l_shldr_x, l_shldr_y, l_hip_x, l_hip_y)
            r_StoH_inclination = findAngle(r_shldr_x, r_shldr_y, r_hip_x, r_hip_y)
            
            angle_text_string = 'l_StoH_inclination : ' + str(int(l_StoH_inclination))
            angle_text_string1 = 'r_StoH_inclination : ' + str(int(r_StoH_inclination))

            
            if 155 < l_StoH_inclination and l_StoH_inclination < 165 and 170 < r_StoH_inclination and r_StoH_inclination < 180:
                
                # cv2.putText(image, angle_text_string, (10, 210), font, 0.6, green, 2)
                # cv2.putText(image, angle_text_string1, (10, 240), font, 0.6, green, 2)
                
                cv2.line(image, (l_shldr_x, l_shldr_y), (l_hip_x, l_hip_y), green, 2)
                cv2.line(image, (r_shldr_x, r_shldr_y), (r_hip_x, r_hip_y), green, 2)
            
            else:
                # cv2.putText(image, angle_text_string, (10, 210), font, 0.6,red, 2)
                # cv2.putText(image, angle_text_string1, (10, 240), font, 0.6, red, 2)
                
                cv2.line(image, (l_shldr_x, l_shldr_x), (l_hip_x, l_hip_x), red, 2)
                cv2.line(image, (r_shldr_x, r_shldr_y), (r_hip_x, r_hip_y), red, 2)             
        except:
            pass 
        
    ########################################################################################################

        cv2.imshow('poseDetection',image)
        cv2.imshow("img", temp_image)
        if cv2.waitKey(1) == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()