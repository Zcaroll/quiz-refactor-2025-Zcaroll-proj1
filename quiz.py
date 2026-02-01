""" A quiz program. Asks the user to choose between art and space questions,
then asks questions on the chosen topic, keeping track of the score. """

total_score = 0

# standerdized input prompt for questions
universal_input_prompt = 'Enter your answer: '


# Input validation loop for topic selection
def get_topic():
    topic = input('Would you like art, space, or sports questions? ').lower()
    while topic not in ['art', 'space', 'sports']:
        print('That is not a valid topic. Please choose "art", "space", or "sports".')
        topic = input('Would you like art, space, or sports questions? ').lower()
    return topic

topic = get_topic()

# function to handle quiz logic for each topic
def run_quiz(quiz_dict):
    total_score = 0
    for question, correct_answer in quiz_dict.items():
        answer = input(question + '\n' + universal_input_prompt)
        if answer.lower() == correct_answer.lower():
            print('Correct!')
            total_score += 1
        else:
            print(f'Sorry, the correct answer is {correct_answer}.')
    return total_score

if topic == 'art':

    # Dictionary stores art questions and answers
    art_quiz_dict = {}

    # Adding questions and answers to the art dictionary
    art_quiz_dict['Who painted the Mona Lisa?'] = 'Leonardo Da Vinci'
    art_quiz_dict['What precious stone is used to make the artist\'s pigment ultramarine?'] = 'Lapiz lazuli'
    art_quiz_dict['Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?'] = 'Chicago'
    art_quiz_dict['Which kid\'s TV characters are named after Renaissance artists?'] = 'Teenage Mutant Ninja Turtles'

    # Loop through art questions and award points for correct answers
    total_score = run_quiz(art_quiz_dict)

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of {len(art_quiz_dict)}.')

    if total_score == len(art_quiz_dict):
        print('You got all the answers correct!')


elif topic == 'space':

    # Dictionary stores space questions and answers
    space_quiz_dict = {}

    # Adding questions and answers to the space dictionary
    space_quiz_dict['Which planet is closest to the sun?'] = 'Mercury'
    space_quiz_dict['Which planet spins in the opposite direction to all the others in the solar system?'] = 'Venus'
    space_quiz_dict['How many moons does Mars have?'] = '2'
    

    # Loop through the space questions and check answers
    total_score = run_quiz(space_quiz_dict)

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of {len(space_quiz_dict)}.')

    if total_score == len(space_quiz_dict):
        print('You got all the answers correct!')

elif topic == 'sports':
    print('Sports questions are coming soon!')
    # Dictionary stores sports questions and answers
    sports_quiz_dict = {}

    # Adding questions and answers to the sports dictionary
    sports_quiz_dict['Which country won the first ever soccer World Cup in 1930?'] = 'Uruguay'
    sports_quiz_dict['In which sport would you perform the Fosbury Flop?'] = 'High Jump'

    total_score = run_quiz(sports_quiz_dict)
    print(f'Your total score on {topic} questions is {total_score} out of {len(sports_quiz_dict)}.')
    
    if total_score == len(sports_quiz_dict):
        print('You got all the answers correct!')
    print('End of quiz!')