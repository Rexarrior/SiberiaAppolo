using CsvHelper;
using CsvHelper.Configuration;
using System;
using System.Globalization;
using System.Text;

namespace TUNVEDTransformer
{
    public  class Program
    {
        public static Dictionary<string, string> LoadTNVEDFileAndDropNotNeededColumns(string filename)
        {
            var lines = File.ReadAllLines(filename);
            var actualCodes = lines.Skip(1).Select(line => line.Split('|')).Where(lst => string.IsNullOrEmpty(lst[5].Trim()));
            var keyValuePairs = actualCodes.Select(lst => KeyValuePair.Create(string.Join("", lst.Take(3)), lst[3]));
            var dict = new Dictionary<string, string>(keyValuePairs);
            return dict;
        }


        public static void Main(string[] args)
        {
            string notPresentedTnvecClaster = "6798";
            string infile = args[0];
            string outFile = args[2];
            string tunved4Filename = args[1];
            var tunved_dict = LoadTNVEDFileAndDropNotNeededColumns(tunved4Filename);
            var config = new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                Delimiter = ";",

            };
            List<List<string>> rowsIn = new List<List<string>>();
            string[] header;
            using (var reader = new StreamReader(infile))
            using (var csv = new CsvReader(reader, config))
            {
                csv.Read();
                csv.ReadHeader();
                header = csv.HeaderRecord.ToArray();
                while (csv.Read())
                {
                    rowsIn.Add(new List<string>());
                    for (int i = 0; i < header.Length; i++)
                        rowsIn[rowsIn.Count - 1].Add(csv.GetField(i));
                }
            }

            int count = 0;
            var rowsOut = new List<List<string>>();
            foreach (var row in rowsIn)
            {
                var oneTnVed = row[2];
                oneTnVed = oneTnVed.Split(";").Distinct().Where(x => tunved_dict.ContainsKey(x)).FirstOrDefault();
                //oneTnVed = oneTnVed.Split(";")[0];
                if (oneTnVed == null || !tunved_dict.ContainsKey(oneTnVed))
                {
                    row[2] = "Not presented";
                    row.Add("NotPresented");
                    row[14] = notPresentedTnvecClaster;
                }
                else
                {
                    row.Add(tunved_dict[oneTnVed]);
                    row[2] = oneTnVed;
                    count++;
                }
                rowsOut.Add(row);

            }

            using (var writer = new StreamWriter(outFile))
            using (var csv = new CsvWriter(writer, config))
            {
                csv.NextRecord();
                foreach (var str in header)
                {
                    csv.WriteField(str);
                }
                csv.NextRecord();
                foreach (var record in rowsOut)
                {
                    foreach (var str in record)
                    {
                        csv.WriteField(str);
                    }
                    csv.NextRecord();
                }

            }
        }
    }


}