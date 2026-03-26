from datetime import datetime
import logging


def analyze_heartbeat(input_file, target_key):
    # задовбався видаляти кожен раз, тому це перезапис вихідного файлу
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        filename='hb_test.log',
        filemode='w',
        level=logging.WARNING,
        format='%(levelname)s - %(message)s'
    )

    # читання логу
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # фільтр по ключу
    filtered_log = [line.strip() for line in lines if target_key in line]

    # переворот хронології (новіші зверху)
    filtered_log.reverse()

    # первірка часових міток
    prev_ts = None

    for line in filtered_log:
        ts_start = line.find("Timestamp ") + 10
        ts_str = line[ts_start: ts_start + 8]
        current_ts = datetime.strptime(ts_str, "%H:%M:%S")

        if prev_ts:
            diff = (current_ts - prev_ts).total_seconds()

            if 31 < diff < 33:
                logging.warning(f"Heartbeat gap: {diff}s at {ts_str} (Key: {target_key})")
            elif diff >= 33:
                logging.error(f"Heartbeat gap: {diff}s at {ts_str} (Key: {target_key})")

        prev_ts = current_ts



analyze_heartbeat('hblog.txt', 'Key TSTFEED0300|7E3E|0400')