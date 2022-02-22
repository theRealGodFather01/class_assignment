import itemsList
import milk
import beverage
import cereal
import vegetable
import lotion
import perfume
import fruit
import detergent
import biscuit
import wine

print("Hello, welcome to our store.")
print("Are you Male or Female? M/F")
gender=input()
gender=gender.upper()
if gender=="M":
    print("Welcome Comrade, here are the list of item categories we have for you:")
    print(itemsList.mlk)
    print(itemsList.bvrg)
    print(itemsList.crl)
    print(itemsList.veg)
    print(itemsList.ltn)
    print(itemsList.prfm)
    print(itemsList.frt)
    print(itemsList.dtgt)
    print(itemsList.bsct)
    print(itemsList.wne)
    print("Which of the categories would you be selecting today Comrade?")
    itemCat=input()
    itemCat=itemCat.upper()

    if itemCat=="MILK":
        print("Which of the Milks Comrade?")
        print("We have:")
        print(milk.itemOne)
        print(milk.itemTwo)
        print(milk.itemThree)
        print(milk.itemFour)
        print(milk.itemFive)
        item=input()
        item=item.upper()

        if item=="PEAK MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.peakMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.peakMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="DANO MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.danoMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.danoMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="THREE CROWNS MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.threeCrownsMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.threeCrownsMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="MIKSI MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.miksiMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.miksiMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="COWBELL MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.cowbellMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.cowbellMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="BEVERAGE":
        print("Which of the Beverages Comrade?")
        print("We have:")
        print(beverage.itemOne)
        print(beverage.itemTwo)
        print(beverage.itemThree)
        print(beverage.itemFour)
        item=input()
        item=item.upper()

        if item=="PEAK CHOCO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.peakChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.peakChoco," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BOURNVITA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.bournvita
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.bournvita," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="HOT CHOCO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.hotChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.hotChoco," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="COWBELL CHOCO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.cowbellChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.cowbellChoco," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="CEREAL":
        print("Which of the Cereals Comrade?")
        print("We have:")
        print(cereal.itemOne)
        print(cereal.itemTwo)
        print(cereal.itemThree)
        item=input()
        item=item.upper()
        if item=="CERELAC":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.cerelac
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.cerelac," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="GOLDEN MORN":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.goldenMorn
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.goldenMorn," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="WHEAT MEAL":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.wheatMeal
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.wheatMeal," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="VEGETABLES":
        print("Which of the Vegetables Comrade?")
        print("We have:")
        print(vegetable.itemOne)
        print(vegetable.itemTwo)
        print(vegetable.itemThree)
        print(vegetable.itemFour)
        print(vegetable.itemFive)
        print(vegetable.itemSix)
        print(vegetable.itemSeven)
        item=input()
        item=item.upper()

        if item=="CABBAGE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.cabbage
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.cabbage," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="SPINACH":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.spinach
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.spinach," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="CARROT":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.carrot
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.carrot," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="GREEN BEANS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.greenBeans
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.greenBeans," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="GREEN PEAS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.greenPeas
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.greenPeas," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="CUCUMBER":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.cucumber
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.cucumber," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="ONIONS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.onions
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.onions," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="LOTION":
        print("Which of the Lotions Comrade?")
        print("We have:")
        print(lotion.itemOne)
        print(lotion.itemTwo)
        print(lotion.itemThree)
        print(lotion.itemFour)
        print(lotion.itemFive)
        item=input()
        item=item.upper()

        if item=="CUSSONS BABY":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.cussonsBaby
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.cussonsBaby," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="PEARS BABY":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.pearsBaby
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.pearsBaby," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BRONZ TONE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.bronzTone
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.bronzTone," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="NIVEA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.nivea
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.nivea," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="VASELINE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.vaseline
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.vaseline," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="PERFUME":
        print("Which of the Perfumes Comrade?")
        print("We have:")
        print(lotion.itemOne)
        print(lotion.itemTwo)
        print(lotion.itemThree)
        print(lotion.itemFour)
        print(lotion.itemFive)
        print(lotion.itemSix)
        item=input()
        item=item.upper()

        if item=="SMART COLLECTION":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.smartCollection
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.smartCollection," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="TONY MONTANA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.tonyMontana
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.tonyMontana," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="INSPIRATION":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.inspiration
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.inspiration," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="TEMPTATION":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.temptation
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.temptation," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="EMERGENCY":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.emergency
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.emergency," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="ONE BILLION":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.oneBillion
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.oneBillion," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="FRUIT":
        print("Which of the Fruits Comrade?")
        print("We have:")
        print(fruit.itemOne)
        print(fruit.itemTwo)
        print(fruit.itemThree)
        print(fruit.itemFour)
        print(fruit.itemFive)
        item=input()
        item=item.upper()

        if item=="PINEAPPLE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.pineapple
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.pineapple," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="APPLE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.apple
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.apple," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="WATERMELON":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.watermelon
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.watermelon," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BANANA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.banana
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.banana," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="AVOCADO PEAR":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.avocadoPear
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.avocadoPear," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="DETERGENT":
        print("Which of the Detergents Comrade?")
        print("We have:")
        print(detergent.itemOne)
        print(detergent.itemTwo)
        print(detergent.itemThree)
        print(detergent.itemFour)
        print(detergent.itemFive)
        print(detergent.itemSix)
        item=input()
        item=item.upper()

        if item=="OMO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.omo
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.omo," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="ARIEL":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.ariel
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.ariel," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="KLIN":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.klin
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.klin," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="WAW":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.waw
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.waw," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="GOOD MAMA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.goodMama
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.goodMama," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="VIVA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.viva
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.viva," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="BISCUIT":
        print("Which of the Biscuits Comrade?")
        print("We have:")
        print(biscuit.itemOne)
        print(biscuit.itemTwo)
        print(biscuit.itemThree)
        print(biscuit.itemFour)
        print(biscuit.itemFive)
        print(biscuit.itemSix)
        item=input()
        item=item.upper()

        if item=="DIGESTIVE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.digestive
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.digestive," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="CHOCOLATE RINGS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.chocolateRings
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.chocolateRings," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="OREO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.oreo
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.oreo," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BELOXXY":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.beloxxy
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.beloxxy," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="MCVITES":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.mcVites
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.mcVites," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="YALE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.yale
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.yale," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="WINE":
        print("Which of the Wines Comrade?")
        print("We have:")
        print(wine.itemOne)
        print(wine.itemTwo)
        print(wine.itemThree)
        print(wine.itemFour)
        print(wine.itemFive)
        print(wine.itemSix)
        item=input()
        item=item.upper()

        if item=="FOUR COUSINS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.fourCousins
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.fourCousins," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="RED GRAPE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.redGrape
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.redGrape," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="CARLO ROSSI":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.carloRossi
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.carloRossi," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="PURE HEAVEN":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.pureHeaven
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.pureHeaven," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="DON SIMON":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.donSimon
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.donSimon," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BAILEYS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.baileys
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.baileys," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
    else:
        print("Sorry Sir we do not have that in our category, please choose any of the categories listed above")
    exit()

