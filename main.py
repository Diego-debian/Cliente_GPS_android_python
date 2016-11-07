#-*- coding:utf-8 -*-
#qpy:kivy
'''
Aplicación desarrollada por el equipo de HACKVISION, Bogotá D.C.; Colombia
	Licenciado en física ---------------------------------> Diego Alberto Parra Garzón     DESARROLLADOR DE CONTENIDO 
	Profesional en ciencia de la información -------------> Luis Ali Ortiz Martínez        DESARROLLADOR DE CONTENIDO  
	Profesional en ciencia de la información -------------> Juan David Bastidas Blanco     DESARROLLADOR DE CONTENIDO
	Ingeniero de sistemas ------------------------------->  Miguel Ángel Garzón            DESARROLLADOR DE CONTENIDO

'''
import kivy
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.app import App
from commands import getoutput
import ArduinoBluetooth
from ArduinoBluetooth import *
from kivy.clock import Clock
from kivy.uix.camera import Camera
from kivy.core.window import Window 
from kivy.uix.scatter import Scatter
import Brujula
from Brujula import *            

kivy.require('1.9.0')
class clienteHACKVISION(App):
    def Label1(self):
        global lbl1
        lbl1 = Label()
        lbl1.text =  "Esperando instrucciones:"
        lbl1.pos = 200+self.xo,280+self.yo
        self.widget1.add_widget(lbl1)
        print "Esperando instrucciones:"

    def Label2(self):
        widget3 = Widget()
        img2 = Image()
        img2.source = "img/text.png"        
        x,y = 130, 370
        img2.pos = x+self.xo, y-160+self.yo
        img2.size= 300, 500
        lbl2 = Label()
        lbl2.pos = x+90+self.xo , y+40+self.yo
        lbl2.text = "            " + 'HACK-VISION DEMO\n                 Recibe GPS \n'+ "          "+'      Blueetooth '
        widget3.add_widget(img2)
        widget3.add_widget(lbl2)  
        self.widget1.add_widget(widget3)


    def Label3(self):
        global lbl3
        lbl3 = Label()
        lbl3.text =  "Esperando instrucciones:"
        lbl3.pos = 200, 80
        self.widget1.add_widget(lbl3)
        print "Esperando instrucciones:"


    def IMAG(self):
        layout = RelativeLayout()
        widget3 = Widget()
        img2 = Image()
        img2.source = "img/text.png"        
        x,y = 130, 370
        img2.pos = x+self.xo, y-420+self.yo
        img2.size= 300, 680
          
        widget3.add_widget(img2)
        self.widget1.add_widget(widget3) 

    def IMAG2(self):
        layout = RelativeLayout()
        widget4 = Widget()
        img2 = Image()
        img2.source = "img/text.png"        
        x,y = 140, -250
        img2.pos = x,y
        img2.size= 300, 680
          
        widget4.add_widget(img2)
        layout.add_widget(widget4)
        self.widget1.add_widget(layout) 


 
    def EncenderBluetooth(self, *args):
        print "Llamado a prender"
        try:
            Dispo = "HC-05"
            lbl1.text = "Espere conectando el Bluetooth"
            ArduinoB.obtenerCorrienteEnchufe('HC-06')
            Mensaje = "Dispositivo conectado"
            print Mensaje
            lbl1.text = Mensaje 
        except:
            Mensaje = "Dispositivo NO CONECTADO revise su conexion "
            print Mensaje
            ArduinoB.obtenerCorrienteEnchufe("HC-05")
            lbl1.text = Mensaje

    def ApagarBluetooth(self, *args):
        try:
            ArduinoB.Cerrar()
            Mensaje = "Conexion cerrada"
            print Mensaje 
            lbl1.text = Mensaje

        except:
            Mensaje = "Revise su conexion"
            print Mensaje
            lbl1.text = Mensaje


    def EscribirBluetooth(self, Mensaje, *args):
        try:
            ArduinoB.Escribir(Mensaje)
            Mensaje1 = "Se envio el mensaje ["+Mensaje+"] correctamente."
            print Mensaje1
            Mensa = Mensaje.split("\t")
            MensajeFinal = "\n\t\t\t\tLatitud: "+ Mensa[1]+ "\n\t\t\t\tLongitud: "+Mensa[2]+ "\n\t\t\t\tAltitud: "+ Mensa[3]+"\n\t\t\t\tRapidez: "+ Mensa[4]
            lbl1.text = MensajeFinal
        except:
            Mensaje1 =  "Fallo el envio del mensaje ["+Mensaje+"]  revise su conexion."
            print Mensaje1
            lbl1.text = Mensaje1
   
    def Lectura(self, *args):
        print "esta leyendo"
        Lec1 = ArduinoB.LeerCADENA()
        lec1 = Lec1.split("\t")
        lec2=str(lec1)
        print lec1
        lec2 = "\n\n\n\n\t\t\t\LECTURA DEL GPS  \n\t\t\t\tLatitud: "+ lec1[1]+ "\n\t\t\t\tLongitud: "+lec1[2]+ "\n\t\t\t\tAltitud: "+ lec1[3]+"\n\t\t\t\tRapidez: "+ lec1[4]
        lbl1.text = str(lec2)
        
        
#comienza la lectura del sensor
    def Com_Lec(self, *args):
        Hilo1 = Clock.schedule_interval(self.Lectura, 3/2)
     #   Clock.unschedule(self.Lectura)


