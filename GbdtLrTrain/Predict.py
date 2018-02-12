import numpy as np
from scipy.sparse.construct import hstack
from sklearn.datasets.svmlight_format import load_svmlight_file
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing.data import OneHotEncoder
from tornado.web import RequestHandler

from GbdtLrTrain.DataHandle import singleton, DataHandle


@singleton
class Predict():
    def __init__(self):
        self.gbdt = GradientBoostingClassifier(n_estimators=40, max_depth=3, verbose=0, max_features=0.5)
        self.lr = LogisticRegression(n_jobs=-1)
        Train_tab = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0,
                     0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0,
                     0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                     0,
                     0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0,
                     0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Train_libsvm = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 1, 2, 2], [1, 1, 1, 1, 3, 1], [2, 2, 2, 1, 4, 1],
                        [3, 3, 2, 1, 5, 2],
                        [2, 2, 2, 1, 6, 1], [4, 4, 3, 1, 6, 2], [5, 5, 3, 1, 7, 2], [2, 2, 2, 1, 8, 1],
                        [2, 2, 2, 1, 6, 1],
                        [2, 2, 2, 1, 9, 2], [6, 6, 2, 1, 8, 3], [1, 1, 1, 1, 10, 1], [2, 2, 2, 1, 4, 2],
                        [2, 2, 2, 1, 4, 1],
                        [2, 2, 2, 1, 10, 2], [1, 1, 1, 1, 8, 1], [1, 1, 1, 1, 11, 1], [2, 2, 2, 1, 12, 1],
                        [2, 2, 2, 1, 2, 1],
                        [5, 5, 3, 1, 13, 2], [2, 2, 2, 1, 14, 1], [7, 7, 2, 1, 15, 2], [1, 1, 1, 1, 16, 1],
                        [1, 1, 1, 1, 8, 1],
                        [1, 1, 1, 1, 17, 1], [5, 5, 3, 1, 18, 2], [2, 2, 2, 1, 19, 2], [1, 1, 1, 1, 2, 1],
                        [2, 2, 2, 1, 20, 1],
                        [2, 2, 2, 1, 10, 1], [2, 2, 2, 1, 14, 2], [5, 5, 3, 1, 15, 2], [5, 5, 3, 1, 21, 2],
                        [2, 2, 2, 1, 21, 1],
                        [1, 1, 1, 1, 22, 1], [6, 6, 2, 1, 5, 2], [2, 2, 2, 1, 1, 2], [8, 8, 2, 1, 15, 3],
                        [4, 4, 3, 1, 23, 2],
                        [9, 9, 2, 2, 6, 2], [1, 1, 1, 1, 21, 1], [2, 2, 2, 1, 10, 2], [5, 5, 3, 1, 24, 2],
                        [2, 2, 2, 1, 20, 1],
                        [2, 2, 2, 1, 8, 1], [5, 5, 3, 1, 2, 2], [6, 6, 2, 1, 3, 3], [1, 1, 1, 1, 19, 1],
                        [2, 2, 2, 1, 12, 2],
                        [2, 2, 2, 1, 25, 1], [1, 1, 1, 1, 2, 1], [4, 4, 3, 1, 11, 2], [2, 2, 2, 1, 10, 1],
                        [1, 1, 1, 1, 21, 1],
                        [2, 2, 2, 1, 14, 2], [1, 1, 1, 1, 19, 1], [2, 2, 2, 1, 14, 1], [2, 2, 2, 1, 9, 1],
                        [2, 2, 2, 1, 20, 2],
                        [2, 2, 2, 1, 4, 2], [1, 1, 1, 1, 4, 1], [2, 2, 2, 1, 26, 1], [2, 2, 2, 1, 14, 1],
                        [2, 2, 2, 1, 4, 2],
                        [2, 2, 2, 1, 23, 1], [5, 5, 3, 1, 13, 2], [3, 3, 2, 1, 22, 2], [2, 2, 2, 1, 11, 2],
                        [2, 2, 2, 1, 1, 2],
                        [2, 2, 2, 1, 9, 1], [1, 1, 1, 1, 9, 1], [2, 2, 2, 1, 12, 2], [2, 2, 2, 1, 20, 1],
                        [2, 2, 2, 1, 1, 2],
                        [1, 1, 1, 1, 14, 1], [10, 10, 2, 1, 23, 3], [5, 5, 3, 1, 21, 2], [1, 1, 1, 1, 1, 1],
                        [2, 2, 2, 1, 19, 2],
                        [1, 1, 1, 1, 23, 1], [2, 2, 2, 1, 20, 1], [1, 1, 1, 1, 14, 1], [4, 4, 3, 1, 11, 2],
                        [2, 2, 2, 1, 19, 1],
                        [5, 5, 3, 1, 19, 2], [2, 2, 2, 1, 1, 2], [2, 2, 2, 1, 14, 1], [11, 11, 2, 1, 10, 1],
                        [2, 2, 2, 1, 14, 2],
                        [1, 1, 1, 1, 22, 1], [9, 9, 2, 2, 27, 2], [4, 4, 3, 1, 1, 2], [4, 4, 3, 1, 12, 2],
                        [2, 2, 2, 1, 6, 1],
                        [4, 4, 3, 1, 8, 2], [1, 1, 1, 1, 16, 1], [1, 1, 1, 1, 28, 1], [2, 2, 2, 1, 15, 2],
                        [1, 1, 1, 1, 3, 1],
                        [2, 2, 2, 1, 14, 1], [1, 1, 1, 1, 21, 1], [2, 2, 2, 1, 24, 2], [2, 2, 2, 1, 23, 1],
                        [2, 2, 2, 1, 8, 1],
                        [2, 2, 2, 1, 21, 2], [6, 6, 2, 1, 6, 2], [1, 1, 1, 1, 2, 1], [2, 2, 2, 1, 12, 1],
                        [5, 5, 3, 1, 23, 2],
                        [1, 1, 1, 1, 29, 1], [1, 1, 1, 1, 8, 1], [4, 4, 3, 1, 2, 2], [1, 1, 1, 1, 8, 1],
                        [1, 1, 1, 1, 30, 1],
                        [2, 2, 2, 1, 8, 1], [1, 1, 1, 1, 8, 1], [4, 4, 3, 1, 23, 2], [5, 5, 3, 1, 9, 2],
                        [4, 4, 3, 1, 1, 2],
                        [9, 9, 2, 2, 19, 2], [1, 1, 1, 1, 11, 1], [2, 2, 2, 1, 1, 2], [10, 10, 2, 1, 30, 1],
                        [9, 9, 2, 2, 24, 2],
                        [5, 5, 3, 1, 14, 2], [2, 2, 2, 1, 4, 1], [2, 2, 2, 1, 22, 2], [2, 2, 2, 1, 26, 1],
                        [2, 2, 2, 1, 14, 1],
                        [2, 2, 2, 1, 1, 1], [4, 4, 3, 1, 2, 2], [3, 3, 2, 1, 29, 2], [2, 2, 2, 1, 6, 2],
                        [2, 2, 2, 1, 9, 2],
                        [2, 2, 2, 1, 16, 2], [5, 5, 3, 1, 13, 2], [13, 13, 2, 1, 3, 2], [2, 2, 2, 1, 27, 1],
                        [2, 2, 2, 1, 1, 2],
                        [2, 2, 2, 1, 4, 1], [2, 2, 2, 1, 1, 2], [2, 2, 2, 1, 29, 2], [3, 3, 2, 1, 12, 2],
                        [2, 2, 2, 1, 2, 2],
                        [2, 2, 2, 1, 5, 1], [5, 5, 3, 1, 28, 2], [6, 6, 2, 1, 22, 3], [1, 1, 1, 1, 5, 1],
                        [1, 1, 1, 1, 2, 1],
                        [2, 2, 2, 1, 21, 2], [2, 2, 2, 1, 1, 1], [2, 2, 2, 1, 19, 1], [2, 2, 2, 1, 4, 1],
                        [4, 4, 3, 1, 11, 2],
                        [2, 2, 2, 1, 4, 2], [5, 5, 3, 1, 18, 2], [2, 2, 2, 1, 18, 1], [1, 1, 1, 1, 23, 1],
                        [9, 9, 2, 2, 25, 2],
                        [2, 2, 2, 1, 1, 2], [2, 2, 2, 1, 5, 1], [10, 10, 2, 1, 2, 3], [2, 2, 2, 1, 9, 2],
                        [2, 2, 2, 1, 14, 2],
                        [1, 1, 1, 1, 26, 1], [1, 1, 1, 1, 3, 1], [14, 14, 2, 1, 23, 2], [4, 4, 3, 1, 2, 2],
                        [2, 2, 2, 1, 23, 2]]
        self.gbdt_lr_train(Train_tab, Train_libsvm)

    def gbdt_lr_train(self, Train_tab, Train_libsvm):
        # load样本数据
        X_all, y_all = load_svmlight_file("sample_libsvm_data.txt")
        # 训练/测试数据分割
        X_train, X_test, y_train, y_test = train_test_split(Train_libsvm, Train_tab, test_size=0.1, random_state=42)
        # 定义GBDT模型
        self.gbdt.fit(X_train, y_train)
        # GBDT编码原有特征
        self.X_train_leaves = self.gbdt.apply(X_train)[:, :, 0]
        X_test_leaves = self.gbdt.apply(X_test)[:, :, 0]
        # 对所有特征进行ont-hot编码
        (self.train_rows, cols) = self.X_train_leaves.shape
        gbdtenc = OneHotEncoder()
        X_trans = gbdtenc.fit_transform(np.concatenate((self.X_train_leaves, X_test_leaves), axis=0))
        X_train_ext = hstack([X_trans[:self.train_rows, :], X_train])
        # lr对组合特征的样本模型训练
        self.lr.fit(X_train_ext, y_train)

    def Predict(self, X_test):
        X_test_leaves = self.gbdt.apply(X_test)[:, :, 0]
        gbdtenc = OneHotEncoder()
        self.X_trans = gbdtenc.fit_transform(np.concatenate((self.X_train_leaves, X_test_leaves), axis=0))
        X_test_ext = hstack([self.X_trans[self.train_rows:, :], X_test])
        y_pred_gbdtlr2 = self.lr.predict_proba(X_test_ext)[:, 1]
        values = []
        for value in y_pred_gbdtlr2:
            values.append(value)
        return values


