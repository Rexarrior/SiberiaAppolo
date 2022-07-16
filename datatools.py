
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder


def preprocess_tnved(all_data_in):
    all_data_in['Коды ТН ВЭД ЕАЭС'] = all_data_in['Коды ТН ВЭД ЕАЭС'].fillna(
        value="Not presented")  # почему-то inplace не работает
    all_data_in['Коды ТН ВЭД ЕАЭС'] = all_data_in['Коды ТН ВЭД ЕАЭС'].astype(
        str)
    all_data_in['Коды ТН ВЭД ЕАЭС'] = all_data_in['Коды ТН ВЭД ЕАЭС'].apply(
        lambda x: remove_replies_from_celll(x))
    return all_data_in


def remove_replies_from_celll(cell, delimiter=";"):
    splitted_cell = [s.strip() for s in cell.split(delimiter)]
    unique_splitted_cell = list(set(splitted_cell))
    result_cell = delimiter.join(unique_splitted_cell)
    return result_cell


def make_columns_categorical(all_data_in,
                             object_cols=['Группа продукции', 'Технические регламенты', 'Коды ТН ВЭД ЕАЭС'],
                             object_cols_target=['Группа продукции_ordinal', 'Технические регламенты_ordinal', 'Коды ТН ВЭД ЕАЭС_ordinal']):
    for col in object_cols:
        count = len(all_data_in[col].value_counts())
        print(f"{col} : {count}")
        all_data_in[col] = all_data_in[col].fillna(
            value="Not presented")  # почему-то inplace не работает
    ordinal_encoder = OrdinalEncoder()
    data_copy = all_data_in.copy()
    all_data_in[object_cols_target] = ordinal_encoder.fit_transform(
        data_copy[object_cols])
    return all_data_in


def make_dataset_categorical(filein, fileout):
    all_data_in = pd.read_excel(filein)
    all_data_in.columns = ['Номер продукции', 'Коды ТН ВЭД ЕАЭС', 'Технические регламенты', 'Группа продукции', 'Общее наименование продукции',
                           'ИЛ', 'Заявитель', 'Адрес Заявителя', 'Изготовитель', 'Страна', 'Адрес изготовителя']
    preprocess_tnved(all_data_in)
    all_data_in = make_columns_categorical(all_data_in)
    all_data_in.to_excel(fileout)
    pass


if __name__ == "__main__":
    dir_hackathon = '.'
    dir_data_in = f'{dir_hackathon}/Data/In'
    dir_data_out = f'{dir_hackathon}/Data/Out'
    make_dataset_categorical(f'{dir_data_in}/dataset.xlsx',
                          f'{dir_data_out}/dateset_categorical.xlsx')
