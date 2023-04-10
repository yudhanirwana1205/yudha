#car
class car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.door = 'closed'
        self.car = 'off'
    
    def open(self):
        if self.door == 'closed':
            print('pintu terbuka')
            self.door = 'opened'
        else:
            print('pintu tertutup')

    def closed(self):
        if self.door == 'opened':
            print('pintu tertutup')
            self.door = 'closed'
        else:
            print('pintu terbuka')

    def on(self):
        if self.car == 'off':
           print('mesin nyalah')
           self.car = 'on'
        else:
            print('mesin mati')

    def off(self):
        if self.car == 'on':
            print('mesin mati')
            self.car = 'off'
        else:
            print('mesin nyalah')

car_1 = car("Honda", 2023)
car_1.open()
car_1.closed()
car_1.on()
car_1.off()

      
   


    




