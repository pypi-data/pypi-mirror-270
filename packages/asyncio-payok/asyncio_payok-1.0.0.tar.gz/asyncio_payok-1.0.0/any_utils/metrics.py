from time import time


class Timer:
	def __aenter__(self):
		self.start = time()

	def __aexit__(self, exc_type, exc_val, exc_tb):
		print(f"Elapsed time: {time() - self.start}")

	def __enter__(self):
		self.start = time()

	def __exit__(self, exc_type, exc_val, exc_tb):
		print(f"Elapsed time: {time() - self.start}")