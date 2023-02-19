import os, requests, time, re, sys

from bs4 import BeautifulSoup as par

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

xxx ="--------------------------------------------"

class Bot:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.cok = "https://api-cdn-fb.yayanxd.my.id/submit.php"
        self.tok, self.be, self.ga, self.su, = [], [], [], []
        self.menu()

    def pilih(self):
        print(f"""
{xxx}
    [01] suka         [04] haha
    [02] super        [05] wow
    [03] peduli       [06] sedih
              [07] marah
{xxx}""")

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""
   ___       __  ____             __             __  
  / _ )___  / /_/ __/__ ________ / /  ___  ___  / /__
 / _  / _ \/ __/ _// _ `/ __/ -_) _ \/ _ \/ _ \/  '_/
/____/\___/\__/_/  \_,_/\__/\__/_.__/\___/\___/_/\_\ 

                  code By Christian S.
             ----------------------------""")

    def menu(self):
        self.logoo()
        print("""
[1] bot like komen
[2] bot like postingan
[3] bot followers facebook
[4] bot balas komentar postingan
""")
        ykh = input(f"{H}[{M}+{H}]{N} CHOSE_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.dump()
            self.mula()
        elif ykh in ["2", "02"]:
            self.dump()
            self.like_cok()
        elif ykh in ["3", "03"]:
            self.dump()
            self.followers()
        elif ykh in ["4", "04"]:
            self.komen()
        else:print("[!] input yang bener");time.sleep(3);self.menu()

    def dump(self):
        try:
            req = self.ses.get(f"{self.cok}?json=true").json()
            for x in req:
                for key, value in x.items():
                    self.tok.append(key+"|"+value)
                    sys.stdout.write(f"\r[{O}*{N}] sedang mengumpulkan {H}{len(self.tok)}{N} user... ");sys.stdout.flush()
        except:pass

    def like_cok(self):
        self.pilih()
        cok = input("╰──> ")
        if cok in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.like_cok()
        elif cok in ["1", "01"]:self.yuZhong("Suka")
        elif cok in ["2", "02"]:self.yuZhong("Super")
        elif cok in ["3", "03"]:self.yuZhong("Peduli")
        elif cok in ["4", "04"]:self.yuZhong("Haha")
        elif cok in ["5", "05"]:self.yuZhong("Wow")
        elif cok in ["6", "06"]:self.yuZhong("Sedih")
        elif cok in ["7", "07"]:self.yuZhong("Marah")
        else:
            print("[!] input yg bnr");time.sleep(2);self.like_cok()

    def yuZhong(self, react):
        print(f"""{xxx}
[>] silahkan masukan url postingan anda
[>] url postingan di haruskan publik no private!
{xxx}""")
        url = input("[?] masukan url: ").replace("https://www.facebook.com", "").replace("https://web.facebook.com", "").replace("https://m.facebook.com", "").replace("https://mbasic.facebook.com", "").replace("https://free.facebook.com", "")
        print(f"""{xxx}
