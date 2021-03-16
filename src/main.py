from sqlalchemy import create_engine
import pandas as pd
import os

config = {
  'user': 'root',
  'password': 'toor',
  'host': 'DMAX101Sofia.local',
  'port': 6603,
  'database': 'statlog'
}

def main():

    db_connection_str = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
      config['user'],
      config['password'],
      config['host'],
      config['port'],
      config['database'])

    
    codetable = open('documents//codetable.txt', 'rt')
    lines = codetable.readlines()
    german_english = {}
    
    for line in lines:
      if('$' in line.strip()):
        line_splited = line.strip()[2:-1].split()
        german_english.update({line_splited[0]: line_splited[2]})

    print(german_english)

    db_connection = create_engine(db_connection_str)

    column_names = ['id', 'status', 'duration', 'credit_history', 'purpose', 'amount', 'savings', 'employment_duration', 'installment_rate', 'personal_status_sex', 'other_debtors', 'present_residence', 'property', 'age', 'other_installment_plans', 'housing', 'number_credits', 'job', 'people_liable', 'telephone', 'foreign_worker', 'credit_risk']

    df = pd.read_sql('SELECT * FROM germancredit', con=db_connection)

    df.columns = column_names

    print(df.head())

    

if __name__ == "__main__":
    main()