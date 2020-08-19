from tkinter import *
from tkinter import ttk
from tkcalendar import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openpyxl import Workbook
from fpdf import FPDF
import os

mydb = mysql.connector.connect(host='localhost', user='root', password='', database="ktuveritabani")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS gorevliler (id INT AUTO_INCREMENT PRIMARY KEY, ad VARCHAR(250), soyad VARCHAR(250), telefon VARCHAR(250), eposta VARCHAR(250), parola VARCHAR(12), adres VARCHAR(250))")
mycursor.execute("CREATE TABLE IF NOT EXISTS uyeler (id INT AUTO_INCREMENT PRIMARY KEY, tur VARCHAR(250), uyeno VARCHAR(250), ad VARCHAR(250), soyad VARCHAR(250), telefon VARCHAR(250), eposta VARCHAR(250), adres VARCHAR(250), hal VARCHAR(250), borc VARCHAR(250))")
mycursor.execute("CREATE TABLE IF NOT EXISTS kitaplar (id INT AUTO_INCREMENT PRIMARY KEY, barkodno TEXT, kitapad TEXT, yazar TEXT, rakam TEXT, raf TEXT, odunctarihi TEXT, teslimtarihi TEXT,  alici TEXT)")

class ktugiris(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.wm_geometry("900x600+270+90")
        self.wm_title("Kütüphane Takip Uygulaması")
        self.wm_resizable(False, False)

        
        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='alt', settings = {'TCombobox':{'configure':{'selectbackground': '#F24405','fieldbackground': '#F24405','background': 'white'}}})
        combostyle.theme_use('combostyle')
    
        
        self.cerceve1 = Frame(self, width=900, height=600, bg="#033E8C")
        self.cerceve1.pack(fill=X)

        resim1 = Image.open("gorseller\kitapvector.png")
        yukle = ImageTk.PhotoImage(resim1)
        goruntu1 = Label(self.cerceve1,text="kitap", image=yukle, bg ="#033E8C" )
        goruntu1.image = yukle
        goruntu1.place(x=50, y=110)

        resim2 = Image.open("gorseller\mail.png")
        yukle = ImageTk.PhotoImage(resim2)
        goruntu1 = Label(self.cerceve1,text="eposta", image=yukle, bg ="#033E8C")
        goruntu1.image = yukle
        goruntu1.place(x=220, y=251, width=80, height=80)

        resim3 = Image.open("gorseller\sifre.png")
        yukle = ImageTk.PhotoImage(resim3)
        goruntu1 = Label(self.cerceve1,text="parola", image=yukle, bg ="#033E8C")
        goruntu1.image = yukle
        goruntu1.place(x=223, y=310, width=80, height=80)

        self.baslik = Label(self.cerceve1, text="KÜTÜPHANE TAKİP UYGULAMASI", fg="#ffffff", font=("Comic Sans MS", 30, "bold"), bg ="#033E8C")
        self.baslik.place(x=110, y=50)

        self.gorevlimail = Entry(self.cerceve1, fg="black", font=("Calibri Italic", 14), bg ="#F24405")
        self.gorevlimail.insert(0, 'E-Posta adresinizi giriniz')
        self.gorevlimail.place(x=300, y= 270, width =300, height = 40)

        self.gorevlisifre = Entry(self.cerceve1, fg="black", font=("Calibri Italic", 14), bg ="#F24405")
        self.gorevlisifre.insert(0, 'Şifrenizi giriniz')
        self.gorevlisifre.place(x=300, y=330, width=300, height=40)

        self.buton = Button(self.cerceve1, text = "GİRİŞ", fg="#ffffff", font=("Calibri", 15, "bold"),bg ="#F21905", activebackground = "#F24405", command=self.girisyap)
        self.buton.place(x=395, y=400, width=100, height=40)
        
        Label(self.cerceve1, text="MUSTAFA MERT KISA", bg="#033E8C", fg="#0455BF", font=("Calibri", 14, "bold")).place(x=0, y=575)

    
    def girisyap(self):
        sql = "SELECT * FROM gorevliler WHERE eposta=%s AND parola=%s"
        val = (self.gorevlimail.get(), self.gorevlisifre.get())
        mycursor.execute(sql, val)
        sonuc = mycursor.fetchall()

        if sonuc:
            anasayfa()
        else:
            self.hata()

    def hata(self):
        messagebox.showerror("Hata", "Bilgiler hatalı!\nTekrar deneyiniz.")
        self.gorevlimail.delete(0, END)
        self.gorevlisifre.delete(0, END)



