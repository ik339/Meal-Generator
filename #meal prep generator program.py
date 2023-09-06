from tkinter import * 
import random
MealG = Tk()                      
MealG.title('Meal Generator')
MealG.geometry("500x200") 
MealG.configure(background = "green") 

Result = Text(MealG,width=40,fg='Black',font=("Arial"), height = 5)
Result.pack()

#list of foods:
proteins = ["Chicken", "Beef", "Tuna", "Salmon", "Eggs", "Sausage"]
vegs = ["Mushroom", "Roast Carrot", "Stemmed Broccoli", "Avocado", "Salad", "Bell Peppers", "Spinach", "Asparagus"]
carbs = ["Bulgur Wheat", "Rice", "Pasta", "Noodles", "Potato", "Sweet Potato"]
fats = ["Avocado", "Olive Oil", "Nuts", "Seeds"]
#function:
def generate_meal():
    protein = random.choice(proteins) 
    veg = random.choice(vegs)
    carb = random.choice(carbs)
    fat=random.choice(fats)
    meal = protein+" + "+carb+" + "+veg+" + "+fat 
    Result.delete("1.0", END)
    Result.insert("1.0", meal)
#button:
Generate_button = Button(text="Generate",bg='black',fg='white',padx=10,pady=10, command=generate_meal)
Generate_button.pack()

MealG.mainloop()
