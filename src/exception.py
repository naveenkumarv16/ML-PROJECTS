import sys
import traceback

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Get traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name where error occurred
    line_number = exc_tb.tb_lineno  # Get the exact line number of the error
    error_message = "Error occurred in Python script name [{0}] at line [{1}]: {2}".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
