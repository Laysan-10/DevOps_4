import logging
import re

import paramiko
from dotenv import load_dotenv
import os

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Подключаем логирование
# logging.basicConfig(
#     filename='logfile.txt', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )

# logger = logging.getLogger(__name__)

def start(update: Update, context):
    update.message.reply_text('привет\n/find_phone_number - найти номер\n/find_email- найти адрес почты\n/verify_password - сложность пароля\n/ssh_connect - подключение по ssh\n/exit - выход')

def helpCommand(update: Update, context):
    update.message.reply_text('Help!')

def findPhoneNumbersCommand(update: Update, context):
    update.message.reply_text('Введите текст для поиска телефонных номеров: ')
    return 'findPhoneNumbers'

def findEmailNumbersCommand(update: Update, context):
    update.message.reply_text('Введите текст для поиска адреса электронной почты: ')
    return 'findEmailNumbers'

def findEmailNumbersCommand(update: Update, context):
    update.message.reply_text('Введите текст для поиска адреса электронной почты: ')
    return 'findEmailNumbers'

def exit(update: Update, context):
    update.message.reply_text('Работа завершена ')
    return ConversationHandler.END #завершает работу
    
def PasswardCorrectMessage(update: Update, context):
    update.message.reply_text('Введите пароль для проверки сложности: ')
    return 'PasswardCorrect'

def SshConnectionMessage(update: Update, context):
    update.message.reply_text('Отправте файл формата .env с данными хоста для подключения по ssh ')
    return 'SshConnection'

def SshConnection(update: Update, context):

    global host 
    global port 
    global username 
    global password 
    global client

    file_id = update.message.document.file_id
    file = context.bot .get_file(file_id) 
    file_name = update.message.document.file_name or "config.env"
    file_type = re.compile(r'.env')

    if(file_type.findall(file_name)):
        file.download (f'/tmp/{file_name}')
        load_dotenv(f'/tmp/{file_name}')
        update.message.reply_text('Файл загружен')
    else:
        update.message.reply_text('Bad file type')
    
    host = os.getenv("SSH_HOST")
    port = int(os.getenv("SSH_PORT"))  # по умолчанию 22
    username = os.getenv("SSH_USERNAME")
    password = os.getenv("SSH_PASSWORD")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    update.message.reply_text('Подождите...')
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        client.close()

        #написать то какие команды можно использовать
        update.message.reply_text('Доступные команды\n/get_release - получение информации о релизе\n\
/get_uname - Об архитектуры процессора, имени хоста системы и версии ядра\n\
/get_uptime - О времени работы. \n/get_df - Сбор информации о состоянии файловой системы.\n\
/get_free - Сбор информации о состоянии оперативной памяти.\n\
/get_mpstat - информации о производительности системы.\n\
/get_w -  Сбор информации о работающих в данной системе пользователях.\n\n\
Сбор логов:\n\
/get_auths - Последние 10 входов в систему.\n\
/get_critical - Последние 5 критических события.\n\
/get_ps - Сбор информации о запущенных процессах.\n\
/get_ss - Сбор информации об используемых портах.\n\
/get_apt_list - Сбор информации об установленных пакетах.\n\
/get_service - получить статус сервиса \n\
/get_repl_logs - получить инфомацию о репликации \n\
/get_emails - ввести почту из базы данных \n\
    /get_phone_numbers - вывести номер телефонов из базы данных')


        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('SshConnection ') # client.close()  
        
    return False


