import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

config = {
  'user': 'root',
  'password': 'toor',
  'host': 'localhost',
  'port': 3306,
  'database': 'statlog'
}

def main():

  print("Starting Credit Analisis Program...")
  ####### Translating column names
  german_english = {'id': 'id'}
  description = {}

  codetable = open('documents//codetable.txt', 'rt')
  lines = codetable.readlines()

  for line in lines:
    if('$' in line.strip()):
      line_splited = line.strip()[2:-1].split()
      
      current_item_de = line_splited[0]
      current_item_en = line_splited[2]
      german_english.update({current_item_de: current_item_en})

      description.update({current_item_en: ''})
    else:
      description.update({
        current_item_en: description[current_item_en] + line
      })

  ####### Starting connection with mySQL to getting data
  db_connection_str = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
      config['user'],
      config['password'],
      config['host'],
      config['port'],
      config['database']
  )

  print("Creating connection with MySQL Database...")
  db_connection = create_engine(db_connection_str)

  column_names = list(german_english.values())

  print("Reading data from database... please wait...", end=" ")
  df = pd.read_sql('SELECT * FROM germancredit', con=db_connection)
  print("Done.")
  df.columns = column_names

  ####### Preparing the data and spliting in to train and test
  print("Preparing data...")
  X = df.iloc[:,1:-1].to_numpy() ## Data
  y = df.iloc[:,-1:].T.to_numpy()[0] ## Target

  test_size = 0.2
  random_state = 0

  X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=test_size,
    random_state=random_state
  )

  # Standardize data
  sc = StandardScaler()
  sc.fit(X_train)
  X_train_std = sc.transform(X_train)
  X_test_std = sc.transform(X_test)

  print('Unique labels: {0}'.format(np.unique(y)))
  
  ####### Training model with data
  # Creating an instance of Perceptron
  print("Trainning ML model (Perceptron)...")
  n_iter = 400
  eta0 = 0.1 # Learn Rate

  ppn = Perceptron(
    max_iter=n_iter,
    eta0=eta0,
    random_state=random_state
  )
  
  # fit the model to the standardized data
  print("Fitting the model...")
  ppn.fit(
    X_train_std,
    y_train
  )

  ####### Making predictions
  print("Making predictions with test data...")
  y_pred = ppn.predict(X_test_std)

  ####### Getting measures
  print("Getting measuriments...\r")

  print(50 * "-")
  print('Measuriments')
  print(50 * "-")
  accuracy = "accuracy: {0:.2f}%".format(accuracy_score(y_test, y_pred) * 100)
  print('\x1b[6;30;42m' + accuracy + '\x1b[0m')
  print(classification_report(y_test, y_pred))
  print(50 * "-")

  input("press enter to continue...")

  print(50 * "-")
  print('\r')
  print(50 * "-")
  
  ####### User input

  repeat = True

  while(repeat):
    answers = {}

    print('Instert the values for:')

    for item in column_names[1:-1]:
      print(50 * "-")
      print(item + " " + ((49 - len(item)) * '-'))
      print("description:")
      print(description[item])
      print(50 * "-")
      answers.update({item: input(item + ' choice: ')})
      print(50 * "-")

    X_user = np.array([list(answers.values())], dtype=np.int64)
    X_user_std = sc.transform(X_user)

    y_user_pred = ppn.predict(X_user_std)

    print(50 * '-')
    print("Resume:")
    print(50 * '-')
    for answer in answers:
      print(answer + ": " + answers[answer])
    print(50 * '-')

    if int(y_user_pred[0]) == 0:
      print(50 * "\x1b[0;30;41m!\x1b[0m")
      print('\x1b[0;30;41m' + "That profile has a BAD credit risk" + '\x1b[0m')
      print(50 * "\x1b[0;30;41m!\x1b[0m")
    else:
      print(50 * "\x1b[6;30;42m$\x1b[0m")
      print('\x1b[6;30;42m' + "That profile has a GOOD credit risk" + '\x1b[0m')
      print(50 * "\x1b[6;30;42m$\x1b[0m")

    print(50 * '-')
    ans = input('Try again? (y) yes| (n) no: ').lower()
    if(ans == 'y'):
      repeat = True
      print(50 * "-")
      print('\r')
      print(50 * "-")
    elif(ans == 'yes'):
      repeat = True
      print(50 * "-")
      print('\r')
      print(50 * "-")
    else:
      repeat = False

  print('\r')
  print('\x1b[6;30;42m' + 'Programa encerrado com sucesso' + '\x1b[0m')

if __name__ == "__main__":
  main()
