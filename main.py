from time import strftime
from datetime import datetime
from bs4 import BeautifulSoup
def clear_():__import__('os').system("cls" if __import__('os').name == "nt" else "clear")
bot = __import__('telebot').TeleBot('6323402729:AAHdM6OcRoG4w5O7hONg_Rhpv9LDnlqotoY')
VND, SDT, TOKEN, CSRF, JOB, MAGD = [], [], [], [], [], []
class REVIEWMAP:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.URL_MAIN = "https://reviewmap.vn/"
        self.HEADERS = {
            "User-Agent": __import__('fake_useragent').UserAgent(),
            "Referer": self.URL_MAIN
        }
        self.session = __import__('requests').Session()
    def get_csrf_token(self):
        response = self.session.get(self.URL_MAIN, headers=self.HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        token = soup.find('input', {'name': '_token'})
        return token['value'] if token else None
    def login(self):
        data = {
            "_token": self.get_csrf_token(),
            "username": self.username,
            "password": self.password,
            "remember": "on"
        }
        response = self.session.post(f"{self.URL_MAIN}login", headers=self.HEADERS, data=data)
        return response if response.status_code == 200 else None
    def register(self, email,momo):
        data = {
            "_token": self.get_csrf_token(),
            "rank": "member",
            "username": self.username,
            "email": email,
            "momo": momo,
            "password": self.password
        }
        response = self.session.post(f"{self.URL_MAIN}register", headers=self.HEADERS, data=data)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            check1 = soup.find('li', string="Tên người dùng đã được sử dụng.")
            check2 = soup.find('li', string="Số momo này đã có trong hệ thống!")
            check3 = soup.find("div", class_="alert alert-danger shadow-sm alert-dismissible fade show", role="alert")
            if check1:return 1
            if check2:return 2
            if check3:return 3
            return "[+] [TẠO TK THÀNH CÔNG]"
        else: return None
    def rut_money(self,money):
        headers = {**self.HEADERS, "Authorization": f"Bearer {TOKEN[0]}","Content-Type": "application/json"}
        data = {"channel": "momo", "amount": money}
        response = self.session.post(f"{self.URL_MAIN}api/users/invoices", headers=headers, json=data)
        if response.status_code == 200:
            _money_ = response.json()
            momo = SDT[0]
            ___ = "*"
            if _money_['status'] == 200:return f"""> {_money_['message']} <
👤 𝗕𝗨𝗜𝗟𝗗 - 𝗛𝗢𝗔́ Đ𝗢̛𝗡 𝗥𝗨́𝗧 𝗧𝗜𝗘̂̀𝗡
 ├ SỐ MOMO: [{momo[:3] + ___*5 + momo[-2:]} 🇻🇳]💰
 ├ TRẠNG THÁI: [{_money_['data']['status']}]...
 ├ SỐ TIỀN NHẬN: [{_money_['data']['amount']}:{_money_['data']['currency']}]💵
 ├ VÍ NGÂN HÀNG: [{_money_['data']['description']}]
 ├ MÃ GIAO DỊCH: [{_money_['data']['code']}]🤖
 ├ {'#'*34}"""
            else:return "None"
        else:return None
    def check_min(self):
        response = self.session.get(f"{self.URL_MAIN}account/deposits", headers=self.HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        amount = soup.find('input', {'id': 'amount'})
        return amount['value'] if amount else None
    def check_th_tin(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        thong_tin = soup.find('script', {})
        web_data_match = __import__('re').search(r'window\.webData\s*=\s*(\{.*?\});', thong_tin.string)
        user_data_match = __import__('re').search(r'window\.userData\s*=\s*(\{.*?\});', thong_tin.string)
        if web_data_match and user_data_match:
            web_data = __import__('json').loads(web_data_match.group(1))
            user_data = __import__('json').loads(user_data_match.group(1))
            job = soup.find("span", class_="badge bg-success").get_text(strip=True)
            momo = user_data['momo']
            email = user_data['email']
            token = user_data['access_token']
            ip = user_data['ip_address']
            VND.append(user_data['balance'])
            SDT.append(momo)
            TOKEN.append(token)
            # CSRF.append(web_data['csrfToken'])
            if int(job) == 1:JOB.append(job)
            ___ = "*"
            return f"""👤 𝙄𝙉𝙁𝙊 - 𝙏𝙃𝙊̂𝙉𝙂 𝙏𝙄𝙉 Đ𝘼̆𝙉𝙂 𝙉𝙃𝘼̣̂𝙋  
 ├ [NHIỆM VỤ HÔM NAY]: [{job}|job]💼
 ├ [TÊN ACCOUNT]: {user_data['username']}༗
 ├ [EMAIL]: {email[:2] + ___*5 + email[-12:]}📧
 ├ [ĐỊA CHỈ IP]: {ip[:5] + ((___*3+':')*3)[:11] + ip[-4:]}🔗
 ├ [SỐ MOMO]: {momo[:3] + ___*5 + momo[-2:]} | Money: {user_data['balance']}VND💵
 ├ [NGÀY TẠO TK]: {user_data['created_at']}📌"""
    def nhiem_vu(self):
        nhiemvu = self.session.get(f"{self.URL_MAIN}public/", headers=self.HEADERS)
        soup = BeautifulSoup(nhiemvu.text, 'html.parser')
        code = soup.find('code',{}).text.split(':')[1]
        time = soup.find('span', {'id': 'time_remaining'}).text
        link = soup.find('input', {'type': 'text', 'class': 'form-control', 'id': 'link_review'})['value']
        if code or time or link or code:
            _O_ = "#"*34
            code = code[-(int(len(code))-1):]
            MAGD.append(code)
            return f"""💼 𝗝𝗢𝗕 - 𝗡𝗛𝗜𝗘̣̂𝗠 𝗩𝗨̣ 𝗛𝗢̂𝗠 𝗡𝗔𝗬
 ├ [MÃ NHIỆM VỤ]: {code}🤖
 ├ [THỜI GIAN LÀM VIỆC]: {time}📟
 ├ [LINK NHIỆM VỤ]: {link}
 ├ {_O_}
 ├ [B1]: [LIKE 5 BÀI VIẾT 5 SAO MỚI NHẤT]⭐
 ├ [B2]: [ĐÁNH GIÁ SAO VÀ KÈM NỘI DUNG]📝
 ├ [B3]: [QUAY LẠI BOT VÀ NỘP KẾT QUẢ]📨
 ├ {_O_}"""
        else:return 0
    def done_nv(self, noidung):
        headers = {**self.HEADERS, "Authorization": f"Bearer {TOKEN[0]}", "Content-Type": "application/json", "X-Requested-With": "application/json"}
        data = {"code": MAGD[0],"assign_content": noidung}
        response = self.session.post(f"{self.URL_MAIN}api/jobs/update", headers=headers, json=data)
        return response.json() if response.status_code == 200 else None
    def check_nhiem_vu(self):
        headers = {**self.HEADERS, "Authorization": f"Bearer {TOKEN[0]}","Content-Type": "application/json"}
        data = {}
        response = self.session.post(f"{self.URL_MAIN}api/jobs/store", headers=headers, json=data)
        return response.json() if response.status_code == 200 else None
    def check_hoa_don(self):
        response = self.session.get(f"{self.URL_MAIN}account/deposits", headers=self.HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='display table table-bordered table-stripped text-nowrap datatable')
        order_data, dsgd = [], []
        note = ["#", "Mã GD", "Số tiền", "Kênh rút", "Số điện thoại", "Trạng thái", "Thời gian"]
        for row in table.find('tbody').find_all('tr'):
            columns = [col.text.strip() for col in row.find_all('td')]
            order = {
                note[0]: columns[1],
                note[1]: columns[2],
                note[2]: columns[4],
                note[3]: columns[5],
                note[4]: columns[6]
            }
            order_data.append(order)
        for order in order_data:dsgd.append(f"🔰 [📣][ {order[note[3]]} ]-[💵][ {order[note[1]]:} ]-[💰][{order[note[2]]}][{order[note[0]]}]-[⏰][{order[note[4]]}]")
        return '\n'.join(dsgd)
    def check_job(self):
        response = self.session.get(f"{self.URL_MAIN}account/profile/transactions", headers=self.HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='datatable')
        order_data, dshoadon = [], []
        note = ["Trạng Thái", "Phần Thưởng", "Thời Gian"]
        for row in table.find('tbody').find_all('tr'):
            columns = [col.text.strip() for col in row.find_all('td')]
            order = {
                note[0]: columns[3],
                note[1]: columns[5],
                note[2]: columns[6]
            }
            order_data.append(order)
        for order in order_data:dshoadon.append(f"🔰 [📣][ {order[note[0]]} ]-[💵][ {order[note[1]]:} ]-[⏰][ {order[note[2]]} ]")
        return '\n'.join(dshoadon)
_ = "="*42
__ = "="*20
clear_()
_id_, _del_, _acc_, _count_, _number_, _so_, _pwd_ = [], [], [], [], [], [], []
ID_TELE = "ACCOUNT_ID"
if not __import__('os').path.exists(ID_TELE):__import__('os').makedirs(ID_TELE)
def save_acc(chat_id, username, password):open(__import__('os').path.join(ID_TELE, str(chat_id)), 'w').write(f'{{"username": ["{username}"],"password": ["{password}"]}}')
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    markup = __import__('telebot').types.ReplyKeyboardMarkup(one_time_keyboard=True)
    user = bot.get_me()
    time = strftime("%d/%m/%Y")
    time_ = strftime("%H:%M:%S")
    if str(chat_id) not in __import__('os').listdir(ID_TELE):
        if chat_id not in _id_:
            _id_.append(chat_id)
            print(f'[+] Người Sử Dụng Mới: {message.chat.first_name} - {message.chat.username} | Time: {time} - {time_}')
            bot.reply_to(message, f">> Xin Chào [{message.chat.first_name} - {message.chat.username}] <<\n\n"
                        "|| TÔI LÀ BOT REVIEW ĐÁNH GIÁ GOOGLE MAP ||\n"
                        f"{'#'*46}\n"
                        "-> Ở ĐÂY BẠN CÓ THỂ KIẾM ĐƯỢC CHÚT THU NHẬP TỪ VIỆC ĐÁNH GIÁ GOOGLE MAP\n"
                        "-> THU NHẬP SẼ ĐƯỢC UPDATE THEO THỊ TRƯỜNG, TÔI SẼ THÔNG BÁO CHO BẠN KHI CÓ CẬP NHẬP MỚI\n"
                        "-> MỖI NGÀY CHỈ LÀM ĐƯỢC 1 NHIỆM VỤ, KHI BẠN LÀM XONG NHIỆM VỤ THÌ TÔI SẼ TRẢ TIỀN CHO BẠN\n"
                        "-> QUÁ TRÌNH TẠO TÀI KHOẢN BẮT BUỘC BẠN PHẢI CÓ VÍ MOMO, ĐĂNG KÍ VÍ MOMO TRÊN 18 TUỔI TẠI ĐÂY\n"
                        f"{'#'*46}\n"
                        ">> MÃ GIỚI THIỆU: 0814463499"
                        ">> LINK ĐĂNG KÍ: https://momoapp.page.link/9NLgfa3vngT4QtvK8?utm_source=referral_others\n"
                        f"{'#'*46}\n"
                        "-> CHÚC BẠN SỬ BOT VUI VẺ - NẾU CÓ LỖI GÌ HÃY LIÊN HỆ ĐẾN AMDIN TELE: @Minh_Nguyen_2412\n"
                        f"{'#'*46}\n") #{user.first_name} - {user.username}
    else:
        if not _id_:_id_.append(chat_id)
        if chat_id in _id_:
            thoi_gian = datetime.now().hour
            if 4 <= thoi_gian <= 5:hello = "BUỔI SÁNG SỚM"
            elif 6 <= thoi_gian <= 7:hello = "BUỔI SÁNG"
            elif 8 <= thoi_gian <= 9:hello = "BUỔI SỚM TRƯA"
            elif 10 <= thoi_gian <= 12:hello = "BUỔI TRƯA"
            elif 13 <= thoi_gian <= 17:hello = "BUỔI CHIỀU"
            elif 18 <= thoi_gian <= 19:hello = "BUỔI CHIỀU TỐI"
            elif 20 <= thoi_gian <= 21:hello = "BUỔI TỐI"
            elif 22 <= thoi_gian <= 24 or thoi_gian == 0:
                hello = "BUỔI KHUYA"
                print(f'[+] Người Sử Dụng Mới: {message.chat.first_name} - {message.chat.username} | Time: {time} - {time_}')
                _del_.clear()
            if not _del_:
                _del_.append(chat_id)
                try:bot.reply_to(message, f">> HELLO, XIN CHÀO {hello} [{message.chat.first_name} - {message.chat.username}] <<\n{'#'*46}\n>> NẾU TRONG QUÁ TRÌNH SỬ DỤNG LÂU NGÀY, TIN NHẮN THỪA THẢI TÍCH TỤ, BẠN CÓ THỂ XOÁ TOÀN BỘ CUỘC TRÒ CHUYỆN SAU ĐÓ [START] LẠI BOT <<")
                except Exception:bot.send_message(chat_id, f">> HELLO, XIN CHÀO {hello} [{message.chat.first_name} - {message.chat.username}] <<\n\n")
    msg1 = bot.send_message(chat_id, f">>>{' '*7}MENU{' '*7}<<<\n/{'-'*31}\\\n   [1]: ĐĂNG NHẬP 🔐\n   [2]: ĐĂNG KÍ 🔏\n\\{'_'*20}/\n[>]: [LỰA CHỌN]", reply_markup=markup)
    bot.register_next_step_handler(message, MENU_MAIN, msg1)
def MENU_MAIN(message, msg1):
    chat_id = message.chat.id
    choice = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if choice == "/start":
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
        return
    elif choice == "1":
        bot.delete_message(chat_id, msg1.message_id)
        USERNAME(message)
    elif choice == "2":
        bot.delete_message(chat_id, msg1.message_id)
        USN_RGT(message)
    else:
        msg2 = bot.send_message(chat_id, "[!] [NHẬP SAI LỰA CHỌN]")
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        start(message)
def USERNAME(message):
    chat_id = message.chat.id
    for file_id in __import__('os').listdir(ID_TELE):
        if file_id == str(chat_id):
            file_id = __import__('os').path.join(ID_TELE, str(chat_id))
            break
    try:
        if __import__('os').path.exists(file_id):
            with open(file_id, "r") as file:
                if file.read().strip():
                    file.seek(0)
                    data = __import__('json').load(file)
                else:data = {"username": [], "passworld": []}
            if "username" in data and "password" in data and data["username"] and data["password"]:
                accounts = list(zip(data["username"], data["password"]))
                msg1 = bot.send_message(chat_id, f"🔐 𝗟𝗢𝗚𝗜𝗡 - Đ𝗔̆𝗡𝗚 𝗡𝗛𝗔̣̂𝗣 𝗔𝗖𝗖𝗢𝗨𝗡𝗧\n ├ [>] [BẠN ĐANG CÓ ({len(accounts)}) TÀI KHOẢN]\n ├ [1] [LOGIN TÀI KHOẢN]\n ├ [2] [DELE TÀI KHOẢN]\n ├ [3] [THÊM TÀI KHOẢN]\n ├ [B] [QUAY LẠI]\n └ [>] [NHẬP LỰA CHỌN]")
                if message.text == "/start":
                    bot.delete_message(chat_id, msg1.message_id)
                    start(message)
                    return
                else:bot.register_next_step_handler(message, CHECK_ACC, data, accounts, file_id, msg1)
            else:
                msg1 = bot.send_message(chat_id, "🔐 𝗟𝗢𝗚𝗜𝗡 - Đ𝗔̆𝗡𝗚 𝗡𝗛𝗔̣̂𝗣 𝗔𝗖𝗖𝗢𝗨𝗡𝗧\n ├ [B]: [QUAY LẠI]\n ├ [>]: [NHẬP TÊN TÀI KHOẢN]")
                if message.text == "/start":
                    bot.delete_message(chat_id, msg1.message_id)
                    start(message)
                    return
                else:bot.register_next_step_handler(message, PASSWORD, msg1)
    except UnboundLocalError:
        msg1 = bot.send_message(chat_id, "🔐 𝗟𝗢𝗚𝗜𝗡 - Đ𝗔̆𝗡𝗚 𝗡𝗛𝗔̣̂𝗣 𝗔𝗖𝗖𝗢𝗨𝗡𝗧\n ├ [B]: [QUAY LẠI]\n ├ [>]: [NHẬP TÊN TÀI KHOẢN]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg1.message_id)
            start(message)
            return
        else:bot.register_next_step_handler(message, PASSWORD, msg1)
def CHECK_ACC(message, data, accounts, file_id, msg1):
    chat_id = message.chat.id
    check = message.text.strip()
    try:bot.delete_message(chat_id, message.message_id)
    except:
        if _so_:check = _so_[0]
    if check.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
    elif check == '1':
        bot.delete_message(chat_id, msg1.message_id)
        for i, (user, pwd) in enumerate(accounts, start=1):_acc_.append(f" ├ [{i}] [TK: {user} || MK: {pwd}]")
        acc = '\n'.join(_acc_)
        msg1 = bot.send_message(chat_id, f"🔐 𝗟𝗢𝗚𝗜𝗡 - Đ𝗔̆𝗡𝗚 𝗡𝗛𝗔̣̂𝗣 𝗔𝗖𝗖𝗢𝗨𝗡𝗧\n ├ [>] [BẠN ĐANG CÓ ({len(accounts)}) TÀI KHOẢN]\n{acc}\n ├ [B] [QUAY LẠI]\n └ [>] [NHẬP LỰA CHỌN]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg1.message_id)
            start(message)
            return
        else:
            _acc_.clear()
            if _so_:_so_.clear()
            bot.register_next_step_handler(message, LOGIN, data, accounts, file_id, msg1)
    elif check == '2':
        bot.delete_message(chat_id, msg1.message_id)
        for i, (user, pwd) in enumerate(accounts, start=1):_acc_.append(f" ├ [{i}] [TK: {user} || MK: {pwd}]")
        acc = '\n'.join(_acc_)
        msg1 = bot.send_message(chat_id, f"✂️ 𝗗𝗘𝗟𝗘 - 𝗫𝗢𝗔́ 𝗧𝗔̀𝗜 𝗞𝗛𝗢𝗔̉𝗡\n ├ [>] [BẠN ĐANG CÓ ({len(accounts)}) TÀI KHOẢN]\n{acc}\n ├ [B] [QUAY LẠI]\n └ [>] [NHẬP LỰA CHỌN (ex: 1, 2, 3,...)]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg1.message_id)
            start(message)
            return
        else:
            _acc_.clear()
            if _so_:_so_.clear()
            bot.register_next_step_handler(message, DELE_ACC, data, accounts, file_id, msg1)
    elif check == '3':
        bot.delete_message(chat_id, msg1.message_id)
        for i, (user, pwd) in enumerate(accounts, start=1):_acc_.append(f" ├ [>] [TK: {user} || MK: {pwd}]")
        acc = '\n'.join(_acc_)
        msg1 = bot.send_message(chat_id, f"📝 𝗔𝗗𝗗 - 𝗧𝗛𝗘̂𝗠 𝗧𝗔̀𝗜 𝗞𝗛𝗢𝗔̉𝗡\n ├ [>] [BẠN ĐANG CÓ ({len(accounts)}) TÀI KHOẢN]\n{acc}\n ├ [B] [QUAY LẠI]\n └ [>] [NHẬP SỐ LƯỢNG TÀI KHOẢN CẦN THÊM]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg1.message_id)
            start(message)
            return
        else:
            _acc_.clear()
            if _so_:_so_.clear()
            bot.register_next_step_handler(message, ADD_ACC, data, file_id, accounts, msg1, msg2=None)
    else:
        msg2 = bot.send_message(chat_id, "[!] [NHẬP SAI LỰA CHỌN]")
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        USERNAME(message)
def LOGIN(message, data, accounts, file_id, msg1):
    chat_id = message.chat.id
    check = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if check.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        USERNAME(message)
    else:
        account = int(check) - 1
        if 0 <= account < len(accounts):
            username, passworld = accounts.pop(account)
            _pwd_.append(passworld)
            LOGIN_NEW(message, username, msg1, msg2=None)
        else:
            msg2 = bot.send_message(chat_id, "[!] [TÀI KHOẢN KHÔNG CÓ TRONG DANH SÁCH]")
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg1.message_id)
            _so_.append("2")
            CHECK_ACC(message, data, accounts, file_id, msg2)
def LOGIN_OLD(message, data, file_id, accounts, msg1, msg2):
    chat_id = message.chat.id
    account = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if account.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        USERNAME(message)
    if len(account.split(':')) > 2:
        msg3 = bot.send_message(chat_id, '[!] [NHẬP SAI CÚ PHÁP]')
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg2.message_id)
        bot.delete_message(chat_id, msg3.message_id)
        ADD_ACC(message, data, file_id, accounts, msg1, msg2=None)
    try:
        if not account.split(':')[0] or not account.split(':')[1]:
            msg3 = bot.send_message(chat_id, '[!] [NHẬP SAI CÚ PHÁP]')
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg2.message_id)
            bot.delete_message(chat_id, msg3.message_id)
            ADD_ACC(message, data, file_id, accounts, msg1, msg2=None)
        elif account.split(':')[0] and account.split(':')[1]:
            if len(account.split(':')[1]) < 10:
                msg3 = bot.send_message(chat_id, '[!] [MẬT KHẨU PHẢI TỪ 10 KÍ TỰ TRỞ LÊN]')
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                ADD_ACC(message, data, file_id, accounts, msg1, msg2=None)
            if account.split(':')[0] in data["username"] and account.split(':')[1] in data["password"]:
                msg3 = bot.send_message(chat_id, '[!] [TÀI KHOẢN ĐÃ CÓ TRONG DANH SÁCH]')
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                ADD_ACC(message, data, file_id, accounts, msg1, msg2=None)
            MAIN = REVIEWMAP(account.split(':')[0], account.split(':')[1])
            LOGIN = MAIN.login()
            try:thong_tin = MAIN.check_th_tin(LOGIN.text)
            except AttributeError:
                msg3 = bot.send_message(chat_id, "[!] [TÀI KHOẢN CHƯA ĐƯỢC ĐĂNG KÍ]")
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                ADD_ACC(message, data, file_id, accounts, msg1, msg2=None)
            if thong_tin != None:
                data["username"].append(account.split(':')[0])
                data["password"].append(account.split(':')[1])
                __import__('json').dump(data, open(file_id, "w"), indent=4)
                msg3 = bot.send_message(chat_id, "[+] [ĐÃ THÊM TÀI KHOẢN]")
                if int(len(_count_)) == int(_number_[0]):
                    _count_.clear()
                    bot.delete_message(chat_id, msg1.message_id)
                    bot.delete_message(chat_id, msg2.message_id)
                    bot.delete_message(chat_id, msg3.message_id)
                    USERNAME(message)
                else:
                    _count_.append(1)
                    __import__('time').sleep(2)
                    bot.delete_message(chat_id, msg2.message_id)
                    bot.delete_message(chat_id, msg3.message_id)
                    ADD_ACC(message, data, file_id, accounts, msg1, msg2=None)
            else:
                msg3 = bot.send_message(chat_id, "[!] [TÀI KHOẢN CHƯA ĐƯỢC ĐĂNG KÍ]")
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                ADD_ACC(message, data, file_id, accounts, msg1, msg2=None)
    except IndexError:
        msg3 = bot.send_message(chat_id, '[!] [NHẬP SAI CÚ PHÁP]')
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg2.message_id)
        bot.delete_message(chat_id, msg3.message_id)
        ADD_ACC(message, data, file_id, accounts, msg1, msg2=None)
def ADD_ACC(message, data, file_id, accounts, msg1, msg2):
    chat_id = message.chat.id
    check = message.text.strip()
    try:bot.delete_message(chat_id, message.message_id)
    except Exception:pass
    if msg2 != None:msg2 = msg2
    if check.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        USERNAME(message)
    else:
        try:
            if check == "0":
                msg3 = bot.send_message(chat_id, "[!] [SỐ LƯỢNG TÀI KHOẢN PHẢI LỚN HƠN (0)]")
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg1.message_id)
                _so_.append("3")
                CHECK_ACC(message, data, accounts, file_id, msg3)
            if not _number_:_number_.append(int(check))
            if _count_:
                if int(_count_[0]) == 1:count = int(_count_[0])
                else:count = int(_count_[0]) - (int(_count_[0])-1)
            else:
                count = int(check) - (int(check)-1)
                _count_.append(count)
            msg2 = bot.send_message(chat_id, f"[+] NHẬP TÀI KHOẢN THỨ {len(_count_)}|(usr:pwd)]")
            if message.text == "/start":
                bot.delete_message(chat_id, msg1.message_id)
                bot.delete_message(chat_id, msg2.message_id)
                start(message)
                return
            else:bot.register_next_step_handler(message, LOGIN_OLD, data, file_id, accounts, msg1, msg2)
        except ValueError:
            msg2 = bot.send_message(chat_id, "[!] [NHẬP SAI ĐỊNH DẠNG CÂU HỎI]")
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg1.message_id)
            _so_.append("3")
            CHECK_ACC(message, data, accounts, file_id, msg2)
def DELE_ACC(message, data, accounts, file_id, msg1):
    chat_id = message.chat.id
    check = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if check.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        USERNAME(message)
    else:
        try:
            if len(check.split(',')) == 1:
                account = int(check) - 1
                if 0 <= account < len(accounts):
                    removed_user, removed_pwd = accounts.pop(account)
                    data["username"].remove(removed_user)
                    data["password"].remove(removed_pwd)
                    __import__('json').dump(data, open(file_id, "w"), indent=4)
                    msg2 = bot.send_message(chat_id, f"[+] [ĐÃ DELETE TÀI KHOẢN ({account+1})]")
                    __import__('time').sleep(2)
                    bot.delete_message(chat_id, msg1.message_id)
                    if len(accounts) == 0:
                        bot.delete_message(chat_id, msg2.message_id)
                        USERNAME(message)
                    else:
                        _so_.append("2")
                        CHECK_ACC(message, data, accounts, file_id, msg2)
                else:
                    msg2 = bot.send_message(chat_id, "[!] [TÀI KHOẢN KHÔNG CÓ TRONG DANH SÁCH]")
                    __import__('time').sleep(2)
                    bot.delete_message(chat_id, msg1.message_id)
                    _so_.append("2")
                    CHECK_ACC(message, data, accounts, file_id, msg2)
            else:
                acc = check.split(',')
                del_acc = [int(acc[i]) for i in range(len(acc)) if acc[i].isdigit()]
                seen = set()
                for account in del_acc:
                    if isinstance(account, int) and account not in seen and 0 <= account-1 < len(accounts):
                        seen.add(account)
                        removed_user, removed_pwd = accounts[account-1]
                        data["username"].remove(removed_user)
                        data["password"].remove(removed_pwd)
                        __import__('json').dump(data, open(file_id, "w"), indent=4)
                        msg2 = bot.send_message(chat_id, f"[+] [ĐÃ DELETE TÀI KHOẢN ({account})]")
                        __import__('time').sleep(2)
                        bot.delete_message(chat_id, msg2.message_id)
                del_acc.clear()
                if len(accounts) == 0:
                    bot.delete_message(chat_id, msg1.message_id)
                    USERNAME(message)
                else:
                    _so_.append("2")
                    data = __import__('json').load(open(file_id, "r"))
                    accounts = list(zip(data["username"], data["password"]))
                    CHECK_ACC(message, data, accounts, file_id, msg1)
        except ValueError:
            msg2 = bot.send_message(chat_id, "[!] [NHẬP SAI LỰA CHỌN]")
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg1.message_id)
            _so_.append("2")
            CHECK_ACC(message, data, accounts, file_id, msg2)
