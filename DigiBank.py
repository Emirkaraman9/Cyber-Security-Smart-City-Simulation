import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import sys
import datetime
import queue 
import random 
import threading 
import http.server 
import socketserver 
import sqlite3 
import os 
import smtplib 
# import time # bunu sonra sileyim
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ========================================================
# OGR NO: 2303022018
# DERS: Siber Güvenlik Ve Büyük Veri
# HOCAM KOD CALISIYOR LUTFEN KUTUPHANELERI YUKLEYIN
# ========================================================


# --- GLOBAL DEGISKENLER ---
# Hocam bunlar her yerden erisilsin diye global yaptim
log_kuyrugu = queue.Queue()
pencere = None
log_ekrani = None 
SECILEN_MOD = None 
debug_modu = True # gelistirirken lazim oldu

# Monitor degiskenleri
lbl_cpu = None
lbl_ram = None
lbl_ping = None
temp_data = [] # ilerde lazim olur diye


# --- MAİL AYARLARI ---
def mail_gonder_gercek(alici_mail, konu, icerik):
    # --- AYARLAR ---
    GONDEREN_MAIL = "emir.karaman200428@gmail.com" 
    
    # !!! SIFRE !!!
    UYGULAMA_SIFRESI = "ifhn oegu ryxd ytdi"  
    
    # print("Mail hazirlaniyor...") 
    
    msg = MIMEMultipart()
    msg['From'] = GONDEREN_MAIL
    msg['To'] = alici_mail
    msg['Subject'] = konu
    
    
    # Log dosyasindan son kayitlari okuyup maile ekleyelim
    log_ozeti = ""
    try:
        if os.path.exists("sistem_loglari.txt"):
            with open("sistem_loglari.txt", "r", encoding="utf-8") as f:
                # son satirlari al
                satirlar = f.readlines()[-15:] 
                log_ozeti = "".join(satirlar)
        else: 
            log_ozeti = "Log dosyasi henuz olusmadi."
    except: 
        log_ozeti = "Log okuma hatasi." # hata verirse bosver

    # govdeyi olustur
    govde = f"Sayin Yetkili,\n\n{icerik}\n\n----------------------------\nSON SISTEM LOGLARI:\n{log_ozeti}\n----------------------------\n\nDigiBank Guvenlik Botu v3.5"
    msg.attach(MIMEText(govde, 'plain'))
    
    try:
        # server baglantisi
        # print("Sunucuya baglaniyor...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GONDEREN_MAIL, UYGULAMA_SIFRESI)
        
        text = msg.as_string()
        server.sendmail(GONDEREN_MAIL, alici_mail, text)
        server.quit()
        print(f"BILGI: {alici_mail} adresine mail basariyla gonderildi.") # kontrol icin yazdim
        
    except Exception as e:
        print(f"HATA: Mail gonderilemedi! (Sifreyi kontrol et): {e}")


# --- VERITABANI SINIFI ---
class Veritabani:
    def __init__(self):
        # Thread hatasi almamak icin check_same_thread=False yaptim hocam yoksa hata veriyo
        self.conn = sqlite3.connect("digibank.db", check_same_thread=False)
        self.imlec = self.conn.cursor()
        self.tablo_kur()
        
    def tablo_kur(self):
        # tablo yoksa olustur
        self.imlec.execute('''CREATE TABLE IF NOT EXISTS loglar 
                              (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                               tarih TEXT, 
                               mesaj TEXT)''')
        self.conn.commit()

    def log_ekle(self, mesaj):
        tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.imlec.execute("INSERT INTO loglar (tarih, mesaj) VALUES (?, ?)", (tarih, mesaj))
            self.conn.commit()
        except: 
            pass # veritabani hatasi olursa program patlamasin
    
    def gecmisi_getir(self):
        # son 50 tanesi yeterli
        self.imlec.execute("SELECT * FROM loglar ORDER BY id DESC LIMIT 50")
        return self.imlec.fetchall()

db = Veritabani()