[*] Sedang Mengirim Bot {react} ke postingan
{xxx}""")
        for x in self.tok:
            nama, coki = x.split("|")[0], x.split("|")[1]
            self.like_post(nama, url, coki, react)
        exit(f"selesai bot {react} ke postingan")

    def mula(self):
        self.pilih()
        cok = input("╰──> ")
        if cok in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.mula()
        elif cok in ["1", "01"]:self.xnxx("Suka")
        elif cok in ["2", "02"]:self.xnxx("Super")
        elif cok in ["3", "03"]:self.xnxx("Peduli")
        elif cok in ["4", "04"]:self.xnxx("Haha")
        elif cok in ["5", "05"]:self.xnxx("Wow")
        elif cok in ["6", "06"]:self.xnxx("Sedih")
        elif cok in ["7", "07"]:self.xnxx("Marah")
        else:
            print("[!] input yg bnr");time.sleep(2);self.mula()

    def komen(self):
        print(f"{xxx}\n[>] Silahkan masukan url postingan facebook\n[>] yang ingin anda pasang bot bales komen\n{xxx}")
        url = input("[?] url postingan: ").replace("https://www.facebook.com", "").replace("https://m.facebook.com", "").replace("https://mbasic.facebook.com", "").replace("https://free.facebook.com", "")
        print(f"{xxx}\n[>] Ingin memasang bot berapa akun Facebook?\n{xxx}")
        try:berapa=int(input("[+] cth: 1 atau 10: "))
        except:berapa=1
        print(f"{xxx}\n[>] Silahkan masukan cookie tumbal akun anda\n[>] yang mau di pasang bot bales komentar.\n{xxx}")
        for x in range(berapa):
            x+=1
            coki = input(f"[?] Cookie ke {x}: ")
            self.tok.append(coki)
            print(xxx)
        print(f"[>] Silahkan tulis balasan komentar anda...\n[+] gunakan '{H}<>{N}' untuk spasi ke bawah\n{xxx}")
        komen = input("[+] Tulis balasan : ").replace("<>", "\n")
        for i in self.tok:
            self.kome_post(url, i, komen);time.sleep(5)
        exit("\n[#] Bot komen telah selesai:)")

    def kome_post(self, url, coki, komen):
        try:
            link = par(self.ses.get(f"{self.url}{url}", cookies={"cookie":coki}).text, "html.parser")
            if 'href="/zero/optin/write/' in str(link):
                self.ubah_data(link, "None", coki)
            for x in link.find_all("a", href=True):
                if "Balas" in x.text:
                    curl = self.ses.get(f"{self.url}{x['href']}", cookies={"cookie":coki}).text
                    data = {
                        "fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(curl)).group(1),
                        "jazoest": re.search('name="jazoest" value="(.*?)"', str(curl)).group(1),
                        "comment_text": komen
                    }
                    post = par(curl, "html.parser").find("form",{"method":"post"})["action"]
                    self.ses.post(f"{self.url}{post}", data=data, cookies={"cookie":coki})
                    print(f"""
{xxx}
[{H}+{N}] status: berhasil komen
[{H}+{N}] komen : {H}{komen}{N}
{xxx}""")
                elif "Masuk" in x.text or "Bukan Anda?" in x.text or "Mulai" in x.text:
                    print(f"""
{xxx}
[{K}!{N}] status: akun anda checkpoint
[{K}!{N}] notice: {M}Gagal komen dikarenakan akun cp{N}
{xxx}""")
                elif "Kembali ke Beranda" in x.text:
                    exit(f"""
{xxx}
[{K}!{N}] status: url invalid
[{K}!{N}] notice: {M}pastikan url anda sudah benar!{N}
{xxx}""")
            for i in link.find_all("a", href=True):
                if "\xa0Lihat komentar sebelumnya…" in list(i.strings):
                    self.kome_post(x["href"], coki, komen)
                elif "\xa0Lihat komentar lainnya…" in list(i.strings):
                    self.kome_post(x["href"], coki, komen)
        except (requests.exceptions.TooManyRedirects, AttributeError):
            print(f"""
{xxx}
[{M}!{N}] cookie akun ini kemungkinan
[{M}!{N}] mati atau kena bates limit.
{xxx}""")
        except requests.exceptions.ConnectionError:
            print(f"""
{xxx}
[{M}!{N}] gagal terhubung ke internet
[{M}!{N}] silahkan hidupankan mode pesawat 3 detik.
{xxx}""");time.sleep(10)

    def xnxx(self, react):
        print(f"""{xxx}
[>] silahkan masukan url komen anda
[>] cara mendapatkan url komen silhakan mengakses browser
[>] ubah url ke mbasic, dan pastekan url komen anda.
[!] contoh: https://mbasic.facebook.com/reactions/picker/?ft_id=884531132763623
{xxx}""")
        url = input("[?] masukan url: ")
        print(f"""{xxx}
