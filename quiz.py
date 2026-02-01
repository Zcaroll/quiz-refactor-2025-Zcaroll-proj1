""" A quiz program. Asks the user to choose between art and space questions,
then asks questions on the chosen topic, keeping track of the score. """

total_score = 0

# standerdized input prompt
universal_input_prompt = 'Enter your answer: '

topic = input('Would you like art, or space questions? ')

if topic == 'art':

    # Dictionary stores art questions and answers
    art_quiz_dict = {}


    art_quiz_dict['Who painted the Mona Lisa?'] = 'Leonardo Da Vinci'
    art_quiz_dict['What precious stone is used to make the artist\'s pigment ultramarine?'] = 'Lapiz lazuli'
    art_quiz_dict['Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?'] = 'Chicago'
    art_quiz_dict['Which kid\'s TV characters are named after Renaissance artists?'] = 'Teenage Mutant Ninja Turtles'

    #TODO: make non case sensitive comparison for answers
    for question, correct_answer in art_quiz_dict.items():
        answer = input(question + '\n' + universal_input_prompt)
        if answer == correct_answer:
            print('Correct!')
            total_score += 1
        else:
            print(f'Sorry, the correct answer is {correct_answer}.')

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of {len(art_quiz_dict)}.')

    if total_score == len(art_quiz_dict):
        print('You got all the answers correct!')


elif topic == 'space':
    
    print('Which planet is closest to the sun?')
    answer = input('Enter your answer: ')
    if answer == 'Mercury':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Mercury.')

    print('Which planet spins in the opposite direction to all the others in the solar system?')
    answer = input('Enter your answer: ')
    if answer == 'Venus':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is Venus.')

    print('How many moons does Mars have?')
    answer = input('Enter your answer: ')
    if answer == '2':
        print('Correct!')
        total_score += 1
    else:
        print('Sorry, the correct answer is 2.')

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 3.')

    if total_score == 3:
        print('You got all the answers correct!')

else:
    print('That is not a valid topic. Restart the program to try again.')