# --- DESIGN PATTERN SINIFLARI ---
class CityManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CityManager, cls).__new__(cls)
            cls._instance.durum = "Normal"
            cls._instance.kullanicilar = []  
        return cls._instance


    def LogYaz(self, mesaj):
        zaman = datetime.datetime.now().strftime("%H:%M:%S")
        text = f"[{zaman}] {mesaj}"
        
        # print(f"DEBUG: {text}") 
        
        db.log_ekle(mesaj)
        
        # Dosyaya yazma islemi
        try:
            with open("sistem_loglari.txt", "a", encoding="utf-8") as f:
                f.write(text + "\n")
        except: 
            pass

        if log_kuyrugu: 
            log_kuyrugu.put(text)

    def abone_ol(self, user):
        self.kullanicilar.append(user)
        # print("yeni abone eklendi")

    def acil_durum(self, sebep="Bilinmeyen"):
        self.durum = "TEHLIKE"
        
        # loglari bas
        self.LogYaz(f"!!! ACIL DURUM ({sebep}) TESPİT EDİLMİŞTİR !!!")
        self.LogYaz(f"Lütfen veri kaybını minimize etmek için faraday kafes uygulamasını başlatınız.")
        self.LogYaz(f"Mail yöneticiye gönderilmiştir güvenlik prosedürlerini uygulayınız !")
        
        # kullanicilara mail at
        for k in self.kullanicilar:
            k.mail_simulasyonu(f"ACIL DURUM: {sebep}! Lutfen sistemi kontrol ediniz.")
            
        # gereksiz dongu (stress testi icin koymustum)
        for i in range(5):
            pass 

    def durum_duzelt(self):
        self.durum = "Normal"
        self.LogYaz("Sistem normale dondu.")


class Vatandas:
    def __init__(self, ad, email):
        self.ad = ad; self.email = email
    
    def mail_simulasyonu(self, mesaj):
        zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # txt ye yaz
        try:
            with open("mail_logs.txt", "a", encoding="utf-8") as f:
                f.write(f"[{zaman}] GONDERILEN: {self.email} | ICERIK: {mesaj}\n")
        except: 
            pass
            
        # mail at
        if "emir.karaman2004" in self.email:
            # thread aciyoruz donmasin diye
            t = threading.Thread(target=mail_gonder_gercek, args=(self.email, "⚠️ SİBER SALDIRI UYARISI", mesaj))
            t.start()

class AkilliEv:
    def rutin_baslat(self):
        islemler = ["Robot süpürge başlatıldı...", "Tüm ışıklar kapatıldı.", "Bulaşık makinesi çalıştırıldı.", "Kombi sabitlendi."]
        for islem in islemler: 
            CityManager().LogYaz(f"[AKILLI EV] {islem}")


class IsikAcKomutu:
    def calistir(self): 
        CityManager().LogYaz("Sehir Isiklari: ACILDI.")
        
class IsikKapatKomutu:
    def calistir(self): 
        CityManager().LogYaz("Sehir Isiklari: KAPATILDI.")


class SabahRutini:
    def calistir(self):
        CityManager().LogYaz("--- Sabah Rutini ---")
        CityManager().LogYaz("Sensorler: OK")
        
        # loglari ac
        CityManager().LogYaz("Log kayıtları Açıldı")
        CityManager().LogYaz("Kamera Kayıtları Aktif")
        CityManager().LogYaz("Trafik lambaları ve sokak lambaları kontrol edildi.")
        
        IsikKapatKomutu().calistir()
        CityManager().LogYaz("--- Bitti ---")
        
class AksamRutini:
    def calistir(self):
        CityManager().LogYaz("--- Aksam Rutini ---")
        CityManager().LogYaz("Sensorler: OK")
        
        CityManager().LogYaz("Log kayıtları Akşam Rutini için hazırlandı.")
        CityManager().LogYaz("Boş yolların trafik lambaları düzenlendi.")
        CityManager().LogYaz("Sokak lambalarının kontrolü gerçekleştirildi")
        
        IsikAcKomutu().calistir()
        CityManager().LogYaz("--- Bitti ---")


# ==========================================
# UYE YONETIM (TXT)
# ==========================================
def uye_ekle_penceresi():
    # pencere ayarlari
    top = tk.Toplevel()
    top.title("Yeni Üye")
    top.geometry("300x400")
    
    entries = {}
    alanlar = ["Ad", "Soyad", "TC", "Tel", "Adres"]
    
    for a in alanlar: 
        tk.Label(top, text=a).pack()
        e=tk.Entry(top)
        e.pack()
        entries[a]=e
        
    def kaydet():
        v = [entries[a].get() for a in alanlar]
        
        # bos kontrolu
        if "" in v: 
            messagebox.showerror("Hata","Bos alan var")
            return
            
        try:
            # dosyaya ekle
            with open("uyeler.txt","a",encoding="utf-8") as f: 
                f.write("|".join(v)+"\n")
            
            CityManager().LogYaz(f"[UYE] {v[0]} {v[1]} eklendi.")
            top.destroy()
        except: 
            messagebox.showerror("Hata","Dosya hatasi")
            
    tk.Button(top, text="Kaydet", bg="green", fg="white", command=kaydet).pack(pady=10)


