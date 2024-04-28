import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math
from collections import namedtuple

# # 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# sns.set(font='SimHei')  # 解决Seaborn中文显示问题

def samples(n_samples=100):
    # 确保复现
    np.random.seed(0)

    def __group__(group_name):
        # 组
        group_series = [group_name for i in range(n_samples)]

        # 连续的时间序列
        time_series = pd.date_range("2019-01-01", periods=n_samples, freq="1D20min")

        # 随机字符串序列1 -- norminal variable
        char1_series = [np.random.choice(list("ABCDEF")) for _ in range(n_samples)]

        # 随机字符串序列2 -- norminal variable
        # char2_series = [np.random.choice(list("MF")) for _ in range(n_samples)]
        char2_series = np.random.choice(list("MF"), size=n_samples, replace=True)

        # 随机字符串序列3 -- norminal variable
        char3_series = [np.random.choice("US,JP,CN".split(",")) for _ in range(n_samples)]

        # 随机整数序列 -- ordinal variable
        int_series = np.random.randint(0, 5, n_samples)

        # 随机浮点数序列1 -- ratio variable
        float1_series = 0 + np.random.rand(n_samples) * 100

        # 随机浮点数序列2 -- ratio variable
        float2_series = 0 + np.random.rand(n_samples) * 100

        # 构造dataframe
        df = pd.DataFrame({"company": group_series, "race": char1_series, "gender": char2_series, "nation": char3_series, "level": int_series, "score1": float1_series, "score2": float2_series})
        df.index = time_series

        return df

    return pd.concat([__group__("Dell"), __group__("Google"), __group__("Tesla")])


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plot.text(rect.get_x() + rect.get_width() / 2. -
                  0.2, 1.03 * height, '%s' % float(height))


'''
def countplot(x, data, hue=None, prop=False, sort_by="count", ascending=False):
    _ = data.fillna("").groupby(x).count().reset_index()
    # print(_.head(1))
    _.rename(columns={_.columns[1]: "count"}, inplace=True)
    if sort_by != None:
        _.sort_values(sort_by, ascending=ascending, inplace=True)
        _.reset_index(inplace=True, drop=True)
    # print(_.head(1))
    total = _.iloc[:, 1].sum() * 1.0
    _["display"] = _.iloc[:, 1]
    if prop:
        _["display"] = _.iloc[:, 1].apply(
            lambda x: str(int(round(x / total * 100))) + "%")
    # add fake col to normalize the bar's sequences
    _[" " + x + " "] = _[x].apply(lambda x: "" + str(x))
    g = sns.barplot(x=" " + x + " ", y=_.columns[1], data=_, hue=hue)
    # 在柱状图的上面显示各个类别的数量
    for index, row in _.iterrows():
        # 在柱状图上绘制该类别的数量
        g.text(row.name, row[1], row.display, color="black", ha="center")
'''


# def init_grid(df, col=None, row=None, col_wrap=4):
#     # 规划axes
#     n_axes, row_wrap = 1
#     if col:
#         n_axes = df[col].nunique()
#         if row:
#             n_axes = df[row].nunique() * df[col].nunique()
#             row_wrap = df[row].nunique()
#         else:
#             row_wrap = int(np.ceil(df[col].nunique() / col_wrap))
#     print("init axes:()".format(row_wrap, col_wrap))
#     f, axes = plot.subplots(row_wrap, col_wrap, figsize=(12, 6), sharey=True, sharex=True)
#     # 对于单一维度（col）的情形，删除多余子图
#     if not row:
#         if col:
#             # 删除多余子图
#             for i in range(n_axes % col_wrap, col_wrap):
#                 f.delaxes(axes[row_wrap - 1, i])
#             # 设置导数第二行子图强制显示坐标轴
#             for i in range(n_axes % col_wrap, col_wrap):
#                 axes[row_wrap - 2, i].tick_params(axis="x")
#     return f, axes


# def init_dataset(df, col=None, row=None, row_order=None, col_order=None):
#     data_in_aspect = []
#     if row:
#         row_order = row_order if row_order else df[row].unique_values()
#     if col:
#         col_order = col_order if col_order else df[col].unique_values()
#     if row:
#         for row_val in row_order:
#             for col_val in col_order:
#                 data_in_aspect.append(df[(df[row] == row_val) & (df[col] == col_val)])
#     else:
#         if col:
#             for col_val in col_order:
#                 data_in_aspect.append(df[df[col] == col_val])
#         else:
#             data_in_aspect.append(df)
#     return data_in_aspect