[*] Sedang Mengirim Bot React {react} Ke Url
{xxx}""")
        for x in self.tok:
            nama, coki = x.split("|")[0], x.split("|")[1]
            self.cook(nama, coki, url, react)
        exit("selesai bot like komen")

    def ubah(self, url):
        if "https" in url or "facebook" in url or "me" in url:user = url.split("/")[3]
        else:user=url
        try:uid = re.findall(";rid=(\d+)&amp;",str(self.ses.get("https://m.facebook.com/"+user).text))[0]
        except:uid = url
        return uid

    def simpan(self, user, pasw):
        kntl = (f"{user}|{pasw}")
        with open("coki_fb.txt", "a", encoding="utf-8") as r:
            r.write(kntl+"\n")

    def followers(self):
        print(
            f"""
{xxx}
[>] salin url facebook anda
[!] yang ingin di tambahkan followers
{xxx}        """
        )
        try:jnck = input("[?] url: ");kntl = self.ubah(jnck)
        except (KeyError, IndexError):exit(f"{N}[{M}×{N}] url lo tidak valid goblok")
        print(
                f"""
{xxx}
[!] tunggu sebentar cok lagi ngirim bot nya
{xxx}""")
        for id in self.tok:
            nama, coki = id.split("|")[0], id.split("|")[1]
            self.mulao(nama, coki, kntl)
        exit(f"""