def PASSWORD(message, msg1):
    chat_id = message.chat.id
    username = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if username.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
    else: 
        msg2 = bot.send_message(chat_id, " └ [>]: [NHẬP MẬT KHẨU]")
        bot.register_next_step_handler(message, LOGIN_NEW, username, msg1, msg2)
def USN_RGT(message):
    chat_id = message.chat.id
    msg1 = bot.send_message(chat_id, "🔏 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 - Đ𝗔̆𝗡𝗚 𝗞𝗜́ 𝗔𝗖𝗖𝗢𝗨𝗡𝗧\n ├ [B]: [QUAY LẠI]\n ├ [>]: [NHẬP TÊN TÀI KHOẢN]")
    if message.text == "/start":
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
        return
    else:bot.register_next_step_handler(message, EML_RGT, msg1)
def EML_RGT(message, msg1):
    chat_id = message.chat.id
    username = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if username.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
    else: 
        msg2 = bot.send_message(chat_id, " ├ [>]: [NHẬP EMAIL]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg2.message_id)
            start(message)
            return
        else:bot.register_next_step_handler(message, MM_RGT, username, msg1, msg2)
def MM_RGT(message, username, msg1, msg2):
    chat_id = message.chat.id
    email = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if email.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        start(message)
    else: 
        msg3 = bot.send_message(chat_id, " ├ [>]: [NHẬP SỐ MOMO]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg3.message_id)
            start(message)
            return
        else:bot.register_next_step_handler(message, PWD_RGT, username, email, msg1, msg2, msg3)
def PWD_RGT(message, username, email, msg1, msg2, msg3):
    chat_id = message.chat.id
    momo = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if momo.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        bot.delete_message(chat_id, msg3.message_id)
        start(message)
    else: 
        msg4 = bot.send_message(chat_id, " └ [>]: [NHẬP MẬT KHẨU]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg4.message_id)
            start(message)
            return
        else:bot.register_next_step_handler(message, REGISTER, username, email, momo, msg1, msg2, msg3, msg4)
def REGISTER(message, username, email, momo, msg1, msg2, msg3, msg4):
    chat_id = message.chat.id
    password = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if password.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        bot.delete_message(chat_id, msg3.message_id)
        bot.delete_message(chat_id, msg4.message_id)
        start(message)
    else:
        if len(password) < 10:
            msg3 = bot.send_message(chat_id, '[!] [MẬT KHẨU PHẢI TỪ 10 KÍ TỰ TRỞ LÊN]')
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg1.message_id)
            bot.delete_message(chat_id, msg2.message_id)
            bot.delete_message(chat_id, msg3.message_id)
            bot.delete_message(chat_id, msg4.message_id)
            start(message)
        msg5 = bot.send_message(chat_id, "[+] [Loading]...")
        REGISTER = REVIEWMAP(username, password).register(email=email,momo=momo)
        if REGISTER == None:
            msg6 = bot.send_message(chat_id, "[!] [LỖI ĐƯỜNG TRUYỀN]")
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg1.message_id)
            bot.delete_message(chat_id, msg2.message_id)
            bot.delete_message(chat_id, msg3.message_id)
            bot.delete_message(chat_id, msg4.message_id)
            bot.delete_message(chat_id, msg5.message_id)
            bot.delete_message(chat_id, msg6.message_id)
            start(message)
        else:
            if REGISTER == 1:
                msg6 = bot.send_message(chat_id, "[!] [TÊN ACC ĐÃ ĐƯỢC SỬ DỤNG!]")
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg1.message_id)
                bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                bot.delete_message(chat_id, msg4.message_id)
                bot.delete_message(chat_id, msg5.message_id)
                bot.delete_message(chat_id, msg6.message_id)
                USN_RGT(message)
            elif REGISTER == 2:
                msg6 = bot.send_message(chat_id, "[!] [SỐ MOMO ĐÃ ĐƯỢC SỬ DỤNG!]")
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg1.message_id)
                bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                bot.delete_message(chat_id, msg4.message_id)
                bot.delete_message(chat_id, msg5.message_id)
                bot.delete_message(chat_id, msg6.message_id)
                USN_RGT(message)
            elif REGISTER == 3:
                msg6 = bot.send_message(chat_id, "[!] [PHÁT HIỆN SPAM REGISTER ĐẾN MÁY CHỦ!]")
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg1.message_id)
                bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                bot.delete_message(chat_id, msg4.message_id)
                bot.delete_message(chat_id, msg5.message_id)
                bot.delete_message(chat_id, msg6.message_id)
                USN_RGT(message)
            else:
                msg6 = bot.send_message(chat_id, REGISTER)
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg1.message_id)
                bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                bot.delete_message(chat_id, msg4.message_id)
                bot.delete_message(chat_id, msg5.message_id)
                bot.delete_message(chat_id, msg6.message_id)
                start(message)