if gender=="F":
    print("Welcome Sweetheart, here are the list of item categories we have for you:")
    print(itemsList.mlk)
    print(itemsList.bvrg)
    print(itemsList.crl)
    print(itemsList.veg)
    print(itemsList.ltn)
    print(itemsList.prfm)
    print(itemsList.frt)
    print(itemsList.dtgt)
    print(itemsList.bsct)
    print(itemsList.wne)
    print("Which of the categories would you be selecting today Sweetheart?")
    itemCat=input()
    itemCat=itemCat.upper()

    if itemCat=="MILK":
        print("Which of the Milks Sweetheart?")
        print("We have:")
        print(milk.itemOne)
        print(milk.itemTwo)
        print(milk.itemThree)
        print(milk.itemFour)
        print(milk.itemFive)
        item=input()
        item=item.upper()

        if item=="PEAK MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.peakMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.peakMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="DANO MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.danoMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.danoMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="THREE CROWNS MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.threeCrownsMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.threeCrownsMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="MIKSI MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.miksiMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.miksiMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="COWBELL MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.cowbellMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.cowbellMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="BEVERAGE":
        print("Which of the Beverages Sweetheart?")
        print("We have:")
        print(beverage.itemOne)
        print(beverage.itemTwo)
        print(beverage.itemThree)
        print(beverage.itemFour)
        item=input()
        item=item.upper()

        if item=="PEAK CHOCO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.peakChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.peakChoco," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BOURNVITA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.bournvita
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.bournvita," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="HOT CHOCO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.hotChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.hotChoco," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="COWBELL CHOCO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.cowbellChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.cowbellChoco," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="CEREAL":
        print("Which of the Cereals Sweetheart?")
        print("We have:")
        print(cereal.itemOne)
        print(cereal.itemTwo)
        print(cereal.itemThree)
        item=input()
        item=item.upper()

        if item=="CERELAC":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.cerelac
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.cerelac," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="GOLDEN MORN":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.goldenMorn
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.goldenMorn," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="WHEAT MEAL":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.wheatMeal
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.wheatMeal," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="VEGETABLES":
        print("Which of the Vegetables Sweetheart?")
        print("We have:")
        print(vegetable.itemOne)
        print(vegetable.itemTwo)
        print(vegetable.itemThree)
        print(vegetable.itemFour)
        print(vegetable.itemFive)
        print(vegetable.itemSix)
        print(vegetable.itemSeven)
        item=input()
        item=item.upper()

        if item=="CABBAGE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.cabbage
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.cabbage," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="SPINACH":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.spinach
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.spinach," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="CARROT":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.carrot
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.carrot," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="GREEN BEANS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.greenBeans
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.greenBeans," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="GREEN PEAS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.greenPeas
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.greenPeas," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="CUCUMBER":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.cucumber
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.cucumber," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="ONIONS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.onions
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.onions," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="LOTION":
        print("Which of the Lotions Sweetheart?")
        print("We have:")
        print(lotion.itemOne)
        print(lotion.itemTwo)
        print(lotion.itemThree)
        print(lotion.itemFour)
        print(lotion.itemFive)
        item=input()
        item=item.upper()

        if item=="CUSSONS BABY":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.cussonsBaby
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.cussonsBaby," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="PEARS BABY":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.pearsBaby
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.pearsBaby," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BRONZ TONE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.bronzTone
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.bronzTone," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="NIVEA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.nivea
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.nivea," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="VASELINE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.vaseline
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.vaseline," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="PERFUME":
        print("Which of the Perfumes Sweetheart?")
        print("We have:")
        print(lotion.itemOne)
        print(lotion.itemTwo)
        print(lotion.itemThree)
        print(lotion.itemFour)
        print(lotion.itemFive)
        print(lotion.itemSix)
        item=input()
        item=item.upper()

        if item=="SMART COLLECTION":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.smartCollection
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.smartCollection," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="TONY MONTANA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.tonyMontana
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.tonyMontana," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="INSPIRATION":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.inspiration
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.inspiration," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="TEMPTATION":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.temptation
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.temptation," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="EMERGENCY":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.emergency
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.emergency," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="ONE BILLION":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.oneBillion
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.oneBillion," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="FRUIT":
        print("Which of the Fruits Sweetheart?")
        print("We have:")
        print(fruit.itemOne)
        print(fruit.itemTwo)
        print(fruit.itemThree)
        print(fruit.itemFour)
        print(fruit.itemFive)
        item=input()
        item=item.upper()

        if item=="PINEAPPLE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.pineapple
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.pineapple," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="APPLE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.apple
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.apple," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="WATERMELON":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.watermelon
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.watermelon," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BANANA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.banana
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.banana," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="AVOCADO PEAR":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.avocadoPear
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.avocadoPear," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="DETERGENT":
        print("Which of the Detergents Sweetheart?")
        print("We have:")
        print(detergent.itemOne)
        print(detergent.itemTwo)
        print(detergent.itemThree)
        print(detergent.itemFour)
        print(detergent.itemFive)
        print(detergent.itemSix)
        item=input()
        item=item.upper()

        if item=="OMO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.omo
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.omo," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="ARIEL":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.ariel
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.ariel," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="KLIN":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.klin
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.klin," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="WAW":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.waw
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.waw," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="GOOD MAMA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.goodMama
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.goodMama," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="VIVA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.viva
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.viva," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="BISCUIT":
        print("Which of the Biscuits Sweetheart?")
        print("We have:")
        print(biscuit.itemOne)
        print(biscuit.itemTwo)
        print(biscuit.itemThree)
        print(biscuit.itemFour)
        print(biscuit.itemFive)
        print(biscuit.itemSix)
        item=input()
        item=item.upper()

        if item=="DIGESTIVE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.digestive
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.digestive," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="CHOCOLATE RINGS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.chocolateRings
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.chocolateRings," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="OREO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.oreo
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.oreo," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BELOXXY":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.beloxxy
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.beloxxy," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="MCVITES":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.mcVites
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.mcVites," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="YALE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.yale
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.yale," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="WINE":
        print("Which of the Wines Sweetheart?")
        print("We have:")
        print(wine.itemOne)
        print(wine.itemTwo)
        print(wine.itemThree)
        print(wine.itemFour)
        print(wine.itemFive)
        print(wine.itemSix)
        item=input()
        item=item.upper()

        if item=="FOUR COUSINS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.fourCousins
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.fourCousins," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="RED GRAPE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.redGrape
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.redGrape," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="CARLO ROSSI":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.carloRossi
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.carloRossi," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="PURE HEAVEN":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.pureHeaven
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.pureHeaven," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="DON SIMON":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.donSimon
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.donSimon," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BAILEYS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.baileys
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.baileys," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
    else:
        print("Sorry Ma'am we do not have that in our category, please choose any of the categories listed above")
    exit()
