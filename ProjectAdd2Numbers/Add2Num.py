import logging

logging.basicConfig(
    level=logging.INFO,
    format=''
)

class MyBigNumber:
    def __init__(self): pass

    def sum(self,num1,num2):
        result = ''
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        step = 1 

        while i >= 0 or j >= 0 or carry > 0:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            total = digit1 + digit2 + carry

            if carry > 0:
                logging.info(f"Bước {step}: Lấy {digit1} cộng với {digit2} được {digit1 + digit2}. Cộng tiếp với nhớ {carry} được {total}.")
            else:
                logging.info(f"Bước {step}: Lấy {digit1} cộng với {digit2} được {total}.")

            digit = total % 10
            carry = total // 10
            result = str(digit) + result

            if step ==1: logging.info(f"         Lưu {digit} vào kết quả và nhớ {carry}")
            else: 
                logging.info(f"         Lưu {digit} vào kết quả được kết quả mới là {"result"}")
                logging.info(f"         Ghi nhớ {carry}.")

            i -= 1
            j -= 1  
            step += 1
        
        return result
