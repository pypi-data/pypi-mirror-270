import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# class stats_viz:


def stats_info_viz(file_path, file_type, init_column = True):
    """
    Description
    -----------
    This function provides both statistical data and visualizations.

    Params
    ----------
    -- The variable 'file_path' represents the path to a file, which can be either a CSV or Excel file.

    -- The parameter file_type allows for specifying the type of file to be accepted, which can either be "csv" or "excel".

    -- If 'init_column' is set to "True" (default), the calculation will consider the values of the first column in the DataFrame as the initial column.

    -- If 'init_column' is set to "False", the calculation will not consider the values of the first column in the DataFrame as the initial column.
    """
    df = stats_info(file_path, file_type, init_column)
    stats_viz(file_path, file_type)



def stats_info(file_path, file_type, init_column = True):
    """
    Description
    -----------
    This function provides statistical information.

    Params
    ----------
    -- The variable 'file_path' represents the path to a file, which can be either a CSV or Excel file.

    -- The parameter file_type allows for specifying the type of file to be accepted, which can either be "csv" or "excel".

    -- If 'init_column' is set to "True" (default), the calculation will consider the values of the first column in the DataFrame as the initial column.

    -- If 'init_column' is set to "False", the calculation will not consider the values of the first column in the DataFrame as the initial column.
    """
    if init_column == True:
        if file_type == "csv":
            df = pd.read_csv(file_path)
            print("Total Number of Rows: ",df.shape[0])
            print("Total number of columns: ", df.shape[1])
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Null Values"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                print("{:<20}{}".format(i, df[i].isna().sum()))
            print("-----------------------------------------")

            print("{:<20}{}".format("Columns", "Non-Null Values"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                print("{:<20}{}".format(i, df[i].count()))
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Mean"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                    print("{:<20}{}".format(i, df[i].mean()))
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Median"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                    print("{:<20}{}".format(i, df[i].median()))
            print("-----------------------------------------")

        elif file_type == "excel":
            df = pd.read_excel(file_path)
            print("Total Number of Rows: ",df.shape[0])
            print("Total number of columns: ", df.shape[1])
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Null Values"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                print("{:<20}{}".format(i, df[i].isna().sum()))
            print("-----------------------------------------")

            print("{:<20}{}".format("Columns", "Non-Null Values"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                print("{:<20}{}".format(i, df[i].count()))
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Mean"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                    print("{:<20}{}".format(i, df[i].mean()))
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Median"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                    print("{:<20}{}".format(i, df[i].median()))
            print("-----------------------------------------")

    elif init_column == False:
        if file_type == "csv":
            df = pd.read_csv(file_path)
            df.drop(df.columns[0], axis=1, inplace=True)
            print("Total Number of Rows: ",df.shape[0])
            print("Total number of columns: ", df.shape[1])
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Null Values"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                print("{:<20}{}".format(i, df[i].isna().sum()))
            print("-----------------------------------------")

            print("{:<20}{}".format("Columns", "Non-Null Values"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                print("{:<20}{}".format(i, df[i].count()))
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Mean"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                    print("{:<20}{}".format(i, df[i].mean()))
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Median"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                    print("{:<20}{}".format(i, df[i].median()))
            print("-----------------------------------------")

        elif file_type == "excel":
            df = pd.read_excel(file_path)
            df.drop(df.columns[0], axis=1, inplace=True)
            print("Total Number of Rows: ",df.shape[0])
            print("Total number of columns: ", df.shape[1])
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Null Values"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                print("{:<20}{}".format(i, df[i].isna().sum()))
            print("-----------------------------------------")

            print("{:<20}{}".format("Columns", "Non-Null Values"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                print("{:<20}{}".format(i, df[i].count()))
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Mean"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                    print("{:<20}{}".format(i, df[i].mean()))
            print("-----------------------------------------")


            print("{:<20}{}".format("Columns", "Median"))
            print("{:<20}{}".format("------------", "------------"))
            for i in df.columns:
                if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                    print("{:<20}{}".format(i, df[i].median()))
            print("-----------------------------------------")

    return df

def stats_viz(file_path, file_type):
    """
    Description
    -----------
    This function provides statistical visualizations.

    Params
    ----------
    -- The variable 'file_path' represents the path to a file, which can be either a CSV or Excel file.

    -- The parameter file_type allows for specifying the type of file to be accepted, which can either be "csv" or "excel".

    """
    if file_type == "csv":
        df = pd.read_csv(file_path)
        print("Data Distribution Plot")
        cols = []
        for i in df.columns:
            if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                cols.append(i)

        plt.figure(figsize=(10, 8))
        for column in cols:
            sns.histplot(df[column], kde=True, label=column)
            plt.title(f"Data distribution of {column}")
            plt.xlabel("Values")
            plt.ylabel("Frequency")
            plt.xticks(rotation=45)
            plt.show()

        print("Box Plot")
        plt.figure(figsize=(10, 8))
        sns.boxplot(data=df)
        plt.title("Box Plot")
        plt.xlabel("Columns")
        plt.ylabel("Values")
        plt.xticks(rotation=45)
        plt.show()

        print("Cumulative Distribution Functions (CDFs)")
        plt.figure(figsize=(10, 8))

        for column in cols:
            sns.kdeplot(df[column], cumulative=True, label=column)

            plt.title(f'Cumulative Distribution Functions (CDFs) for {column}')
            plt.xlabel('Values')
            plt.ylabel('Cumulative Probability')
            plt.xticks(rotation=45)
            plt.show()

    elif file_type == "excel":
        df = pd.read_excel(file_path)
        print("Data Distribution Plot")
        cols = []
        for i in df.columns:
            if df[i].dtype == "int" or df[i].dtype == "int32" or df[i].dtype == "int64" or df[i].dtype == "float" or df[i].dtype == "float32" or df[i].dtype == "float64":
                cols.append(i)

        plt.figure(figsize=(10, 8))
        for column in cols:
            sns.histplot(df[column], kde=True, label=column)
            plt.title(f"Data distribution of {column}")
            plt.xlabel("Values")
            plt.ylabel("Frequency")
            plt.xticks(rotation=45)
            plt.show()

        print("Box Plot")
        plt.figure(figsize=(10, 8))
        sns.boxplot(data=df)
        plt.title("Box Plot")
        plt.xlabel("Columns")
        plt.ylabel("Values")
        plt.xticks(rotation=45)
        plt.show()

        print("Cumulative Distribution Functions (CDFs)")
        plt.figure(figsize=(10, 8))

        for column in cols:
            sns.kdeplot(df[column], cumulative=True, label=column)

            plt.title(f'Cumulative Distribution Functions (CDFs) for {column}')
            plt.xlabel('Values')
            plt.ylabel('Cumulative Probability')
            plt.xticks(rotation=45)
            plt.show()

# obj = stats_viz()
# obj.stats_info_viz('Advertising_data.csv', file_type='csv', init_column=True)