def getUname(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('uname --all')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getUptime(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('uptime')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getDf(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('df')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getFree(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('free')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getMpstat(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('mpstat')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False


def getW(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('w')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getAuths(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('last -n 10')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False


def getCritical(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('journalctl -p crit -n 5 --no-pager')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getPs(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('ps')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getSs(update: Update, context): 
#Проверка подлючения
    update.message.reply_text('Подождите...')
    
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('ss -4 state listening')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False


def getAptListMessage(update: Update, context):
     update.message.reply_text('Вывести все пакеты ("Да") или определенный ("введите название")')
     return 'getAptList'
def getAptList(update: Update, context):
    user_input = update.message.text
    update.message.reply_text('Подождите...')
    print(user_input)
    if(user_input == 'Да' or user_input == "да"):
        print('ifyes')
        try:
            client.connect(hostname=host, username=username, password=password, port=port)
            update.message.reply_text('Успешное подключение')
            stdin, stdout, stderr = client.exec_command('dpkg -l | head -n 6')
            data = stdout.read() + stderr.read()
            client.close()
            data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
            update.message.reply_text(data)
            return True
        except Exception as e:
             update.message.reply_text('Ошибка подключения')
        finally:
            print('getRelease') # client.close() 
    else:
        try:
            client.connect(hostname=host, username=username, password=password, port=port)
            update.message.reply_text('Успешное подключение')
            stdin, stdout, stderr = client.exec_command(f'dpkg -l | grep {user_input}')
            data = stdout.read() + stderr.read()
            client.close()
            data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
            update.message.reply_text(data)
            return True
        except Exception as e:
             update.message.reply_text(f'Ошибка подключения или введено неправильное имя пакета {user_input}')
        finally:
            print('getRelease') # client.close()
        return ConversationHandler.END  

def getRelease(update: Update, context):
#Проверка подлючения
    
    update.message.reply_text('Подождите...')
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        stdin, stdout, stderr = client.exec_command('lsb_release -a')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getRepl(update: Update, context):
#Проверка подлючения
    
    update.message.reply_text('Подождите...')
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        
        stdin, stdout, stderr = client.exec_command('sudo tail /var/log/postgresql/postgresql-15-main.log')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getEmails(update: Update, context):
#Проверка подлючения
    
    update.message.reply_text('Подождите...')
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        
        stdin, stdout, stderr = client.exec_command('sudo -u postgres psql -d db_tg -c "SELECT * from Emails;"')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False


def getPhoneNumber(update: Update, context):
#Проверка подлючения
    
    update.message.reply_text('Подождите...')
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        
        stdin, stdout, stderr = client.exec_command('sudo -u postgres psql -d db_tg -c "SELECT * from Phones;"')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getServiceMessage(update: Update, context):
    update.message.reply_text('Вывести все сервисф ("Да") или определенный ("введите название")')
    return 'getService'

def docker(update: Update, context):
    update.message.reply_text('Подождите...')
    try:
        client.connect(hostname=host, username=username, password=password, port=port)
        update.message.reply_text('Успешное подключение')
        
        stdin, stdout, stderr = client.exec_command('sudo docker exec postgres_primary psql -U postgres -d db_tg -c "SELECT * FROM Phones;"')
        data = stdout.read() + stderr.read()
        client.close()
        data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
        update.message.reply_text(data)
        return True
    except Exception as e:
             update.message.reply_text('Ошибка подключения')
    finally:
            print('getRelease') # client.close()  
        
    return False

def getService(update: Update, context):
    user_input = update.message.text
    print(user_input)
    update.message.reply_text('Подождите...')
    if(user_input == "Да" or user_input == "да"):
        print('ifyes')
        try:
            client.connect(hostname=host, username=username, password=password, port=port)
            update.message.reply_text('Успешное подключение')
            stdin, stdout, stderr = client.exec_command('service --status-all | head -n 5')
            data = stdout.read() + stderr.read()
            client.close()
            data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
            update.message.reply_text(data)
            return True
        except Exception as e:
             update.message.reply_text('Ошибка подключения')
        finally:
            print('getRelease') # client.close() 
    else:
        try:
            client.connect(hostname=host, username=username, password=password, port=port)
            update.message.reply_text('Успешное подключение')
            stdin, stdout, stderr = client.exec_command(f'service {user_input} status')
            data = stdout.read() + stderr.read()
            client.close()
            data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
            update.message.reply_text(data)
            return True
        except Exception as e:
             update.message.reply_text(f'Ошибка подключения или введено неправильное имя пакета {user_input}')
        finally:
            print('getRelease') # client.close()
        return ConversationHandler.END 

def PasswardCorrect(update: Update, context):
    user_input = update.message.text
    passwordCorrect =0 #Степень сложности пароля
    bigWord = re.compile(r'[A-Z]')
    smallWord = re.compile(r'[a-z]')
    numbers = re.compile(r'[0-9]')
    specialSymbol=re.compile(r'\W')

    if (len(user_input)>=8):
        passwordCorrect +=1
    else:
        update.message.reply_text("Длина пароля меньше 8 символов")
        return 
    if (bigWord.findall(user_input)):
        passwordCorrect +=1   #Кол-во заглавный букв

    else:
        update.message.reply_text('Стоит добавить заглавную букву')

    if (smallWord.findall(user_input)):
        passwordCorrect +=1   #Кол-во заглавный букв

    else:
        update.message.reply_text('Стоит добавить прописную букву ')

    if (numbers.findall(user_input)):
        passwordCorrect +=1  #Кол-во цифр
    else:
        update.message.reply_text('Стоит добавить цифры')

    if (specialSymbol.findall(user_input)) :   
        passwordCorrect +=1  #Кол-во спец символов
    else:
        update.message.reply_text('Стоит добавить спец символ')

    update.message.reply_text('Пароль плохой') if(passwordCorrect<=4) else update.message.reply_text('Пароль сложный') if(passwordCorrect>=5) else print("Error")


def findEmailNumbers(update: Update, context):
    user_input = update.message.text
    patterns = re.compile(r'\w+@yandex\.ru'
                            r'|'
                            r'\w+@gmail\.com' r'|'
                            r'\w+@rambler\.ru' r'|'
                            r'\w+@mail\.ru' r'|'
                            r'\w+@inbox\.ru' r'|'
                            r'\w+@list\.ru' r'|'
                            r'\w+@bk\.ru' r'|'
                            r'\w+@ya\.ru' r'|'
                            r'\w+@yandex\.com' r'|'
                            r'\w+@lenta\.ru' r'|'
                            r'\w+@autorambler\.ru' r'|' r'\w+@\w+\.ru'  r'|' r'\w+@\w+\.com')
    EmailList = patterns.findall(user_input)

    if not EmailList:
        update.message.reply_text('Не найден адрес эдектронной почты')
        return
    Emails = ''
    for i in range (len(EmailList)):
        Emails += f'{i+1}. {EmailList[i]}\n'
    
    update.message.reply_text(Emails)
    context.user_data['email'] = EmailList#сохраняем данные

    update.message.reply_text("Хотите добавить почту в базу данных? (Да/Нет)")
    return 'InsertEmail' #передача телефонный номеров

def findPhoneNumbers (update: Update, context):
    user_input = update.message.text # Получаем текст, содержащий(или нет) номера телефонов

    patterns = re.compile(
    r'8 \(\d{3}\) \d{3}-\d{2}-\d{2}' 
    r'|'    # 8 (000) 000-00-00
    r'8 \d{3} \d{3}-\d{2}-\d{2}' 
    r'|'   # 8 000 000-00-00   
    r'8\d{10}' 
    r'|'  
    r'8\(\d{3}\)\d{3}\d{2}\d{2}' 
    r'|' 
    r'8 \d{3} \d{3} \d{2} \d{2}' r'|'  
    r'8\d{3} \d{3} \d{2} \d{2}' r'|'  
    r'8 \d{3}\d{3} \d{2} \d{2}' r'|'  
    r'8 \d{3} \d{3}\d{2} \d{2}' r'|'  
    r'8 \d{3} \d{3} \d{2}\d{2}' r'|'  
    r'8\d{3}\d{3} \d{2} \d{2}' r'|'  
    r'8\d{3}\d{3}\d{2} \d{2}' r'|'  
    r'8\d{3} \d{3} \d{2}\d{2}' 
    r'|' 
     r'7\d{10}' 
    r'|' 
    r'7 \d{3} \d{3} \d{2} \d{2}' r'|'
    r'7\d{3} \d{3} \d{2} \d{2}' r'|'
    r'7 \d{3}\d{3} \d{2} \d{2}' r'|'
    r'7 \d{3} \d{3}\d{2} \d{2}' r'|'
    r'7 \d{3} \d{3} \d{2}\d{2}' r'|'
    r'7\d{3}\d{3} \d{2} \d{2}' r'|'
    r'7\d{3}\d{3}\d{2} \d{2}' r'|'
    r'7\d{3} \d{3} \d{2}\d{2}'
   
    
    )         
   
    phoneNumberList = patterns.findall(user_input) # Ищем номера телефонов
    print( phoneNumberList)
    

    if not phoneNumberList: # Обрабатываем случай, когда номеров телефонов нет
        update.message.reply_text('Телефонные номера не найдены')
        return ConversationHandler.END# Завершаем выполнение функции
    else:
        phoneNumbers = '' # Создаем строку, в которую будем записывать номера телефонов
        for i in range(len(phoneNumberList)):
            phoneNumbers += f'{i+1}. {phoneNumberList[i]}\n' # Записываем очередной номер
            
        update.message.reply_text(phoneNumbers)
        context.user_data['phone_numbers'] = phoneNumberList #сохраняем данные

        update.message.reply_text("Хотите добавить номера телефонов в базу данных? (Да/Нет)")
        return 'InsertPhoneNumber' #передача телефонный номеров
  


def InsertPhoneNumber(update: Update, context):
      
    user_input= update.message.text
    phoneNumberList = context.user_data.get('phone_numbers', [])#достаем список
    print("Я сохранил:", phoneNumberList)
    if(user_input == 'Да' or user_input == 'да' ):
    
        try:
                update.message.reply_text('Идет подключение к базе данных')
                client.connect(hostname=host, username=username, password=password, port=port)

                # Экранируем только одинарные кавычки для SQL
               
                # Экранируем только одинарные кавычки для SQL
                phoneNumberList = [num.replace("'", "''") for num in phoneNumberList]

                # Формируем один общий SQL-запрос для всех номеров
                sql_values = ", ".join([f"('{num}')" for num in phoneNumberList])
                sql_command = f"INSERT INTO Phones(phone) VALUES {sql_values};"


                # Формируем полную команду для выполнения через sudo
                full_command = f"sudo -u postgres psql -d db_tg -c \"{sql_command}\""

                # Выполняем команду
                stdin, stdout, stderr = client.exec_command(full_command)
                data = stdout.read() + stderr.read()

                client.close()

                update.message.reply_text('Успешно!')
                
        except Exception as e:
                update.message.reply_text('Ошибка подключения, проверте ssh соеднение')
        finally:
                print('getRelease') # client.close() 
    else:
        update.message.reply_text('Работа завершена')
        return  ConversationHandler.END


def InsertEmail(update: Update, context):
      
    user_input= update.message.text
    Emails = context.user_data.get('email', [])#достаем список
    print("Я сохранил:", Emails)
    if(user_input == 'Да' or user_input == 'да' ):
    
        try:
                update.message.reply_text('Идет подключение к базе данных')
                client.connect(hostname=host, username=username, password=password, port=port)

                # Формируем один общий SQL-запрос для всех номеров
                sql_values = ", ".join([f"('{num}')" for num in Emails])
                sql_command = f"INSERT INTO Emails(email) VALUES {sql_values};"

                # Формируем полную команду для выполнения через sudo
                full_command = f"sudo -u postgres psql -d db_tg -c \"{sql_command}\""

                # Выполняем команду
                stdin, stdout, stderr = client.exec_command(full_command)
                data = stdout.read() + stderr.read()
                client.close()

                update.message.reply_text('Успешно!')
                
        except Exception as e:
                update.message.reply_text('Ошибка подключения, проверте ssh соеднение')
        finally:
                print('getRelease') # client.close() 
    else:
        update.message.reply_text('Работа завершена')
        return  ConversationHandler.END
 
def main():
    updater = Updater(TOKEN, use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher
    
    # ТЕЛЕФОН
    convHandlerFindPhoneNumbers = ConversationHandler(
        entry_points=[CommandHandler('find_phone_number', findPhoneNumbersCommand)],
        states={
            'findPhoneNumbers': [MessageHandler(Filters.text & ~Filters.command, findPhoneNumbers)],
            'InsertPhoneNumber': [MessageHandler(Filters.regex(r'^(Да|Нет)$'), InsertPhoneNumber)],
        },
        fallbacks=[]#способ завершения работы
    )   

     


    #ПОЧТА
    convHandlerFindEmailNumbers =  ConversationHandler(
        entry_points=[CommandHandler('find_email', findEmailNumbersCommand)],
        states={
            'findEmailNumbers': [MessageHandler(Filters.text & ~Filters.command, findEmailNumbers)],   
            'InsertEmail': [MessageHandler(Filters.regex(r'^(Да|Нет)$'), InsertEmail)],     
    },
        fallbacks=[]#способ завершения работы
    )

    #ПАРОЛЬ
    convPasswardCorrect=  ConversationHandler(
        entry_points=[CommandHandler('verify_password', PasswardCorrectMessage)],
        states={
            'PasswardCorrect': [MessageHandler(Filters.text & ~Filters.command, PasswardCorrect)],        
    },
        fallbacks=[CommandHandler("exit", exit)]#способ завершения работы
    )
    #ПОДКЛЮЧЕНИЕ ПО SSH
    convSSHConnection =  ConversationHandler(
        entry_points=[CommandHandler('ssh_connect', SshConnectionMessage)],
        states={
            'SshConnection': [MessageHandler(Filters.document & ~Filters.command, SshConnection)],        
    },
        fallbacks=[CommandHandler("exit", exit)]#способ завершения работы
    )


   #  #ОБ УСТАНОВЛЕННЫХ ПАКЕТАХ
    convaptlist =  ConversationHandler(
        entry_points=[CommandHandler('get_apt_list', getAptListMessage)],
        states={
            'getAptList': [MessageHandler(Filters.text & ~Filters.command, getAptList)],        
    },
        fallbacks=[CommandHandler("exit", exit)]#способ завершения работы
    )
   
    
 #  #ОБ УСТАНОВЛЕННЫХ ПАКЕТАХ
    convaptlist =  ConversationHandler(
        entry_points=[CommandHandler('get_apt_list', getAptListMessage)],
        states={
            'getAptList': [MessageHandler(Filters.text & ~Filters.command, getAptList)],        
    },
        fallbacks=[CommandHandler("exit", exit)]#способ завершения работы
    )
     #  #О СЕРВИСАХ
    convservice=  ConversationHandler(
        entry_points=[CommandHandler('get_service', getServiceMessage)],
        states={
            'getService': [MessageHandler(Filters.text & ~Filters.command, getService)],        
    },
        fallbacks=[CommandHandler("exit", exit)]#СЃРїРѕСЃРѕР± Р·Р°РІРµСЂС€РµРЅРёСЏ СЂР°Р±РѕС‚С‹
    )
    
     #
    
  
  # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", helpCommand))

     #О РЕЛИЗЕ
    dp.add_handler(CommandHandler('get_release', getRelease))
    #АРХ ХОСТА ИМЯ
    dp.add_handler(CommandHandler('get_uname', getUname))
    #ВРЕМЯ РАБОТЫ
    dp.add_handler(CommandHandler('get_uptime', getUptime))
    dp.add_handler(CommandHandler('docker', docker))
    # #О СОСТОЯНИЕ ФАЙЛОВОЙ СИСТЕМЫ
    dp.add_handler(CommandHandler('get_df', getDf))

    # #ОБ ОЗУ
    dp.add_handler(CommandHandler('get_free', getFree))

    # #О ПРОИЗВОДИТЕЛЬНОСТИ
    dp.add_handler(CommandHandler('get_mpstat', getMpstat))

    # #О РАБОТАЮЩИЙ ПОЛЬЗОВАТЕЛЯХ
    dp.add_handler(CommandHandler('get_W', getW))

    #  #ПОСЛЕДНИЕ 10 ПОЛЬЗОВАТЕЛЕЙ
    dp.add_handler(CommandHandler('get_auths', getAuths))

    #  #ПОСЛЕДНИЕ 5 КРИТИЧЕСКИХ СОБЫТИЯ
    dp.add_handler(CommandHandler('get_critical', getCritical))

    #  #О ЗАПУЩЕННЫХ ПРОЦЕССАХ
    dp.add_handler(CommandHandler('get_ps', getPs))

    #  #ОБ ИСПОЛЬЗУЕМЫХ ПОРТАХ
    dp.add_handler(CommandHandler('get_ss', getSs))

    #ПОЛУЧИТЬ ИНФОРМАЦИЮ О РЕПЛИКАЦИИ
    dp.add_handler(CommandHandler('get_repl_logs', getRepl))

    #ВЫВЕСТИ ПОЧТУ
    dp.add_handler(CommandHandler('get_emails', getEmails))
    #ВЫВЕСТИ ТЕЛЕФОНЫ
    dp.add_handler(CommandHandler('get_phone_numbers', getPhoneNumber))

    dp.add_handler(convHandlerFindPhoneNumbers)


    dp.add_handler(convHandlerFindEmailNumbers)
    dp.add_handler(convPasswardCorrect)
    dp.add_handler(convSSHConnection)
    dp.add_handler(convaptlist)
    dp.add_handler(convservice)

            


    
  # Запускаем бота
    updater.start_polling()

  # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