# IDENTIFICADOR DE PROCESOS EN ARDUINO
    def Procesos_Arduino(self):
        try:
            global ArduinoB
            print "Llamado a la libreria"
            from ArduinoBluetooth import *
            
            print "paso el llamado"
            print "instanciando la clase ArduinoBluetooth"
            ArduinoB = ArduinoBluetooth()
            Mensaje = "Todos los procesos Arduino Activados "
            print Mensaje 
            lbl1.text = Mensaje
            
        except:
            Mensaje = "Fallo al activar los procesos Arduino"
            print Mensaje
            lbl1.text = Mensaje

        try: 
            print "Revizando la lectura del Bluetooth"
            self.EncenderBluetooth()
            self.Com_Lec()
            print "Lectura correcta"
        except:
            Mensaje = "Fallo La Lectura del bluetooth"
            print Mensaje
            lbl1.text = Mensaje
        pass


#LECTURAS SENSOR DE CAMPO MAGNETICO
    def lecturaas(self, *args):
        lectura = self.SensorM.Disparo()
        if (lectura == None):
            pass
        if (lectura != None):
            try:
                lecto = str(lectura)
                lec = lecto.split("\t")
                print 'aca voy pendejo ',lec
                ang = lec[1]
                Bx = lec[2]
                By = lec[3]
                Bz = lec[4]
                lec2 = "\n\n\n\n\t\t\t\LECTURA DEL SCM  \n\t\t\t\tAngulo "+ str(ang)+ "\n\t\t\t\tBx: "+str(Bx)+ "\n\t\t\t\tBy:  "+ str(By)+"\n\t\t\t\tBz: "+ str(Bz)
                lbl3.text = str(lec2)
            except:
                pass
        else:
            pass



    #identificaor de procesos Brujula
    def ProcesosBrujula(self):
        try:
            self.SensorM = Brujula()
            self.SensorM.Hardware()
            if True:
                Clock.schedule_interval(self.lecturaas, 3/2)
        except:
            pass        

# IDENTIFICADOR DE PROCESOS EN PYTHON
    def Procesos_Kivy(self):      
        Mensaje0 = "Cativado Label1"
        Mensaje1 = "Fallo al activar label 1"
        Mensaje2 = "Label2 Activado"
        Mensaje3 = "Fallo al Activar el label 2"
        Mensaje4 = "boton imagen1 activado"
        Mensaje5 = "Fallo Al activar la imagen boton1"
        Mensaje6 = "boton imagen2 activado"
        Mensaje7 = "Fallo Al activar la imagen boton2"
        Mensaje8 = "boton imagen3 activado"
        Mensaje9 = "Fallo Al activar la imagen boton3"
        Mensaje10 = "boton imagen4 activado"
        Mensaje11 = "Fallo Al activar la imagen boton4"
        try:
            self.Label1()
            self.IMAG()
            self.Label3()
            self.IMAG2()
            print Mensaje0
        except:
            print Mensaje1

        try:
            self.Label2()
            print Mensaje2
        except:
            self.Label2()
            print Mensaje3

        

      
        pass


    def PROCESOS(self):
        self.Procesos_Kivy()
       # import time
   #     time.sleep(1)
        self.Procesos_Arduino()
#        self.Procesos_Kivy()
        self.ProcesosBrujula()


    def Dispersion2(self):
        self.dis2 = Scatter()
        self.dis2.pos =  -90, -50
        #self.dis2.pos =  random.randrange(100,680), 100
        self.dis2.size_hint = None,None
        #      self.dis2.size = 86, 86
        self.dis2.do_rotation= False
        self.dis2.do_scale= False
        self.dis2.do_translation= False
        self.dis2.rotation = 0
        self.dis2.scale= 1.7

    def Camara(self, *args):
        self.Dispersion2()
        camwidget = Widget()  #Create a camera Widget
        cam = Camera()        #Get the camera
        cam.resolution=(640,480)
        cam.size= 1000,800
        cam.pos=(-100,-100)
        cam.play=True         #Start the camera
        camwidget.add_widget(cam) 
        self.dis2.add_widget(camwidget)
        self.RelativaDispo.add_widget(self.dis2)

    def BotonCamara(self):
        Layout = RelativeLayout()
        wid2 = Widget()
        Btn5 = Button()
        Btn5.background_normal =  'img/observa.png'
        Btn5.pos = 750, 30
        Btn5.bind(on_press = self.TomarFoto)
        wid2.add_widget(Btn5)
        Layout.add_widget(wid2)
        self.RelativaDispo.add_widget(Layout)

    def TomarFoto(self, *args):
        #  Layout = RelativeLayout()
        #    wid2 = Widget()
        #   Mensaje = getoutput("pwd")
        #  LBL1 = Label()
        #   LBL1.pos = 150, 200        
        #   LBL1.text = Mensaje
        #    print Mensaje
        #    wid2.add_widget(LBL1)
        # Layout.add_widget(wid2)
        #   self.DisposicionRelativa.add_widget(wid2)
        try:
            Window.screenshot(name='../../../../../mnt/sdcard/DCIM/imagen.png')
        except:
            print "No se pudo tomar  la foto"     


        
    def build(self):
        self.xo = 0
        self.yo = -40
        self.RelativaDispo = RelativeLayout()
        self.Camara()
        self.BotonCamara()
        self.widget1 = Widget()
        self.widget2 = Widget()
        self.RelativaDispo.add_widget(self.widget1)
        self.RelativaDispo.add_widget(self.widget2)
        self.PROCESOS()
        return self.RelativaDispo

if __name__=='__main__':
    clienteHACKVISION().run()
    
