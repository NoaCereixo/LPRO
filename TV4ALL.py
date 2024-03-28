import cec
import sys
import os
import selectors

def acciones(accion):
	#print("accion: " + accion)
	if accion == "0": #encender
		#print("enceder")
		tv.power_on()
		
	elif accion == "1": #apagar
		#print("apagar")
		tv.standby()
		return True
		
	elif accion == "2": #subir volumen
		selector = selectors.DefaultSelector()
		selector.register(sys.stdin, selectors.EVENT_READ)
		entrada = ""
		while True:
			#print("subir volumen")
			cec.volume_up()
			events = selector.select(timeout=0.5)
			for key, mask in events:
				entrada = key.fileobj.read(1)
				if entrada == "2":
					break
			if entrada == "2":
				break
		
	elif accion == "3": #bajar volumen
		selector = selectors.DefaultSelector()
		selector.register(sys.stdin, selectors.EVENT_READ)
		entrada = ""
		while True:
			#print("bajar volumen")
			cec.volume_down()
			events = selector.select(timeout=0.5)
			for key, mask in events:
				entrada = key.fileobj.read(1)
				if entrada == "2":
					break
			if entrada == "2":
				break
		
	elif accion == "4": #canal siguiente
		#print("canal siguiente")
		cec.transmit(cec.CECDEVICE_TV, cec.CEC_OPCODE_USER_CONTROL_PRESSED, bytes([2]))
		
	elif accion == "5": #canal anterior
		#print("canal anterior")
		cec.transmit(cec.CECDEVICE_TV, cec.CEC_OPCODE_USER_CONTROL_PRESSED, bytes([1]))
		
if __name__=="__main__":
	
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	
	while True:
		if acciones(input()):
			break