else:
    print("Sorry we dont have a categoey for you here, thanks, do check another store")
exit()
import biscuit
import wine

print("Hello, welcome to our store.")
print("Are you Male or Female? M/F")
gender=input()
gender=gender.upper()
if gender=="M":
    print("Welcome Comrade, here are the list of item categories we have for you:")
    print(itemsList.mlk)
    print(itemsList.bvrg)
    print(itemsList.crl)
    print(itemsList.veg)
    print(itemsList.ltn)
    print(itemsList.prfm)
    print(itemsList.frt)
    print(itemsList.dtgt)
    print(itemsList.bsct)
    print(itemsList.wne)
    print("Which of the categories would you be selecting today Comrade?")
    itemCat=input()
    itemCat=itemCat.upper()

    if itemCat=="MILK":
        print("Which of the Milks Comrade?")
        print("We have:")
        print(milk.itemOne)
        print(milk.itemTwo)
        print(milk.itemThree)
        print(milk.itemFour)
        print(milk.itemFive)
        item=input()
        item=item.upper()

        if item=="PEAK MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.peakMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.peakMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="DANO MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.danoMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.danoMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="THREE CROWNS MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.threeCrownsMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.threeCrownsMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="MIKSI MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.miksiMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.miksiMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="COWBELL MILK":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.cowbellMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.cowbellMilk," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
                exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="BEVERAGE":
        print("Which of the Beverages Comrade?")
        print("We have:")
        print(beverage.itemOne)
        print(beverage.itemTwo)
        print(beverage.itemThree)
        print(beverage.itemFour)
        item=input()
        item=item.upper()

        if item=="PEAK CHOCO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.peakChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.peakChoco," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BOURNVITA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.bournvita
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.bournvita," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="HOT CHOCO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.hotChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.hotChoco," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="COWBELL CHOCO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.cowbellChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.cowbellChoco," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="CEREAL":
        print("Which of the Cereals Comrade?")
        print("We have:")
        print(cereal.itemOne)
        print(cereal.itemTwo)
        print(cereal.itemThree)
        item=input()
        item=item.upper()
        if item=="CERELAC":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.cerelac
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.cerelac," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="GOLDEN MORN":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.goldenMorn
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.goldenMorn," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="WHEAT MEAL":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.wheatMeal
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.wheatMeal," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="VEGETABLES":
        print("Which of the Vegetables Comrade?")
        print("We have:")
        print(vegetable.itemOne)
        print(vegetable.itemTwo)
        print(vegetable.itemThree)
        print(vegetable.itemFour)
        print(vegetable.itemFive)
        print(vegetable.itemSix)
        print(vegetable.itemSeven)
        item=input()
        item=item.upper()

        if item=="CABBAGE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.cabbage
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.cabbage," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="SPINACH":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.spinach
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.spinach," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="CARROT":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.carrot
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.carrot," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="GREEN BEANS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.greenBeans
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.greenBeans," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="GREEN PEAS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.greenPeas
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.greenPeas," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="CUCUMBER":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.cucumber
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.cucumber," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="ONIONS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.onions
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.onions," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="LOTION":
        print("Which of the Lotions Comrade?")
        print("We have:")
        print(lotion.itemOne)
        print(lotion.itemTwo)
        print(lotion.itemThree)
        print(lotion.itemFour)
        print(lotion.itemFive)
        item=input()
        item=item.upper()

        if item=="CUSSONS BABY":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.cussonsBaby
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.cussonsBaby," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="PEARS BABY":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.pearsBaby
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.pearsBaby," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BRONZ TONE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.bronzTone
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.bronzTone," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="NIVEA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.nivea
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.nivea," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="VASELINE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.vaseline
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.vaseline," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="PERFUME":
        print("Which of the Perfumes Comrade?")
        print("We have:")
        print(lotion.itemOne)
        print(lotion.itemTwo)
        print(lotion.itemThree)
        print(lotion.itemFour)
        print(lotion.itemFive)
        print(lotion.itemSix)
        item=input()
        item=item.upper()

        if item=="SMART COLLECTION":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.smartCollection
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.smartCollection," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="TONY MONTANA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.tonyMontana
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.tonyMontana," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="INSPIRATION":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.inspiration
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.inspiration," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="TEMPTATION":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.temptation
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.temptation," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="EMERGENCY":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.emergency
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.emergency," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="ONE BILLION":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.oneBillion
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.oneBillion," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="FRUIT":
        print("Which of the Fruits Comrade?")
        print("We have:")
        print(fruit.itemOne)
        print(fruit.itemTwo)
        print(fruit.itemThree)
        print(fruit.itemFour)
        print(fruit.itemFive)
        item=input()
        item=item.upper()

        if item=="PINEAPPLE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.pineapple
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.pineapple," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="APPLE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.apple
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.apple," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="WATERMELON":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.watermelon
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.watermelon," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BANANA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.banana
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.banana," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="AVOCADO PEAR":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.avocadoPear
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.avocadoPear," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="DETERGENT":
        print("Which of the Detergents Comrade?")
        print("We have:")
        print(detergent.itemOne)
        print(detergent.itemTwo)
        print(detergent.itemThree)
        print(detergent.itemFour)
        print(detergent.itemFive)
        print(detergent.itemSix)
        item=input()
        item=item.upper()

        if item=="OMO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.omo
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.omo," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="ARIEL":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.ariel
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.ariel," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="KLIN":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.klin
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.klin," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="WAW":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.waw
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.waw," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="GOOD MAMA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.goodMama
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.goodMama," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="VIVA":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.viva
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.viva," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="BISCUIT":
        print("Which of the Biscuits Comrade?")
        print("We have:")
        print(biscuit.itemOne)
        print(biscuit.itemTwo)
        print(biscuit.itemThree)
        print(biscuit.itemFour)
        print(biscuit.itemFive)
        print(biscuit.itemSix)
        item=input()
        item=item.upper()

        if item=="DIGESTIVE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.digestive
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.digestive," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="CHOCOLATE RINGS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.chocolateRings
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.chocolateRings," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="OREO":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.oreo
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.oreo," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BELOXXY":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.beloxxy
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.beloxxy," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="MCVITES":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.mcVites
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.mcVites," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="YALE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.yale
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.yale," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="WINE":
        print("Which of the Wines Comrade?")
        print("We have:")
        print(wine.itemOne)
        print(wine.itemTwo)
        print(wine.itemThree)
        print(wine.itemFour)
        print(wine.itemFive)
        print(wine.itemSix)
        item=input()
        item=item.upper()

        if item=="FOUR COUSINS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.fourCousins
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.fourCousins," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="RED GRAPE":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.redGrape
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.redGrape," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="CARLO ROSSI":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.carloRossi
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.carloRossi," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="PURE HEAVEN":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.pureHeaven
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.pureHeaven," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="DON SIMON":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.donSimon
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.donSimon," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()

        if item=="BAILEYS":
            print("How many would you like to get Boss?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.baileys
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.baileys," which is = N",total)
            print("Would that be all for today Boss? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Boss?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a handsome day, as handsome as you Sir")
            exit()
        else:
            print("Sorry Sir we do not have that item in this category, please choose any of the items listed above for this category")
    else:
        print("Sorry Sir we do not have that in our category, please choose any of the categories listed above")
    exit()

