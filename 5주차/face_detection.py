# 1. OpenCV 라이브러리를 불러옵니다.
import cv2

# 2. 얼굴 검출을 위한 Haar Cascade 분류기를 불러옵니다.
# 'haarcascade_frontalface_default.xml' 파일이 코드와 같은 경로에 있어야 합니다.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 3. 웹캠을 엽니다. (0은 기본 웹캠을 의미합니다)
cap = cv2.VideoCapture(1)

# 웹캠이 열리지 않았을 경우 에러 메시지를 출력합니다.
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

# 4. 웹캠이 켜져 있는 동안 무한 반복합니다.
while True:
    # 5. 웹캠에서 프레임(이미지)을 한 장씩 읽어옵니다.
    # ret는 성공 여부(True/False), frame은 읽어온 이미지입니다.
    ret, frame = cap.read()

    # 프레임을 제대로 읽어오지 못했다면 루프를 종료합니다.
    if not ret:
        print("프레임을 읽어올 수 없습니다.")
        break

    # 6. 얼굴 검출 성능을 높이기 위해 이미지를 흑백으로 변환합니다.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 7. 흑백 이미지에서 얼굴을 검출합니다.
    # detectMultiScale 함수는 얼굴을 찾고, 그 위치를 리스트로 반환합니다.
    # scaleFactor: 이미지 피라미드 스케일. 숫자가 작을수록 더 꼼꼼하게 찾습니다.
    # minNeighbors: 얼굴로 인정하기 위한 최소 이웃 사각형 수.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # 8. 검출된 얼굴 주변에 사각형을 그립니다.
    # faces 리스트에는 (x좌표, y좌표, 너비, 높이) 정보가 들어있습니다.
    for (x, y, w, h) in faces:
        # 원본 컬러 이미지에 초록색(0, 255, 0) 사각형을 그립니다. 두께는 2.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    num_faces = len(faces)

    # 9. 얼굴에 사각형이 그려진 이미지를 'Face Detection'이라는 이름의 창에 보여줍니다.
    cv2.imshow('Face Detection', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s') and num_faces > 0:
        cv2.imwrite('detected_face.png', frame)
        print("Frame with detected face saved as 'detected_face.png'.")


    # 10. 'q' 키를 누르면 무한 루프를 종료합니다.
    # waitKey(1)은 1ms 동안 키 입력을 기다립니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 11. 사용이 끝난 모든 자원을 해제합니다.
cap.release() # 웹캠을 닫습니다.
cv2.destroyAllWindows() # 모든 창을 닫습니다.