def uye_ara_penceresi():
    # --- AKILLI ARAMA SISTEMI ---
    top = tk.Toplevel()
    top.title("Üye Arama Sistemi")
    top.geometry("500x400")
    
    tk.Label(top, text="ÜYE SORGULAMA (TC veya İsim)", font=("Arial", 12, "bold")).pack(pady=10)
    
    f_ara = tk.Frame(top)
    f_ara.pack(pady=5)
    
    tk.Label(f_ara, text="Aranacak Kelime:").pack(side="left")
    ent_ara = tk.Entry(f_ara)
    ent_ara.pack(side="left", padx=5)
    
    txt_sonuc = scrolledtext.ScrolledText(top, height=15)
    txt_sonuc.pack(fill="both", expand=True, padx=10, pady=10)
    
    def bul():
        anahtar = ent_ara.get().lower() # Kucuk harfe cevir
        txt_sonuc.delete(1.0, tk.END)
        
        # dosya var mi
        if not os.path.exists("uyeler.txt"):
            txt_sonuc.insert(tk.END, "Henüz hiç üye kaydı yok (uyeler.txt bulunamadı).")
            return
            
        bulunan_sayisi = 0
        
        try:
            with open("uyeler.txt", "r", encoding="utf-8") as f:
                for line in f:
                    # satirlari oku
                    if anahtar in line.lower():
                        parts = line.strip().split('|')
                        
                        if len(parts) >= 5:
                            formatli = f"TC: {parts[2]}\nAD SOYAD: {parts[0]} {parts[1]}\nTEL: {parts[3]}\nADRES: {parts[4]}\n----------------------\n"
                            txt_sonuc.insert(tk.END, formatli)
                            bulunan_sayisi += 1
                            
            if bulunan_sayisi == 0:
                txt_sonuc.insert(tk.END, "Eşleşen kayıt bulunamadı.")
            else:
                # loga yaz
                CityManager().LogYaz(f"[UYE ARAMA] '{anahtar}' icin {bulunan_sayisi} kayit bulundu.")
        except Exception as e:
            txt_sonuc.insert(tk.END, f"Dosya okuma hatası: {e}")

    tk.Button(f_ara, text="BUL / LİSTELE", command=bul, bg="#17a2b8", fg="white").pack(side="left", padx=5)


# ==========================================
# ARAYUZ (GUI)
# ==========================================
def monitoru_guncelle():
    if not pencere: 
        return 
    
    # fake degerler uret
    cpu = random.randint(10, 85)
    ram = random.randint(200, 1024)
    ping = random.randint(15, 120)
    
    # renkleri ayarla
    if lbl_cpu: 
        lbl_cpu.config(text=f"CPU: %{cpu}", fg="red" if cpu>80 else "lime")
        
    if lbl_ram: 
        lbl_ram.config(text=f"RAM: {ram} MB")
        
    if lbl_ping: 
        lbl_ping.config(text=f"Ping: {ping} ms")
        
    # 2 saniyede bir guncelle
    if pencere: 
        pencere.after(2000, monitoru_guncelle)

def loglari_guncelle():
    # kuyruktan al ekrana bas
    while not log_kuyrugu.empty():
        try:
            msg = log_kuyrugu.get_nowait()
            if log_ekrani: 
                log_ekrani.insert(tk.END, str(msg)+"\n")
                log_ekrani.see(tk.END)
        except: 
            pass
            
    if pencere: 
        pencere.after(100, loglari_guncelle)


def secim_ekrani():
    global secim_penceresi
    secim_penceresi = tk.Tk()
    secim_penceresi.title("Giriş v3.5")
    secim_penceresi.geometry("400x350")
    
    tk.Label(secim_penceresi, text="GIRIS SECIMI", font=("Arial", 14, "bold")).pack(pady=30)
    
    tk.Button(secim_penceresi, text="1. YONETICI", bg="#343a40", fg="white", width=25, height=2, command=lambda: giris_paneli_ac("yonetici")).pack(pady=5)
    
    tk.Button(secim_penceresi, text="2. KULLANICI", bg="#007bff", fg="white", width=25, height=2, command=lambda: giris_paneli_ac("kullanici")).pack(pady=5)
    
    secim_penceresi.mainloop()


