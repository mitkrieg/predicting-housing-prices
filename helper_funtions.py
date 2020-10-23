from statsmodels.formula.api import ols
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
import seaborn as sns
from sklearn.linear_model import LinearRegression

def reg_formula(outcome,features):
    """
    Takes in outcome and features and returns linear regression formula in r
    
    Outcome: String of title of outcome column
    features: list of strings of feature columns
    """
    
    pred_sum = '+'.join(features)
    return outcome + '~' + pred_sum

def sm_reg(outcome,features,dataset):
    """
    Takes in outcome, features and data set and returns linear regression summary table using statsmodels
    
    outcome: String of title of outcome column
    features: list of strings of feature columns
    dataset: pandas dataframe containing columns that include outcome and features as titles to train model on
    """
    formula = reg_formula(outcome,dataset[features])
    regression = ols(formula=formula,data=dataset).fit()
    return regression.summary()

def sk_rsme(outcome,features,train_set,test_set):
    """
    Takes in outcome, features and dataset and returns rsme and r^2 using sklearn
    
    outcome: String of title of outcome column
    features: list of strings of feature columns
    train_set: pandas dataframe containing columns that include outcome and features as titles to train model on
    test_set: pandas dataframe containing columns that include outcome and features as titles to test model on
    """
    lr = LinearRegression()

    X_train = train_set[features]

    y_train = train_set[outcome]

    lr.fit(X_train,y_train)
    
    X_test = test_set[features]
    
    y_test = test_set[outcome]

    y_train_pred = lr.predict(X_train)
    
    y_test_pred = lr.predict(X_test)

    rmse_train =  mean_squared_error(y_train,y_train_pred,squared=False)
    rmse_test = mean_squared_error(y_test,y_test_pred,squared=False)
    
    sns.residplot(y_train_pred, train_set['price'], lowess=True, color="g")
    
    return (rmse_train, rmse_test, float(lr.score(X_train,y_train)))