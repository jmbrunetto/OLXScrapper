import pandas as pd

def dict_to_csv(dict_list, file_path):
    pd.DataFrame(dict_list).to_csv(file_path, index=False, mode='a')


class Utils:

    def extract_url_parameters(self, full_url):
        url = full_url.split("?")
        base_url = url[0]
        parameters = url[1]
        parameters_raw_list = parameters.split("&")
        result_list = []
        for parameter in parameters_raw_list:
            result = parameter.split('=')
            result_dict = {result[0]:result[1]}
            # print ("Chave {} Valor {}".format(result[0], result[1]))
            result_list.append(result_dict)
        return result_list
