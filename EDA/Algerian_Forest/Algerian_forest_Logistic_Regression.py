import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')
from statsmodels.stats.outliers_influence import variance_inflation_factor 
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn.linear_model  import LogisticRegression

df = pd.read_csv("D:\Python Programs\Data_Science Task\Ineuron_Tasks\EDA\Algerian_Forest\Algerian_test.csv")
#df.head()
#df.columns
X = df.drop(['Classes','year','Region'],axis=1)
y = df['Classes'] # Region
#Standardize or feature scaling the datasets 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

vif = pd.DataFrame()
vif["vif"] = [variance_inflation_factor(X_scaled,i) for i in range(X_scaled.shape[1])]
vif["Features"] = X.columns

X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.25, random_state= 355)

log_reg = LogisticRegression()
log_reg.fit(X_train,y_train)

y_pred = log_reg.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
#print(accuracy)
conf_mat = confusion_matrix(y_test,y_pred)
#print(conf_mat)

true_positive = conf_mat[0][0]
false_positive = conf_mat[0][1]
false_negative = conf_mat[1][0]
true_negative = conf_mat[1][1]

Accuracy = (true_positive + true_negative) / (true_positive +false_positive + false_negative + true_negative)
print(Accuracy)

Precision = true_positive/(true_positive+false_positive)
print(Precision)

Recall = true_positive/(true_positive+false_negative)
print(Recall)

F1_Score = 2*(Recall * Precision) / (Recall + Precision)
print(F1_Score)

auc = roc_auc_score(y_test, y_pred)
print(auc)

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

plt.plot(fpr, tpr, color='orange', label='ROC')
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--',label='ROC curve (area = %0.2f)' % auc)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show()