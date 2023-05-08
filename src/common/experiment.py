# -*- coding: <utf-8> -*-

import time
import threading
import datetime


class ThreadOperate:

    def start_thread(self):
        # 创建两个线程
        try:
            thread1 = threading.Thread(target=self.print_time,
                                       args=("Thread-1", 2))
            thread1.start()
            thread2 = threading.Thread(target=self.print_time,
                                       args=("Thread-2", 4))
            thread2.start()
            thread1.join()
            thread2.join()
            print("完成")
        except Exception as e:
            print(e)

    # 为线程定义一个函数
    def print_time(self, thread_name, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            dt = datetime.datetime.now()
            print("%s: %s" % (thread_name, dt.strftime('%Y-%m-%d %H:%M:%S')))

    def get_thread_info(self):
        print(threading.current_thread())
        print(threading.active_count())
        print(threading.get_ident())
        print(threading.main_thread())


if __name__ == "__main__":
    thread_operate = ThreadOperate()
    # thread_operate.startThread()
    # thread_operate.getThreadInfo()
    f = open('/Users/acc/logs/nacos/config.log')
    print(type(f))
