import sys
import time

# import threading
import multiprocessing

sys.path.append("../Q8")
from mars_mission_computer3 import MissionComputer


def run_computer_info():
    runComputer1 = MissionComputer()
    while True:
        print("=======[Processing Computer Info]=======")
        computer_info = runComputer1.get_mission_computer_info()
        time.sleep(20)


def run_computer_load():
    runComputer2 = MissionComputer()
    while True:
        print("=======[Processing Computer Load]=======")
        computer_load = runComputer2.get_mission_computer_load()
        time.sleep(20)


def run_sensor_data():
    runComputer3 = MissionComputer()
    while True:
        print("=======[Processing Computer Data]=======")
        sensor_data = runComputer3.get_sensor_data()
        time.sleep(20)


if __name__ == "__main__":
    # 멀티 프로세스 생성
    process1 = multiprocessing.Process(target=run_computer_info)
    process2 = multiprocessing.Process(target=run_computer_load)
    process3 = multiprocessing.Process(target=run_sensor_data)

    # 데몬 process로 설정 (메인 프로그램 종료 시 함께 종료)
    process1.daemon = True
    process2.daemon = True
    process3.daemon = True

    # process 시작
    process1.start()
    process2.start()
    process3.start()

    # 메인 process가 종료되지 않도록 대기
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("프로그램을 종료합니다.")

        # threading과 multiprocessing의 차이점# 프로세스 종료
        process1.terminate()
        process2.terminate()
        process3.terminate()

        # 프로세스가 완전히 종료될 때까지 대기
        process1.join()
        process2.join()
        process3.join()


# threading : 동시에 여러 작업을 병렬로 처리할 수 있다. threading을 사용하기 위해서는 threading 모듈을 import 해야 한다.
# multiprocessing : 여러 프로세스를 동시에 실행할 수 있다. 각 프로세스는 독립적인 메모리 공간을 가진다.
# threading과 달리 CPU 집약적인 작업에서 더 좋은 성능을 보인다.
