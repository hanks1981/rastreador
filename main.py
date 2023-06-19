import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
from tkinter import messagebox
import requests
import re


class App:
    Lista = None;
    SoloMaliciosas = None;
    IpUnica = True;
    Analizando = False;
    ListaInaddrArpa = None;
    Invertida = None;
  

    def __init__(self, root):
        # Create the main window
        root.title("BUSCADOR") 
        #setting window size
        width=1088
        height=662
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.configure(bg='#1B2433')
        root.resizable(width=False, height=False)
        
      
        #API_KEY
        self.EtiquetaApi=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaApi["font"] = ft
        self.EtiquetaApi["fg"] = "#000"
        self.EtiquetaApi["bg"] = "#1A3F52"
        self.EtiquetaApi["justify"] = "center"
        self.EtiquetaApi["text"] = "Insert Api_ Key: "
        self.EtiquetaApi.place(x=520,y=30,width=100,height=30)
        
        self.ApiKeyText=tk.Entry(root)
        self.ApiKeyText["bg"] = "#ffffff"
        self.ApiKeyText["borderwidth"] = "0.2px"
        ft = tkFont.Font(family='Times',size=10)
        self.ApiKeyText["font"] = ft
        self.ApiKeyText["fg"] = "#333333"
        self.ApiKeyText["justify"] = "center"
        self.ApiKeyText["text"] = "API KEY"
        self.ApiKeyText.place(x=620,y=30,width=450,height=30)
        
      
        #IP UNICA
        self.EtiquetaIPUnica= tk.Label()
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaIPUnica["font"] = ft
        self.EtiquetaIPUnica["fg"] = "#000"
        self.EtiquetaIPUnica["bg"] = "#365B6D"
        self.EtiquetaIPUnica["justify"] = "left"
        self.EtiquetaIPUnica["text"] = "Only 1 IP"
        self.EtiquetaIPUnica.place(x=20,y=10,width=200,height=30)
        
        self.BusquedaUnica=tk.Entry(root)
        self.BusquedaUnica["bg"] = "#ffffff"
        self.BusquedaUnica["borderwidth"] = "0.2px"
        ft = tkFont.Font(family='Times',size=10)
        self.BusquedaUnica["font"] = ft
        self.BusquedaUnica["fg"] = "#333333"
        self.BusquedaUnica["justify"] = "center"
        self.BusquedaUnica["text"] = "IP"
        self.BusquedaUnica.place(x=20,y=40,width=200,height=30)
        
        self.BotonBuscarIP=tk.Button(root)
        self.BotonBuscarIP["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.BotonBuscarIP["font"] = ft
        self.BotonBuscarIP["fg"] = "#333333"
        self.BotonBuscarIP["justify"] = "center"
        self.BotonBuscarIP["text"] = "Check"
        self.BotonBuscarIP.place(x=270,y=40,width=70,height=30)
        self.BotonBuscarIP["command"] = self.Busca_IP

        self.RadioButtonInAddrArpa = tk.Checkbutton(root)
        # self.RadioButtonInAddrArpa["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.RadioButtonInAddrArpa["font"] = ft
        self.RadioButtonInAddrArpa["fg"] = "#333333"
        self.RadioButtonInAddrArpa["text"] = "In-Addr.arpa"
        self.RadioButtonInAddrArpa["offvalue"] = "0"
        self.RadioButtonInAddrArpa["onvalue"] = "1"
        self.RadioButtonInAddrArpa.place(x=350,y=40,width=130,height=30)
        self.RadioButtonInAddrArpa["command"] = self.pruebaradiobutton

      
        #LISTA DE IPs
        
        self.EtiquetaIPLista= tk.Label()
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaIPLista["font"] = ft
        self.EtiquetaIPLista["fg"] = "#000"
        self.EtiquetaIPLista["bg"] = "#A5A6AB"
        self.EtiquetaIPLista["justify"] = "left"
        self.EtiquetaIPLista["text"] = "Multiple Ips"
        self.EtiquetaIPLista.place(x=20,y=90,width=200,height=30) 
    
        self.EligeArchivoBoton=tk.Button()
        ft = tkFont.Font(family='Times',size=10)
        self.EligeArchivoBoton["font"] = ft
        self.EligeArchivoBoton["fg"] = "#000"
        self.EligeArchivoBoton["justify"] = "center"
        self.EligeArchivoBoton["text"] = "Choise file"
        self.EligeArchivoBoton.place(x=20,y=120,width=200,height=62)
        self.EligeArchivoBoton["command"] = self.Elige_Archivo
  
        self.Rastrea=tk.Button()
        ft = tkFont.Font(family='Times',size=10)
        self.Rastrea["font"] = ft
        self.Rastrea["fg"] = "#000"
        self.Rastrea["justify"] = "center"
        self.Rastrea["text"] = "Check list"
        self.Rastrea.place(x=20,y=200,width=200,height=40)
        self.Rastrea["command"] = self.Rastrea_AbuseIP
        
        
        self.GuardaArchivo=tk.Button()
        ft = tkFont.Font(family='Times',size=10)
        self.GuardaArchivo["font"] = ft
        self.GuardaArchivo["fg"] = "#000"
        self.GuardaArchivo["justify"] = "center"
        self.GuardaArchivo["text"] = "Export malicious IP to File"
        self.GuardaArchivo.place(x=20,y=260,width=200,height=40)
        # self.GuardaArchivo["bg"] = "yellow"
        self.GuardaArchivo["command"] = self.Guarda_Archivos
        
        self.VentanaResultado=tk.Listbox()
        self.VentanaResultado["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.VentanaResultado["font"] = ft
        self.VentanaResultado["bg"] = "#fff"
        self.VentanaResultado["fg"] = "#000"
        self.VentanaResultado["justify"] = "left"
        self.VentanaResultado.place(x=270,y=80,width=800,height=532)
        
        
        # Boton cerrar ventana
        self.BotonSalir=tk.Button(root)
        self.BotonSalir["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.BotonSalir["font"] = ft
        self.BotonSalir["fg"] = "#333333"
        self.BotonSalir["justify"] = "center"
        self.BotonSalir["text"] = "Cerrar"
        self.BotonSalir.place(x=20,y=580,width=70,height=35)
        self.BotonSalir["command"] = self.Cierra_Ventana


        # comprobadores
        self.EtiquetaArchivo= tk.Label()
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaArchivo["font"] = ft
        self.EtiquetaArchivo["fg"] = "#000"
        self.EtiquetaArchivo["bg"] = "#DFA18C"
        self.EtiquetaArchivo["justify"] = "left"
        self.EtiquetaArchivo["text"] = "Archivo cargado"
        self.EtiquetaArchivo.place(x=20,y=320,width=200,height=30)

        self.EtiquetaAnalizado= tk.Label()
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaAnalizado["font"] = ft
        self.EtiquetaAnalizado["fg"] = "#000"
        self.EtiquetaAnalizado["bg"] = "#DFA18C"
        self.EtiquetaAnalizado["justify"] = "left"
        self.EtiquetaAnalizado["text"] = "IPs Analizadas"
        self.EtiquetaAnalizado.place(x=20,y=380,width=200,height=30)

        self.EtiquetaExportado= tk.Label()
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaExportado["font"] = ft
        self.EtiquetaExportado["fg"] = "#000"
        self.EtiquetaExportado["bg"] = "#DFA18C"
        self.EtiquetaExportado["justify"] = "left"
        self.EtiquetaExportado["text"] = "Archivo exportado"
        self.EtiquetaExportado.place(x=20,y=440,width=200,height=30)



    def Cambia_Estado_Etiqueta_Archivo(self):
        self.EtiquetaArchivo["bg"] = "#81F79F"

    def Cambia_Estado_Etiqueta_Analizadas_acabado(self):
        self.EtiquetaAnalizado["bg"] = "#81F79F"

    def Cambia_Estado_Etiqueta_exportadas(self):
        self.EtiquetaExportado["bg"] = "#81F79F"

    def pruebaradiobutton(self):
        print("radiobuton activo")
        self.Invertida = not self.Invertida
        print("radiobuton activo",self.Invertida)

        

    def Cierra_Ventana(self):
        print("cierra")
        root.destroy()
 
    def Elige_Archivo(self):
        filepath = filedialog.askopenfilename()
        with open(filepath, 'r', encoding='utf-8') as file:
            self.Lista = file.read()
            # self.ListaInaddrArpa = self.Lista
        # self.Lista = re.findall(r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.(in\-addr\.arpa)', self.ListaInaddrArpa)
        # if Aux == "in-addr.arpa":
        #     self.Invertida()
        self.Lista = re.findall(r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}', self.Lista)
        self.Lista = list(set(self.Lista))
        if self.Lista != []:
            self.Cambia_Estado_Etiqueta_Archivo()
        self.VentanaResultado.configure(justify="center")
        self.VentanaResultado.insert(tk.END , '                                                                                                     Lista IPs ' )
        self.VentanaResultado.insert(tk.END, '--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        
        for self.ip in self.Lista:
             print("esto es el self",self.Lista)
             self.VentanaResultado.configure(justify="left")
             self.VentanaResultado.insert(tk.END, f' SIN ANALIZAR -  {self.ip}    ')
             self.VentanaResultado.insert(tk.END, '------------------------------------------------------')
            
    
        
    def Rastrea_AbuseIP(self):
       #borramos lista anterior
        self.IpUnica=False;
        Apikey = self.ApiKeyText.get()
        self.VentanaResultado.delete(0, tk.END)
        self.VentanaResultado.configure(justify="center")
        self.VentanaResultado.insert(tk.END ,'Lista De IPs analizadas' )
        self.VentanaResultado.insert(tk.END, '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        self.Analiza()
        
                

    def Analiza(self):
        for self.ip in self.Lista:
            try:
                response = requests.get(f'https://api.abuseipdb.com/api/v2/check',
                                        params={'ipAddress': self.ip, 'maxAgeInDays': 90},
                                        headers={'key': "6d504eb54fa446701a31679bcc42b2e09861920a67b1f410c43efefd29e756f75d9ccf2dec75b9fa"}, timeout=5)
                self.data = response.json()
            except requests.exceptions.RequestException as e:
                self.ErrorConexionAPi()
                return
            if self.data:
                self.PrintaLinea()


    def Busca_IP(self):
       #borramos lista anterior
        self.IpUnica = True;
        Apikey = self.ApiKeyText.get()
        Only_IP = self.BusquedaUnica.get()
        
        self.VentanaResultado.delete(0, tk.END)
        self.VentanaResultado.configure(justify="center")
        self.VentanaResultado.insert(tk.END ,'Lista De IPs analizadas' )
        self.VentanaResultado.insert(tk.END, '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        try:
            response = requests.get(f'https://api.abuseipdb.com/api/v2/check',
                                    params={'ipAddress': Only_IP, 'maxAgeInDays': 90},
                                     headers={'key': "6d504eb54fa446701a31679bcc42b2e09861920a67b1f410c43efefd29e756f75d9ccf2dec75b9fa"}, timeout=5)
            self.data = response.json()
            if self.data:
               self.BusquedaUnica.delete(0, tk.END)
        except requests.exceptions.RequestException as e:
            self.ErrorConexionAPi()
            return
        if self.data:
            self.PrintaLinea()
                           
    def Guarda_Archivos(self):
        # Ask user where they want to save the file
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        fileMaliciososPath = "IPMaliciosas.txt"
        # Open the file for writing and write the flagged IPs to it
        with open(filepath, "w", encoding='utf-8') as file:
            for ip in self.VentanaResultado.get(0, tk.END):
                if "Alto" in ip:
                    print("alto", ip)
                    aux = re.findall(r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}', ip)
                    file.write(aux[0] + "\n")
        # Inform the user that the file was saved
        messagebox.showinfo("Save to File", "File saved successfully!")
        self.Cambia_Estado_Etiqueta_exportadas()
        
    def MuestraResultadoApi():
        print("todas")
        
    def ErrorConexionAPi(self):
         
        self.VentanaResultado.insert(" Ocurrio un problema intentalo nuevamente en breve" )
        print("-----------------------")
        
        
        
  
    def PrintaLinea(self):
        if(self.IpUnica):
            if (self.data["data"]["abuseConfidenceScore"]==0 and self.data["data"]["abuseConfidenceScore"]<10):
                self.VentanaResultado.configure(fg="#000", justify="left")
                self.PrintaSoloIPBajo()
            if  (self.data["data"]["abuseConfidenceScore"]< 50 and  self.data["data"]["abuseConfidenceScore"]>= 10):
                self.VentanaResultado.configure(fg="#000", justify="left")
                self.PrintaSoloIPMedio()
            if self.data["data"]["abuseConfidenceScore"]>= 50:
                self.VentanaResultado.configure(fg="#000", justify="left")
                self.PrintaSoloIPAlto()
        else:  
            self.Cambia_Estado_Etiqueta_Analizadas_acabado()
            if (self.data["data"]["abuseConfidenceScore"]==0 and self.data["data"]["abuseConfidenceScore"]<10):
                self.VentanaResultado.configure(fg="#000", justify="left")
                self.PrintaBajo()
            if self.IpUnica == False and (self.data["data"]["abuseConfidenceScore"]< 50 and  self.data["data"]["abuseConfidenceScore"]>= 10):
                self.VentanaResultado.configure(fg="#000", justify="left")
                self.PrintaMedio()
            if  (self.data["data"]["abuseConfidenceScore"]>= 50):
                self.VentanaResultado.configure(fg="#000", justify="left")
                self.PrintaAlto()
       
     
    
    # Para lista de IPS
    def PrintaAlto(self):
        self.VentanaResultado.insert(tk.END, f' Riesgo: Alto - {self.ip} - Score: {self.data["data"]["abuseConfidenceScore"]} - ISP: {self.data["data"]["isp"]}')
        self.VentanaResultado.insert(tk.END, '-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            
    def PrintaMedio(self):
        self.VentanaResultado.insert(tk.END, f' Riesgo: Medio - {self.ip} - Score: {self.data["data"]["abuseConfidenceScore"]} - ISP: {self.data["data"]["isp"]}')
        self.VentanaResultado.insert(tk.END, '-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    
    def PrintaBajo(self):
        self.VentanaResultado.insert(tk.END, f' Riesgo: Bajo - {self.ip} - Score: {self.data["data"]["abuseConfidenceScore"]} - ISP: {self.data["data"]["isp"]}')
        self.VentanaResultado.insert(tk.END, '-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        
    def PrintaSoloIPAlto(self):
        self.VentanaResultado.insert(tk.END, f' Riesgo: Alto - {self.data["data"]["ipAddress"]} - Score: {self.data["data"]["abuseConfidenceScore"]} - isp: {self.data["data"]["isp"]}')
        self.VentanaResultado.insert(tk.END, '-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    
    # solo 1 IP
    def PrintaSoloIPMedio(self):
        self.VentanaResultado.insert(tk.END, f' Riesgo: Medio - {self.data["data"]["ipAddress"]} - Score: {self.data["data"]["abuseConfidenceScore"]} - isp: {self.data["data"]["isp"]}')
        self.VentanaResultado.insert(tk.END, '-------------------------------------------------------------------------------------------------------------------------------------------------------------') 
        
    def PrintaSoloIPBajo(self):
        self.VentanaResultado.insert(tk.END, f' Riesgo: Bajo - {self.data["data"]["ipAddress"]} - Score: {self.data["data"]["abuseConfidenceScore"]} - isp: {self.data["data"]["isp"]}')
        self.VentanaResultado.insert(tk.END, '-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        
    def DameCriticas(self):
        print("---------DameCriticas--------------")
        print("data->", self.data)
        print("-----------------------")
                
    def DameBuenas(self):
        print("----------DameBuenas-------------")
        print("data->", self.data)
        print("-----------------------")
        
   
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
   

  


 