def LOGIN_NEW(message, username, msg1, msg2):
    chat_id = message.chat.id
    if _pwd_:password = _pwd_[0]
    else:password = message.text.strip()
    try:bot.delete_message(chat_id, message.message_id)
    except Exception:pass
    if password.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        if msg2 != None:bot.delete_message(chat_id, msg2.message_id)
        start(message)
    else:
        if len(password) < 10:
            msg3 = bot.send_message(chat_id, '[!] [MẬT KHẨU PHẢI TỪ 10 KÍ TỰ TRỞ LÊN]')
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg1.message_id)
            if msg2 != None:bot.delete_message(chat_id, msg2.message_id)
            bot.delete_message(chat_id, msg3.message_id)
            start(message)
        msg3 = bot.send_message(chat_id, "[+] [Loading]...")
        MAIN = REVIEWMAP(username, password)
        LOGIN = MAIN.login()
        _pwd_.clear()
        if LOGIN != None:
            try:thong_tin = MAIN.check_th_tin(LOGIN.text)
            except AttributeError:
                msg4 = bot.send_message(chat_id, "[!] [LOGIN FAILED]")
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg1.message_id)
                if msg2 != None:bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                bot.delete_message(chat_id, msg4.message_id)
                USERNAME(message)
            if thong_tin != None:
                if msg2 != None:save_acc(chat_id, username, password)
                msg4 = bot.send_message(chat_id, "[+] [LOGIN SUCCESSFUL]...")
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg1.message_id)
                if msg2 != None:bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                bot.delete_message(chat_id, msg4.message_id)
                NHIEMVU(message, MAIN, thong_tin)
            else:
                msg4 = bot.send_message(chat_id, "[!] [LOGIN FAILED]")
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg1.message_id)
                if msg2 != None:bot.delete_message(chat_id, msg2.message_id)
                bot.delete_message(chat_id, msg3.message_id)
                bot.delete_message(chat_id, msg4.message_id)
                USERNAME(message)
        else:
            msg4 = bot.send_message(chat_id, "[!] [LỖI ĐƯỜNG TRUYỀN]")
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg1.message_id)
            if msg2 != None:bot.delete_message(chat_id, msg2.message_id)
            bot.delete_message(chat_id, msg3.message_id)
            bot.delete_message(chat_id, msg4.message_id)
            start(message)
