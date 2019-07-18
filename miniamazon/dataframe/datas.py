#IMPORTS :
import os
import pandas as pd


class Main:
    os.chdir('C://Users//Dheeraj//PycharmProjects//miniamazon//csvs')

    def __init__(self):
        self.all_data = {}
        for file in os.listdir(os.getcwd()):
            self.all_data[file[0:-4]] = pd.read_csv('C://Users//Dheeraj//PycharmProjects//miniamazon//csvs//' + file)

    def get_cat(self, types, arguments):
        data = self.all_data[types]
        for args in arguments:
            if arguments[args].isdigit():
                data = data.loc[data[args] == float(arguments[args])]
            else:
                data = data.loc[data[args] == arguments[args]]
        return data.set_index('ITEM NO.').T.to_dict(orient="dict")



    @staticmethod
    def get_pro(types, name):
        if name in types:
            return types[types['PRODUCT'] == name]
        else:
            return 'Product is not yet launched in our E-Market.'