if gender=="F":
    print("Welcome Sweetheart, here are the list of item categories we have for you:")
    print(itemsList.mlk)
    print(itemsList.bvrg)
    print(itemsList.crl)
    print(itemsList.veg)
    print(itemsList.ltn)
    print(itemsList.prfm)
    print(itemsList.frt)
    print(itemsList.dtgt)
    print(itemsList.bsct)
    print(itemsList.wne)
    print("Which of the categories would you be selecting today Sweetheart?")
    itemCat=input()
    itemCat=itemCat.upper()

    if itemCat=="MILK":
        print("Which of the Milks Sweetheart?")
        print("We have:")
        print(milk.itemOne)
        print(milk.itemTwo)
        print(milk.itemThree)
        print(milk.itemFour)
        print(milk.itemFive)
        item=input()
        item=item.upper()

        if item=="PEAK MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.peakMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.peakMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="DANO MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.danoMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.danoMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="THREE CROWNS MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.threeCrownsMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.threeCrownsMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="MIKSI MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.miksiMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.miksiMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="COWBELL MILK":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*milk.cowbellMilk
            print("The cost of your selection is:")
            print(itemQty ,item," X ",milk.cowbellMilk," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="BEVERAGE":
        print("Which of the Beverages Sweetheart?")
        print("We have:")
        print(beverage.itemOne)
        print(beverage.itemTwo)
        print(beverage.itemThree)
        print(beverage.itemFour)
        item=input()
        item=item.upper()

        if item=="PEAK CHOCO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.peakChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.peakChoco," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BOURNVITA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.bournvita
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.bournvita," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="HOT CHOCO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.hotChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.hotChoco," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="COWBELL CHOCO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*beverage.cowbellChoco
            print("The cost of your selection is:")
            print(itemQty ,item," X ",beverage.cowbellChoco," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="CEREAL":
        print("Which of the Cereals Sweetheart?")
        print("We have:")
        print(cereal.itemOne)
        print(cereal.itemTwo)
        print(cereal.itemThree)
        item=input()
        item=item.upper()

        if item=="CERELAC":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.cerelac
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.cerelac," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="GOLDEN MORN":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.goldenMorn
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.goldenMorn," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="WHEAT MEAL":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*cereal.wheatMeal
            print("The cost of your selection is:")
            print(itemQty ,item," X ",cereal.wheatMeal," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="VEGETABLES":
        print("Which of the Vegetables Sweetheart?")
        print("We have:")
        print(vegetable.itemOne)
        print(vegetable.itemTwo)
        print(vegetable.itemThree)
        print(vegetable.itemFour)
        print(vegetable.itemFive)
        print(vegetable.itemSix)
        print(vegetable.itemSeven)
        item=input()
        item=item.upper()

        if item=="CABBAGE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.cabbage
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.cabbage," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="SPINACH":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.spinach
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.spinach," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="CARROT":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.carrot
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.carrot," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="GREEN BEANS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.greenBeans
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.greenBeans," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="GREEN PEAS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.greenPeas
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.greenPeas," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="CUCUMBER":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.cucumber
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.cucumber," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="ONIONS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*vegetable.onions
            print("The cost of your selection is:")
            print(itemQty ,item," X ",vegetable.onions," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="LOTION":
        print("Which of the Lotions Sweetheart?")
        print("We have:")
        print(lotion.itemOne)
        print(lotion.itemTwo)
        print(lotion.itemThree)
        print(lotion.itemFour)
        print(lotion.itemFive)
        item=input()
        item=item.upper()

        if item=="CUSSONS BABY":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.cussonsBaby
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.cussonsBaby," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="PEARS BABY":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.pearsBaby
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.pearsBaby," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BRONZ TONE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.bronzTone
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.bronzTone," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="NIVEA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.nivea
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.nivea," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="VASELINE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.vaseline
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.vaseline," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="PERFUME":
        print("Which of the Perfumes Sweetheart?")
        print("We have:")
        print(lotion.itemOne)
        print(lotion.itemTwo)
        print(lotion.itemThree)
        print(lotion.itemFour)
        print(lotion.itemFive)
        print(lotion.itemSix)
        item=input()
        item=item.upper()

        if item=="SMART COLLECTION":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.smartCollection
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.smartCollection," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="TONY MONTANA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.tonyMontana
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.tonyMontana," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="INSPIRATION":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.inspiration
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.inspiration," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="TEMPTATION":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.temptation
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.temptation," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="EMERGENCY":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.emergency
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.emergency," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="ONE BILLION":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*lotion.oneBillion
            print("The cost of your selection is:")
            print(itemQty ,item," X ",lotion.oneBillion," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="FRUIT":
        print("Which of the Fruits Sweetheart?")
        print("We have:")
        print(fruit.itemOne)
        print(fruit.itemTwo)
        print(fruit.itemThree)
        print(fruit.itemFour)
        print(fruit.itemFive)
        item=input()
        item=item.upper()

        if item=="PINEAPPLE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.pineapple
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.pineapple," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="APPLE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.apple
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.apple," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="WATERMELON":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.watermelon
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.watermelon," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BANANA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.banana
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.banana," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="AVOCADO PEAR":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*fruit.avocadoPear
            print("The cost of your selection is:")
            print(itemQty ,item," X ",fruit.avocadoPear," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="DETERGENT":
        print("Which of the Detergents Sweetheart?")
        print("We have:")
        print(detergent.itemOne)
        print(detergent.itemTwo)
        print(detergent.itemThree)
        print(detergent.itemFour)
        print(detergent.itemFive)
        print(detergent.itemSix)
        item=input()
        item=item.upper()

        if item=="OMO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.omo
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.omo," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="ARIEL":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.ariel
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.ariel," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="KLIN":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.klin
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.klin," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="WAW":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.waw
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.waw," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="GOOD MAMA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.goodMama
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.goodMama," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="VIVA":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*detergent.viva
            print("The cost of your selection is:")
            print(itemQty ,item," X ",detergent.viva," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="BISCUIT":
        print("Which of the Biscuits Sweetheart?")
        print("We have:")
        print(biscuit.itemOne)
        print(biscuit.itemTwo)
        print(biscuit.itemThree)
        print(biscuit.itemFour)
        print(biscuit.itemFive)
        print(biscuit.itemSix)
        item=input()
        item=item.upper()

        if item=="DIGESTIVE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.digestive
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.digestive," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="CHOCOLATE RINGS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.chocolateRings
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.chocolateRings," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="OREO":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.oreo
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.oreo," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BELOXXY":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.beloxxy
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.beloxxy," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="MCVITES":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.mcVites
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.mcVites," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="YALE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*biscuit.yale
            print("The cost of your selection is:")
            print(itemQty ,item," X ",biscuit.yale," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
        exit()

    if itemCat=="WINE":
        print("Which of the Wines Sweetheart?")
        print("We have:")
        print(wine.itemOne)
        print(wine.itemTwo)
        print(wine.itemThree)
        print(wine.itemFour)
        print(wine.itemFive)
        print(wine.itemSix)
        item=input()
        item=item.upper()

        if item=="FOUR COUSINS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.fourCousins
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.fourCousins," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="RED GRAPE":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.redGrape
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.redGrape," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="CARLO ROSSI":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.carloRossi
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.carloRossi," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="PURE HEAVEN":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.pureHeaven
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.pureHeaven," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="DON SIMON":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.donSimon
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.donSimon," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()

        if item=="BAILEYS":
            print("How many would you like to get Dear?")
            itemQty=input()
            print("You have selected ", itemQty , item)
            total=int(itemQty)*wine.baileys
            print("The cost of your selection is:")
            print(itemQty ,item," X ",wine.baileys," which is = N",total)
            print("Would that be all for today Dear? Yes/No")
            response=input()
            response=response.upper()
            if response=="NO":
                print("What other item would you want to get Dear?")
                item2=input()
                item2=item2.upper()
            if response=="YES":
                print("Thank you for your patronage, do have a beautiful day, as beautiful as you Ma'am")
            exit()
        else:
            print("Sorry Ma'am we do not have that item in this category, please choose any of the items listed above for this category")
    else:
        print("Sorry Ma'am we do not have that in our category, please choose any of the categories listed above")
    exit()
else:
    print("Sorry we dont have a categoey for you here, thanks, do check another store")
exit()