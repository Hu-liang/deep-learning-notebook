# 独立样本SEM(SE)

## $ S_{\bar{x}_1 - \bar{x}_2} = {\sqrt{ {S_1^2 \over n_1} + {S_2^2 \over n_2}  }} $ 

通过合并方差来纠正样本量

利用 $ S_p^2 $ 来合并方差


# Pooled variance :
### one sample
## $ S^2 = {SS \over df} = {{SS_1 +SS_2} \over {df_1+df2}} = {\sum(x_i-\bar{x})^2 \over n-1} $ 


## $ \sum(x_i - \bar{x} ) $

# t 统计量 :

## $ t = {{\bar{x}_1 -  \bar{x}_2 } \over S_{\bar{x}_1 - \bar{x}_2} }$ (反向也是正常)

一般来说是 : 


## $ t = {{ (\bar{x}_1 -  \bar{x}_2) - (\bar{u}_1 -  \bar{u}_2) } \over S_{\bar{x}_1 - \bar{x}_2} }$  

但是 $ \bar{u}_1 -  \bar{u}_2 = 0 $ 因为零假设通常是 0 


## $ t = {{\bar{x}_1 -  \bar{x}_2 } \over {\sqrt{( {S_1^2 \over n_1} + {S_2^2 \over n_2} ) }}} $  

## $ df = n_1+n_2 - 2 $

## $ CI : \bar{x} \pm t*SEM $



单独样本T检验（One-Samples T Test）用于进行样本所在总体均数与已知总体均数的比较，独立样本T检验（Independent-Samples T Test)用于进行两样本均数的比较。


## 相依样本 (Dependent samples) 受试者内设计
同一受试者参加两次测试 
示例 : 每个受试者按随机顺序呗分配到两个组 或是处在对照组 接受某种处理 或者接受两种治疗

### within - subject design
- two condition 
- Pre-test , post-test
- Growth over time (longitudinal study ) 纵向研究 比如在16年和17年作出比较

### Advantages 
 - controls for individual differences
 - cost-effective
 - less time - consuming
 - less expensive

### Disadvantages
 - carry-over effects 残留效应 (second measurement can be affected by first measurement)
 - order may influence results


## 独立样本(Independent samples) 受试者间设计
开展实验性实验 对受试者实施处理措施 
或开展观察性实验 观察两组不同总体的特性
### between - subject design
 - Experimental
 - Observational
 
$H_0 : u_1 - u_2 = 0$
$H_A : u_1 - u_2 > 0$
$u_1 - u_2 < 0  $ 
$ u_1 - u_2 \pm 0 $
### $ t = {\bar{x_1} -  \bar{x_2} \over SE} $

Reject $H_0$ if  p < a
Fail to reject $H_0$ if  p > a 

知道样本均值 和大小以及标准差


# z-test works when we konw u and sigma 
# samples 
 - How different a sample mean is from a population
 - How different tow sample means are from each other
    - dependent
    - independent

用贝塞尔校正系数 , 根据样本标准偏差估算总体标准偏差
mean = u , SD = sigma / sqrt(n)