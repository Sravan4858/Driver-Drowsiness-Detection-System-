# import cv2
# import mediapipe as mp
# import time
# from playsound import playsound
# from win10toast import ToastNotifier
# import winsound
# from twilio.rest import Client
# import geocoder

# g = geocoder.ip('me')

# lat = g.latlng[0]
# lng = g.latlng[1]

# print("Latitude:", lat)
# print("Longitude:", lng)
# # -----------------------------
# # Twilio Credentials
# # -----------------------------



# import winsound
# import geocoder
# from twilio.rest import Client

# # -----------------------------
# # Twilio Credentials
# # -----------------------------


# client = Client(account_sid, auth_token)

# # -----------------------------
# # Get live location
# # -----------------------------
# def get_location():
#     g = geocoder.ip('me')
#     lat, lng = g.latlng
#     return f"https://www.google.com/maps?q={lat},{lng}"

# # -----------------------------
# # Send SMS with location
# # -----------------------------
# def send_sms():
#     location_link = get_location()

#     message = client.messages.create(
#         body=f"⚠️ ALERT: Driver is drowsy!\nLocation: {location_link}",
#         from_=twilio_number,
#         to=receiver_number
#     )
#     print("SMS sent:", message.sid)

# # -----------------------------
# # Make automated call
# # -----------------------------
# def make_call():
#     call = client.calls.create(
#         twiml='<Response><Say>Alert. Driver is feeling drowsy. Please check immediately.</Say></Response>',
#         from_=twilio_number,
#         to=receiver_number
#     )
#     print("Call initiated:", call.sid)

# # -----------------------------
# # SIMULATED DROWSINESS ALERT
# # -----------------------------
# print("Drowsiness Detected!")

# # 🔊 Alarm sound
# winsound.PlaySound("alarm.wav",
#                    winsound.SND_FILENAME | winsound.SND_ASYNC)

# # 📱 Send SMS
# send_sms()

# # 📞 Make call
# make_call()

# # -----------------------------
# # Twilio Credentials
# # -----------------------------


# client = Client(account_sid, auth_token)

# # -----------------------------
# # Function to get location
# # -----------------------------

# # Simulated alert
# # -----------------------------
# print("Drowsiness Detected!")

# # Play alarm
# winsound.PlaySound("alarm.wav",
#                    winsound.SND_FILENAME | winsound.SND_ASYNC)

# # Send SMS with location
# send_sms()

# # -----------------------------
# # Simulated drowsiness alert
# # -----------------------------
# print("Drowsiness Detected!")

# # Play alarm sound
# winsound.PlaySound("alarm.wav",
#                    winsound.SND_FILENAME | winsound.SND_ASYNC)


# # -----------------------------
# # Initialize MediaPipe Face Mesh
# # -----------------------------
# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh(
#     refine_landmarks=True,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5
# )

# # Notification object
# toaster = ToastNotifier()

# # Eye landmark indexes (MediaPipe)
# LEFT_EYE = [33, 160, 158, 133, 153, 144]
# RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# EAR_THRESHOLD = 0.25
# FRAME_COUNT = 0
# ALARM_ON = False

# # -----------------------------
# # Function to calculate EAR
# # -----------------------------
# def eye_aspect_ratio(landmarks, eye_points, w, h):
#     coords = [(int(landmarks[p].x * w), int(landmarks[p].y * h)) for p in eye_points]

#     A = ((coords[1][1] - coords[5][1])**2 + (coords[1][0] - coords[5][0])**2) ** 0.5
#     B = ((coords[2][1] - coords[4][1])**2 + (coords[2][0] - coords[4][0])**2) ** 0.5
#     C = ((coords[0][1] - coords[3][1])**2 + (coords[0][0] - coords[3][0])**2) ** 0.5

#     ear = (A + B) / (2.0 * C)
#     return ear, coords

# # -----------------------------
# # Start Webcam
# # -----------------------------
# cap = cv2.VideoCapture(0)

# print("Driver Drowsiness Detection Started...")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     h, w, _ = frame.shape
#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     results = face_mesh.process(rgb)

#     if results.multi_face_landmarks:
#         for face_landmarks in results.multi_face_landmarks:

