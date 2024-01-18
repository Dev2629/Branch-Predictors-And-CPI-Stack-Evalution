import Generate_CSV
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
df = pandas.read_csv("op.csv")
from sklearn import preprocessing
import pandas as pd
from mlxtend.preprocessingr_Reg
import sys
df = CSV(sys.argv[1])


#For 502 benchmark
#df[['Cycles', 'Instructions', 'branch_misses','l1d_replacement' ,'L1_icache_load_misses','l2_rqsts_all_demand_miss','longest_lat_cache_miss','br_inst_retired_all_branches','dtlb_load_misses_walk_completed','dtlb_store_misses_walk_completed' ,'frontend_retired_itlb_miss','itlb_misses_walk_completed']]=df[['Cycles', 'Instructions', 'branch_misses','l1d_replacement' ,'L1_icache_load_misses','l2_rqsts_all_demand_miss','longest_lat_cache_miss','br_inst_retired_all_branches','dtlb_load_misses_walk_completed','dtlb_store_misses_walk_completed' ,'frontend_retired_itlb_miss','itlb_misses_walk_completed']].div(df['Instructions'], axis=0)
#X = df[['branch_misses','l1d_replacement' ,'L1_icache_load_misses','longest_lat_cache_miss',
#        'br_inst_retired_all_branches','dtlb_load_misses_walk_completed','dtlb_store_misses_walk_completed' ,'frontend_retired_itlb_miss','itlb_misses_walk_completed']]

#For Other benchmarks

df[['Cycles','Instructions', 'branch_misses','cache_misses','L1_dcache_load_misses','L1_icache_load_misses','LLC_load_misses',
     'Mem_Stores','l2_rqsts_code_rd_miss','l2_rqsts_rfo_miss','l2_rqsts_demand_data_rd_miss',
     'l1d_pend_miss_pending','frontend_retired_l1i_miss','dTLB_load_misses','dTLB_store_misses','iTLB_load_misses']] =df[['Cycles','Instructions', 'branch_misses','cache_misses','L1_dcache_load_misses','L1_icache_load_misses','LLC_load_misses',
     'Mem_Stores','l2_rqsts_code_rd_miss','l2_rqsts_rfo_miss','l2_rqsts_demand_data_rd_miss',
     'l1d_pend_miss_pending','frontend_retired_l1i_miss','dTLB_load_misses','dTLB_store_misses','iTLB_load_misses']].div(df['Instructions'], axis=0)

#We Have Different combinaation of miss events for each program.

X = df[['branch_misses','L1_dcache_load_misses','L1_icache_load_misses','LLC_load_misses',
     'Mem_Stores','l2_rqsts_code_rd_miss','l2_rqsts_rfo_miss','l2_rqsts_demand_data_rd_miss',
     'l1d_pend_miss_pending','frontend_retired_l1i_miss','dTLB_load_misses','dTLB_store_misses','iTLB_load_misses']]

#We Will Consider Only that Events which is less correlated to each other.Hence All benchmarks have different Events considered.

y = df['Cycles']
X = X.fillna(0)
y = y.fillna(0)


reg_model = Reg(X,y)

y_pred= reg_model.predict(X_test)
x_pred= reg_model.predict(X_train)


y_p = statistics.mean(y_pred)
y_m = statistics.mean(y_test)

X_mean = X.sum(axis = 0)
X_mean = list(X_mean)
X_mean = preprocessing.normalize([X_mean])
X_mean = X_mean[0]
p = 1-f.cdf(450.97572,X_test.shape[1],(y_test.shape[0]-1-X_test.shape[1]))

K = len(list(zip(X, reg_model.coef_)))
N = len(X_test)
Rsq = R_square
fstat = (Rsq/(1-Rsq))*((N-K-1)/K)
rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
R_square = r2_score(y_test , y_pred)
Adj = 1 - (1-R_square)*(len(y_train)-1)/(len(y_train)-X_train.shape[1]-1)
p = 1-f.cdf(fstate,X.shape[1],(y.shape[0]-1-X.shape[1]))


StackGraph(X_mean)

print("Base : " , reg_model.intercept_)
print('Mean Square Error:', rmse)
print('R_Square : ',R_square)
print("Adj : " , Adj)
print("fstat :",fstat)
print("Predicted : ",y_p)
print("True :",y_m)
print("P Value : " ,p)