# def grid_plot(df, x, y, plot_func, col=None, row=None, hue=None, col_wrap=4, row_order=None, col_order=None, hue_order=None):
#     f, axes = init_grid(df, col, row, col_wrap)
#     data_in_aspect = init_dataset(df, col, row, row_order, col_order)
#     for axe in axes:
#         plot_func(df, x, y, hue, axe)


# def grid_datasets(df, col, col_order=None, col_wrap=None, row=None, row_order=None):
#     row_wrap, col_wrap, rows, _ = 0, 0, [], []
#     cols = col_order if col_order else np.sort(df[col].unique())
#     if row:
#         rows = row_order if row_order else np.sort(df[row].unique())
#         for row_val in rows:
#             for col_val in cols:
#                 _.append(df[(df[row] == row_val) & (df[col] == col_val)])
#     else:
#         for col_val in cols:
#             _.append(df[df[col] == col_val])
#     return (len(rows) if len(rows) else 1, len(cols)), _


# def grid_subplots(shape, col_wrap=None, share_x=False, share_y=False):
#     if shape[0] == 1 and col_wrap:
#         # 重塑reshape
#         row_wrap = math.ceil(shape[1] / col_wrap)
#         col_wrap = shape[1] if shape[1] < col_wrap else col_wrap
#     else:
#         row_wrap, col_wrap = shape
#     fig, axes = plot.subplots(row_wrap, col_wrap, sharex=share_x, sharey=share_y)
#     # 移除多余子图
#     if row_wrap > 1 and share_x and shape[0] == 1:
#         for i in range(shape[1] % col_wrap, col_wrap):
#             # 若共享x轴，移除多余子图，需在倒数第二行补轴
#             fig.delaxes(axes[row_wrap - 1, i])
#             # if share_x and (row_wrap * col_wrap) % col_wrap:
#             axes[row_wrap - 2, i].xaxis.set_tick_params(which="both", labelbottom=True)
#             # axes[row_wrap-2,i].tick_params(axis="x")
#     return fig, axes


# def grid_plot_2dim(plot_func, df, x, col, y=None, row=None, hue=None, row_order=None, col_order=None, col_wrap=4, x_label_alias=None, x_order=None, x_label_rotation=None, share_x=True, share_y=True):
#     shape, datasets = grid_datasets(df, col, col_order=col_order, row=row, row_order=row_order)
#     f, axes = grid_subplots(shape, col_wrap=col_wrap, share_x=share_x, share_y=share_y)
#     if len(axes.shape) > 1:
#         for i in range(0, len(datasets)):
#             row_idx, col_idx = int(i / col_wrap), i % col_wrap
#             plot_func(data=datasets[row_idx * col_wrap + col_idx], x=x, y=y, hue=hue, ax=axes[row_idx, col_idx])
#     else:
#         for col_idx in range(0, axes.shape[0]):
#             plot_func(data=datasets[col_idx], x=x, y=y, hue=hue, ax=axes[col_idx])
#     plot.show()


def categorical(data, categories):
    for col, cat in categories.items():
        if cat:
            data[col] = pd.Categorical(data[col], categories=cat, ordered=True)
        else:
            data[col] = data[col].astype("category")
            # data.loc[:,col] = data[col].astype("category")
            # TO-DO
            # 采用loc()的方法无法转变为category类型，原因未知
            # print(data[col].dtype)
    return data


def categorical1(data, categories):
    for col, cat in categories.items():
        if cat:
            data.loc[:, col] = pd.Series(pd.Categorical(data[col], categories=cat, ordered=True))
        else:
            data.loc[:, col] = pd.Series(data[col].astype("category"))
    return data


