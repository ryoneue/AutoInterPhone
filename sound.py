import machine
from machine import Pin, I2C
import time


class sound_sensor:
    def __init__(self, adc_pin, limit, pio=False, out_pin=25, freq=10000):
        self.pin = machine.ADC(adc_pin)
        self.count = 0
        self.limit = limit
        self.value_list = []
        self.max_value = 0
        if pio:
            from pio_timer import pio_timer
            self.freq = freq
            self.timer = pio_timer(sm=1, freq=self.freq, pin=18)
            self.out_pin = Pin(out_pin)
            self.timer.active()
#             self.pio_sensor(sm=2, self.detect_loud_pio, freq=125000, pin=)
        
    def check_loudness_limit(self):
        count = 0
        value_list = []
        while True:
#             print(self.pin.read_u16())
            value = self.pin.read_u16()
            
            value_list.append(value)
            count += 1
            max_value = 0
            if count > self.limit:
                max_value = max(value_list)
    #             print("loudness:{}".format(max_value))
                count = 0
                value_list = []
                break
        return max_value        

    # pio_timer()による正確な時間計測版
    def check_loudness_time(self, msec, limit=None):
#         frame = int((msec / self.freq) * 100000)
        self.timer.put(msec)
        tmp = self.limit
#         self.limit = 1000
        if not limit is None:
            self.limit = limit
            

        while True:
#             print("stop")
            if self.out_pin.value()==1:
                break    
#         print("start")            
        max_value = 0
        value_list = []
        while True:
#             print(Pin(25).value())
#             continue
        
            value = self.pin.read_u16()
#             value = self.check_loudness_limit()
            value_list.append(value)
            self.count += 1
                      
#             print(self.out_pin.value())
            if self.out_pin.value()==0:
                max_value = max(value_list)
#                 print("loudness:{}".format(self.value_list))
#                 print(len(self.value_list), max_value)
                self.count = 0
#                 value_list = []
                self.limit = tmp
                return value_list
    
    def check_loudness(self):
        return self.pin.read_u16()

    def detect_loud(self, thresh):
#         print("a")
        check = False
        max_value = self.check_loudness_limit()
#         print(max_value)
        self.max_value = max_value
        if max_value > thresh:
            check = True
        
        
        return check, max_value
    
#     @asm_pio(set_init=PIO.OUT_LOW)
#     def detect_loud_pio(self, thresh):
#         wrap_target()
# #         pull()
#         label("read_adc")
#         adc(ival(26),0)
#         mov(isr, osr)
#         jmp()
#         set(pins, 1)
#         mov(x,osr)
#         label("loop")
#         jmp(x_dec, "loop")
#         set(pins, 0)
#         
#         wrap()
#         
#         
#         return check
    
if __name__ == '__main__':
    
    # Raspberry Pi Picoの26ピン=ADC0
#     pin26 = machine.ADC(0)
    pin25 = machine.Pin(16, Pin.OUT)
    pin1 = machine.Pin(16, Pin.OUT)

    # def setpin(pin1,pin25):
        
    # value = 0
    # value_add = 0
    # value_list = []
    # count = 0
    sound = sound_sensor(adc_pin=1, limit=100, pio=True, out_pin=18)
    
#     pin25.value(1)
#     print(pin26.read_u16())
    while True:
        check, max_value = sound.detect_loud(thresh=10000)
        if check:        
#             print("b")
#             read_u16()
#             pin25.off()
            
#             print(Pin(25).value())
            value_list = sound.check_loudness_time(msec=100, limit=7)
#             pin25.value(0)
            print(min(value_list))
#             print(Pin(25).value())
#             time.sleep(1)
#             pin1.value(1)
#             time.sleep(1)
        else:
#             pin25.value(0)
#             print(pin26.read_u16())
            pass
        

            
            

