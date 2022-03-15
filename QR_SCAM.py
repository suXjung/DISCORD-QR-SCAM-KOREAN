from copy import error
from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import base64
import time
import os
from colorama import Fore, init
init(convert=True)


def logo_qr():
    im1 = Image.open('temp/qr_code.png', 'r')
    im2 = Image.open('temp/overlay.png', 'r')
    im1 = im1.resize((176, 176))
    im2 = im2.resize((50, 50))
    im1.paste(im2, (65, 65), im2)
    im1.save('temp/final_qr.png', quality=100)

def paste_template():
    im1 = Image.open('temp/template.png', 'r')
    im2 = Image.open('temp/final_qr.png', 'r')
    im1.paste(im2, (113, 401))
    im1.save('디스코드.png', quality=100)

def main():
    print(f"[{Fore.CYAN}!!{Fore.RESET}] By bsj")
    print(f"[{Fore.CYAN}!!{Fore.RESET}] Telegram : @sujung02 - https://bit.ly/31zWPst")
    print(f"\n[{Fore.GREEN}◈{Fore.RESET}] QR Code 생성...")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
    driver.get('https://discord.com/login')
    print(f"\n[{Fore.RED}!!{Fore.RESET}] 실행 완료")
    time.sleep(3.5)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, features='lxml')

    div = soup.find('div', {'class': 'qrCode-2R7t9S'}) # qrCode-wG6ZgU
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'temp/qr_code.png')

    img_data =  base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

    with open(file,'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    print(f"[{Fore.CYAN}>{Fore.RESET}] QR Code 생성완료 > 디스코드.png")
    print(f"[{Fore.GREEN}>{Fore.RESET}] QR 코드 스캔 감지 중...")
    
    while True:
        if discord_login != driver.current_url:
            print(f"[{Fore.RED}★{Fore.RESET}] 스캔 감지 완료...")
    #         token = driver.execute_script('''

    # var req = webpackJsonp.push([
    #     [], {
    #         extra_id: (e, t, r) => e.exports = r
    #     },
    #     [
    #         ["extra_id"]
    #     ]
    # ]);
    # for (let e in req.c)
    #     if (req.c.hasOwnProperty(e)) {
    #         let t = req.c[e].exports;
    #         if (t && t.__esModule && t.default)
    #             for (let e in t.default) "getToken" === e && (token = t.default.getToken())
    #     }
    # return token;   
    #             ''')
            with open('grab_token.js', 'r') as token_js:
                token = driver.execute_script(token_js.read())

            print(f"\n[{Fore.YELLOW}>{Fore.RESET}] Token : ",token)
            break

    print('작업 성공 - 엔터키를 눌러 Token.txt 파일에 토큰을 저장할 수 있습니다.')
    input("\n")
    token_file = open("Token.txt", "a", encoding="UTF-8")
    token_file.write(token + "\n")

if __name__ == '__main__':
    main()
