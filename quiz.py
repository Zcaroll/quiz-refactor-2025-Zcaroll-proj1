""" A quiz program. Asks the user to choose between art and space questions,
then asks questions on the chosen topic, keeping track of the score. """

total_score = 0

# standerdized input prompt for questions
universal_input_prompt = 'Enter your answer: '


# Input validation loop for topic selection
def get_topic():
    topic = input('Would you like art, or space questions? ').lower()
    while topic not in ['art', 'space']:
        print('That is not a valid topic. Please choose "art" or "space".')
        topic = input('Would you like art, or space questions? ').lower()
    return topic

topic = get_topic()

if topic == 'art':

    # Dictionary stores art questions and answers
    art_quiz_dict = {}

    # Adding questions and answers to the art dictionary
    art_quiz_dict['Who painted the Mona Lisa?'] = 'Leonardo Da Vinci'
    art_quiz_dict['What precious stone is used to make the artist\'s pigment ultramarine?'] = 'Lapiz lazuli'
    art_quiz_dict['Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?'] = 'Chicago'
    art_quiz_dict['Which kid\'s TV characters are named after Renaissance artists?'] = 'Teenage Mutant Ninja Turtles'

    # Loop through art questions and award points for correct answers
    for question, correct_answer in art_quiz_dict.items():
        answer = input(question + '\n' + universal_input_prompt)
        if answer.lower() == correct_answer.lower():
            print('Correct!')
            total_score += 1
        else:
            print(f'Sorry, the correct answer is {correct_answer}.')

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
    for question, correct_answer in space_quiz_dict.items():
        answer = input(question + '\n' + universal_input_prompt)
        if answer.lower() == correct_answer.lower():
            print('Correct!')
            total_score += 1
        else:
            print(f'Sorry, the correct answer is {correct_answer}.')

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of {len(space_quiz_dict)}.')

    if total_score == len(space_quiz_dict):
        print('You got all the answers correct!')
#TODO remove this else block since input validation loop handles invalid topics
else:
    print('That is not a valid topic. Restart the program to try again.')