def NHIEMVU(message, MAIN, thong_tin):
    chat_id = message.chat.id
    try:check_nv = MAIN.nhiem_vu()
    except AttributeError as e:
        if "'NoneType' object has no attribute 'text'" in str(e):check_nv = 0
    if JOB or check_nv != 0:job = f" ├ {'#'*34}\n ├ [PHÁT HIỆN NHIỆM VỤ (0=LÀM NÓ)]"
    else:job = f" ├ {'#'*34}\n ├ [HIỆN TẠI KHÔNG CÓ NHIỆM VỤ!]\n ├ [THỜI GIAN XUẤT HIỆN NHIỆM VỤ]\n ├ [7h01, 8h01, 9h01, 22h01,....]⏰\n ├ {'#'*34}"
    msg1 = bot.send_message(chat_id, f"""{thong_tin}
{job}
 ├ [1]: [CHECK LỊCH SỬ NHIỆM VỤ]
 ├ [2]: [RÚT TIỀN VỀ TÀI KHOẢN]
 ├ [3]: [ĐỔI TÀI KHOẢN KHÁC]
 └ [>]: [NHẬP LỰA CHỌN]""")
    if message.text == "/start":
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
        return
    else:bot.register_next_step_handler(message, DONHANG, MAIN, thong_tin, msg1)
