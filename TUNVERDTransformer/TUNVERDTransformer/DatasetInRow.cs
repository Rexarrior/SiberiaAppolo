using CsvHelper.Configuration.Attributes;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TUNVEDTransformer
{
    internal class DatasetInRow
    {
        //Номер продукции;Коды ТН ВЭД ЕАЭС;Технические регламенты;Группа продукции;Общее наименование продукции;ИЛ;Заявитель;Адрес Заявителя;Изготовитель;Страна;Адрес изготовителя;Группа продукции_ordinal;Технические регламенты_ordinal;Коды ТН ВЭД ЕАЭС_ordinal
        [Index(0)]
        public string ID;

        [Index(1)]
        public string ProdNum;
        [Index(2)]
        public string TNVED;
        [Index(3)]
        public string Reglament;
        [Index(4)]
        public string ProdGroup;
        [Index(5)]
        public string ProdName;
        [Index(6)]
        public string IL;
        [Index(7)]
        public string Seller;
        [Index(8)]
        public string SellerAddress;
        [Index(9)]
        public string Manufacturer;
        [Index(10)]
        public string Country;
        [Index(11)]
        public string ManufacturerAddress;
        [Index(12)]
        public string ProdGroupOrdinal;
        [Index(13)]
        public string ReglamentOrdinalk;
        [Index(14)]
        public string TNVEDOrdinal;

    }
}