class anasayfa(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("900x600+270+90")
        self.wm_title("Kütüphane Takip Uygulaması")
        self.wm_resizable(False, False)

        self.cerceve1 = Frame(self, width = 900, height= 600, bg = "#033E8C")
        self.cerceve1.pack()

        resim1 = Image.open("gorseller\kitapvector.png")
        yukle = ImageTk.PhotoImage(resim1)
        goruntu1 = Label(self.cerceve1,text="kitap", image=yukle, bg ="#033E8C")
        goruntu1.image = yukle
        goruntu1.place(x=50, y=110)

        self.baslik = Label(self.cerceve1, text="KÜTÜPHANE TAKİP UYGULAMASI", fg="#ffffff",font=("Comic Sans MS", 30, "bold"), bg ="#033E8C")
        self.baslik.place(x=110, y=50)

        self.buton = Button(self.cerceve1, text = "ÜYELER", fg="#ffffff", font=("Calibri", 18, "bold"), bg="#F21905", activebackground = "#F24405", command = uyeler)
        self.buton.place(x=300, y=220, width=300, height=60)

        self.buton = Button(self.cerceve1, text = "KİTAPLAR", fg="#ffffff", font=("Calibri", 18, "bold"), bg="#F21905", activebackground = "#F24405", command = kitaplar)
        self.buton.place(x=300, y=300, width=300, height=60)

        self.buton = Button(self.cerceve1, text = "KİTAP LİSTESİ", fg="#ffffff", font=("Calibri", 18, "bold"), bg="#F21905", activebackground = "#F24405", command = kitaplik)
        self.buton.place(x=300, y=380, width=300, height=60)
        
        Label(self.cerceve1, text="İşlemlerinizi, ÜYELER sayfası için ÜYE NO, KİTAPLAR sayfası için BARKOD NO bilgileri ile yapabilirsiniz.", bg="#033E8C", fg="#ffffff", font=("Calibri", 14)).place(x=60, y=120)
        

class uyeler(Toplevel):
    
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("900x600+270+90")
        self.wm_title("Kütüphane Takip Uygulaması")
        self.wm_resizable(False, False)

        style = ttk.Style()
        style.theme_use("combostyle")

        self.cerceve1 = Frame(self, width=900, height=600, bg="#033E8C")
        self.cerceve1.pack()

        Label(self.cerceve1, text="ÜYELER", bg="#033E8C", fg="#ffffff", font=("Comic Sans MS", 20)).place(x=390, y=10)
        
        Label(self.cerceve1, text="Üye No", bg="#033E8C", fg="#ffffff", font=("Calibri", 15, "bold")).place(x=200, y=100)
        Label(self.cerceve1, text="Üyelik Türü", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=140)
        Label(self.cerceve1, text="Ad", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=180)
        Label(self.cerceve1, text="Soyad", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=220)
        Label(self.cerceve1, text="Telefon", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=260)
        Label(self.cerceve1, text="E-Posta", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=300)
        Label(self.cerceve1, text="Adres", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=340)
        Label(self.cerceve1, text="Üyelik Hâli", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=420)
        Label(self.cerceve1, text="Borç Bilgisi", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=460)

        self.uyeno = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.uyeno.place(x=450, y=100, width=300)

        self.tur = ttk.Combobox(self.cerceve1, font=("Calibri", 13), state="readonly", values=["Sivil", "Öğrenci"])
        self.tur.place(x=450, y=140, width=300)

        self.ad = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.ad.place(x=450, y=180, width=300)

        self.soyad = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.soyad.place(x=450, y=220, width=300)

        self.telefon = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.telefon.place(x=450, y=260, width=300)

        self.eposta = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.eposta.place(x=450, y=300, width=300)

        self.adres = Text(self.cerceve1, font=("Calibri", 13), height=3, bg="#F24405")
        self.adres.place(x=450, y=340, width=300)

        self.rakam = IntVar(self.cerceve1)
        self.uyelikhali1 = Radiobutton(self.cerceve1, text="Aktif", variable=self.rakam, value=1, bg="#F24405") 
        self.uyelikhali1.place(x=450, y=420)
        self.uyelikhali2 = Radiobutton(self.cerceve1, text="Beklemede", variable=self.rakam, value=2, bg="#F24405") 
        self.uyelikhali2.place(x=560, y=420)
        self.uyelikhali3 = Radiobutton(self.cerceve1, text="İptal", variable=self.rakam, value=3, bg="#F24405") 
        self.uyelikhali3.place(x=700, y=420)

        self.borc = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.borc.place(x=450, y=460, width=300)

        Button(self.cerceve1, text = "KAYDET", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.kaydet).place(x=80, y=530, width=150)
        Button(self.cerceve1, text = "GÖSTER", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.goster).place(x=280, y=530, width=150)
        Button(self.cerceve1, text = "GÜNCELLE", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.guncelle).place(x=480, y=530, width=150)
        Button(self.cerceve1, text = "E-POSTA", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.mailgonder).place(x=680, y=530, width=150)
        Button(self.cerceve1, text = "ANASAYFA", fg="#ffffff", font=("Calibri", 12, "bold"), bg="#F21905", activebackground="#F24405", command=anasayfa).place(x=800, y=10, width=90)

    
    def mailgonder(self):
        gonderici = "abdulazizslmz@gmail.com"
        alici = self.eposta.get()
        parola = "azizsolmaz28"

        ileti = MIMEMultipart("alternative")
        ileti["Subject"] =  "Kütüphane Borç Bilgilendirmesi"
        ileti["From"] = "Kütüphane Takip Uygulaması"
        ileti["To"] = alici

        icerik = f"Merhaba, kütüphanemize {self.borc.get()} ₺ tutarında borcunuz bulunmaktadır. 30 gün içerisinde ödeme yapmamanız durumunda üyeliğiniz iptal edilecektir. İyi günler dileriz."

        part1 = MIMEText(icerik, "html")
        ileti.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(gonderici, parola)
            server.sendmail(gonderici, alici, ileti.as_string())

        self.temizle()

    def kaydet(self):
        
        sql = "INSERT INTO uyeler (tur, uyeno, ad, soyad, telefon, eposta, adres, hal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.tur.get(), self.uyeno.get(), self.ad.get(), self.soyad.get(), self.telefon.get(), self.eposta.get(), self.adres.get('1.0', END), self.rakam.get())
        mycursor.execute(sql, val)
        mydb.commit()
        self.temizle()

    def goster(self):
        
        sql = "SELECT * FROM uyeler WHERE uyeno=%s"
        val = (self.uyeno.get(),)
        mycursor.execute(sql, val)
        sonuc = mycursor.fetchall()

        for i in sonuc:
            self.tur.set("")
            self.ad.delete(0, END)
            self.soyad.delete(0, END)
            self.telefon.delete(0, END)
            self.eposta.delete(0, END)
            self.adres.delete("1.0", END)
            self.rakam.set(0)

            self.tur.set(i[1])
            self.ad.insert(0,i[3])
            self.soyad.insert(0,i[4])
            self.telefon.insert(0,i[5])
            self.eposta.insert(0,i[6])
            self.adres.insert("end",i[7])
            self.rakam.set(i[8])
          
    def guncelle(self):

        sql = "UPDATE uyeler SET tur=%s, ad=%s, soyad=%s, telefon=%s, eposta=%s, adres=%s, hal=%s WHERE uyeno=%s"
        val = (self.tur.get(), self.ad.get(), self.soyad.get(), self.telefon.get(), self.eposta.get(), self.adres.get('1.0', END), self.rakam.get(), self.uyeno.get())
        mycursor.execute(sql, val)
        mydb.commit()
        self.temizle()

    def temizle(self):

        messagebox.showinfo("Başarılı", "İşleminiz başarıyla gerçekleşti.")
        self.tur.set("")
        self.uyeno.delete(0, END)
        self.ad.delete(0, END)
        self.soyad.delete(0, END)
        self.telefon.delete(0, END)
        self.eposta.delete(0, END)
        self.adres.delete("1.0", END)
        self.rakam.set(0)
        self.focus()

        
class kitaplar(Toplevel):
    
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("900x600+270+90")
        self.wm_title("Kütüphane Takip Uygulaması")
        self.wm_resizable(False, False)

        style = ttk.Style()
        style.theme_use("combostyle")

        self.cerceve1 = Frame(self, width=900, height=600, bg="#033E8C")
        self.cerceve1.pack()

        Label(self.cerceve1, text="KİTAPLAR", bg="#033E8C", fg="#ffffff", font=("Comic Sans MS", 20)).place(x=390, y=10)
        
        Label(self.cerceve1, text="Barkod No", bg="#033E8C", fg="#ffffff", font=("Calibri", 15, "bold")).place(x=200, y=100)
        Label(self.cerceve1, text="Kitap Adı", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=140)
        Label(self.cerceve1, text="Yazar", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=180)
        Label(self.cerceve1, text="Durum", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=220)
        Label(self.cerceve1, text="Raf", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=260)
        Label(self.cerceve1, text="Alıcı", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=300)
        Label(self.cerceve1, text="Ödünç Tarihi", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=340)
        Label(self.cerceve1, text="Teslim Tarihi", bg="#033E8C", fg="#ffffff", font=("Calibri", 15,)).place(x=200, y=380)
        

        self.barkodno = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.barkodno.place(x=450, y=100, width=300)

        self.kitapad = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.kitapad.place(x=450, y=140, width=300)

        self.yazar = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.yazar.place(x=450, y=180, width=300)

        self.rakam = IntVar(self.cerceve1)
        self.durum1 = Radiobutton(self.cerceve1, text="Stokta", variable=self.rakam, value=1, bg="#F24405") 
        self.durum1.place(x=450, y=220)
        self.durum2 = Radiobutton(self.cerceve1, text="Ödünç", variable=self.rakam, value=2, bg="#F24405") 
        self.durum2.place(x=685, y=220)

        self.raf = Entry(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.raf.place(x=450, y=260, width=300)
        
        self.alici = ttk.Combobox(self.cerceve1, font=("Calibri", 13), values=["Teslim Al"])
        self.alici.place(x=450, y=300, width=300)
        self.alici.bind("<KeyRelease>", self.islemler)
        self.alici.bind("<Button-1>", self.islemler)
        self.alici.bind("<Return>", self.islemler)
        self.alici.bind("<<ComboboxSelected>>", self.islemler)

        self.odunctarihi = DateEntry(self.cerceve1, font=("Calibri", 13), bg="#F24405", locale="tr_TR", selectbackground="#F21905", state="disabled")
        self.odunctarihi.place(x=450, y=340, width=300)

        self.teslimtarihi = DateEntry(self.cerceve1, font=("Calibri", 13), bg="#F24405", locale="tr_TR",  selectbackground="#F21905", state="disabled")
        self.teslimtarihi.place(x=450, y=380, width=300)
        
        self.borc = Label(self.cerceve1, font=("Calibri", 13), bg="#F24405")
        self.borc.place(x=450, y=420, width=300)

        Button(self.cerceve1, text = "KAYDET", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.kaydet).place(x=80, y=490, width=150)
        Button(self.cerceve1, text = "GÖSTER", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.goster).place(x=280, y=490, width=150)
        Button(self.cerceve1, text = "GÜNCELLE", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.guncelle).place(x=480, y=490, width=150)
        Button(self.cerceve1, text = "SİL", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.sil).place(x=680, y=490, width=150)
        Button(self.cerceve1, text = "ANASAYFA", fg="#ffffff", font=("Calibri", 12, "bold"), bg="#F21905", activebackground="#F24405", command=anasayfa).place(x=800, y=10, width=90)
        
        self.eskiborc = 0

    def islemler(self, event):
        if len(self.alici.get()) != 0:
            if self.alici.get() != "Teslim Al":
                self.rakam.set(2)
                self.odunctarihi.config(state='normal')
                self.teslimtarihi.config(state='normal')
                self.teslim(event=None)
            else:
                if len(self.odunctarihi.get()) != 0:
                    self.teslimtarihi.config(state='normal')
                    a1 = self.teslimtarihi.get_date()
                    a2 = date.today()
                    self.teslimtarihi.delete(0, END)
                    a3 = str(a2).split("-")
                    a4 = str(a3[2]) + "." + str(a3[1]) + "." + str(a3[0])
                    self.teslimtarihi.insert(0, a4)
                    gun = (a2-a1).days
                    
                    if gun > 0:
                        self.borc['text'] = gun*2
                    else:
                        self.borc['text'] = 0

                else:
                    messagebox.showerror("Hata", "Kitap ödünç verilmemiş olarak gözükmektedir.")
                    self.alici.delete(0, END)
                    self.focus()
        else:
            self.rakam.set(1)
            self.odunctarihi.delete(0, END)
            self.teslimtarihi.delete(0, END)
            self.odunctarihi.config(state='disabled')
            self.teslimtarihi.config(state='disabled')
    
    def teslim(self, event):
        a = self.odunctarihi.get_date()
        b = a + timedelta(days=14)
        c = str(b).split("-")
        d = c[2] + "." + c[1] + "." + c[0]
        self.teslimtarihi.delete(0, END)
        self.teslimtarihi.insert(0, d)
        self.odunctarihi.config(state='disabled')
        self.teslimtarihi.config(state='disabled')       

    def kaydet(self):
        sql = "INSERT INTO kitaplar (barkodno, kitapad, yazar, rakam, raf, odunctarihi, teslimtarihi) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (self.barkodno.get(), self.kitapad.get(), self.yazar.get(), self.rakam.get(), self.raf.get(), self.odunctarihi.get(), self.teslimtarihi.get())
        mycursor.execute(sql, val)
        mydb.commit()
        self.temizle()
        
    def goster(self):
        sql = "SELECT * FROM kitaplar WHERE barkodno=%s"
        val = (self.barkodno.get(),)
        mycursor.execute(sql, val)
        sonuc = mycursor.fetchall()

        for i in sonuc:
            self.barkodno.delete(0, END)
            self.barkodno.insert(0, i[1])
            self.kitapad.delete(0, END)
            self.kitapad.insert(0, i[2])
            self.yazar.delete(0, END)
            self.yazar.insert(0, i[3])
            self.rakam.set(i[4])
            self.raf.delete(0, END)
            self.raf.insert(0, i[5])
            self.odunctarihi.config(state="normal")     
            self.odunctarihi.delete(0, END)
            self.odunctarihi.insert(0, i[6])
            self.odunctarihi.config(state="disabled")
            self.teslimtarihi.config(state="normal")     
            self.teslimtarihi.delete(0, END)
            self.teslimtarihi.insert(0, i[7])
            self.teslimtarihi.config(state="disabled")   

            try:
                self.alici.delete(0, END)
                self.alici.insert(0, i[8])
            except TclError:
                pass

            self.uyeno = self.alici.get()
        
    def guncelle(self):
        if self.alici.get() == "Teslim Al":
            self.rakam.set(1)
            self.odunctarihi.config(state='normal')
            self.teslimtarihi.config(state='normal')
            self.odunctarihi.delete(0, END)
            self.teslimtarihi.delete(0, END)
            self.alici.delete(0, END)

            sql = "UPDATE kitaplar SET kitapad=%s, yazar=%s, rakam=%s, raf=%s, odunctarihi=%s, teslimtarihi=%s, alici=%s WHERE barkodno=%s"
            val = (self.kitapad.get(), self.yazar.get(), self.rakam.get(), self.raf.get(), self.odunctarihi.get(), self.teslimtarihi.get(), self.alici.get(), self.barkodno.get())
            mycursor.execute(sql, val)
            mydb.commit()
            
            sql = "SELECT * FROM uyeler WHERE uyeno=%s"
            val = (self.uyeno,)
            mycursor.execute(sql, val)
            sonuc = mycursor.fetchall()

            for i in sonuc:
                self.eskiborc = i[9]

            try: 
                sql = "UPDATE uyeler SET borc=%s WHERE uyeno=%s"
                val = (int(self.eskiborc) + int(self.borc['text']), self.uyeno)
                mycursor.execute(sql, val)
                mydb.commit()
                    
            except TypeError:
                sql = "UPDATE uyeler SET borc=%s WHERE uyeno=%s"
                val = (0 + int(self.borc['text']), self.uyeno)
                mycursor.execute(sql, val)
                mydb.commit()              

        else:
            
            sql = "UPDATE kitaplar SET kitapad=%s, yazar=%s, rakam=%s, raf=%s, odunctarihi=%s, teslimtarihi=%s, alici=%s WHERE barkodno=%s"
            val = (self.kitapad.get(), self.yazar.get(), self.rakam.get(), self.raf.get(), self.odunctarihi.get(), self.teslimtarihi.get(), self.alici.get(), self.barkodno.get())
            mycursor.execute(sql, val)
            mydb.commit()             
        self.temizle()

    def sil(self):
        sql = "DELETE FROM kitaplar WHERE barkodno=%s"
        val = (self.barkodno.get(),)
        mycursor.execute(sql, val)
        mydb.commit()
        self.temizle()   

    def temizle(self):
        messagebox.showinfo("Başarılı", "İşleminiz başarıyla gerçekleşti.")
        self.barkodno.delete(0, END)
        self.kitapad.delete(0, END)
        self.yazar.delete(0, END)
        self.rakam.set(0)
        self.alici.delete(0, END)
        self.raf.delete(0, END)
        self.odunctarihi.config(state="normal")
        self.teslimtarihi.config(state="normal")
        self.odunctarihi.delete(0, END)
        self.teslimtarihi.delete(0, END)
        self.odunctarihi.config(state="disabled")
        self.teslimtarihi.config(state="disabled")  
        self.borc['text'] = ""
        self.focus()



class kitaplik(Toplevel):
    
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("900x600+270+90")
        self.wm_title("Kütüphane Takip Uygulaması")
        self.wm_resizable(False, False)

        style = ttk.Style()
        style.theme_use("alt")

        self.cerceve1 = Frame(self, width=900, height=600, bg="#033E8C")
        self.cerceve1.pack()

        Label(self.cerceve1, text="MEVCUT KİTAPLAR", bg="#033E8C", fg="#ffffff", font=("Comic Sans MS", 20)).place(x=320, y=10)

        self.slider = ttk.Scrollbar(self.cerceve1)
        self.slider.place(x=829, y=75, height=430)

        self.diyagram = ttk.Treeview(self.cerceve1, yscrollcommand = self.slider.set, column=("sutun1","sutun2","sutun3","sutun4", "sutun5"), show="headings")

        self.diyagram.heading("sutun1", text="Barkod No")
        self.diyagram.heading("sutun2", text="Kitap")
        self.diyagram.heading("sutun3", text="Yazar")
        self.diyagram.heading("sutun4", text="Konum")
        self.diyagram.heading("sutun5", text="Durum")

        self.diyagram.column("sutun1", width=156)
        self.diyagram.column("sutun2", width=156)
        self.diyagram.column("sutun3", width=156)
        self.diyagram.column("sutun4", width=156)
        self.diyagram.column("sutun5", width=156)

        self.diyagram.place(x=50, y=75, height=430)
        self.slider.config(command=self.diyagram.yview)

        self.barkodliste = []
        self.kitapliste = []
        self.yazarliste = []
        self.konumliste = []
        self.durumliste = []
        self.durumliste1 = []

        mycursor.execute("SELECT * FROM kitaplar")
        sonuc = mycursor.fetchall()
 
        for i in sonuc:
            self.barkodliste.append(i[1])
            self.kitapliste.append(i[2])
            self.yazarliste.append(i[3])
            self.konumliste.append(i[5])
            self.durumliste.append(i[4])

        for i in self.durumliste:
            if i == '1':
                self.durumliste1.append("Stokta")
            elif i == '2':
                self.durumliste1.append("Ödünç")
            else:
                self.durumliste1.append("-")

        self.kitaplikliste = list(zip(self.barkodliste, self.kitapliste, self.yazarliste, self.konumliste, self.durumliste1))

        for i in self.kitaplikliste:
            self.diyagram.insert("", END, values=(i[0], i[1], i[2], i[3], i[4]))

        Button(self.cerceve1, text = "EXCEL", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.excel).place(x=290, y=530, width=150)
        Button(self.cerceve1, text = "PDF", fg="#ffffff", font=("Calibri", 15, "bold"), bg="#F21905", activebackground="#F24405", command=self.pdf).place(x=460, y=530, width=150)
        Button(self.cerceve1, text = "ANASAYFA", fg="#ffffff", font=("Calibri", 12, "bold"), bg="#F21905", activebackground="#F24405", command=anasayfa).place(x=800, y=10, width=90)

    def excel(self):
        belge = Workbook()
        sayfa = belge.active
        sayfa.append(["Barkod No", "Kitap", "Yazar", "Konum", "Durum"])

        for i in self.kitaplikliste:
            sayfa.append(i)
        
        belge.save("kitaplistesi.xlsx")
        os.startfile("kitaplistesi.xlsx")

    def pdf(self):
        veri = [["Barkod No", "Kitap", "Yazar", "Konum", "Durum"]]

        for i in self.kitaplikliste:
            veri.append(list(i))
        
        pdf = FPDF()
        pdf.add_font("Times New Roman", style="", fname="fontlar\TTimesb.ttf", uni=True)
        pdf.set_font("Times New Roman", size=10)
        pdf.add_page()

        sutunboyut = pdf.w/5
        satirboyut = pdf.font_size

        for i in veri:
            for j in i:
                pdf.cell(sutunboyut, satirboyut*2, txt=j, border=0)
            pdf.ln(satirboyut*2)
        
        pdf.output("kitaplistesi.pdf")
        os.startfile("kitaplistesi.pdf")


if __name__ == "__main__":
    app = ktugiris()
    app.mainloop()