def DONHANG(message, MAIN, thong_tin, msg1):
    chat_id = message.chat.id
    choice = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if choice == "1":
        bot.delete_message(chat_id, msg1.message_id)
        msg1 = bot.send_message(chat_id, f">>>{' '*32}𝗟𝗜̣𝗖𝗛 𝗦𝗨̛̉ 𝗡𝗛𝗜𝗘̣̂𝗠 𝗩𝗨̣{' '*32}<<<\n{'#'*46}\n{MAIN.check_job()}\n{'#'*46}\n[>]: [B = QUAY LẠI]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg1.message_id)
            start(message)
            return
        else:bot.register_next_step_handler(message, CHECKDONHANG, MAIN, thong_tin, msg1)
    elif choice == "2":
        bot.delete_message(chat_id, msg1.message_id)
        RUTTIEN(message, MAIN, thong_tin)
    elif choice == "3":
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
    elif choice == "0":
        try:check_nv = MAIN.nhiem_vu()
        except AttributeError as e:
            if "'NoneType' object has no attribute 'text'" in str(e):check_nv = 0
        if check_nv == 0:
            nhiem_vu = MAIN.check_nhiem_vu()
            if nhiem_vu == None:
                msg2 = bot.send_message(chat_id, '[!] [KHÔNG CÓ NHIỆM VỤ]')
                __import__('time').sleep(2)
                bot.delete_message(chat_id, msg1.message_id)
                bot.delete_message(chat_id, msg2.message_id)
                NHIEMVU(message, MAIN, thong_tin)
            else:msg2 = bot.send_message(chat_id, f"[+] [{nhiem_vu['message']}]")
            msg3 = bot.send_message(chat_id, "[+] [LOADING NHIỆM VỤ...]")
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg1.message_id)
            bot.delete_message(chat_id, msg2.message_id)
            bot.delete_message(chat_id, msg3.message_id)
            GET_NV(message, MAIN, thong_tin, MAIN.nhiem_vu())
        else:
            msg2 = bot.send_message(chat_id, "[+] [LOADING NHIỆM VỤ...]")
            __import__('time').sleep(2)
            bot.delete_message(chat_id, msg1.message_id)
            bot.delete_message(chat_id, msg2.message_id)
            GET_NV(message, MAIN, thong_tin, check_nv)
    else:
        msg2 = bot.send_message(chat_id, "[!] [NHẬP SAI LỰA CHỌN]")
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        NHIEMVU(message, MAIN, thong_tin)
def GET_NV(message, MAIN, thong_tin, check_nv):
    chat_id = message.chat.id
    msg1 = bot.send_message(chat_id, f"{check_nv}\n ├ [B] [QUAY LẠi]\n └ [!DÁN NHẬN XÉT DÁNH ĐÁNH TẠI ĐÂY!]")
    if message.text == "/start":
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
        return
    else:bot.register_next_step_handler(message, XD_NV, MAIN, thong_tin, msg1, check_nv)