[+] berhasil   : {len(self.be)}
[-] sudah folow: {len(self.su)}
[!] gagal folow: {len(self.ga)}
""")

    def mulao(self, nama, coki, uid):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id={uid}", cookies={"cookie":coki}).text, "html.parser")
            if 'href="/zero/optin/write/' in str(link):
                self.ubah_data(link, nama, coki)
            elif "/login/?privacy_mutation_token" in str(link):
                print(f"""
{xxx}
[{M}!{N}] nama  : {nama}
[{M}!{N}] status: gagal follow akun anda
{xxx}""")
                self.ga.append(nama)
            elif "mbasic_logout_button" not in str(link):
                print(f"""
{xxx}
[{M}!{N}] nama  : {nama}
[{M}!{N}] status: gagal follow akun anda
{xxx}""")
            elif "/a/subscriptions/remove" in str(link):
                print(f"""
{xxx}
[{M}!{N}] nama  : {nama}
[{M}!{N}] status: akun ini sudah follow anda
{xxx}""")
                self.su.append(nama)
                #self.simpan(nama, coki)
            elif "Anda Diblokir Sementara" in str(link):
                print(f"""
{xxx}
[{K}!{N}] nama  : {nama}
[{K}!{N}] status: akun ini di blokir sementara.
{xxx}""")
            else:
                self.ses.get(self.url+link.find("a", string="Ikuti").get("href"), cookies={"cookie": coki})
                print(f"""
{xxx}
[{H}+{N}] nama  : {nama}
[{H}+{N}] status: berhasil follow akun anda
{xxx}""")
                self.be.append(nama)
                #self.simpan(nama, coki)
        except (requests.exceptions.TooManyRedirects, AttributeError):
            print(f"""
{xxx}
[{M}!{N}] cookie akun ini kemungkinan
[{M}!{N}] mati atau kena bates limit.
{xxx}""")
        except requests.exceptions.ConnectionError:
            print(f"""
{xxx}
[{M}!{N}] gagal terhubung ke internet
[{M}!{N}] silahkan hidupankan mode pesawat 3 detik.
{xxx}""");time.sleep(10)

    def cook(self, nama, coki, url, react):
        try:
            link = par(self.ses.get(url, cookies={"cookie": coki}).text, "html.parser")
            if 'href="/zero/optin/write/' in str(link):
                self.ubah_data(link, nama, coki)
            elif "Lupa Kata Sandi?" in str(link):
                print(f"""
{xxx}
[{M}!{N}] nama  : {nama}
[{M}!{N}] status: gagal {react} komen
{xxx}""")
            elif "Login ke Akun Lain" in str(link):
                print(f"""
{xxx}
[{M}!{N}] nama  : {nama}
[{M}!{N}] status: gagal {react} komen
{xxx}""")
            elif "Temukan Akun Anda" in str(link):
                print(f"""
{xxx}
[{M}!{N}] nama  : {nama}
[{M}!{N}] status: gagal {react} komen
{xxx}""")
            elif "Anda Diblokir Sementara" in str(link):
                print(f"""
{xxx}
[{K}!{N}] nama  : {nama}
[{K}!{N}] status: akun ini di blokir sementara.
{xxx}""")
            else:
                for x in link.find_all("a", href=True):
                    if (f"{react}(Hapus)") in x.text:
                        print(f"""
{xxx}
[{K}!{N}] nama  : {nama}
[{K}!{N}] status: akun ini sudah {H}{react}{N} komen
{xxx}""")
                    elif react in x.text:
                        self.ses.get(f"{self.url}{x['href']}", cookies={"cookie":coki})
                        print(f"""
{xxx}
[{H}+{N}] nama  : {nama}
[{H}+{N}] status: berhasil {react} komen
{xxx}""")
                    else:continue
        except (requests.exceptions.TooManyRedirects, AttributeError):
            print(f"""
{xxx}
[{M}!{N}] cookie akun ini kemungkinan
[{M}!{N}] mati atau kena bates limit.
{xxx}""")
        except requests.exceptions.ConnectionError:
            print(f"""
{xxx}
[{M}!{N}] gagal terhubung ke internet
[{M}!{N}] silahkan hidupankan mode pesawat 3 detik.
{xxx}""");time.sleep(10)

    def like_post(self, nama, url, coki, men):
        try:
            link = par(self.ses.get(self.url+url, cookies={"cookie": coki}).text, "html.parser")
            if 'href="/zero/optin/write/' in str(link):
                self.ubah_data(link, nama, coki)
            elif 'href="/reactions/picker/?is_permalink=' in str(link):
                urll = re.search('href="/reactions/picker/?(.*?)"', str(link)).group(1).replace("amp;", "")
                for z in par(self.ses.get(f"{self.url}/reactions/picker/{urll}", cookies={"cookie": coki}).content, "html.parser").find_all("a"):
                    if (f"{men}(Hapus)") in z.text:
                        print(f"""
{xxx}
[{K}!{N}] nama  : {nama}
[{K}!{N}] status: akun ini sudah {H}{men}{N} postingan
{xxx}""")
                    elif men in z.text:
                        self.ses.get(f"{self.url}{z['href']}", cookies={"cookie": coki})
                        print(f"""
{xxx}
[{H}+{N}] nama  : {nama}
[{H}+{N}] status: berhasil {men} postingan
{xxx}""")
                    else:continue
            elif "/login.php?" in str(link):
                print(f"""
{xxx}
[{M}!{N}] nama  : {nama}
[{M}!{N}] status: gagal {men} postingan
{xxx}""")
            elif "Anda Diblokir Sementara" in str(link):
                print(f"""
{xxx}
[{K}!{N}] nama  : {nama}
[{K}!{N}] status: akun ini di blokir sementara.
{xxx}""")
            else:
                print(f"""
{xxx}
[{M}!{N}] nama  : {nama}
[{M}!{N}] status: gagal {men} postingan
{xxx}""")
        except (requests.exceptions.TooManyRedirects, AttributeError):
            print(f"""
{xxx}
[{M}!{N}] cookie akun ini kemungkinan
[{M}!{N}] mati atau kena bates limit.
{xxx}""")
        except requests.exceptions.ConnectionError:
            print(f"""
{xxx}
[{M}!{N}] gagal terhubung ke internet
[{M}!{N}] silahkan hidupankan mode pesawat 3 detik.
{xxx}""");time.sleep(10)

    def ubah_data(self, link, nama, coki):
        try:
            gett = self.ses.get(self.url+link.find("a", string="Tidak, Terima Kasih").get("href"), cookies={"cookie": coki}).text
            date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
            self.ses.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=date, cookies={"cookie": coki})
            print(f"""
{xxx}
[{K}!{N}] nama  : {nama}
[{K}!{N}] status: akun ini sedang menggunakan mode free
{xxx}""");time.sleep(5)
        except:pass

Bot()