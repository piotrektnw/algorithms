import datetime
import logging

# Configure logging procedure
logging.basicConfig(filename='errorsLog.txt', level=logging.DEBUG)

agreeWords = ['y', 'yes', 'si', 'agree', 'ok', 'sure', 'of course', 'yup']

def say_goodbye():
    print("Goodbye")


def read_file():
    file = open("errorsLog.txt", "r")
    print(file.read())
    file.close()


def clear_file():
    file = open("errorsLog.txt", "w")
    file.write(" ")
    file.close()

# Fixed time addition
def validate(user_input, current_time=None):
    if current_time is None:
        current_time = datetime.datetime.now()

    try:
        user_input = int(user_input)
        # Improved log file data save by using logging lib instead of standard file management
        logging.info("User entered {}".format(type(user_input)) + " datatype on: {}".format(
             current_time.strftime("%d/%m/%Y") + " at {}".format(current_time.strftime("%H:%M:%S\n"))))

    except:
        try:
            user_input = float(user_input)
            # Improved log file data save by using logging lib instead of standard file management
            logging.info("User entered {}".format(type(user_input)) + " datatype on: {}".format(
                current_time.strftime("%d/%m/%Y") + " at {}".format(current_time.strftime("%H:%M:%S\n"))))
        except:
            user_input = str(user_input)
            # Improved log file data save by using logging lib instead of standard file management
            logging.info("User entered {}".format(type(user_input)) + " datatype on: {}".format(
                current_time.strftime("%d/%m/%Y") + " at {}".format(current_time.strftime("%H:%M:%S\n"))))
