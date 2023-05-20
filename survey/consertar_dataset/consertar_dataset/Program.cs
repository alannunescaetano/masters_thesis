
using System.Text.RegularExpressions;

string[] files = Directory.GetFiles("C:\\Projetos\\Mestrado\\pavement_defects_dataset", "Japan*.txt", SearchOption.AllDirectories);

foreach (string file in files)
{
    string[] lines = File.ReadAllLines(file);

    for (int i = 0; i < lines.Length; i++)
    {
        if (lines[i].StartsWith("4") || lines[i].StartsWith("5") || lines[i].StartsWith("6") || lines[i].StartsWith("7"))
        {
            lines[i] = string.Empty;
        }

        /*if (lines[i].StartsWith("3"))
        {
            var regex = new Regex(Regex.Escape("3"));
            lines[i] = regex.Replace(lines[i], "1", 1);
        }

        if (lines[i].StartsWith("5"))
        {
            var regex = new Regex(Regex.Escape("5"));
            lines[i] = regex.Replace(lines[i], "2", 1);
        }

        if (lines[i].StartsWith("6"))
        {
            var regex = new Regex(Regex.Escape("6"));
            lines[i] = regex.Replace(lines[i], "3", 1);
        }*/

        File.WriteAllLines(file, lines);
    }
}

