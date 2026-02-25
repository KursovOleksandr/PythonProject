"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


#виконання дз
import unittest
import logging


class TestLogEvent(unittest.TestCase):

    def test_success_status_logs_info(self):
        with self.assertLogs('log_event', level='INFO') as log:
            log_event("user1", "success")
            self.assertTrue(any("Status: success" in message for message in log.output))

    def test_expired_status_logs_warning(self):
        with self.assertLogs('log_event', level='WARNING') as log:
            log_event("user2", "expired")
            self.assertTrue(any("Status: expired" in message for message in log.output))

    def test_failed_status_logs_error(self):
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("user3", "failed")
            self.assertTrue(any("Status: failed" in message for message in log.output))

    def test_unknown_status_logs_error(self):
        with self.assertLogs('log_event', level='ERROR') as log:
            log_event("user4", "unknown")
            self.assertTrue(any("Status: unknown" in message for message in log.output))


if __name__ == "__main__":
    unittest.main()
