import unittest
import spongebox.plotbox as plotbox
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plot


class MyTestCase(unittest.TestCase):
    def test_grid_dataset(self):
        df = plotbox.samples()
        # print(df)
        col_order = "US,JP,CN".split(",")
        shape, data_lst = plotbox.grid_datasets(df, "nation", col_order)
        print(shape)
        print(data_lst[0])

    def test_col_aspect_countplot(self):
        plotbox.grid_plot_2dim(sns.countplot, plotbox.samples(), "race", "nation", col_wrap=2, col_order="US,JP,CN".split(","), hue="gender")

    def test_col_aspect_lineplot(self):
        df = plotbox.samples()
        # print(df)
        df = df.groupby(["company"]).resample("D").mean()["score1"].reset_index()
        df.rename(columns={"level_1": "biz_date"}, inplace=True)
        print(df)
        # sns.lineplot(data = pd.DataFrame([[0,1],[2,3]],columns=list("ab")),x="a",y="b")
        # sns.lineplot(data=df[df.company=="Dell"],x="biz_date",y="score1")
        # plot.show()
        # plotbox.grid_plot_2dim(sns.lineplot, df, "biz_date","company", y="score1", col_wrap=2)
        g = sns.FacetGrid(data=df, col="company", col_wrap=2)
        g.map(sns.lineplot, "biz_date", "score1")
        plot.show()

    def test_spongebob_countplot(self):
        df = plotbox.samples()
        print(df)
        f, axe = plot.subplots(1, 1)
        print(plotbox.spongebob_countplot(df, "race", axe, hue="level", normalize=True,legend=True,norminal=True))
        plot.show()


if __name__ == '__main__':
    unittest.main()