def XD_NV(message, MAIN, thong_tin, msg1, check_nv):
    chat_id = message.chat.id
    ketqua = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if ketqua.upper() == 'B':
        bot.delete_message(chat_id, msg1.message_id)
        NHIEMVU(message, MAIN, thong_tin)
    else:
        msg2 = bot.send_message(chat_id, f"""♻️ CHECK LẠI NỘI DUNG
 ├ NỘI DUNG: {ketqua}
 ├ [1]: CHUẨN, NỘP
 ├ [2]: CHƯA, SỬA LẠI
 └ [>]: [NHẬP LỰA CHỌN]""")
        if message.text == "/start":
            bot.delete_message(chat_id, msg2.message_id)
            start(message)
            return
        else:bot.register_next_step_handler(message, DONE_NV, MAIN, thong_tin, msg1, msg2, ketqua, check_nv)
def DONE_NV(message, MAIN, thong_tin, msg1, msg2, ketqua, check_nv):
    chat_id = message.chat.id
    choice = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if choice == "1":
        msg3 = bot.send_message(chat_id, "[+] [Loading]...")
        msg4 = bot.send_message(chat_id, f"[+] [{MAIN.done_nv(ketqua)['message']}]\n[!] [VUI LÒNG CHỜ 5s ĐỂ QUAY LẠI]")
        JOB.clear()
        __import__('time').sleep(3)
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        bot.delete_message(chat_id, msg3.message_id)
        bot.delete_message(chat_id, msg4.message_id)
        NHIEMVU(message, MAIN, thong_tin)
    elif choice == "2":
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        GET_NV(message, MAIN, thong_tin, check_nv)
    else:
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        GET_NV(message, MAIN, thong_tin, check_nv)
def CHECKDONHANG(message, MAIN, thong_tin, msg1):
    chat_id = message.chat.id
    choice = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if choice.upper() == "B":
        bot.delete_message(chat_id, msg1.message_id)
        NHIEMVU(message, MAIN, thong_tin)
    else:
        bot.delete_message(chat_id, msg1.message_id)
        NHIEMVU(message, MAIN, thong_tin)
