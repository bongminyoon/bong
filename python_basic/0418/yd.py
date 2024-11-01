import time

# 각 역과 알림 간격 설정
itx_stations = [
    ("서울역", 60),
    ("용산역", 2),
    ("수서역", 3),
    ("대전역", 1),
    ("동대구역", 2),
    ("부산역", 3),
    ("울산역", 1)
]

def notify_station(station, interval):
    print(f"알림: {station}에 도착했습니다.")
    time.sleep(interval)

def main():
    while True:
        user_input = input("시작을 입력하세요: ")
        if user_input.strip().lower() == "시작":
            for station, interval in itx_stations:
                notify_station(station, interval)
            break
        else:
            print("시작을 입력하세요.")

if __name__ == "__main__":
    main()