class PredictHandler(RequestHandler):
    def get(self):
        libstr = self.get_argument("lib")
        liblist = libstr.split(":", -1)
        listlib = []
        for libs in liblist:
            listlib.append(self.getLib(libs))

        predict = Predict()
        data = predict.Predict(listlib)
        self.write({"dic": data})

    def getLib(self, libstr):
        libsvm = []
        handle = DataHandle()
        lits = libstr.split(",", -1)
        libsvm.append(handle.Dic_App_Id.get(lits[0], 0))
        libsvm.append(handle.Dic_Ad_Unit_Id.get(lits[1], 0))
        libsvm.append(handle.Dic_Ad_Type.get(lits[2], 0))
        libsvm.append(handle.Dic_Os.get(lits[3], 0))
        libsvm.append(handle.Dic_Region.get(lits[4], 0))
        libsvm.append(handle.Dic_Advertiser_id.get(lits[5], 0))
        return libsvm

    def post(self):
        libstr = self.get_argument("lib")
        liblist = libstr.split(":", -1)
        listlib = []
        for libs in liblist:
            listlib.append(self.getLib(libs))

        predict = Predict()
        data = predict.Predict(listlib)
        self.write({"dic": data})


if __name__ == '__main__':
    Train_tab = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0,
                 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0,
                 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                 0,
                 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0,
                 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Train_libsvm = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 1, 2, 2], [1, 1, 1, 1, 3, 1], [2, 2, 2, 1, 4, 1],
                    [3, 3, 2, 1, 5, 2],
                    [2, 2, 2, 1, 6, 1], [4, 4, 3, 1, 6, 2], [5, 5, 3, 1, 7, 2], [2, 2, 2, 1, 8, 1],
                    [2, 2, 2, 1, 6, 1],
                    [2, 2, 2, 1, 9, 2], [6, 6, 2, 1, 8, 3], [1, 1, 1, 1, 10, 1], [2, 2, 2, 1, 4, 2],
                    [2, 2, 2, 1, 4, 1],
                    [2, 2, 2, 1, 10, 2], [1, 1, 1, 1, 8, 1], [1, 1, 1, 1, 11, 1], [2, 2, 2, 1, 12, 1],
                    [2, 2, 2, 1, 2, 1],
                    [5, 5, 3, 1, 13, 2], [2, 2, 2, 1, 14, 1], [7, 7, 2, 1, 15, 2], [1, 1, 1, 1, 16, 1],
                    [1, 1, 1, 1, 8, 1],
                    [1, 1, 1, 1, 17, 1], [5, 5, 3, 1, 18, 2], [2, 2, 2, 1, 19, 2], [1, 1, 1, 1, 2, 1],
                    [2, 2, 2, 1, 20, 1],
                    [2, 2, 2, 1, 10, 1], [2, 2, 2, 1, 14, 2], [5, 5, 3, 1, 15, 2], [5, 5, 3, 1, 21, 2],
                    [2, 2, 2, 1, 21, 1],
                    [1, 1, 1, 1, 22, 1], [6, 6, 2, 1, 5, 2], [2, 2, 2, 1, 1, 2], [8, 8, 2, 1, 15, 3],
                    [4, 4, 3, 1, 23, 2],
                    [9, 9, 2, 2, 6, 2], [1, 1, 1, 1, 21, 1], [2, 2, 2, 1, 10, 2], [5, 5, 3, 1, 24, 2],
                    [2, 2, 2, 1, 20, 1],
                    [2, 2, 2, 1, 8, 1], [5, 5, 3, 1, 2, 2], [6, 6, 2, 1, 3, 3], [1, 1, 1, 1, 19, 1],
                    [2, 2, 2, 1, 12, 2],
                    [2, 2, 2, 1, 25, 1], [1, 1, 1, 1, 2, 1], [4, 4, 3, 1, 11, 2], [2, 2, 2, 1, 10, 1],
                    [1, 1, 1, 1, 21, 1],
                    [2, 2, 2, 1, 14, 2], [1, 1, 1, 1, 19, 1], [2, 2, 2, 1, 14, 1], [2, 2, 2, 1, 9, 1],
                    [2, 2, 2, 1, 20, 2],
                    [2, 2, 2, 1, 4, 2], [1, 1, 1, 1, 4, 1], [2, 2, 2, 1, 26, 1], [2, 2, 2, 1, 14, 1],
                    [2, 2, 2, 1, 4, 2],
                    [2, 2, 2, 1, 23, 1], [5, 5, 3, 1, 13, 2], [3, 3, 2, 1, 22, 2], [2, 2, 2, 1, 11, 2],
                    [2, 2, 2, 1, 1, 2],
                    [2, 2, 2, 1, 9, 1], [1, 1, 1, 1, 9, 1], [2, 2, 2, 1, 12, 2], [2, 2, 2, 1, 20, 1],
                    [2, 2, 2, 1, 1, 2],
                    [1, 1, 1, 1, 14, 1], [10, 10, 2, 1, 23, 3], [5, 5, 3, 1, 21, 2], [1, 1, 1, 1, 1, 1],
                    [2, 2, 2, 1, 19, 2],
                    [1, 1, 1, 1, 23, 1], [2, 2, 2, 1, 20, 1], [1, 1, 1, 1, 14, 1], [4, 4, 3, 1, 11, 2],
                    [2, 2, 2, 1, 19, 1],
                    [5, 5, 3, 1, 19, 2], [2, 2, 2, 1, 1, 2], [2, 2, 2, 1, 14, 1], [11, 11, 2, 1, 10, 1],
                    [2, 2, 2, 1, 14, 2],
                    [1, 1, 1, 1, 22, 1], [9, 9, 2, 2, 27, 2], [4, 4, 3, 1, 1, 2], [4, 4, 3, 1, 12, 2],
                    [2, 2, 2, 1, 6, 1],
                    [4, 4, 3, 1, 8, 2], [1, 1, 1, 1, 16, 1], [1, 1, 1, 1, 28, 1], [2, 2, 2, 1, 15, 2],
                    [1, 1, 1, 1, 3, 1],
                    [2, 2, 2, 1, 14, 1], [1, 1, 1, 1, 21, 1], [2, 2, 2, 1, 24, 2], [2, 2, 2, 1, 23, 1],
                    [2, 2, 2, 1, 8, 1],
                    [2, 2, 2, 1, 21, 2], [6, 6, 2, 1, 6, 2], [1, 1, 1, 1, 2, 1], [2, 2, 2, 1, 12, 1],
                    [5, 5, 3, 1, 23, 2],
                    [1, 1, 1, 1, 29, 1], [1, 1, 1, 1, 8, 1], [4, 4, 3, 1, 2, 2], [1, 1, 1, 1, 8, 1],
                    [1, 1, 1, 1, 30, 1],
                    [2, 2, 2, 1, 8, 1], [1, 1, 1, 1, 8, 1], [4, 4, 3, 1, 23, 2], [5, 5, 3, 1, 9, 2],
                    [4, 4, 3, 1, 1, 2],
                    [9, 9, 2, 2, 19, 2], [1, 1, 1, 1, 11, 1], [2, 2, 2, 1, 1, 2], [10, 10, 2, 1, 30, 1],
                    [9, 9, 2, 2, 24, 2],
                    [5, 5, 3, 1, 14, 2], [2, 2, 2, 1, 4, 1], [2, 2, 2, 1, 22, 2], [2, 2, 2, 1, 26, 1],
                    [2, 2, 2, 1, 14, 1],
                    [2, 2, 2, 1, 1, 1], [4, 4, 3, 1, 2, 2], [3, 3, 2, 1, 29, 2], [2, 2, 2, 1, 6, 2],
                    [2, 2, 2, 1, 9, 2],
                    [2, 2, 2, 1, 16, 2], [5, 5, 3, 1, 13, 2], [13, 13, 2, 1, 3, 2], [2, 2, 2, 1, 27, 1],
                    [2, 2, 2, 1, 1, 2],
                    [2, 2, 2, 1, 4, 1], [2, 2, 2, 1, 1, 2], [2, 2, 2, 1, 29, 2], [3, 3, 2, 1, 12, 2],
                    [2, 2, 2, 1, 2, 2],
                    [2, 2, 2, 1, 5, 1], [5, 5, 3, 1, 28, 2], [6, 6, 2, 1, 22, 3], [1, 1, 1, 1, 5, 1],
                    [1, 1, 1, 1, 2, 1],
                    [2, 2, 2, 1, 21, 2], [2, 2, 2, 1, 1, 1], [2, 2, 2, 1, 19, 1], [2, 2, 2, 1, 4, 1],
                    [4, 4, 3, 1, 11, 2],
                    [2, 2, 2, 1, 4, 2], [5, 5, 3, 1, 18, 2], [2, 2, 2, 1, 18, 1], [1, 1, 1, 1, 23, 1],
                    [9, 9, 2, 2, 25, 2],
                    [2, 2, 2, 1, 1, 2], [2, 2, 2, 1, 5, 1], [10, 10, 2, 1, 2, 3], [2, 2, 2, 1, 9, 2],
                    [2, 2, 2, 1, 14, 2],
                    [1, 1, 1, 1, 26, 1], [1, 1, 1, 1, 3, 1], [14, 14, 2, 1, 23, 2], [4, 4, 3, 1, 2, 2],
                    [2, 2, 2, 1, 23, 2]]
    train = Predict()
    train.gbdt_lr_train(Train_tab, Train_libsvm)
    train.Predict([[1, 1, 1, 1, 1, 1]])
