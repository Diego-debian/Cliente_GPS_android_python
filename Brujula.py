#*-* coding:utf-8 *-*
#qpy:kivy
import kivy
kivy.require('1.9.0')
from plyer import compass

class Brujula:

#función que verifica si el dispositivo soporta el sensor de campo magnético
    def Hardware(self, *args):
        Mensaje1 =  "\nEncendiendo compas\n"
        try:
            self.tetha = 0
            Encender = self.Encender()
            if Encender == True:
                return True
              

        except NotImplementedError:
            import traceback
            traceback.print_exc()
            status = "No reconoce el sensor magnetico en su dispositivo"
            print "No reconoce el compas"
            return False

    # funcion que inicia la lectura del sensor de campo magnetico y devuelve el angulo tetha
    def Disparo(self, *args):
        tetha = self.tetha
        try:
            Mensaje1 =  "\nEmpezando lectura del sesor de campo magnetico\n"
            Mensaje2 = "\nLectura del sensor de campo magnetico correcta: \n"
            Mensaje3 = "\nFallo la lectura del sensor de campo magnetico\n"
            print Mensaje1
            self.Lectura()
            self.Clasifica_tetha()
            print Mensaje2 + str(tetha)
            ENVIO = "\t"+str(tetha)+"\t"+str(self.Bx) +"\t"+str(self.Bz) +"\t"+str(self.Bz)+"\t"
            return ENVIO
        except:
            print Mensaje3 


        return tetha
    #Funcion que enciende el compass o brujula
    def Encender(self, *args):
        Mensaje1 = "\nSe esta encendiendo el sensor de campo magnetico\n"
        Mensaje2 = "\nSensor de campo magnetico encendido\n"
        Mensaje3 = "\nFallo al activar el sensor de campo magnetico\n"
        print Mensaje1
        try:
            compass.enable()
            print Mensaje2
            return True            
        except:
            print Mensaje3
            return False
        pass
        
    #Fuincion que apaga el sensor de campo magnetico
    def Apagar(self, *args):
	Mensaje1 =  "\nSe esta encendiendo el sensor de campo magnético\n"
	Mensaje2 = "\nSensor de Campo magnético apagado\n"
        Mensaje3 = "\nFallo al desactivar el sensor de campo magnetico\n"
	print Mensaje1
        try:
            compass.disable()
            print Mensaje2
        except:
            print Mensaje3

    #Comienza la lectura del sensor de campo magnetico en el dispositivo
    def Lectura(self, *args):
        Mensaje1 = "\nAdquiriendo Datos del sensor de campo magnetico\n"
        print Mensaje1
        x,y,z = compass.orientation
        Mensaje2 = "\nDatos adquiridos correctamente:\n Campo magnetico en x: " +str(x) +"\n Campo magnetico en y: " + str(y) + " \n Campo magnetico en z:" +str(z)
        Mensaje3 = "\nIniciadoo el redondeo de los valores a 3 cifras significativas\n"
        print Mensaje2
        print Mensaje3
        try:
            xf = round(x,  3)
            yf = round(y,  3)
            zf = round(z,  3)
            self.Bx = xf
            self.By = yf
            self.Bz = zf
            Mensaje4  = "Sensor de Campo Magnético \nBx = "+str(xf)+"\n"+"By = "+str(yf)+"\n"+"Bz = "+str(zf)          
	    print Mensaje4 
            return self.Bx, self.By, self.Bz

        except: 
            print "No hay ningun dato todavia espere"



    def Clasifica_tetha(self):
        #Sentido MAnecillas del reloj
        #Primer cuadrante
        try:
            self.tetha != None
                #Primer cuadrante
            if ((self.Bz > -25)&(self.Bz <=0)&(self.Bx <= 0)&(self.By<=0)):
                tetha = (self.Bz*90)/25 + 90
                self.tetha = round(tetha,3)
                return self.tetha
            

                #segundo cuadrante
            if ((self.Bz>0)&(self.Bz<=25)&(self.Bx <= 0)&(self.By<=0)):
                tetha= self.Bz*90/25 + 90
                self.tetha = round(tetha,3)
                return self.tetha
                
       
                #tercer cuadrante
            if ((self.Bz>0)&(self.Bz<=25)&(self.Bx >= 0)&(self.By<=0)):
                tetha= (-1)*(self.Bz*90/25 -270) 
                self.tetha = round(tetha,3)
                return self.tetha
            
                #Cuarto cuadrante
            if ((self.Bz > -25)&(self.Bz <=0)&(self.Bx >= 0)&(self.By<=0)):         
                tetha= (-1)*(self.Bz*90/25 - 270)
                self.tetha = round(tetha,3)
                return self.tetha

        except:
            print "Nada"
            
            
    def __init__(self):
        self.Hardware()
    
#Medida = Brujula()        
