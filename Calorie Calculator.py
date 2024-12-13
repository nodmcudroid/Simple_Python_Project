print("Welcome to Calorie Calculator ")
print("Breakfast--1")
print("Lunch--2")
print("Dinner--3")
a = input("Enter your food time(q to exit): ")
if a =='q':
    exit()
item = input("How many item did you eat: ")
if a == '1': #breakfast
    if item == '1':#the number of item
        print('''- Paratha with Chutney -- I  
    - Panta Bhat -- II  
    - Chirer Pulao -- III  
    - Muri with Gur -- IV  
    - Muri with Banana -- V  
    - Bread and Banana -- VI  
    - Shingara -- VII  
    - Sujir Halwa -- VIII  
    - Khirsa -- IX  
    - Luchi with Aloo Tarkari -- X  
    - Roti with Honey -- XI  
    - Egg Toast -- XII  
    - Chola Bhuna -- XIII  
    - Dal Puri -- XIV  
    - Puffed Rice with Mustard Oil -- XV  
    - Sweet Pitha -- XVI  
    - Doi with Gur -- XVII  
    - Fruits with Yogurt -- XVIII  
    - Mishti Doi with Chira -- XIX  
    - Cholar Dal with Ruti -- XX  ''')
        while True:
            b = input("Enter your food item: ")
            i = "Paratha with Chutney"
            ii = "Panta Bhat"
            iii = "Chirer Pulao"
            iv = "Muri with Gur"
            v = "Muri with Banana"
            vi = "Bread and Banana"
            vii = "Shingara"
            viii = "Sujir Halwa"
            ix = "Khirsa"
            x = "Luchi with Aloo Tarkari"
            xi = "Roti with Honey"
            xii = "Egg Toast"
            xiii = "Chola Bhuna"
            xiv = "Dal Puri"
            xv = "Puffed Rice with Mustard Oil"
            xvi = "Sweet Pitha"
            xvii = "Doi with Gur"
            xviii = "Fruits with Yogurt"
            xix = "Mishti Doi with Chira"
            xx = "Cholar Dal with Ruti"
            if b == 'i':
                print("Paratha with Chutney -- 180 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'ii':
                print("Panta Bhat -- 160 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'iii':
                print("Chirer Pulao -- 250 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'iv':
                print("Muri with Gur -- 170 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'v':
                print("Muri with Banana -- 200 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'vi':
                print("Bread and Banana -- 160 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'vii':
                print("Shingara -- 130 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'viii':
                print("Sujir Halwa -- 200 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'ix':
                print("Khirsa -- 180 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'x':
                print("Luchi with Aloo Tarkari -- 200 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xi':
                print("Roti with Honey -- 180 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xii':
                print("Egg Toast -- 140 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xiii':
                print("Chola Bhuna -- 150 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xiv':
                print("Dal Puri -- 150 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xv':
                print("Puffed Rice with Mustard Oil -- 230 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xvi':
                print("Sweet Pitha -- 150 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xvii':
                print("Doi with Gur -- 160 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xviii':
                print("Fruits with Yogurt -- 160 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xix':
                print("Mishti Doi with Chira -- 250 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            elif b == 'xx':
                print("Cholar Dal with Ruti -- 240 calories")
                print("Thank you so much")
                print("Have a nice day")
                break
            else:
                print("Invalid input! Please try again.")
    elif item == '2':
            print('''    - Paratha with Chutney -- I  
        - Panta Bhat -- II  
        - Chirer Pulao -- III  
        - Muri with Gur -- IV  
        - Muri with Banana -- V  
        - Bread and Banana -- VI  
        - Shingara -- VII  
        - Sujir Halwa -- VIII  
        - Khirsa -- IX  
        - Luchi with Aloo Tarkari -- X  
        - Roti with Honey -- XI  
        - Egg Toast -- XII  
        - Chola Bhuna -- XIII  
        - Dal Puri -- XIV  
        - Puffed Rice with Mustard Oil -- XV  
        - Sweet Pitha -- XVI  
        - Doi with Gur -- XVII  
        - Fruits with Yogurt -- XVIII  
        - Mishti Doi with Chira -- XIX  
        - Cholar Dal with Ruti -- XX  ''')
            while True:
                i = 180  # Paratha with Chutney
                ii = 160  # Panta Bhat
                iii = 250  # Chirer Pulao
                iv = 170  # Muri with Gur
                v = 200  # Muri with Banana
                vi = 160  # Bread and Banana
                vii = 130  # Shingara
                viii = 200  # Sujir Halwa
                ix = 180  # Khirsa
                x = 200  # Luchi with Aloo Tarkari
                xi = 180  # Roti with Honey
                xii = 140  # Egg Toast
                xiii = 150  # Chola Bhuna
                xiv = 150  # Dal Puri
                xv = 230  # Puffed Rice with Mustard Oil
                xvi = 150  # Sweet Pitha
                xvii = 160  # Doi with Gur
                xviii = 160  # Fruits with Yogurt
                xix = 250  # Mishti Doi with Chira
                xx = 240  # Cholar Dal with Ruti

                while True:
                    b = input("Enter your 1st food item: ").strip().lower()
                    c = input("Enter your 2nd food item: ").strip().lower()

                    # Use a dictionary to map inputs to their calorie values
                    calorie_map = {
                        "i": i, "ii": ii, "iii": iii, "iv": iv, "v": v,
                        "vi": vi, "vii": vii, "viii": viii, "ix": ix, "x": x,
                        "xi": xi, "xii": xii, "xiii": xiii, "xiv": xiv,
                        "xv": xv, "xvi": xvi, "xvii": xvii, "xviii": xviii,
                        "xix": xix, "xx": xx
                    }

                    if b in calorie_map and c in calorie_map:
                        calorie_b = calorie_map[b]
                        calorie_c = calorie_map[c]
                        total_calories = calorie_b + calorie_c

                        print(f"The amount of calories for {b} is {calorie_b}, and for {c} is {calorie_c}.")
                        print(f"The total amount of calories is {total_calories}.")
                        print("-----------------------------------------")
                        print("Thank you so much!")
                        break
                    else:
                        print("Invalid input, please try again.")
    elif item == '3':
        print('''    - Paratha with Chutney -- I  
        - Panta Bhat -- II  
        - Chirer Pulao -- III  
        - Muri with Gur -- IV  
        - Muri with Banana -- V  
        - Bread and Banana -- VI  
        - Shingara -- VII  
        - Sujir Halwa -- VIII  
        - Khirsa -- IX  
        - Luchi with Aloo Tarkari -- X  
        - Roti with Honey -- XI  
        - Egg Toast -- XII  
        - Chola Bhuna -- XIII  
        - Dal Puri -- XIV  
        - Puffed Rice with Mustard Oil -- XV  
        - Sweet Pitha -- XVI  
        - Doi with Gur -- XVII  
        - Fruits with Yogurt -- XVIII  
        - Mishti Doi with Chira -- XIX  
        - Cholar Dal with Ruti -- XX  ''')
        while True:
            i = 180  # Paratha with Chutney
            ii = 160  # Panta Bhat
            iii = 250  # Chirer Pulao
            iv = 170  # Muri with Gur
            v = 200  # Muri with Banana
            vi = 160  # Bread and Banana
            vii = 130  # Shingara
            viii = 200  # Sujir Halwa
            ix = 180  # Khirsa
            x = 200  # Luchi with Aloo Tarkari
            xi = 180  # Roti with Honey
            xii = 140  # Egg Toast
            xiii = 150  # Chola Bhuna
            xiv = 150  # Dal Puri
            xv = 230  # Puffed Rice with Mustard Oil
            xvi = 150  # Sweet Pitha
            xvii = 160  # Doi with Gur
            xviii = 160  # Fruits with Yogurt
            xix = 250  # Mishti Doi with Chira
            xx = 240  # Cholar Dal with Ruti

            while True:
                b = input("Enter your 1st food item: ").strip().lower()
                c = input("Enter your 2nd food item: ").strip().lower()
                d = input("Enter your 3rd food item: ").strip().lower()

                # Use a dictionary to map inputs to their calorie values
                calorie_map = {
                    "i": i, "ii": ii, "iii": iii, "iv": iv, "v": v,
                    "vi": vi, "vii": vii, "viii": viii, "ix": ix, "x": x,
                    "xi": xi, "xii": xii, "xiii": xiii, "xiv": xiv,
                    "xv": xv, "xvi": xvi, "xvii": xvii, "xviii": xviii,
                    "xix": xix, "xx": xx
                }

                if b in calorie_map and c in calorie_map and d in calorie_map:
                    calorie_b = calorie_map[b]
                    calorie_c = calorie_map[c]
                    calorie_d = calorie_map[d]
                    total_calories = calorie_b + calorie_c + calorie_d

                    print(f"The amount of calories for {b} is {calorie_b}, for {c} is {calorie_c} and for {d} is {calorie_d}.")
                    print(f"The total amount of calories is {total_calories}.")
                    print("-----------------------------------------")
                    print("Thank you so much!")
                    break
                else:
                    print("Invalid input, please try again.")
    elif item == '4':
        print('''    - Paratha with Chutney -- I  
        - Panta Bhat -- II  
        - Chirer Pulao -- III  
        - Muri with Gur -- IV  
        - Muri with Banana -- V  
        - Bread and Banana -- VI  
        - Shingara -- VII  
        - Sujir Halwa -- VIII  
        - Khirsa -- IX  
        - Luchi with Aloo Tarkari -- X  
        - Roti with Honey -- XI  
        - Egg Toast -- XII  
        - Chola Bhuna -- XIII  
        - Dal Puri -- XIV  
        - Puffed Rice with Mustard Oil -- XV  
        - Sweet Pitha -- XVI  
        - Doi with Gur -- XVII  
        - Fruits with Yogurt -- XVIII  
        - Mishti Doi with Chira -- XIX  
        - Cholar Dal with Ruti -- XX  ''')
        while True:
            i = 180  # Paratha with Chutney
            ii = 160  # Panta Bhat
            iii = 250  # Chirer Pulao
            iv = 170  # Muri with Gur
            v = 200  # Muri with Banana
            vi = 160  # Bread and Banana
            vii = 130  # Shingara
            viii = 200  # Sujir Halwa
            ix = 180  # Khirsa
            x = 200  # Luchi with Aloo Tarkari
            xi = 180  # Roti with Honey
            xii = 140  # Egg Toast
            xiii = 150  # Chola Bhuna
            xiv = 150  # Dal Puri
            xv = 230  # Puffed Rice with Mustard Oil
            xvi = 150  # Sweet Pitha
            xvii = 160  # Doi with Gur
            xviii = 160  # Fruits with Yogurt
            xix = 250  # Mishti Doi with Chira
            xx = 240  # Cholar Dal with Ruti

            while True:
                b = input("Enter your 1st food item: ").strip().lower()
                c = input("Enter your 2nd food item: ").strip().lower()
                d = input("Enter your 3rd food item: ").strip().lower()
                e = input("Enter your 4th food item: ").strip().lower()

                # Use a dictionary to map inputs to their calorie values
                calorie_map = {
                    "i": i, "ii": ii, "iii": iii, "iv": iv, "v": v,
                    "vi": vi, "vii": vii, "viii": viii, "ix": ix, "x": x,
                    "xi": xi, "xii": xii, "xiii": xiii, "xiv": xiv,
                    "xv": xv, "xvi": xvi, "xvii": xvii, "xviii": xviii,
                    "xix": xix, "xx": xx
                }

                if b in calorie_map and c in calorie_map and d in calorie_map and e in calorie_map:
                    calorie_b = calorie_map[b]
                    calorie_c = calorie_map[c]
                    calorie_d = calorie_map[d]
                    calorie_e = calorie_map[e]
                    total_calories = calorie_b + calorie_c + calorie_d + calorie_e

                    print(
                        f"The amount of calories for {b} is {calorie_b}, for {c} is {calorie_c}, for {d} is {calorie_d} and for {e} is {calorie_e}.")
                    print(f"The total amount of calories is {total_calories}.")
                    print("-----------------------------------------")
                    print("Thank you so much!")
                    break
                else:
                    print("Invalid input, please try again.")
    elif item == '5':
        print('''    - Paratha with Chutney -- I  
        - Panta Bhat -- II  
        - Chirer Pulao -- III  
        - Muri with Gur -- IV  
        - Muri with Banana -- V  
        - Bread and Banana -- VI  
        - Shingara -- VII  
        - Sujir Halwa -- VIII  
        - Khirsa -- IX  
        - Luchi with Aloo Tarkari -- X  
        - Roti with Honey -- XI  
        - Egg Toast -- XII  
        - Chola Bhuna -- XIII  
        - Dal Puri -- XIV  
        - Puffed Rice with Mustard Oil -- XV  
        - Sweet Pitha -- XVI  
        - Doi with Gur -- XVII  
        - Fruits with Yogurt -- XVIII  
        - Mishti Doi with Chira -- XIX  
        - Cholar Dal with Ruti -- XX  ''')
        while True:
            i = 180  # Paratha with Chutney
            ii = 160  # Panta Bhat
            iii = 250  # Chirer Pulao
            iv = 170  # Muri with Gur
            v = 200  # Muri with Banana
            vi = 160  # Bread and Banana
            vii = 130  # Shingara
            viii = 200  # Sujir Halwa
            ix = 180  # Khirsa
            x = 200  # Luchi with Aloo Tarkari
            xi = 180  # Roti with Honey
            xii = 140  # Egg Toast
            xiii = 150  # Chola Bhuna
            xiv = 150  # Dal Puri
            xv = 230  # Puffed Rice with Mustard Oil
            xvi = 150  # Sweet Pitha
            xvii = 160  # Doi with Gur
            xviii = 160  # Fruits with Yogurt
            xix = 250  # Mishti Doi with Chira
            xx = 240  # Cholar Dal with Ruti

            while True:
                b = input("Enter your 1st food item: ").strip().lower()
                c = input("Enter your 2nd food item: ").strip().lower()
                d = input("Enter your 3rd food item: ").strip().lower()
                e = input("Enter your 4th food item: ").strip().lower()
                f = input("Enter your 5th food item: ").strip().lower()

                # Use a dictionary to map inputs to their calorie values
                calorie_map = {
                    "i": i, "ii": ii, "iii": iii, "iv": iv, "v": v,
                    "vi": vi, "vii": vii, "viii": viii, "ix": ix, "x": x,
                    "xi": xi, "xii": xii, "xiii": xiii, "xiv": xiv,
                    "xv": xv, "xvi": xvi, "xvii": xvii, "xviii": xviii,
                    "xix": xix, "xx": xx
                }

                if b in calorie_map and c in calorie_map and d in calorie_map and e in calorie_map and f in calorie_map:
                    calorie_b = calorie_map[b]
                    calorie_c = calorie_map[c]
                    calorie_d = calorie_map[d]
                    calorie_e = calorie_map[e]
                    calorie_f = calorie_map[f]
                    total_calories = calorie_b + calorie_c + calorie_d + calorie_e + calorie_f

                    print(
                        f"The amount of calories for {b} is {calorie_b}, for {c} is {calorie_c}, for {d} is {calorie_d}, for {e} is {calorie_e}and for {f} is {calorie_f}.")
                    print(f"The total amount of calories is {total_calories}.")
                    print("-----------------------------------------")
                    print("Thank you so much!")
                    break
                else:
                    print("Invalid input, please try again.")
elif a == '2':
    if item =='1':
        print('''Plain Rice with Dal -- I
    Bhuna Khichuri -- II
    Panta Bhat with Fried Hilsa Fish -- III
    Shorshe Ilish -- IV
    Begun Bharta -- V
    Alu Bharta -- VI
    Shutki Bhuna -- VII
    Chingri Malai Curry -- VIII
    Dim Curry -- IX
    Rui Machher Jhol -- X
    Chicken Curry -- XI
    Beef Tehari -- XII
    Kacchi Biryani -- XIII
    Shada Bhat with Shak -- XIV
    Beef Rezala -- XV
    Chanar Dalna -- XVI
    Fried Fish with Rice -- XVII
    Murgir Roast with Polao -- XVIII
    Shutki Bharta -- XIX
    Seasonal Vegetables Stir-Fry -- XX''')
        while True:
            b = input("Enter your food item (use Roman numerals i-xx): ")
            i = "Plain Rice with Dal"
            ii = "Bhuna Khichuri"
            iii = "Panta Bhat with Fried Hilsa Fish"
            iv = "Shorshe Ilish"
            v = "Begun Bharta"
            vi = "Alu Bharta"
            vii = "Shutki Bhuna"
            viii = "Chingri Malai Curry"
            ix = "Dim Curry"
            x = "Rui Machher Jhol"
            xi = "Chicken Curry"
            xii = "Beef Tehari"
            xiii = "Kacchi Biryani"
            xiv = "Shada Bhat with Shak"
            xv = "Beef Rezala"
            xvi = "Chanar Dalna"
            xvii = "Fried Fish with Rice"
            xviii = "Murgir Roast with Polao"
            xix = "Shutki Bharta"
            xx = "Seasonal Vegetables Stir-Fry"

            if b == 'i':
                print("Plain Rice with Dal -- 350 calories")
            elif b == 'ii':
                print("Bhuna Khichuri -- 400 calories")
            elif b == 'iii':
                print("Panta Bhat with Fried Hilsa Fish -- 500 calories")
            elif b == 'iv':
                print("Shorshe Ilish -- 300 calories")
            elif b == 'v':
                print("Begun Bharta -- 100 calories")
            elif b == 'vi':
                print("Alu Bharta -- 150 calories")
            elif b == 'vii':
                print("Shutki Bhuna -- 200 calories")
            elif b == 'viii':
                print("Chingri Malai Curry -- 350 calories")
            elif b == 'ix':
                print("Dim Curry -- 250 calories")
            elif b == 'x':
                print("Rui Machher Jhol -- 200 calories")
            elif b == 'xi':
                print("Chicken Curry -- 300 calories")
            elif b == 'xii':
                print("Beef Tehari -- 550 calories")
            elif b == 'xiii':
                print("Kacchi Biryani -- 650 calories")
            elif b == 'xiv':
                print("Shada Bhat with Shak -- 250 calories")
            elif b == 'xv':
                print("Beef Rezala -- 400 calories")
            elif b == 'xvi':
                print("Chanar Dalna -- 300 calories")
            elif b == 'xvii':
                print("Fried Fish with Rice -- 400 calories")
            elif b == 'xviii':
                print("Murgir Roast with Polao -- 600 calories")
            elif b == 'xix':
                print("Shutki Bharta -- 150 calories")
            elif b == 'xx':
                print("Seasonal Vegetables Stir-Fry -- 150 calories")
            else:
                print("Invalid input! Please try again.")
                continue

            print("Thank you so much")
            print("Have a nice day")
            break
    elif item =='2':
        print('''
            - Plain Rice with Dal -- I
            - Bhuna Khichuri -- II
            - Panta Bhat with Fried Hilsa Fish -- III
            - Shorshe Ilish -- IV
            - Begun Bharta -- V
            - Alu Bharta -- VI
            - Shutki Bhuna -- VII
            - Chingri Malai Curry -- VIII
            - Dim Curry -- IX
            - Rui Machher Jhol -- X
            - Chicken Curry -- XI
            - Beef Tehari -- XII
            - Kacchi Biryani -- XIII
            - Shada Bhat with Shak -- XIV
            - Beef Rezala -- XV
            - Chanar Dalna -- XVI
            - Fried Fish with Rice -- XVII
            - Murgir Roast with Polao -- XVIII
            - Shutki Bharta -- XIX
            - Seasonal Vegetables Stir-Fry -- XX
        ''')

        while True:
            # Define calorie values
            i = 350  # Plain Rice with Dal
            ii = 400  # Bhuna Khichuri
            iii = 500  # Panta Bhat with Fried Hilsa Fish
            iv = 300  # Shorshe Ilish
            v = 100  # Begun Bharta
            vi = 150  # Alu Bharta
            vii = 200  # Shutki Bhuna
            viii = 350  # Chingri Malai Curry
            ix = 250  # Dim Curry
            x = 200  # Rui Machher Jhol
            xi = 300  # Chicken Curry
            xii = 550  # Beef Tehari
            xiii = 650  # Kacchi Biryani
            xiv = 250  # Shada Bhat with Shak
            xv = 400  # Beef Rezala
            xvi = 300  # Chanar Dalna
            xvii = 400  # Fried Fish with Rice
            xviii = 600  # Murgir Roast with Polao
            xix = 150  # Shutki Bharta
            xx = 150  # Seasonal Vegetables Stir-Fry

            # Input from user
            b = input("Enter your 1st food item: ").strip().lower()
            c = input("Enter your 2nd food item: ").strip().lower()

            # Mapping calories to inputs
            calorie_map = {
                "i": i, "ii": ii, "iii": iii, "iv": iv, "v": v,
                "vi": vi, "vii": vii, "viii": viii, "ix": ix, "x": x,
                "xi": xi, "xii": xii, "xiii": xiii, "xiv": xiv,
                "xv": xv, "xvi": xvi, "xvii": xvii, "xviii": xviii,
                "xix": xix, "xx": xx
            }

            if b in calorie_map and c in calorie_map:
                calorie_b = calorie_map[b]
                calorie_c = calorie_map[c]
                total_calories = calorie_b + calorie_c

                print(f"The amount of calories for {b} is {calorie_b}, and for {c} is {calorie_c}.")
                print(f"The total amount of calories is {total_calories}.")
                print("-----------------------------------------")
                print("Thank you so much!")
                break
            else:
                print("Invalid input, please try again.")
    elif item =='3':
        print('''    - Plain Rice with Dal -- I
                - Bhuna Khichuri -- II
                - Panta Bhat with Fried Hilsa Fish -- III
                - Shorshe Ilish -- IV
                - Begun Bharta -- V
                - Alu Bharta -- VI
                - Shutki Bhuna -- VII
                - Chingri Malai Curry -- VIII
                - Dim Curry -- IX
                - Rui Machher Jhol -- X
                - Chicken Curry -- XI
                - Beef Tehari -- XII
                - Kacchi Biryani -- XIII
                - Shada Bhat with Shak -- XIV
                - Beef Rezala -- XV
                - Chanar Dalna -- XVI
                - Fried Fish with Rice -- XVII
                - Murgir Roast with Polao -- XVIII
                - Shutki Bharta -- XIX
                - Seasonal Vegetables Stir-Fry -- XX  ''')
        while True:
            i = 350  # Plain Rice with Dal
            ii = 400  # Bhuna Khichuri
            iii = 500  # Panta Bhat with Fried Hilsa Fish
            iv = 300  # Shorshe Ilish
            v = 100  # Begun Bharta
            vi = 150  # Alu Bharta
            vii = 200  # Shutki Bhuna
            viii = 350  # Chingri Malai Curry
            ix = 250  # Dim Curry
            x = 200  # Rui Machher Jhol
            xi = 300  # Chicken Curry
            xii = 550  # Beef Tehari
            xiii = 650  # Kacchi Biryani
            xiv = 250  # Shada Bhat with Shak
            xv = 400  # Beef Rezala
            xvi = 300  # Chanar Dalna
            xvii = 400  # Fried Fish with Rice
            xviii = 600  # Murgir Roast with Polao
            xix = 150  # Shutki Bharta
            xx = 150  # Seasonal Vegetables Stir-Fry

            while True:
                b = input("Enter your 1st food item: ").strip().lower()
                c = input("Enter your 2nd food item: ").strip().lower()
                d = input("Enter your 3rd food item: ").strip().lower()

                # Use a dictionary to map inputs to their calorie values
                calorie_map = {
                    "i": i, "ii": ii, "iii": iii, "iv": iv, "v": v,
                    "vi": vi, "vii": vii, "viii": viii, "ix": ix, "x": x,
                    "xi": xi, "xii": xii, "xiii": xiii, "xiv": xiv,
                    "xv": xv, "xvi": xvi, "xvii": xvii, "xviii": xviii,
                    "xix": xix, "xx": xx
                }

                if b in calorie_map and c in calorie_map and d in calorie_map:
                    calorie_b = calorie_map[b]
                    calorie_c = calorie_map[c]
                    calorie_d = calorie_map[d]
                    total_calories = calorie_b + calorie_c + calorie_d

                    print(
                        f"The amount of calories for {b} is {calorie_b}, for {c} is {calorie_c} and for {d} is {calorie_d}.")
                    print(f"The total amount of calories is {total_calories}.")
                    print("-----------------------------------------")
                    print("Thank you so much!")
                    break
                else:
                    print("Invalid input, please try again.")
    elif item == '4':
        print('''
            - Plain Rice with Dal -- I
            - Bhuna Khichuri -- II
            - Panta Bhat with Fried Hilsa Fish -- III
            - Shorshe Ilish -- IV
            - Begun Bharta -- V
            - Alu Bharta -- VI
            - Shutki Bhuna -- VII
            - Chingri Malai Curry -- VIII
            - Dim Curry -- IX
            - Rui Machher Jhol -- X
            - Chicken Curry -- XI
            - Beef Tehari -- XII
            - Kacchi Biryani -- XIII
            - Shada Bhat with Shak -- XIV
            - Beef Rezala -- XV
            - Chanar Dalna -- XVI
            - Fried Fish with Rice -- XVII
            - Murgir Roast with Polao -- XVIII
            - Shutki Bharta -- XIX
            - Seasonal Vegetables Stir-Fry -- XX
        ''')

        while True:
            i = 350  # Plain Rice with Dal
            ii = 400  # Bhuna Khichuri
            iii = 500  # Panta Bhat with Fried Hilsa Fish
            iv = 300  # Shorshe Ilish
            v = 100  # Begun Bharta
            vi = 150  # Alu Bharta
            vii = 200  # Shutki Bhuna
            viii = 350  # Chingri Malai Curry
            ix = 250  # Dim Curry
            x = 200  # Rui Machher Jhol
            xi = 300  # Chicken Curry
            xii = 550  # Beef Tehari
            xiii = 650  # Kacchi Biryani
            xiv = 250  # Shada Bhat with Shak
            xv = 400  # Beef Rezala
            xvi = 300  # Chanar Dalna
            xvii = 400  # Fried Fish with Rice
            xviii = 600  # Murgir Roast with Polao
            xix = 150  # Shutki Bharta
            xx = 150  # Seasonal Vegetables Stir-Fry

            while True:
                b = input("Enter your 1st food item: ").strip().lower()
                c = input("Enter your 2nd food item: ").strip().lower()
                d = input("Enter your 3rd food item: ").strip().lower()
                e = input("Enter your 4th food item: ").strip().lower()

                # Use a dictionary to map inputs to their calorie values
                calorie_map = {
                    "i": i, "ii": ii, "iii": iii, "iv": iv, "v": v,
                    "vi": vi, "vii": vii, "viii": viii, "ix": ix, "x": x,
                    "xi": xi, "xii": xii, "xiii": xiii, "xiv": xiv,
                    "xv": xv, "xvi": xvi, "xvii": xvii, "xviii": xviii,
                    "xix": xix, "xx": xx
                }

                if b in calorie_map and c in calorie_map and d in calorie_map and e in calorie_map:
                    calorie_b = calorie_map[b]
                    calorie_c = calorie_map[c]
                    calorie_d = calorie_map[d]
                    calorie_e = calorie_map[e]
                    total_calories = calorie_b + calorie_c + calorie_d + calorie_e

                    print(
                        f"The amount of calories for {b} is {calorie_b}, for {c} is {calorie_c}, for {d} is {calorie_d} and for {e} is {calorie_e}.")
                    print(f"The total amount of calories is {total_calories}.")
                    print("-----------------------------------------")
                    print("Thank you so much!")
                    break
                else:
                    print("Invalid input, please try again.")
    elif item == '5':
        print('''
            - Plain Rice with Dal -- I  
            - Bhuna Khichuri -- II  
            - Panta Bhat with Fried Hilsa Fish -- III  
            - Shorshe Ilish -- IV  
            - Begun Bharta -- V  
            - Alu Bharta -- VI  
            - Shutki Bhuna -- VII  
            - Chingri Malai Curry -- VIII  
            - Dim Curry -- IX  
            - Rui Machher Jhol -- X  
            - Chicken Curry -- XI  
            - Beef Tehari -- XII  
            - Kacchi Biryani -- XIII  
            - Shada Bhat with Shak -- XIV  
            - Beef Rezala -- XV  
            - Chanar Dalna -- XVI  
            - Fried Fish with Rice -- XVII  
            - Murgir Roast with Polao -- XVIII  
            - Shutki Bharta -- XIX  
            - Seasonal Vegetables Stir-Fry -- XX  ''')

        while True:
            i = 350  # Plain Rice with Dal
            ii = 400  # Bhuna Khichuri
            iii = 500  # Panta Bhat with Fried Hilsa Fish
            iv = 300  # Shorshe Ilish
            v = 100  # Begun Bharta
            vi = 150  # Alu Bharta
            vii = 200  # Shutki Bhuna
            viii = 350  # Chingri Malai Curry
            ix = 250  # Dim Curry
            x = 200  # Rui Machher Jhol
            xi = 300  # Chicken Curry
            xii = 550  # Beef Tehari
            xiii = 650  # Kacchi Biryani
            xiv = 250  # Shada Bhat with Shak
            xv = 400  # Beef Rezala
            xvi = 300  # Chanar Dalna
            xvii = 400  # Fried Fish with Rice
            xviii = 600  # Murgir Roast with Polao
            xix = 150  # Shutki Bharta
            xx = 150  # Seasonal Vegetables Stir-Fry

            while True:
                b = input("Enter your 1st food item: ").strip().lower()
                c = input("Enter your 2nd food item: ").strip().lower()
                d = input("Enter your 3rd food item: ").strip().lower()
                e = input("Enter your 4th food item: ").strip().lower()
                f = input("Enter your 5th food item: ").strip().lower()

                # Use a dictionary to map inputs to their calorie values
                calorie_map = {
                    "i": i, "ii": ii, "iii": iii, "iv": iv, "v": v,
                    "vi": vi, "vii": vii, "viii": viii, "ix": ix, "x": x,
                    "xi": xi, "xii": xii, "xiii": xiii, "xiv": xiv,
                    "xv": xv, "xvi": xvi, "xvii": xvii, "xviii": xviii,
                    "xix": xix, "xx": xx
                }

                if b in calorie_map and c in calorie_map and d in calorie_map and e in calorie_map and f in calorie_map:
                    calorie_b = calorie_map[b]
                    calorie_c = calorie_map[c]
                    calorie_d = calorie_map[d]
                    calorie_e = calorie_map[e]
                    calorie_f = calorie_map[f]
                    total_calories = calorie_b + calorie_c + calorie_d + calorie_e + calorie_f

                    print(
                        f"The amount of calories for {b} is {calorie_b}, for {c} is {calorie_c}, for {d} is {calorie_d}, for {e} is {calorie_e}and for {f} is {calorie_f}.")
                    print(f"The total amount of calories is {total_calories}.")
                    print("-----------------------------------------")
                    print("Thank you so much!")
                    break
                else:
                    print("Invalid input, please try again.")
elif a == '3':
    if item == '1':
        print('''Plain Rice with Dal -- I
        Bhuna Khichuri -- II
        Panta Bhat with Fried Hilsa Fish -- III
        Shorshe Ilish -- IV
        Begun Bharta -- V
        Alu Bharta -- VI
        Shutki Bhuna -- VII
        Chingri Malai Curry -- VIII
        Dim Curry -- IX
        Rui Machher Jhol -- X
        Chicken Curry -- XI
        Beef Tehari -- XII
        Kacchi Biryani -- XIII
        Shada Bhat with Shak -- XIV
        Beef Rezala -- XV
        Chanar Dalna -- XVI
        Fried Fish with Rice -- XVII
        Murgir Roast with Polao -- XVIII
        Shutki Bharta -- XIX
        Seasonal Vegetables Stir-Fry -- XX''')

        while True:
            b = input("Enter your food item (use Roman numerals i-xx): ").lower()

            if b == 'i':
                print("Plain Rice with Dal -- 350 calories")
            elif b == 'ii':
                print("Bhuna Khichuri -- 400 calories")
            elif b == 'iii':
                print("Panta Bhat with Fried Hilsa Fish -- 500 calories")
            elif b == 'iv':
                print("Shorshe Ilish -- 300 calories")
            elif b == 'v':
                print("Begun Bharta -- 100 calories")
            elif b == 'vi':
                print("Alu Bharta -- 150 calories")
            elif b == 'vii':
                print("Shutki Bhuna -- 200 calories")
            elif b == 'viii':
                print("Chingri Malai Curry -- 350 calories")
            elif b == 'ix':
                print("Dim Curry -- 250 calories")
            elif b == 'x':
                print("Rui Machher Jhol -- 200 calories")
            elif b == 'xi':
                print("Chicken Curry -- 300 calories")
            elif b == 'xii':
                print("Beef Tehari -- 550 calories")
            elif b == 'xiii':
                print("Kacchi Biryani -- 650 calories")
            elif b == 'xiv':
                print("Shada Bhat with Shak -- 250 calories")
            elif b == 'xv':
                print("Beef Rezala -- 400 calories")
            elif b == 'xvi':
                print("Chanar Dalna -- 300 calories")
            elif b == 'xvii':
                print("Fried Fish with Rice -- 400 calories")
            elif b == 'xviii':
                print("Murgir Roast with Polao -- 600 calories")
            elif b == 'xix':
                print("Shutki Bharta -- 150 calories")
            elif b == 'xx':
                print("Seasonal Vegetables Stir-Fry -- 150 calories")
            else:
                print("Invalid input! Please try again.")
                continue

            print("Thank you so much")
            print("Have a nice day")
            break
    elif item == '2':
        print('''
            - Plain Rice with Dal -- I
            - Bhuna Khichuri -- II
            - Panta Bhat with Fried Hilsa Fish -- III
            - Shorshe Ilish -- IV
            - Begun Bharta -- V
            - Alu Bharta -- VI
            - Shutki Bhuna -- VII
            - Chingri Malai Curry -- VIII
            - Dim Curry -- IX
            - Rui Machher Jhol -- X
            - Chicken Curry -- XI
            - Beef Tehari -- XII
            - Kacchi Biryani -- XIII
            - Shada Bhat with Shak -- XIV
            - Beef Rezala -- XV
            - Chanar Dalna -- XVI
            - Fried Fish with Rice -- XVII
            - Murgir Roast with Polao -- XVIII
            - Shutki Bharta -- XIX
            - Seasonal Vegetables Stir-Fry -- XX
        ''')

        while True:
            # Define calorie values using "text-2"
            calorie_map = {
                "i": 350,  # Plain Rice with Dal
                "ii": 400,  # Bhuna Khichuri
                "iii": 500,  # Panta Bhat with Fried Hilsa Fish
                "iv": 300,  # Shorshe Ilish
                "v": 100,  # Begun Bharta
                "vi": 150,  # Alu Bharta
                "vii": 200,  # Shutki Bhuna
                "viii": 350,  # Chingri Malai Curry
                "ix": 250,  # Dim Curry
                "x": 200,  # Rui Machher Jhol
                "xi": 300,  # Chicken Curry
                "xii": 550,  # Beef Tehari
                "xiii": 650,  # Kacchi Biryani
                "xiv": 250,  # Shada Bhat with Shak
                "xv": 400,  # Beef Rezala
                "xvi": 300,  # Chanar Dalna
                "xvii": 400,  # Fried Fish with Rice
                "xviii": 600,  # Murgir Roast with Polao
                "xix": 150,  # Shutki Bharta
                "xx": 150  # Seasonal Vegetables Stir-Fry
            }

            # Input from user
            b = input("Enter your 1st food item (use Roman numerals I-XX): ").strip().lower()
            c = input("Enter your 2nd food item (use Roman numerals I-XX): ").strip().lower()

            if b in calorie_map and c in calorie_map:
                calorie_b = calorie_map[b]
                calorie_c = calorie_map[c]
                total_calories = calorie_b + calorie_c

                print(f"The amount of calories for {b.upper()} is {calorie_b}, and for {c.upper()} is {calorie_c}.")
                print(f"The total amount of calories is {total_calories}.")
                print("-----------------------------------------")
                print("Thank you so much!")
                break
            else:
                print("Invalid input, please try again.")
    elif item == '3':
        print('''    - Plain Rice with Dal -- I
                        - Bhuna Khichuri -- II
                        - Panta Bhat with Fried Hilsa Fish -- III
                        - Shorshe Ilish -- IV
                        - Begun Bharta -- V
                        - Alu Bharta -- VI
                        - Shutki Bhuna -- VII
                        - Chingri Malai Curry -- VIII
                        - Dim Curry -- IX
                        - Rui Machher Jhol -- X
                        - Chicken Curry -- XI
                        - Beef Tehari -- XII
                        - Kacchi Biryani -- XIII
                        - Shada Bhat with Shak -- XIV
                        - Beef Rezala -- XV
                        - Chanar Dalna -- XVI
                        - Fried Fish with Rice -- XVII
                        - Murgir Roast with Polao -- XVIII
                        - Shutki Bharta -- XIX
                        - Seasonal Vegetables Stir-Fry -- XX  ''')

        while True:
            # Use a dictionary to map Roman numerals to their respective calorie values from "text-2"
            calorie_map = {
                "i": 350,  # Plain Rice with Dal
                "ii": 400,  # Bhuna Khichuri
                "iii": 500,  # Panta Bhat with Fried Hilsa Fish
                "iv": 300,  # Shorshe Ilish
                "v": 100,  # Begun Bharta
                "vi": 150,  # Alu Bharta
                "vii": 200,  # Shutki Bhuna
                "viii": 350,  # Chingri Malai Curry
                "ix": 250,  # Dim Curry
                "x": 200,  # Rui Machher Jhol
                "xi": 300,  # Chicken Curry
                "xii": 550,  # Beef Tehari
                "xiii": 650,  # Kacchi Biryani
                "xiv": 250,  # Shada Bhat with Shak
                "xv": 400,  # Beef Rezala
                "xvi": 300,  # Chanar Dalna
                "xvii": 400,  # Fried Fish with Rice
                "xviii": 600,  # Murgir Roast with Polao
                "xix": 150,  # Shutki Bharta
                "xx": 150  # Seasonal Vegetables Stir-Fry
            }

            # Get inputs from the user
            b = input("Enter your 1st food item (Roman numerals i-xx): ").strip().lower()
            c = input("Enter your 2nd food item (Roman numerals i-xx): ").strip().lower()
            d = input("Enter your 3rd food item (Roman numerals i-xx): ").strip().lower()

            if b in calorie_map and c in calorie_map and d in calorie_map:
                calorie_b = calorie_map[b]
                calorie_c = calorie_map[c]
                calorie_d = calorie_map[d]
                total_calories = calorie_b + calorie_c + calorie_d

                print(
                    f"The calories for {b.upper()} is {calorie_b}, for {c.upper()} is {calorie_c}, and for {d.upper()} is {calorie_d}.")
                print(f"The total amount of calories is {total_calories}.")
                print("-----------------------------------------")
                print("Thank you so much!")
                break
            else:
                print("Invalid input, please try again.")
    elif item == '4':
        print('''
                    - Plain Rice with Dal -- I
                    - Bhuna Khichuri -- II
                    - Panta Bhat with Fried Hilsa Fish -- III
                    - Shorshe Ilish -- IV
                    - Begun Bharta -- V
                    - Alu Bharta -- VI
                    - Shutki Bhuna -- VII
                    - Chingri Malai Curry -- VIII
                    - Dim Curry -- IX
                    - Rui Machher Jhol -- X
                    - Chicken Curry -- XI
                    - Beef Tehari -- XII
                    - Kacchi Biryani -- XIII
                    - Shada Bhat with Shak -- XIV
                    - Beef Rezala -- XV
                    - Chanar Dalna -- XVI
                    - Fried Fish with Rice -- XVII
                    - Murgir Roast with Polao -- XVIII
                    - Shutki Bharta -- XIX
                    - Seasonal Vegetables Stir-Fry -- XX
                ''')

        while True:
            # Dictionary to map items with their calorie values
            calorie_map = {
                "i": 350,  # Plain Rice with Dal
                "ii": 400,  # Bhuna Khichuri
                "iii": 500,  # Panta Bhat with Fried Hilsa Fish
                "iv": 300,  # Shorshe Ilish
                "v": 100,  # Begun Bharta
                "vi": 150,  # Alu Bharta
                "vii": 200,  # Shutki Bhuna
                "viii": 350,  # Chingri Malai Curry
                "ix": 250,  # Dim Curry
                "x": 200,  # Rui Machher Jhol
                "xi": 300,  # Chicken Curry
                "xii": 550,  # Beef Tehari
                "xiii": 650,  # Kacchi Biryani
                "xiv": 250,  # Shada Bhat with Shak
                "xv": 400,  # Beef Rezala
                "xvi": 300,  # Chanar Dalna
                "xvii": 400,  # Fried Fish with Rice
                "xviii": 600,  # Murgir Roast with Polao
                "xix": 150,  # Shutki Bharta
                "xx": 150  # Seasonal Vegetables Stir-Fry
            }

            b = input("Enter your 1st food item (use Roman numerals i-xx): ").strip().lower()
            c = input("Enter your 2nd food item (use Roman numerals i-xx): ").strip().lower()
            d = input("Enter your 3rd food item (use Roman numerals i-xx): ").strip().lower()
            e = input("Enter your 4th food item (use Roman numerals i-xx): ").strip().lower()

            if b in calorie_map and c in calorie_map and d in calorie_map and e in calorie_map:
                calorie_b = calorie_map[b]
                calorie_c = calorie_map[c]
                calorie_d = calorie_map[d]
                calorie_e = calorie_map[e]
                total_calories = calorie_b + calorie_c + calorie_d + calorie_e

                print(
                    f"The amount of calories for {b} is {calorie_b}, for {c} is {calorie_c}, for {d} is {calorie_d} and for {e} is {calorie_e}.")
                print(f"The total amount of calories is {total_calories}.")
                print("-----------------------------------------")
                print("Thank you so much!")
                break
            else:
                print("Invalid input, please try again.")
    elif item == '5':
        print('''
                    - Plain Rice with Dal -- I  
                    - Bhuna Khichuri -- II  
                    - Panta Bhat with Fried Hilsa Fish -- III  
                    - Shorshe Ilish -- IV  
                    - Begun Bharta -- V  
                    - Alu Bharta -- VI  
                    - Shutki Bhuna -- VII  
                    - Chingri Malai Curry -- VIII  
                    - Dim Curry -- IX  
                    - Rui Machher Jhol -- X  
                    - Chicken Curry -- XI  
                    - Beef Tehari -- XII  
                    - Kacchi Biryani -- XIII  
                    - Shada Bhat with Shak -- XIV  
                    - Beef Rezala -- XV  
                    - Chanar Dalna -- XVI  
                    - Fried Fish with Rice -- XVII  
                    - Murgir Roast with Polao -- XVIII  
                    - Shutki Bharta -- XIX  
                    - Seasonal Vegetables Stir-Fry -- XX  
        ''')

        while True:
            # Define calorie values using a dictionary
            calorie_map = {
                "i": 350,  # Plain Rice with Dal
                "ii": 400,  # Bhuna Khichuri
                "iii": 500,  # Panta Bhat with Fried Hilsa Fish
                "iv": 300,  # Shorshe Ilish
                "v": 100,  # Begun Bharta
                "vi": 150,  # Alu Bharta
                "vii": 200,  # Shutki Bhuna
                "viii": 350,  # Chingri Malai Curry
                "ix": 250,  # Dim Curry
                "x": 200,  # Rui Machher Jhol
                "xi": 300,  # Chicken Curry
                "xii": 550,  # Beef Tehari
                "xiii": 650,  # Kacchi Biryani
                "xiv": 250,  # Shada Bhat with Shak
                "xv": 400,  # Beef Rezala
                "xvi": 300,  # Chanar Dalna
                "xvii": 400,  # Fried Fish with Rice
                "xviii": 600,  # Murgir Roast with Polao
                "xix": 150,  # Shutki Bharta
                "xx": 150  # Seasonal Vegetables Stir-Fry
            }

            # Get inputs for food items
            b = input("Enter your 1st food item: ").strip().lower()
            c = input("Enter your 2nd food item: ").strip().lower()
            d = input("Enter your 3rd food item: ").strip().lower()
            e = input("Enter your 4th food item: ").strip().lower()
            f = input("Enter your 5th food item: ").strip().lower()

            # Validate inputs and calculate total calories
            if b in calorie_map and c in calorie_map and d in calorie_map and e in calorie_map and f in calorie_map:
                calorie_b = calorie_map[b]
                calorie_c = calorie_map[c]
                calorie_d = calorie_map[d]
                calorie_e = calorie_map[e]
                calorie_f = calorie_map[f]
                total_calories = calorie_b + calorie_c + calorie_d + calorie_e + calorie_f

                print(
                    f"The amount of calories for {b.upper()} is {calorie_b}, for {c.upper()} is {calorie_c}, for {d.upper()} is {calorie_d}, for {e.upper()} is {calorie_e}, and for {f.upper()} is {calorie_f}."
                )
                print(f"The total amount of calories is {total_calories}.")
                print("-----------------------------------------")
                print("Thank you so much!")
                break
            else:
                print("Invalid input, please try again.")


#Thank you so much