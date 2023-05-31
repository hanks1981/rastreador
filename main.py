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
        root.configure(bg='#0aa')
        root.resizable(width=False, height=False)
      
        #API_KEY
        self.EtiquetaApi=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaApi["font"] = ft
        self.EtiquetaApi["fg"] = "#000"
        self.EtiquetaApi["bg"] = "#0aa"
        self.EtiquetaApi["justify"] = "center"
        self.EtiquetaApi["text"] = "Insert Api_ Key: "
        self.EtiquetaApi.place(x=520,y=30,width=90,height=30)
        
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
        self.EtiquetaIPUnica["bg"] = "#0aa"
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
        
        
        
       
        
        #LISTA DE IPs
        
        self.EtiquetaIPLista= tk.Label()
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaIPLista["font"] = ft
        self.EtiquetaIPLista["fg"] = "#000"
        self.EtiquetaIPLista["bg"] = "#0aa"
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
        # self.EligeArchivoBoton["bg"] = "#e4cc52"
        # self.EligeArchivoBoton.configure( fg="#31dc2b")
        self.EligeArchivoBoton["command"] = self.Elige_Archivo
        
        # self.NombreArchivoTexto= tk.Label()
        # ft = tkFont.Font(family='Times',size=10)
        # self.NombreArchivoTexto["font"] = ft
        # self.NombreArchivoTexto["fg"] = "#000"
        # self.NombreArchivoTexto["bg"] = "#fff"
        # self.NombreArchivoTexto["justify"] = "left"
        # self.NombreArchivoTexto["text"] = "Sin cargar archivo"
        # self.NombreArchivoTexto.place(x=20,y=200,width=200,height=25)
        
        
        self.Rastrea=tk.Button()
        ft = tkFont.Font(family='Times',size=10)
        self.Rastrea["font"] = ft
        self.Rastrea["fg"] = "#000"
        # self.Rastrea["bg"] = "#333"
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
        self.EtiquetaArchivo["bg"] = "red"
        self.EtiquetaArchivo["justify"] = "left"
        self.EtiquetaArchivo["text"] = "Archivo cargado"
        self.EtiquetaArchivo.place(x=20,y=320,width=200,height=30)

        self.EtiquetaAnalizado= tk.Label()
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaAnalizado["font"] = ft
        self.EtiquetaAnalizado["fg"] = "#000"
        self.EtiquetaAnalizado["bg"] = "red"
        self.EtiquetaAnalizado["justify"] = "left"
        self.EtiquetaAnalizado["text"] = "IPs Analizadas"
        self.EtiquetaAnalizado.place(x=20,y=380,width=200,height=30)

        self.EtiquetaExportado= tk.Label()
        ft = tkFont.Font(family='Times',size=10)
        self.EtiquetaExportado["font"] = ft
        self.EtiquetaExportado["fg"] = "#000"
        self.EtiquetaExportado["bg"] = "red"
        self.EtiquetaExportado["justify"] = "left"
        self.EtiquetaExportado["text"] = "Archivo exportado"
        self.EtiquetaExportado.place(x=20,y=440,width=200,height=30)



    def Cambia_Estado_Etiqueta_Archivo(self):
        self.EtiquetaArchivo["bg"] = "#A2FF33"

    def Cambia_Estado_Etiqueta_Analizadas_acabado(self):
        self.EtiquetaAnalizado["bg"] = "#A2FF33"

    def Cambia_Estado_Etiqueta_exportadas(self):
        self.EtiquetaExportado["bg"] = "#A2FF33"

        

    def Cierra_Ventana(self):
        print("cierra")
        root.destroy()
 
    def Elige_Archivo(self):
        filepath = filedialog.askopenfilename()
        with open(filepath, 'r', encoding='utf-8') as file:
            self.Lista = file.read()
        self.Lista = re.findall(r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}', self.Lista)
        self.Lista = list(set(self.Lista))
        if self.Lista != []:
            self.Cambia_Estado_Etiqueta_Archivo()
        self.VentanaResultado.configure(justify="center")
        self.VentanaResultado.insert(tk.END , '                                                                                                     Lista IPs ' )
        self.VentanaResultado.insert(tk.END, '--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        
        for self.ip in self.Lista:
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
        self.Cambia_Estado_Etiqueta_Analizadas_pendiente()
        self.Analiza()
        
                

    def Analiza(self):
        for self.ip in self.Lista:
            try:
                response = requests.get(f'https://api.abuseipdb.com/api/v2/check',
                                        params={'ipAddress': self.ip, 'maxAgeInDays': 90},
                                        headers={'key': "85ab2690d87e8423af50b6ec2f948f7f8af224636a75ccaff7c1c5bb9bb3b6557a7e9f3ed43f7499"}, timeout=5)
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
                                     headers={'key': "85ab2690d87e8423af50b6ec2f948f7f8af224636a75ccaff7c1c5bb9bb3b6557a7e9f3ed43f7499"}, timeout=5)
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
                print("1er if")
                self.VentanaResultado.configure(fg="#000", justify="left")
                self.PrintaBajo()
            if self.IpUnica == False and (self.data["data"]["abuseConfidenceScore"]< 50 and  self.data["data"]["abuseConfidenceScore"]>= 10):
                print("2er if")
                self.VentanaResultado.configure(fg="#000", justify="left")
                self.PrintaMedio()
            if  (self.data["data"]["abuseConfidenceScore"]>= 50):
                print("3er if")
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
        print("quee es self", self.data)
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
        
   















    
        
        
    

    #     # Create the Open File button
    #     open_file_button = tk.Button(root, text="Choose File", command=self.open_file)
    #     open_file_button.pack()

    #     # Create the Search IPs button
    #     search_ips_button = tk.Button(root, text="Search Abusedb", command=self.search_ips_button_clicked)
    #     search_ips_button.pack()

    #     # Create the IP list box
    #     IP_LIST_BOX = tk.Listbox(root, height=20, width=35)
    #     IP_LIST_BOX.pack()

    #     # Create the Save to File button
    #     save_to_file_button = tk.Button(root, text="Save to File", command=self.save_to_file)
    #     save_to_file_button.pack()

    #     # Create the Close button
    #     close_button = tk.Button(root, text="Close", command=self.close_button_clicked)
    #     close_button.pack()


    # def save_api_key():
    #     """
    #     Save the API key
    #     """
    #     # App.api_key = API_KEY_ENTRY.get()
    #     # API_KEY_WINDOW.destroy()
    #     print("save api key ")


    # def enter_api_key():
    #     """
    #     Create a window for the user to enter their API key
    #     """
    #     global API_KEY_WINDOW
    #     API_KEY_WINDOW = tk.Toplevel(root)
    #     API_KEY_WINDOW.geometry("250x100")
    #     API_KEY_WINDOW.title("API KEY")
    #     api_key_label = tk.Label(API_KEY_WINDOW, text="Enter your Abuseipdb API key:")
    #     api_key_label.pack()
    #     global API_KEY_ENTRY
    #     API_KEY_ENTRY = tk.Entry(API_KEY_WINDOW)
    #     API_KEY_ENTRY.pack()
    #     save_api_key_button = tk.Button(API_KEY_WINDOW, text="Save", command=save_api_key)
    #     save_api_key_button.pack()


    # # Function to open a file.
    # def open_file(self):
    #     """
    #     Open a file
    #     """
    #     filepath = filedialog.askopenfilename()
    #     global IPS
    #     with open(filepath, 'r', encoding='utf-8') as file:
    #         IPS = file.read()
    #     IPS = re.findall(r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}', IPS)
    #     IPS = list(set(IPS))


    # def search_ips_button_clicked(self):
    #     """
    #     Search the IPs in the file
    #     """
    #     # Clear the previous IP list
    #     IP_LIST_BOX.delete(0, tk.END)
    #     for ip in IPS:
    #         try:
    #             response = requests.get(f'https://api.abuseipdb.com/api/v2/check',
    #                                     params={'ipAddress': ip, 'maxAgeInDays': 90},
    #                                     headers={'Key': "App.api_key"}, timeout=5)
    #             data = response.json()
    #         except requests.exceptions.RequestException as e:
    #             IP_LIST_BOX.insert(tk.END, f'{ip} - API request error')
    #             return
    #         if data["data"]["abuseConfidenceScore"] >= 50:
    #             IP_LIST_BOX.insert(tk.END, f'{ip} - IP flagged as suspicious')


    # def save_to_file(self):
    #     """
    #     Save the flagged IPs to a file
    #     """
    #     # Ask user where they want to save the file
    #     filepath = filedialog.asksaveasfilename(defaultextension=".txt",
    #                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    #     # Open the file for writing and write the flagged IPs to it
    #     with open(filepath, "w", encoding='utf-8') as file:
    #         for ip in IP_LIST_BOX.get(0, tk.END):
    #             if "suspicious" in ip:
    #                 file.write(ip + "\n")
    #     # Inform the user that the file was saved
    #     messagebox.showinfo("Save to File", "File saved successfully!")


    # def close_button_clicked(self):
    #     print("cierra")
    #     # """
    #     # Close the main window
    #     # """
    #     # # window.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
   

  


 