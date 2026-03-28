print("Quiz game has started")
print("Quiz type:basic geography")
score = 0
questions = [ ]
questions.append({
        "question" : "Which country is the largest in area?" ,
        "a" : "China" ,
        "b" : "Canada" ,
        "c" : "India" ,
        "d" : "Russia" ,
        "answer" : "d"
})
questions.append({
    "question": "Which country has the largest population?",
    "a": "India",
    "b": "Indonesia",
    "c": "Nigeria",
    "d": "Spain",
    "answer": "a"
})
questions.append({
    "question": "What is the tallest mountain in the world?",
    "a": " Mount K2",
    "b": "Mount Kilimanjaro",
    "c": "Mount Everest",
    "d": "Mount Makalu",
    "answer": "c"
})
questions.append({
    "question": "What is the longest river in the world?",
    "a": "The Amazon",
    "b": "The Nile",
    "c": "The Yellow river",
    "d": "The Mississippi",
    "answer": "b"
})
for q in questions:
	print(q["question"])
	print("a)", q["a"])
	print("b)", q["b"])
	print("c)", q["c"])
	print("d)", q["d"])
	guess = input("Enter your answer (a/b/c/d): ")
	if guess == q["answer"]:
		print("Correct!")
		score += 1
	else :
		print("Wrong!")
print("Game Over! Your score", score)