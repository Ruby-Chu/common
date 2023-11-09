from datetime import datetime
# import base64
# import os


def is_number(n):
    """
    判斷是否為數字
    :param n:
    :return:
    """
    is_number = True
    try:
        num = float(n)
        # 檢查 "nan"
        is_number = num == num  # 或者使用 `math.isnan(num)`
    except ValueError:
        is_number = False

    return is_number

def is_datatime(dt, dt_format):
    """
    判斷是否為日期
    :param dt:
    :param dt_format:
    :return:
    """
    try:
        datetime.strptime(dt, dt_format)
        return True
    except Exception as e:
        return False

# def readBytes(file_path):
#     """
#     將檔案轉成Bytes
#     :param file_path:
#     :return:
#     """
#     encoded_data = base64.b64encode(open(file_path, 'rb').read())
#     strg = ''
#     for i in range(int(len(encoded_data) / 40) + 1):
#         strg += str(encoded_data[i * 40:(i + 1) * 40], 'utf-8')
#     return strg