class FacetGrid:

    def __init__(self, data=None, row=None, col=None, hue=None, col_wrap=None, sharex=False, sharey=False, margin_title=True, **kwargs):
        groupers = [col]
        row_wrap = 1
        if row:
            row_wrap = data[row].nunique()
            col_wrap = data[col].nunique()
            groupers.append(row)
        else:
            row_wrap = math.ceil(data[col].nunique() / col_wrap)
        self.shape = (row_wrap, col_wrap)
        self.row = row
        self.col = col
        self.hue = hue
        self.sharex = sharex
        self.sharey = sharey
        self.margin_title = margin_title
        self.kwargs = kwargs

        _ = []
        for g_idx, g in data.groupby(groupers):
            _.append({"idx": g_idx})
        self.grid_index = np.array(_).reshape(self.shape)
        print(self.grid_index)
        self.data = data.set_index(groupers).sort_index()

        # TO-DO
        # 绘制标题

    def loc(self, i, j):
        return self.grid_index[i, j]["idx"]

    def map(self, plot_func, **kwargs):
        f, axes = plt.subplots(*self.shape, sharex=self.sharex, sharey=self.sharey)

        if self.shape[0] > 1:
            for i in range(0, self.shape[0]):
                for j in range(0, self.shape[1]):
                    # print(self.data.loc[self.grid_index[i,j]["idx"]])
                    plot_func(data=self.data.loc[self.grid_index[i, j]["idx"]], hue=self.hue, ax=axes[i, j], **kwargs)
        else:
            for col_idx in range(0, sel):
                plot_func(data=self.data, x=x, y=y, hue=hue, ax=axes[col_idx])

        # 绘制标题
        if self.margin_title:
            for col_idx in range(self.shape[1]):
                axes[0, col_idx].set_title("{}={}".format(self.col, self.loc(0, col_idx)[1]))
            if self.row:
                for row_idx in range(self.shape[0]):
                    # print("xlim,ylim",axes[row_idx,-1].get_xlim()[1],axes[row_idx,-1].get_ylim()[1]/2)
                    axes[row_idx, -1].text(axes[row_idx, -1].get_xlim()[1], axes[row_idx, -1].get_ylim()[1] / 2, "{}={}".format(self.row, self.loc(row_idx, 0)[0]), size=12, verticalalignment='center', rotation=270)
        else:
            for row_idx in range(0, self.shape[0]):
                for col_idx in range(0, self.shape[1]):
                    axes[row_idx, col_idx].set_title("{}={}|{}={}".format(self.row, self.loc(row_idx, col_idx)[0], self.col, self.loc(row_idx, col_idx)[1]))


def countplot(data=None, x=None, hue=None, normalize=False, ax=None, cluster_width=0.8, legend=False, annotation=False):
    if hue:
        _ = []
        for hue_val in data[hue].cat.categories:
            _.append(data.query("{}=='{}'".format(hue, hue_val))[x].value_counts(normalize=normalize).sort_index().rename(hue_val))
        t = pd.concat(_, axis=1)
        # print(t)
    else:
        t = pd.DataFrame(data[x].value_counts(normalize=normalize).sort_index())

    x_location, bar_width = np.arange(t.shape[0]), cluster_width / t.shape[1]
    for i in range(0, t.shape[1]):
        rects = ax.bar(x_location + i * bar_width - (cluster_width / 2 - bar_width / 2), t.iloc[:, i], width=bar_width, label=t.columns[i])
        if annotation:
            ax.bar_label(rects, padding=3)
    if legend:
        ax.legend(loc='upper right')

    # print(x_location,data[x].cat.categories)
    ax.set_xticks(x_location, data[x].cat.categories)
    # print("xlim,ylim",ax.get_xlim()[1],ax.get_ylim()[1]/2)
    return t


if __name__ == "__main__":
    df = samples()
    df = categorical(data=df, categories={"race": list("ACEBDFG"), "gender": None})
    print(df.dtypes)
    g = FacetGrid(data=df, row="nation", col="company", hue="gender", sharey=True, margin_title=True)
    # print(g.grid_index)
    # print(g.data)
    g.map(countplot, x="race", normalize=True)
    plt.show()

    # f,axes = plot.subplots(1,1)
    # spongebob_countplot(dataset=df,x="race",ax=axes,hue=None,legend=True,categories=list("ACEBDFG"),hue_categories=None)
    # plot.show()
    # f,axes = plot.subplots(1,1)
    # spongebob_countplot(dataset=df,x="race",ax=axes,hue="gender",legend=True,categories=list("ACEBDFG"),hue_categories=list("MF"),normalize=True,annotation=False)
    # plot.show()

    # 绘制标题
    # if margin_title:
    #     for col_idx in range(len(cols)):
    #         axes[0,col_idx].set_title("{}={}".format(col,cols[col_idx]))
    #     for row_idx in range(len(rows)):
    #         axes[row_idx,-1].text(axes[row_idx,-1].get_xlim()[1],axes[row_idx,-1].get_ylim()[1]/2,"{}={}".format(row,rows[row_idx]), size=12, verticalalignment='center', rotation=270)
    # else:
    #     for col_idx in range(len(cols)):
    #         axes[row_idx,col_idx].set_title("{}={}|{}={}".format(row,rows[row_idx],col,cols[col_idx]))

    # # 绘制共享图例
    # if sharelegend:
    #     handles_list=[]
    #     labels_list=[]
    #     for ax in figure.axes:
    #         try:
    #             handles, labels = ax.get_legend_handles_labels()
    #             ax.get_legend().remove()
    #             handles_list.extend(handles)
    #             labels_list.extend(labels)
    #         except AttributeError as e:
    #             pass
    #     if handles_list:
    #         unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
    #         figure.legend(*zip(*unique), loc="center right",title=hue)
