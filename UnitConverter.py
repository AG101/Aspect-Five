# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:50:22 2020

@author: Aspect

Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another. 
The user enters the type of unit being entered, the type of unit they want to convert to and then the 
value. The program will then make the conversion.


"""

conversions = ['mass', 'currency', 'speed', 'frequency', 'temperature', 'area']
mass_type = ['gigatonne','megatonne','tonne','kilogram','gram','milligram','microgram','nanogram','picogram','pound','ounce', 'stone']
currency_type = ['pound','euro','yuan','yen','dollar']
speed_type = ['mps', 'fps', 'mph', 'kph', 'knot']
frequency_type = ['hertz', 'kilohertz', 'megahertz', 'gigahertz']
temperature_type = ['celsius', 'fahrenheit', 'kelvin']
area_type = ['square kilometre','square metre', 'square mile', 'square yard', 'square foot', 'square inch', 'hectare', 'acre'  ]

class Questions:
    
    def __init__(self):
        self.answer_1 = ''
        self.answer_2 = ''
        self.answer_3 = ''
        #no self.answer_4? well 1-3 are used within each other, 4 is not and is just a single value unrelated to anythign that came before
    def question_1(self):
        #Asks the user what type of conversion they'd like whilst showing a list of available types to choose from
        print("What type of conversion would you like today?")
        self.answer_1 = 1 #answer isn't in conversion by defualt so they have to input something valid
        while self.answer_1 not in conversions:
            self.answer_1 = input("We offer: mass, currency, speed, frequency, temperature, area \n ")
        print(f"Fantastic, you've chosen {self.answer_1}\n")
        return self.answer_1
    
    def question_2(self):
        #takes the type from question 1 and offers the available units within that type to convert
        #stores the answer
        if self.answer_1 == 'mass':
            print("Which unit will you be converting from")
            while self.answer_2 not in mass_type:
                print(f"Here is a list of available units: \n {mass_type} ")
                self.answer_2 = input("Pick one: ")
            print(f"You've chosen {self.answer_2} \n")
            return self.answer_2
        
        elif self.answer_1 == 'currency':
            print("Currency conversion awaaaay, what currency will we be converting from today?")
            while self.answer_2 not in currency_type:
                print(f"Here is a list of available currencies: \n {currency_type}")
                self.answer_2 = input("pick one: ")
            print(f"You've chosen {self.answer_2} \n")
            return self.answer_2
        
        elif self.answer_1 == 'speed':
            print("Speedster eh, what unit will you be converting from?")
            while self.answer_2 not in speed_type:
                print(f"Here's a list of speed units: \n {speed_type}")
                self.answer_2 = input("pick one: ")
            print(f"You've chosen {self.answer_2} \n")
            return self.answer_2
        
        elif self.answer_1 == 'frequency':
            print(f"Sound is your game, what shall we be converting from")
            while self.answer_2 not in frequency_type:
                print(f"Here's a list of frequency units: \n{frequency_type}")
                self.answer_2 = input("pick one: ")
            print(f"You have chosen {self.answer_2}")
            return self.answer_2
        
        elif self.answer_1 == 'temperature':
            print(f"Heat is your game, what shall we be converting from")
            while self.answer_2 not in temperature_type:
                print(f"Here's a list of temperature units: \n{temperature_type}")
                self.answer_2 = input("pick one: ")
            print(f"You have chosen {self.answer_2}")
            return self.answer_2
        
        elif self.answer_1 == 'area':
            print(f"Space is your game, what shall we be converting from")
            while self.answer_2 not in area_type:
                print(f"Here's a list of area units: \n{area_type}")
                self.answer_2 = input("pick one: ")
            print(f"You have chosen {self.answer_2}")
            return self.answer_2
        
    def question_3(self):
        #does the same as question 2 but allows the user to pick a unit to convert into, 
        #disallowing the same choice and storing the answer
        if self.answer_1 == 'mass':
            print("Which unit will you be converting to?")
            #makes sure you can't pick the same answer twice
            while self.answer_3 not in mass_type or self.answer_3 == self.answer_2:
                print(f"Here is a list of available units: \n {mass_type}")
                self.answer_3 = input("Pick one: ")   
            print(f"You have chosen {self.answer_3}\n")
            return self.answer_3
        
        elif self.answer_1 == 'currency':
            print("And to which currency will you be converting to?")
            while self.answer_3 not in currency_type or self.answer_3 == self.answer_2:
                print(f"Here is a list of available currencies: \n {currency_type}")
                self.answer_3 = input("Pick one: ")
            print(f"You've chosen {self.answer_3}\n")
            return self.answer_3
        
        elif self.answer_1 == 'speed':
            print(f"And which unit will you be converting to? ")
            while self.answer_3 not in speed_type or self.answer_3 == self.answer_2:
                print(f"Here is a list of speeds: \n {speed_type} ")
                self.answer_3 = input("pick one :")
            print(f"You've chosen {self.answer_3}\n")
            return self.answer_3
        
        elif self.answer_1 == 'frequency':
            print(f"And which unit will you be converting to? ")
            while self.answer_3 not in frequency_type or self.answer_3 == self.answer_2:
                print(f"Here is a list of speeds: \n {frequency_type} ")
                self.answer_3 = input("pick one :")
            print(f"You've chosen {self.answer_3}\n")
            return self.answer_3
        
        elif self.answer_1 == 'temperature':
            print(f"And which unit will you be converting to? ")
            while self.answer_3 not in temperature_type or self.answer_3 == self.answer_2:
                print(f"Here is a list of temps: \n {temperature_type} ")
                self.answer_3 = input("pick one :")
            print(f"You've chosen {self.answer_3}\n")
            return self.answer_3
        
        elif self.answer_1 == 'area':
            print(f"And which unit will you be converting to? ")
            while self.answer_3 not in area_type or self.answer_3 == self.answer_2:
                print(f"Here is a list of areas: \n {area_type} ")
                self.answer_3 = input("pick one :")
            print(f"You've chosen {self.answer_3}\n")
            return self.answer_3
        
    def question_4(self):
        #gets the numerical value of hte conversion from the user and stores it
        print(f"And finally, how many {self.answer_2}s would you like converting into {self.answer_3}s today?")
        while True:
            try:
                val = int(input("Enter a Value: "))
            except:
                print("integer please")
                continue
            else:                
                break
        return val
    
class converter():
    #initialises with the answers given by the user
    def __init__(self,ans1,ans2,ans3,ans4):
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
       
        #answer 1 contains which type of conversion to be done
        #each conversion type has its own associated function
        if self.ans1 == 'mass':
            self.mass()
        elif self.ans1 == 'currency':
            self.currency()
        elif self.ans1 == 'speed':
            self.speed()
        elif self.ans1 == 'frequency':
            self.frequency()
        elif self.ans1 == 'temperature':
            self.temperature()
        elif self.ans1 == 'area':
            self.area()
            
    def mass(self):
        print("it might work")
        mass_dict = {'gigatonne':1000000000000000, 'megatonne':1000000000000, 'tonne': 1000000, 'kilogram': 1000, 'gram': 1,
                     'milligram':0.001, 'microgram': 0.000001, 'nanogram':0.000000001, 'picogram':0.000000000001,
                     'stone': 6350, 'pound':454, 'ounce': 28.35}
        
        '''
        Gt = 1000000000000000
        Mt = 1000000000000
        t = 1000000
        kg = 1000
        g = 1
        mg =0.001
        mewg = 0.000001
        ng = 0.000000001
        pg = 0.000000000001 
        stone = 6350
        pound = 454
        ounce = 28.35
        
        leaving this here as reminder that dictionaries are great
        '''
        
        x = mass_dict[self.ans2] #answer2 has the unit to be converted from and the value is obtained from the dicitonary
        y = mass_dict[self.ans3]#same but with answer 3
        
        conversion = (self.ans4 * x)/y #masses convert quite nicely into each other
        
        print(f"Okidoke {self.ans1} conversion in full swing\n {self.ans4} {self.ans2}s converts into {conversion} {self.ans3}s")
    
        
    def currency(self):
        
        '''
        conversion rates as of 2020/11/19 found on google
        there is probably a better way to do this but this made the most sense to me at the time
        treat each currency as abase currency and work out conversions into other currencies so that a conversion
        can be made by multiplying the value given by the user by that exchange rate based upon the currencies selected
        this would be terrible with many currencies 
        '''
        base_pound = {'pound': 1, 'yuan':8.71,'dollar':1.32,'yen':137.34 ,'euro':1.12}
        base_yuan = {'pound': 0.11, 'yuan':1,'dollar':0.15,'yen':15.77 ,'euro':0.13}
        base_dollar = {'pound': 0.76, 'yuan':6.58,'dollar':1,'yen':103.82 ,'euro':0.84}
        base_euro = {'pound': 0.9, 'yuan':7.8,'dollar':1.18,'yen':123.02 ,'euro':1}
        base_yen = {'pound': 0.0073, 'yuan':0.063,'dollar':0.0096,'yen':1 ,'euro':0.0081}
        
        exchange_rate = 0 #you dont need ot initalise vairables in python
        
        if self.ans2 == 'pound':
            exchange_rate = base_pound[self.ans3]
        elif self.ans2 == 'yuan':
            exchange_rate = base_yuan[self.ans3]
        elif self.ans2 == 'yen':
            exchange_rate = base_yen[self.ans3]
        elif self.ans2 == 'dollar':
            exchange_rate = base_dollar[self.ans3]
        elif self.ans2 == 'euro':
            exchange_rate = base_euro[self.ans3]
        
        conversion = self.ans4 * exchange_rate
        
        print(f"Okidoke {self.ans1} conversion in full swing\n {self.ans4} {self.ans2}s converts into {conversion} {self.ans3}s")
    
    def speed(self):
        #same idea as above
        #i'm a fan of the currency conversion method when there are only a few cases
        base_mph = {'mph': 1, 'kmh': 1.609, 'knot': 0.868976, 'fps': 1.467, 'mps': 0.44704}
        base_kmh = {'mph': 0.2777, 'kmh':1, 'knot': 0.5399, 'fps': 0.911, 'mps': 0.2777}
        base_knot = {'mph': 1.151, 'kmh': 0.5144, 'knot': 1, 'fps': 1.688, 'mps': 0.5144}
        base_fps = {'mph': 0.6818 , 'kmh': 1.0972, 'knot': 0.5924 , 'fps': 1,'mps': 0.3048}
        base_mps = {'mph': 2.2369 , 'kmh': 3.6 , 'knot': 1.943, 'fps': 3.281 , 'mps': 1}
        
        multi = 0 #you still don't need to initialise variables in python
        
        if self.ans2 == 'mph':
            multi = base_mph[self.ans3]
        elif self.ans2 == 'kmh':
            multi = base_kmh[self.ans3]
        elif self.ans2 == 'knot':
            multi = base_knot[self.ans3]
        elif self.ans2 == 'fps':
            multi = base_fps[self.ans3]
        elif self.ans2 == 'mps':
            multi = base_mps[self.ans3]
        conversion = self.ans4 * multi
        print(f"Okidoke {self.ans1} conversion in full swing\n {self.ans4} {self.ans2}s converts into {conversion} {self.ans3}s")
    
    def frequency(self):
        
        #factor of 10 conversions work just like the mass conversions
        base = {'hertz':1, 'kilohertz':1000,'megahertz':1000000,'gigahertz':1000000000}
        
        x = base[self.ans2]
        y = base[self.ans3]
        
        conversion = (self.ans4 * x)/y
        
        print(f"Okidoke {self.ans1} conversion in full swing\n {self.ans4} {self.ans2}s converts into {conversion} {self.ans3}s")
        #dictionaries are amazing
    
    def temperature(self):
       conversion = 0 #again, python
       #temperature conversions are weird so each line is unique 
       if self.ans2 == 'celsius' and self.ans3 == 'kelvin':
           conversion = self.ans4 + 273.15
       elif self.ans2 == 'celsius' and self.ans3 == 'fahrenheit':
           conversion = (self.ans4 * (9/5)) + 32
       elif self.ans2 == 'kelvin' and self.ans3 == 'celsius':
           conversion = self.ans4 - 273.15
       elif self.ans2 == 'kelvin' and self.ans3 == 'fahrenheit':
           conversion = ((self.ans4 - 273.15)*(9/5))+32
       elif self.ans2 == 'fahrenheit' and self.ans3 == 'celsius':
           conversion = (self.ans4 -32)*(5/9)
       elif self.ans2 == 'fahrenheit' and self.ans3 == 'kelvin':
           conversion = ((self.ans4 -32)*(5/9)) + 273.15
       print(f"Okidoke {self.ans1} conversion in full swing\n {self.ans4} {self.ans2}s converts into {conversion} {self.ans3}s")
       
    def area(self):
       
        #at this point i question the use of this method and wonder if there was a better way
        sq_mile = {'square kilometre':2.58999,'square metre':2.59e+6,'square mile':1,'square yard':3.098e+6,'square foot':2.788e+7, 'square inch':4.014e+9,'hectare':258.999,'acre':640}
        sq_metre ={'square kilometre':1e-6,'square metre':1,'square mile':3.861e-7,'square yard':1.1959876543333338716,'square foot':10.763888889, 'square inch':1550,'hectare':1e-4,'acre':0.000247105}
        sq_km = {'square kilometre':1,'square metre':1e+6,'square mile':0.386102,'square yard':1.196e+6,'square foot':1.076e+7, 'square inch':1.55e+9,'hectare':100,'acre':247.105}
        sq_inch = {'square kilometre':6.4516e-10,'square metre':0.00064516,'square mile':2.491e-10,'square yard':0.000771605,'square foot':0.00694444, 'square inch':1,'hectare':6.4516e-8,'acre':1.5942e-7}
        sq_yard = {'square kilometre':8.3613e-7,'square metre':0.836127,'square mile':3.2283e-7,'square yard':1,'square foot':9, 'square inch':1296,'hectare':8.3613e-5,'acre':0.000206612}
        sq_foot = {'square kilometre':9.2903e-8,'square metre':0.092903,'square mile':3.587e-8,'square yard':0.111111,'square foot':1, 'square inch':144,'hectare':9.2903e-6,'acre':2.2957e-5}
        hectare = {'square kilometre':0.01,'square metre':10000,'square mile':0.00386102,'square yard':11959.9,'square foot':107639, 'square inch':1.55e+7,'hectare':1,'acre':2.47105}
        acre = {'square kilometre':0.00404686,'square metre':4046.86,'square mile':0.0015625,'square yard':4840,'square foot':43560, 'square inch':6.273e+6,'hectare':0.404686,'acre':1}
        
        if self.ans2 == 'square kilometre':
            conversion = self.ans4 * sq_km[self.ans3]
        elif self.ans2 == 'square metre':
            conversion = self.ans4 * sq_metre[self.ans3]
        elif self.ans2 == 'square mile':
            conversion = self.ans4 * sq_mile[self.ans3]
        elif self.ans2 == 'square yard':
            conversion = self.ans4 * sq_yard[self.ans3]
        elif self.ans2 == 'square foot':
            conversion = self.ans4 * sq_foot[self.ans3]
        elif self.ans2 == 'square inch':
            conversion = self.ans4 * sq_inch[self.ans3]
        elif self.ans2 == 'hectare':
            conversion = self.ans4 * hectare[self.ans3]
        elif self.ans2 == 'acre':
            conversion = self.ans4 * acre[self.ans3]
        print(f"Okidoke {self.ans1} conversion in full swing\n {self.ans4} {self.ans2}s converts into {conversion} {self.ans3}s")
        
#lovely simple logic   
q = Questions()
ans1 = q.question_1()
ans2 = q.question_2()
ans3 = q.question_3()
ans4 = q.question_4()
conv = converter(ans1,ans2,ans3,ans4)
