print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("you can go out with your friends!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("good job! you will do well and life is good ")
      counter += 1
    if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("don't worry! take your mind off, and you can do well!")
      counter += 1
    if each_word == "upset":
      feelings_list.append("upset")
      encouragement_list.append("your grades are not a measure of your ability!")
      counter += 1
if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("calm down")
      counter += 1
      if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("it's ok to feel sad sometimes! just go out and do what you want to! everything will fall into place soon! cheer up!")
      counter += 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
