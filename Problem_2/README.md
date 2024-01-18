# Building CPI Stack Of Programe Using Hardware Counters And Linier Regression

## Introduction
We obtain the CPI (Cycles Per Instruction) stack for programs using hardware performance monitoring counters.
**CPI stack** divides the total CPI of an application into components that reflect the time spent in various events, such L1-I Cache misses, L1-D cache misses, L2/L3 Cache misses, I-TLB and D-TLB misses, branch misprediction, etc.
The counts of various miss events occuring during program execution can be obtained using hardware Performane Monitoring Counters (PMC) on modern architectures.  Performance counter values for running application can be obtained using performance monitoring tools such as PAPI and  Perf.
We are using Perf Tool.
We Get various Miss Events for the program usinig perf and we built regression model on each program and plot CPI Stack Graph For Each Benchmark.

## How To Get Analyze Programe Using Perf

We Used Following Benchmarks.

| 502.gcc_r|523.xalancbmk_r|
|--|--|
| **526.blender_r** |**544.nab_r**  |




First We Need To Install Perf Tool in System.
```
apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`


```
Now Let's See How We have Compile Each Benchmark
###  502.gcc_r

    perf stat -I 15 -o per_out_502.txt -e cpu-cycles,instructions,l1d.replacement,dTLB-load-misses,dTLB-store-misses,iTLB-load-misses,l2_rqsts.all_demand_miss,longest_lat_cache.miss,br_inst_retired.all_branches,frontend_retired.itlb_miss,itlb_misses.walk_completed,dtlb_load_misses.walk_completed,dtlb_store_misses.walk_completed,branch-misses exe/cpugcc_r_base.mytest-m64 data/refrate/input/gcc-pp.c -O3 -finline-limit=0 -fif-conversion -fif-conversion2 -o gcc-pp.opts-O3_-finline-limit_0_-fif-conversion_-fif-conversion2.s

We truncated All ' , ' From the Number so that we can easily convert it into python float data type

    tr -d ',' < per_out_502.txt > perout1_502.txt

###  523.xalancbmk_r

    perf stat -I 15 -o per_out.txt -e cpu-cycles,instructions,branch-misses,cache-misses,L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores,L1-dcache-store-misses,L1-dcache-prefetches,L1-dcache-prefetch-misses,L1-icache-loads,L1-icache-load-misses,L1-icache-prefetches,L1-icache-prefetch-misses,LLC-loads,LLC-load-misses,mem-loads,mem-stores,l2_rqsts.code_rd_miss,l2_rqsts.demand_data_rd_miss,l2_rqsts.rfo_miss,l1d_pend_miss.pending,frontend_retired.l1i_miss,frontend_retired.itlb_miss,frontend_retired.stlb_miss exe/cpuxalan_r_base.mytest-m64 -v data/refrate/input/t5.xml data/refrate/input/xalanc.xsl

    tr -d ',' < per_out.txt > perout1_523.txt

###  526.blender_r

    perf stat -I 15 -o per_out_526.txt -e cpu-cycles,instructions,branch-misses,cache-misses,L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores,L1-dcache-store-misses,L1-dcache-prefetches,L1-dcache-prefetch-misses,L1-icache-loads,L1-icache-load-misses,L1-icache-prefetches,L1-icache-prefetch-misses,LLC-loads,LLC-load-misses,mem-loads,mem-stores,l2_rqsts.code_rd_miss,l2_rqsts.demand_data_rd_miss,l2_rqsts.rfo_miss,l1d_pend_miss.pending,frontend_retired.l1i_miss,frontend_retired.itlb_miss,frontend_retired.stlb_miss exe/blender_r_base.mytest-m64 data/refrate/input/sh3_no_char.blend --render-output sh3_no_char_--threads1 -b -F RAWTGA -s 849 -e 849 -a


     tr -d ',' < per_out_526.txt > perout1_526.txt

### 544.nab_r

    perf stat -I 15 -o per_out_526.txt -e cpu-cycles,instructions,branch-misses,cache-misses,L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores,L1-dcache-store-misses,L1-dcache-prefetches,L1-dcache-prefetch-misses,L1-icache-loads,L1-icache-load-misses,L1-icache-prefetches,L1-icache-prefetch-misses,LLC-loads,LLC-load-misses,mem-loads,mem-stores,l2_rqsts.code_rd_miss,l2_rqsts.demand_data_rd_miss,l2_rqsts.rfo_miss,l1d_pend_miss.pending,frontend_retired.l1i_miss,frontend_retired.itlb_miss,frontend_retired.stlb_miss exe/nab_r_base.mytest-m64 1am0 1122214447 122

    tr -d ',' < per_out_544.txt > perout1_544.txt




## How To Use Data to plot Linear Regression
Unzip the Problem_2 Folder.

    cd Problem_2

Now We have .txt File of the benchmark output.
We Have to give path of that txt file as input to the Main.py.
All the Text files are in Test folder.We can use Any one of those text file.
It will take text file and then internally it will create csv file from that text file.
And Do Linier Regression using csv and give various parameters as output.
And also plot CPI Stack and Residual Plot.

    python3 Main.py path/to/text/file

## Output

We Have All Parameters like RMSE , F State , P-value , R Square etc.
And We have Stack Graph of Cpi and get Residuals Plot.

    Base :  0.15327224279399115
    Mean Square Error: 0.03509010472581555
    R_Square :  0.9351548068220135
    Adj :  0.9345556212587671
    fstat : 660.1770591848838
    Predicted :  0.4184557996221837
    True : 0.5512553770464241
    P value : 1.1102230246251565e-16



