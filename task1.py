import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    pd.read_csv(file)

def exercise_1(df):
    col_names = df.columns.tolist()

def exercise_2(df, k):
    k_rows = df.iloc[:k]

def exercise_3(df, k):
    df2 = df.sample(n=k)

def exercise_4(df):
    unique_list = df.type.unique().tolist()

def exercise_5(df):
    transac_destn = df.nameDest.value_counts()[:10]

def exercise_6(df):
    df_rows = df.loc[df["isFraud"]==1]

def exercise_7(df):
    df_bonus = df[df.groupby('nameDest')['nameOrig'].transform('nunique').gt(20)]

def visual_1(df):
    def transaction_counts(df):
        # TODO
        transac_destn = df.nameDest.value_counts()[:10]
        pass
    def transaction_counts_split_by_fraud(df):
        # TODO
        fig = plt.figure(figsize = (10, 5))
        transaction_type = df["type"].tolist()
        transaction_type = transaction_counts(transaction_type)
        isfraud = df["isFraud"].tolist()
        plt.bar(transaction_type,isfraud, width=0.4);
        plt.title("Transaction type bar chart")
        plt.xlabel("Transaction Types")
        plt.ylabel("Is Fraud")
        plt.show()
        pass

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('TODO')
    axs[0].set_xlabel('TODO')
    axs[0].set_ylabel('TODO')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('TODO')
    axs[1].set_xlabel('TODO')
    axs[1].set_ylabel('TODO')
    fig.suptitle('TODO')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'TODO'

def visual_2(df):
    def query(df):
        fig = plt.figure(figsize = (10, 5))
        balance_orig = (df["newbalanceOrig"] - df["oldbalanceOrig"]).tolist()
        balance_dest = (df["newbalanceDest"] - df['oldbalanceDest']).tolist()
        plot.scatter(balance_orig, balance_dest, width=0.4);
        plot.title("Cash out transactions")
        plot.xlabel("Balance Source")
        plot.ylabel("Balance Destination")
        plot.show()
        pass
    plot = query(df).plot.scatter(x='TODO',y='TODO')
    plot.set_title('TODO')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'TODO'

def exercise_custom(df):
    df_rows = df.loc[df["isFlaggedFraud"]==1 and df["isFraud"]==0];
    
def visual_custom(df):
    def transaction_counts_split_by_flagged_fraud(df): 
        fig = plt.figure(figsize = (10, 5))
        transaction_type = df["type"].tolist()
        transaction_type = df.nameDest.value_counts()[:10]
        isfraud = df["isFlaggedFraud"].tolist()
        plt.bar(transaction_type,isfraud, width=0.4);
        plt.title("Transaction type bar chart")
        plt.xlabel("Transaction Types")
        plt.ylabel("Is Flagged Fraud")
        plt.show()
        pass

    fig, axs = plt.subplots(2, figsize=(6,10))
    axs[0].set_title('TODO')
    axs[0].set_xlabel('TODO')
    axs[0].set_ylabel('TODO')
    transaction_counts_split_by_flagged_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('TODO')
    axs[1].set_xlabel('TODO')
    axs[1].set_ylabel('TODO')
    fig.suptitle('TODO')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'TODO'
df = exercise_0('Task_1/transactions.csv')