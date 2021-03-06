

# 砍掉尾巴
虽然 Katie 建议去除上下各 25% 的数据点，但我们在去除数据点时还需要特别谨慎，特别是在数据量不大的情况下，去除一半的数据点会让我们丢失大量数据的信息。

一般来说，在去除数据点前，我们建议首先将数据点通过图像表述出来（直方图、散点图、箱线图等），这样可以帮助你获得对数据整理分析的了解。然后，基于项目的背景，判断你更关心数据的哪一部分（大多数正常数据，还是小部分异常数据），因为在一些项目背景下，你可能更关心那些异常值，比如在 数据分析（进阶）课程的安然数据分析中，那些工资异常高的人更有可能腐败。最后，是基于现有的数据量作出决定，究竟是直接丢弃部分数据还是对部分作出调整，亦或是有保留地接受所有数据。特别记住一点，没有一种分析方法100%正确，但我们总可以尝试根据不同的需求找到一种最合理的方法。


# 四分位数（Quartile）

指在统计学中把所有数值由小到大排列并分成四等份，处于三个分割点位置的数值。多应用于统计学中的箱线图绘制。

分位数是将总体的全部数据按大小顺序排列后，处于各等分位置的变量值。如果将全部数据分成相等的两部分，它就是中位数；如果分成四等分，就是四分位数；八等分就是八分位数等。四分位数也称为四分位点，它是将全部数据分成相等的四部分，其中每部分包括25%的数据，处在各分位点的数值就是四分位数。四分位数有三个，第一个四分位数就是通常所说的四分位数，称为下四分位数，第二个四分位数就是中位数，第三个四分位数称为上四分位数，分别用Q1、Q2、Q3表示[1]  。
第一四分位数 (Q1)，又称“较小四分位数”，等于该样本中所有数值由小到大排列后第25%的数字。
第二四分位数 (Q2)，又称“中位数”，等于该样本中所有数值由小到大排列后第50%的数字。
第三四分位数 (Q3)，又称“较大四分位数”，等于该样本中所有数值由小到大排列后第75%的数字。
第三四分位数与第一四分位数的差距又称四分位距（InterQuartile Range,IQR）。

实例1
数据总量: 6, 47, 49, 15, 42, 41, 7, 39, 43, 40, 36
由小到大排列的结果: 6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49
一共11项
Q1 的位置=（11+1） × 0.25=3， Q2 的位置=（11+1）× 0.5=6， Q3的位置=（11+1） × 0.75=9
Q1 = 15，
Q2 = 40，
Q3 = 43


# IQR(四分位间距)错误还是正确？

- [X] 几乎 50% 的数据在 IQR 间。
- [ ] IQR 受到数据集中每一个值的影响。
- [X] IQR 不受异常值的影响。



## 离均差(Deviation from mean  $x_i - \bar{x}  $) :
 $x_i - \bar{x}  $

## 平均偏差(Average deviation  $ \frac {\sum (x_i - \bar{x}) }{ n } $) :
 $  \frac {\sum (x_i - \bar{x}) }{ n } $

## 平均绝对偏差(Average absolute deviation  $ \frac {\sum (|x_i - \bar{x}|) }{ n } $) :
 $ \frac {\sum (|x_i - \bar{x}|) }{ n } $

## 平方差和(Sum of squares  $\sum(x_i - \bar{x})^2  $) :
 $\sum(x_i - \bar{x})^2  $

## 标准偏差(Standard deviation  $ \sqrt{  \frac {\sum (x_i - \bar{x})^2 }{ n } }$) :  -->总体标准偏差
  $ \sigma = \sqrt{  \frac {\sum (x_i - \bar{x})^2 }{ n } }$

# 标准差的重要性
 在正态分布即数据分布均匀下 $ \bar{x} = mean = mode  $
 68%表示一个标准差的范围 ($x \pm \sigma $) 
 95%为不超过两个标准差($x \pm 2\sigma $)

## 贝塞尔标准偏差(Bessel's correction standard deviation  $ \sqrt{  \frac {\sum (x_i - \bar{x})^2 }{ n-1 } }$) :  -->样本标准偏差
  $ S = \sqrt{  \frac {\sum (x_i - \bar{x})^2 }{ n-1 }}  \approx \sigma  $ 
## 样本方差为 $ \frac {\sum (x_i - \bar{x})^2 }{ n-1 } $