import smtplib
import speech_recognition as sr
import pyttsx3
import datetime
from email.message import EmailMessage

engine = pyttsx3.init()

def speak(voices):
    engine.say(voices)
    engine.runAndWait()

def WishMe():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<12:
<<<<<<< HEAD
        speak('goodu morning ramu')
    elif time>=12 and time<18:
        speak('goodu afternoon ramu')
    else:
        speak('goodu evening ramu')
=======
        speak('good morning ramuji')
    elif time>=12 and time<18:
        speak('good afternoon ramuji')
    else:
        speak('good evening ramuji')
>>>>>>> update
    speak('this is jarvis sir.. how can i help you')




def TakeCommand():
    r=sr.Recognizer()
    with sr.microphone() as source:
        print('listening.........')
        audio=r.listen(sourse)#start listening

    try:
        print('recognising...........')
        query = r.recognize_google(audio)
        print(f"you said {query}")
    except Exception as e:
        print('plz try again something may wrong happend...........')
    return query.lower()

def sendEmail(to, subject, text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('approxgameplay@gmail.com', 'approx@786')
    email = EmailMessage
    email['From'] = 'approxgameplay@gmail.com' 
    email['To'] = to
    email['Subject'] = subject
    email.set_content(text)
    server.send_message(email)

        
def get_info():
    speak('whom you want to send email')
    name = TakeCommand()
    name_email = name_lst[name]
    print(name_email)
    speak('what is the subject')
    subject = TakeCommand()
    speak(f'what is the text you want to send to {name}')
    text = TakeCommand()
    sendEmail(name_email, subject, text)
    speak('your message has sent successfully')
    speak('do you want to send another email')
    query = TakeCommand()
    if 'yes' in query:
        get_info()





if __name__ == "__main__":

    WishMe()
    get_info()
    name_lst = {
        'mahesh':'maheshtamarakar369@gmail.com',
        'suraj':'doesntm087@gmail.com',
        'karan':'maheshtamarakar2@gmail.com',
        'sangam':'maheshtamarakar123@gmail.com'

    }