# --- GIRIS EKRANI ---
def giris_paneli_ac(mod):
    global SECILEN_MOD, giris_penceresi, ent_tc, ent_sifre
    
    SECILEN_MOD = mod
    secim_penceresi.destroy()
    
    giris_penceresi = tk.Tk()
    giris_penceresi.title(mod.upper())
    giris_penceresi.geometry("350x450") # Pencere boyutu
    
    
    tk.Label(giris_penceresi, text=mod.upper(), font=("Arial", 12)).pack(pady=20)
    
    tk.Label(giris_penceresi, text="TC:").pack()
    ent_tc=tk.Entry(giris_penceresi)
    ent_tc.pack()
    
    tk.Label(giris_penceresi, text="Sifre:").pack()
    ent_sifre=tk.Entry(giris_penceresi, show="*")
    ent_sifre.pack()
    
    # DEV GIRIS BUTONU
    tk.Button(giris_penceresi, text="GİRİŞ YAP", bg="green", fg="white", 
              font=("Arial", 12, "bold"), width=20, height=2, 
              command=kimlik_dogrula).pack(pady=20)
    
    # DEV GERI DON BUTONU
    tk.Button(giris_penceresi, text="< GERİ DÖN", bg="red", fg="white", 
              font=("Arial", 12, "bold"), width=20, height=2, 
              command=lambda:[giris_penceresi.destroy(), secim_ekrani()]).pack(pady=5)
    
    giris_penceresi.mainloop()


def kimlik_dogrula():
    tc = ent_tc.get()
    sifre = ent_sifre.get()
    
    # basit dogrulama
    if SECILEN_MOD=="yonetici" and tc=="12345" and sifre=="admin": 
        giris_penceresi.destroy()
        yonetici_arayuzu_baslat()
        
    elif SECILEN_MOD=="kullanici" and tc=="11111" and sifre=="user": 
        giris_penceresi.destroy()
        kullanici_arayuzu_baslat()
        
    else: 
        messagebox.showerror("Hata","Bilgiler Yanlis")


# --- YONETICI EKRANI ---
def yonetici_arayuzu_baslat():
    global pencere, log_ekrani, lbl_cpu, lbl_ram, lbl_ping
    
    pencere = tk.Tk()
    pencere.title("Yonetici")
    pencere.geometry("950x650")
    
    yonetici = CityManager()
    yonetici.abone_ol(Vatandas("Emir", "emir.karaman2004@gmail.com"))
    
    
    menubar = tk.Menu(pencere)
    filemenu = tk.Menu(menubar, tearoff=0)
    
    def gecmis():
        top = tk.Toplevel()
        top.geometry("500x300")
        for v in db.gecmisi_getir(): 
            tk.Label(top, text=f"{v[1]} | {v[2]}").pack(anchor="w")
            
    filemenu.add_command(label="Log Kayitlari", command=gecmis)
    filemenu.add_command(label="Cikis", command=lambda:[pencere.destroy(), secim_ekrani()])
    
    menubar.add_cascade(label="Sistem", menu=filemenu)
    pencere.config(menu=menubar)

    # sol panel
    sol = tk.Frame(pencere, padx=10)
    sol.pack(side="left", fill="both", expand=True)
    
    tk.Label(sol, text="YONETIM MERKEZI", font=("Arial", 14, "bold")).pack(pady=10)
    
    f_uye = tk.LabelFrame(sol, text="Uye Yonetimi (TXT)")
    f_uye.pack(fill="x", pady=5)
    
    tk.Button(f_uye, text="Uye Ekle", bg="#007bff", fg="white", command=uye_ekle_penceresi).pack(side="left", fill="x", expand=True)
    tk.Button(f_uye, text="Uye Ara", bg="#17a2b8", fg="white", command=uye_ara_penceresi).pack(side="left", fill="x", expand=True)

    frm_rutin = tk.LabelFrame(sol, text="Otomasyon")
    frm_rutin.pack(fill="x", pady=5)
    
    tk.Button(frm_rutin, text="Sabah Modu", command=lambda: SabahRutini().calistir()).pack(fill="x")
    tk.Button(frm_rutin, text="Aksam Modu", command=lambda: AksamRutini().calistir()).pack(fill="x")
    
    # butonlarin altina bosluk
    tk.Label(sol, text="").pack()
    
    tk.Button(sol, text="🚨 SALDIRI ALARMI (Mail Atar)", bg="red", fg="white", command=lambda:yonetici.acil_durum("DDOS SALDIRISI")).pack(fill="x", pady=10)
    tk.Button(sol, text="✅ NORMALE DON", bg="green", fg="white", command=lambda:yonetici.durum_duzelt()).pack(fill="x")
    
    
    tk.Label(sol, text="Loglar:").pack(anchor="w")
    log_ekrani = scrolledtext.ScrolledText(sol, height=12, bg="black", fg="lime")
    log_ekrani.pack(fill="both")

    # sag panel (Monitor)
    sag = tk.LabelFrame(pencere, text="Monitor", bg="black", fg="lime")
    sag.pack(side="right", fill="y", padx=10)
    
    lbl_cpu = tk.Label(sag, text="CPU: %0", bg="black", fg="lime", font=("Consolas",16))
    lbl_cpu.pack(pady=20)
    
    lbl_ram = tk.Label(sag, text="RAM: 0", bg="black", fg="lime")
    lbl_ram.pack()
    
    lbl_ping = tk.Label(sag, text="PING: 0", bg="black", fg="lime")
    lbl_ping.pack()
    
    
    tk.Button(sag, text="OTURUMU KAPAT", bg="#dc3545", fg="white", command=lambda:[pencere.destroy(), secim_ekrani()]).pack(side="bottom", fill="x", pady=10)

    monitoru_guncelle()
    loglari_guncelle()
    
    yonetici.LogYaz("Yonetici paneli aktif.")
    
    pencere.mainloop()


