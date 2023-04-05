import openai

'''
Utilizing the OpenAI API, this program creates a baseline physical therapy
plan for users. This is done by asking the prospective physical therapy patient
to enter the number of weeks they plan to participate in physical therapy, the primary
area in the body where they are experiencing pain, their current physical limitations,
and their physical therapy goals. Because time is limited during a patient's first PT appointment,
the baseline plan is meant to complement the physical examination performed on the patient
by their therapist and serve as a secondary source of data when creating the patient's final
PT plan. Having more information regarding patient pain, limitations, and goals may help
improve patient outcomes and ultimately help them achieve their physical therapy goals.

In addition to creating the baseline plan, patients can also ask the AI Assistant to save their
physical therapy plan to a file for them to take to their initial appointment, and they
can also ask the AI Assistant to provide directions on one more of the exercises listed
in their plan (e.g., how to perform 'toe raises').
'''


def print_input_summary(number_of_weeks, pain, current_limitations, goals):
    '''
    Prints a summary of the physical therapy plan based on the users inputs.

    Parameters:
    -----------
    number_of_weeks: int
        The number of weeks for the physical therapy plan
    pain: str
        The type of pain the user is experiencing
    current_limitations: str
        The current physical limitations the user is experiencing
    goals: str
        The user's physical therapy goals

    Returns:
    --------
    None
    '''
    print(f'We will make you a {number_of_weeks} week physical therapy plan.')
    if pain != '':
        print(f'Your plan will focus on alleviating your {pain} pain.')
    if current_limitations != '':
        print(
            f'Your plan will help you work toward reducing your limitations with {current_limitations}.')
    if goals != '':
        print(
            f'Your plan will help you work toward achieving your {goals} goal.')


def get_AI_response(number_of_weeks, pain, current_limitations, goals):
    '''
    Generates an OpenAI API response for a physical therapy plan based on user inputs.

    Parameters:
    -----------
    number_of_weeks: int
        The number of weeks for the physical therapy plan
    pain: str
        The type of pain the user is experiencing
    current_limitations: str
        The current physical limitations the user is experiencing
    goals: str
        The user's physical therapy goals

    Returns:
    --------
    response: str
        The OpenAI API-generated response for the physical therapy plan.
    '''
    prompt = f'{number_of_weeks} week physical therapy plan for {pain} pain'
    if current_limitations != '':
        prompt += f', {current_limitations} limitations'
    if goals != '':
        prompt += f', with a {goals} goal.'
    prompt += f"Include exercises."

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=2000,
    )
    return response['choices'][0]['text']


def write_results_to_file(results):
    '''
    Write the physical therapy results to a file, if the user chooses to.

    Parameters:
    ----------
    results: str
        The physical therapy results to be saved to a file named 'my_PT_plan.txt'.

    Returns:
    --------
    None
    '''
    print_results = input(
        'Would you like to save your results? Enter Y or N: ')
    if print_results != 'N':
        with open('my_PT_plan.txt', 'w') as f:
            f.write(results)


def get_exercise_directions():
    '''
    Generates an OpenAI API response for exercise directions based on user inputs, if the user chooses to.

    Returns:
    --------
    None
    '''
    directions_ask = input(
        'Would you like specific directions on how to do one of your exercises? Enter Y or N: ')
    while directions_ask != 'N':
        exercise = input('Which exercise would you like directions for? ')
        prompt = f'Directions on how to perform {exercise}.'

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=150,
        )
        print(response['choices'][0]['text'])
        directions_ask = input(
            'Would you like to search for directions for another exercise? Enter Y or N: ')
    else:
        print('Good bye!')


def main():
    '''
    Driver for program
    '''
    api_key = ''

    with open('api-key') as f:  # user must use their own OpenAI API key
        api_key = f.read()

    openai.api_key = api_key

    pain_areas = [
        'ankle',
        'arm',
        'back',
        'elbow',
        'foot',
        'hand',
        'head',
        'hip',
        'knee',
        'leg',
        'neck',
        'shoulder']

    print('I\'m going to make you a physical therapy plan.')

    # constrain number of weeks to a max of 8
    number_of_weeks = input(
        'Tell me the number of weeks you plan to participate in physical therapy (1 - 8): ')
    while not number_of_weeks.isdigit() and number_of_weeks != '' and int(
            number_of_weeks) > 8 or int(number_of_weeks) < 1:
        number_of_weeks = input(
            'Invalid input. Please enter a whole number between 1 and 8: ')
    if number_of_weeks == '':
        number_of_weeks = 6  # set default number of weeks to 6 if no response given

    pain = input('Tell me the primary area of pain: ')
    while pain.lower() not in pain_areas and pain != '':
        pain = input(
            f'Invalid input. Please enter the primary area of pain, such as {pain_areas}: ')

    current_limitations = input(
        'Tell me one activity you are physically limited from performing: ')

    goals = input(
        'Tell me one goal you would like to achieve through physical therapy: ')
    print_input_summary(number_of_weeks, pain, current_limitations, goals)
    print()
    results = get_AI_response(
        number_of_weeks,
        pain,
        current_limitations,
        goals)
    print()
    print(results)
    print()
    write_results_to_file(results)
    print()
    get_exercise_directions()


if __name__ == '__main__':
    main()
