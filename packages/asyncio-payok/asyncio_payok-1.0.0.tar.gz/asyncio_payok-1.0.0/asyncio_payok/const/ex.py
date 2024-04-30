class ApiError(Exception):
	def __init__(self, code: int, text: str):
		super().__init__(f'Error code:{code} Error: {text}')