# --- KULLANICI EKRANI ---
def kullanici_arayuzu_baslat():
    global pencere, t_tutar, log_ekrani
    
    pencere = tk.Tk()
    pencere.title("DigiBank")
    pencere.geometry("600x650")
    
    yonetici = CityManager()

    tk.Button(pencere, text="Cikis", bg="red", fg="white", command=lambda:[pencere.destroy(), secim_ekrani()]).pack(anchor="ne", padx=10, pady=5)
    
    tk.Label(pencere, text="HOSGELDINIZ", font=("Arial", 16)).pack(pady=5)
    
    f_ode = tk.LabelFrame(pencere, text="Odeme")
    f_ode.pack(fill="x", padx=10)
    
    t_tutar = tk.Entry(f_ode)
    t_tutar.pack(side="left", padx=5)
    
    tk.Button(f_ode, text="Nakit", command=lambda: [yonetici.LogYaz(f"[DIGIBANK] {t_tutar.get()} TL tutarın ödenmiştir."), messagebox.showinfo("OK","İşleminiz Başarıyla Gerçekleşmiştir!")]).pack(side="left")
    tk.Button(f_ode, text="Bitcoin", bg="orange", command=lambda: [yonetici.LogYaz(f"[DIGIBANK] {t_tutar.get()} TL tutarında BTC kayıtlı sanal cüzdanınıza gönderilmiştir"), messagebox.showinfo("OK","İşleminiz Başarıyla Gerçekleştirilmiştir!")]).pack(side="left")
    
    
    f_hiz = tk.LabelFrame(pencere, text="Hizmetler")
    f_hiz.pack(fill="x", padx=10, pady=5)
    
    tk.Button(f_hiz, text="Fatura Ode", command=lambda: [yonetici.LogYaz("[DIGIBANK] Elektrik , Su , Doğalgaz ve internet faturalarınız borçları varsa borçlarıyla beraber ödenmiştir."), messagebox.showinfo("OK","Odendi")]).pack(side="left", padx=5)
    tk.Button(f_hiz, text="Otopark", command=lambda: [yonetici.LogYaz("[DIGIBANK] Otopark borçların ve normal ücretleriniz ödendi."), messagebox.showinfo("OK","Odendi")]).pack(side="left", padx=5)
    
    f_ev = tk.LabelFrame(pencere, text="Akilli Ev")
    f_ev.pack(fill="x", padx=10, pady=5)
    
    tk.Button(f_ev, text="Ev Sistemini Baslat", bg="blue", fg="white", command=lambda: [AkilliEv().rutin_baslat(), messagebox.showinfo("Ev", "Baslatildi")]).pack(fill="x")
    
    tk.Label(pencere, text="Islem Gecmisi:", font=("Arial", 10, "bold")).pack(anchor="w", padx=10)
    
    log_ekrani = scrolledtext.ScrolledText(pencere, height=10, bg="#222", fg="white", font=("Consolas", 9))
    log_ekrani.pack(fill="both", padx=10, pady=10)
    
    loglari_guncelle()
    
    yonetici.LogYaz("Kullanici girisi yapildi.")
    pencere.mainloop()


def sunucu():
    # arka planda calisacak
    try:
        h = http.server.SimpleHTTPRequestHandler
        # socket server baslat
        with socketserver.TCPServer(("", 8080), h) as d: 
            d.serve_forever()
    except: 
        pass


if __name__ == "__main__":
    
    # print("Sistem baslatiliyor...")
    
    t = threading.Thread(target=sunucu)
    t.daemon = True
    t.start()
    
    secim_ekrani()
    
    # burasi hic calismayacak
    print("Kapanis")