def RUTTIEN(message, MAIN, thong_tin):
    chat_id = message.chat.id
    msg1 = bot.send_message(chat_id, f"💸 𝗕𝗔𝗡𝗛𝗞𝗜𝗡𝗚 - 𝗥𝗨́𝗧 𝗧𝗜𝗘̂̀𝗡 𝗠𝗢𝗠𝗢\n ├ [1]: [CHECK HOÁ ĐƠN][📝]\n ├ [2]: [RÚT TIỀN][💵]\n ├ [B]: [QUAY LẠI]\n └ [>]: [NHẬP LỰA CHỌN]")
    if message.text == "/start":
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
        return
    else:bot.register_next_step_handler(message, HOADON, MAIN, thong_tin, msg1)
def HOADON(message, MAIN, thong_tin, msg1):
    chat_id = message.chat.id
    choice = message.text.strip()
    if msg1 !=0:bot.delete_message(chat_id, message.message_id)
    if choice.upper() == "B":
        if msg1 !=0:bot.delete_message(chat_id, msg1.message_id)
        NHIEMVU(message, MAIN, thong_tin)
    elif choice == "1":
        if msg1 !=0:bot.delete_message(chat_id, msg1.message_id)
        msg1 = bot.send_message(chat_id, f">>>{' '*32}𝗟𝗜̣𝗖𝗛 𝗦𝗨̛̉ 𝗥𝗨́𝗧 𝗧𝗜𝗘̂̀𝗡{' '*32}<<<\n{'#'*46}\n{MAIN.check_hoa_don()}\n{'#'*46}\n[>]: [B = QUAY LẠI]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg1.message_id)
            start(message)
            return
        else:bot.register_next_step_handler(message, CHECKHOADON, MAIN, thong_tin, msg1)
    elif choice == "2":
        bot.delete_message(chat_id, msg1.message_id)
        RUT(message, MAIN, thong_tin)
    else:
        msg2 = bot.send_message(chat_id, "[!] [NHẬP SAI LỰA CHỌN!]")
        __import__('time').sleep(2)
        if msg1 !=0: bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        RUTTIEN(message, MAIN, thong_tin)
def CHECKHOADON(message, MAIN, thong_tin, msg1):
    chat_id = message.chat.id
    choice = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if choice.upper() == "B":
        bot.delete_message(chat_id, msg1.message_id)
        RUTTIEN(message, MAIN, thong_tin)
    else:
        bot.delete_message(chat_id, msg1.message_id)
        RUTTIEN(message, MAIN, thong_tin)
def RUT(message, MAIN, thong_tin):
    chat_id = message.chat.id
    min = MAIN.check_min()
    msg1 = bot.send_message(chat_id, f"""💸 𝗕𝗔𝗡𝗛𝗞𝗜𝗡𝗚 - 𝗥𝗨́𝗧 𝗧𝗜𝗘̂̀𝗡 𝗩𝗘̂̀ 𝗠𝗢𝗠𝗢
 ├ [+]: [VÍ TIỀN HIỆN TẠI]: [{VND[0]}:VND]
 ├ [+]: [MIN RÚT TIỀN]: [{min}:VND]
 ├ [B]: [QUAY LẠI]
 └ [>]: [NHẬP SỐ TIỀN MUỐN RÚT]""")
    if message.text == "/start":
        bot.delete_message(chat_id, msg1.message_id)
        start(message)
        return
    else:bot.register_next_step_handler(message, CHECHRUT, MAIN, thong_tin, min, msg1)
def CHECHRUT(message, MAIN, thong_tin, min, msg1):
    chat_id = message.chat.id
    money = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if money.upper() == "B":
        bot.delete_message(chat_id, msg1.message_id)
        RUTTIEN(message, MAIN, thong_tin)
    elif int(money) > int(VND[0]):
        msg2 = bot.send_message(chat_id, "[!] [SỐ TIỀN VƯỢT QUÁ VÍ HIỆN TẠI]")
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        RUT(message, MAIN, thong_tin)
    elif int(money) >= int(min):
        msg2 = bot.send_message(chat_id, "[+] [WAITING]...")
        bot.delete_message(chat_id, msg1.message_id)
        DONERUT(message, MAIN, thong_tin, money, msg2)
    elif int(money) < int(min):
        msg2 = bot.send_message(chat_id, f"[!] [RÚT TỐI THIỂU ({min}:VND)]")
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        RUT(message, MAIN, thong_tin)
    else:
        msg2 = bot.send_message(chat_id, "[!] [LỖI CÚ PHÁP SỐ TIỀN]")
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        RUT(message, MAIN, thong_tin)
def DONERUT(message, MAIN, thong_tin, money, msg1):
    chat_id = message.chat.id
    rut = MAIN.rut_money(money=money)
    if rut == None:
        msg2 = bot.send_message(chat_id, "[!] [LỖI ĐƯỜNG TRUYỀN]")
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        RUT(message, MAIN, thong_tin)
    elif rut == "None":
        msg2 = bot.send_message(chat_id, "[!] [TẠO HOÁ ĐƠN THẤT BẠI!]")
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg1.message_id)
        bot.delete_message(chat_id, msg2.message_id)
        RUT(message, MAIN, thong_tin)
    else:
        bot.delete_message(chat_id, msg1.message_id)
        msg1 = bot.send_message(chat_id, f"{rut}\n ├ [1]: XEM HOÁ ĐƠN\n ├ [B]: [QUAY LẠI]\n └ [>]: [NHẬP LỰA CHỌN]")
        if message.text == "/start":
            bot.delete_message(chat_id, msg1.message_id)
            start(message)
            return
        else:bot.register_next_step_handler(message, CHECKDONERUT, MAIN, thong_tin, money, msg1)
def CHECKDONERUT(message, MAIN, thong_tin, money, msg1):
    chat_id = message.chat.id
    check = message.text.strip()
    bot.delete_message(chat_id, message.message_id)
    if check.upper() == "B":
        bot.delete_message(chat_id, msg1.message_id)
        NHIEMVU(message, MAIN, thong_tin)
    elif check == "1":
        bot.delete_message(chat_id, msg1.message_id)
        HOADON(message, MAIN, thong_tin, msg1=0)
    else:
        msg2 = bot.send_message(chat_id, "[!] [NHẬP SAI LỰA CHỌN!]")
        __import__('time').sleep(2)
        bot.delete_message(chat_id, msg1.message_id)
        DONERUT(message, MAIN, thong_tin, money, msg2)
if __name__ == "__main__":bot.polling(none_stop=True)
