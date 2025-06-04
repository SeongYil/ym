# OpenCV 라이브러리를 불러옵니다.
import cv2

# 웹캠을 엽니다. (0은 기본 웹캠을 의미합니다)
cap = cv2.VideoCapture(0)

# 웹캠이 열리지 않았을 경우 에러 메시지를 출력합니다.
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

# 웹캠이 켜져 있는 동안 무한 반복합니다.
while True:
    # 웹캠에서 프레임(이미지)을 한 장씩 읽어옵니다.
    # ret는 성공 여부(True/False), frame은 읽어온 이미지입니다.
    ret, frame = cap.read()

    # 프레임을 제대로 읽어오지 못했다면 루프를 종료합니다.
    if not ret:
        print("프레임을 읽어올 수 없습니다.")
        break

    # 얼굴에 사각형이 그려진 이미지를 'Face Detection'이라는 이름의 창에 보여줍니다.
    cv2.imshow('Face Detection', frame)

    # 'q' 키를 누르면 무한 루프를 종료합니다.
    # waitKey(1)은 1ms 동안 키 입력을 기다립니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 사용이 끝난 모든 자원을 해제합니다.
cap.release() # 웹캠을 닫습니다.
cv2.destroyAllWindows() # 모든 창을 닫습니다.