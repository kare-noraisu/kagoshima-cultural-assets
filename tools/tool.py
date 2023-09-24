import pandas as pd
def main():
    f1='file.csv'
    df1=pd.read_csv(f1,usecols=['所在地等'])
    #for column_name,item in df1.iteritems():
    #print(f'[df1]type:[type(column_name)],value:[column_name]')
    #print(f'[item]type:[type(item)],value:')
    print(df1)
    df1.drop_duplicates().to_csv('output.csv',index=False,encoding='utf-8-sig')
main()