#             leftEAR, leftCoords = eye_aspect_ratio(
#                 face_landmarks.landmark, LEFT_EYE, w, h
#             )
#             rightEAR, rightCoords = eye_aspect_ratio(
#                 face_landmarks.landmark, RIGHT_EYE, w, h
#             )

#             ear = (leftEAR + rightEAR) / 2.0

#             # Draw eye points
#             for x, y in leftCoords + rightCoords:
#                 cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

#             # Check drowsiness
#             if ear < EAR_THRESHOLD:
#                 FRAME_COUNT += 1

#                 if FRAME_COUNT >= 20:
#                     if not ALARM_ON:
#                         ALARM_ON = True

#                         # Play alarm
#                         import winsound

#                         winsound.PlaySound(r"D:\drowsiness\alarm.wav",
#                         winsound.SND_FILENAME)
#                         # Windows notification
#                         toaster.show_toast(
#                             "Drowsiness Alert!",
#                             "Wake up! You are sleepy!",
#                             duration=5,
#                             threaded=True
#                         )

#                     cv2.putText(frame, "DROWSINESS ALERT!",
#                                 (120, 50),
#                                 cv2.FONT_HERSHEY_SIMPLEX,
#                                 1, (0, 0, 255), 3)
#             else:
#                 FRAME_COUNT = 0
#                 ALARM_ON = False

#     cv2.imshow("Drowsiness Detection", frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import winsound
import geocoder
from twilio.rest import Client

# -----------------------------
# Twilio Credentials
# -----------------------------
account_sid = "AC083a491af82358716d620855bfb2bd92"
auth_token = "7f7165d7b52604410a30ca8dc7bca58e"
twilio_number = "+18316037032"
receiver_number = "+919398354858"

client = Client(account_sid, auth_token)

# -----------------------------
# MediaPipe Face Mesh
# -----------------------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

EAR_THRESHOLD = 0.23
FRAME_LIMIT = 20
frame_count = 0
alert_sent = False

# -----------------------------
# Get Live Location
# -----------------------------
def get_location():
    g = geocoder.ip('me')
    lat, lng = g.latlng
    return f"https://www.google.com/maps?q={lat},{lng}"

# -----------------------------
# Send SMS
# -----------------------------
def send_sms():
    location = get_location()

    client.messages.create(
        body=f"⚠️ Driver is drowsy!\nLocation: {location}",
        from_=twilio_number,
        to=receiver_number
    )

# -----------------------------
# Make Call
# -----------------------------
def make_call():
    client.calls.create(
        twiml='<Response><Say>Alert. Driver is sleeping. Please check immediately.</Say></Response>',
        from_=twilio_number,
        to=receiver_number
    )

# -----------------------------
# Eye Aspect Ratio
# -----------------------------
def eye_ratio(landmarks, eye_points, w, h):
    coords = [(int(landmarks[p].x * w), int(landmarks[p].y * h)) for p in eye_points]

    A = ((coords[1][1]-coords[5][1])**2 + (coords[1][0]-coords[5][0])**2) ** 0.5
    B = ((coords[2][1]-coords[4][1])**2 + (coords[2][0]-coords[4][0])**2) ** 0.5
    C = ((coords[0][1]-coords[3][1])**2 + (coords[0][0]-coords[3][0])**2) ** 0.5

    return (A + B) / (2.0 * C)

# -----------------------------
# Start Camera
# -----------------------------
cap = cv2.VideoCapture(0)

print("System Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:

            left = eye_ratio(face.landmark, LEFT_EYE, w, h)
            right = eye_ratio(face.landmark, RIGHT_EYE, w, h)
            ear = (left + right) / 2

            if ear < EAR_THRESHOLD:
                frame_count += 1

                if frame_count >= FRAME_LIMIT:

                    cv2.putText(frame, "DROWSINESS ALERT!",
                                (100, 50),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 0, 255), 3)

                    

                    # 📱 Send alert only once
                    if not alert_sent:
                        send_sms()
                        make_call()
                        alert_sent = True

            else:
                frame_count = 0
                alert_sent = False

    cv2.imshow("Smart Driver Safety System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
import winsound
import threading

def beep_alarm():
    for i in range(5):
        winsound.Beep(2000, 400)

threading.Thread(target=beep_alarm).start()
cap.release()
cv2.destroyAllWindows()