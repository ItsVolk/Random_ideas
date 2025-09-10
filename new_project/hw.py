class Queue(self):
    def __init__(self):
        self.print_queue = []

    def enqueue_print_job(self, job):
        self.print_queue.append(job)
        print(f"Thêm {job} vào hàng đợi in")

    def dequeue_print_job(self):
        if self.print_queue:
            print("Không có tác vụ trong hàng đợi")
        else:
            while self.print_queue:
                current_job = dequeue_print_job(self.print_queue)
                print(f"Đang in tác vụ: {current_job}")
