import datetime

from api_data import download_course_data


def menu():
    """
    Shows alternative options about courses and trainers for user to choose
    :return: string
    """
    course_data = download_course_data()
    while True:
        print("""
---> MENU <---
1) List all trainers sorted by name
2) List 5 next upcoming courses sorted by date
3) List all courses with a specific trainer
4) List telephone number of most popular trainer
Q) Quit
""")
        answer = input("What say you? ").upper().strip()
        if answer == '1':
            list_of_trainers(course_data)
        if answer == '2':
            list_next_five(course_data)
        if answer == '3':
            courses_with_specific_trainer(course_data)
        if answer == '4':
            # TODO (10 p): Print the name of the trainer who
            # holds most courses in the future.
            # TODO (15 p): Also print out the phone number
            # of that trainer.
            # Note: The trainer is an employee of ProAgile,
            # and public data about employees are available
            # from this API endpoint:
            #    https://proagile.se/api/publicEmployees
            print('fix me')
        if answer.upper() == 'Q':
            print("Good-bye and thank you for the fish!")
            return


# 1
def list_of_trainers(course_data):
    """
    List all trainers sorted by family name (A-Z)
    :param course_data:
    :return:
    """
    # Sort the trainers before printing them.
    print("The trainers at ProAgile are:")
    trainers = []
    for course in course_data:
        trainer = course['trainerName']
        if trainer not in trainers:
            trainers.append(trainer)
    for trainer in sorted(trainers):
        print(f'  {trainer}')


# 2
def list_next_five(course_data):
    """
    List next five courses sorted by date
    :param course_data:
    :return:
    """
    print("Next 5 courses sorted by date:")
    # lambda sorterar här på startdatum
    course_data = sorted(course_data, key=lambda c: c['segments'][0]['start'])
    for num, course in enumerate(course_data[0:5], start=1):
        start_date = datetime.datetime.fromtimestamp(course['segments'][0]['start'])
        print(f"{num:2}. {course['courseName']:50} ({start_date})")


# 3
def courses_with_specific_trainer(course_data):
    """
    Lists courses with specific trainer, also when part of name is inserted
    :param course_data:
    :return: printed string of course names and dates
    """
    # E.g. if the user enters "fredrik", all courses
    # held by "Fredrik Wendt" will be listed.
    trainer_name = input("Name of trainer: ").lower()
    print(f"These courses are held by {trainer_name}:")
    courses_by_trainer = [course for course in course_data  # list
                          if trainer_name in course['trainerName'].lower()]
    for num, course in enumerate(courses_by_trainer, start=1):
        start_date = datetime.datetime.fromtimestamp(course['segments'][0]['start'])
        print(f"{num}. {course['courseName']} ({start_date}) held by {course['trainerName']}")





if __name__ == '__main__':
    menu()
