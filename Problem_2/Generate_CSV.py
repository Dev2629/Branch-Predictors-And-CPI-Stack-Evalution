import pandas as pd
import numpy as np

def CSV(path):

    cnt = 0
    cycles = []
    instructions = []
    branch_misses = []
    cache_misses = []
    L1_dcache_load_misses = []
    L1_icache_load_misses = []
    LLC_load_misses = []
    dTLB_load_misses = []
    dTLB_store_misses = []
    iTLB_load_misses = []

    mem_stores = []
    l2_rqsts_code_rd_miss = []
    l2_rqsts_rfo_miss = []
    l2_rqsts_demand_data_rd_miss = []
    l1d_pend_miss_pending = []
    frontend_retired_l1i_miss = []
    with open(path) as topo_file:
      for line in topo_file:
              if(len(line.split())>2):
                  x = line.split()
                  z = x[1]
                  y = -1
                  if(z.isnumeric()):
                    y = int(z)
                  x = x[2]
                  if("cpu_core/cpu-cycles/" == x):
                    cycles.append(y)
                  elif("cpu_core/instructions/" == x):
                    instructions.append(y)
                  elif("cpu_core/branch-misses/" == x):
                    branch_misses.append(y)
                  elif("cpu_core/cache-misses/" == x):
                    cache_misses.append(y)
                  elif("cpu_core/L1-dcache-load-misses/" == x):
                    L1_dcache_load_misses.append(y)
                  elif("cpu_core/L1-icache-load-misses/" == x):
                    L1_icache_load_misses.append(y)
                  elif("cpu_core/LLC-load-misses/" == x):
                    LLC_load_misses.append(y)
                  elif("cpu_core/mem-stores/"==x):
                    mem_stores.append(y)
                  elif("cpu_core/l2_rqsts.code_rd_miss/"==x):
                    l2_rqsts_code_rd_miss.append(y)
                  elif("cpu_core/l2_rqsts.demand_data_rd_miss/" == x):
                    l2_rqsts_demand_data_rd_miss.append(y)
                  elif("cpu_core/l2_rqsts.rfo_miss/"==x):
                    l2_rqsts_rfo_miss.append(y)
                  elif("cpu_core/l1d_pend_miss.pending/"==x):
                    l1d_pend_miss_pending.append(y)
                  elif("cpu_core/frontend_retired.l1i_miss/"==x):
                    frontend_retired_l1i_miss.append(y)
                  elif("cpu_core/dTLB-load-misses/" == x):
                    dTLB_load_misses.append(y)
                  elif("cpu_core/dTLB-store-misses/" == x):
                    dTLB_store_misses.append(y)
                  elif("cpu_core/iTLB-load-misses/"== x):
                    iTLB_load_misses.append(y)
                  elif("cpu_core/dTLB-load-misses/" == x):
                    dTLB_load_misses.append(y)
                  elif("cpu_core/dTLB-store-misses/" == x):
                    dTLB_store_misses.append(y)
                  elif("cpu_core/iTLB-load-misses/"== x):
                    iTLB_load_misses.append(y)



    d = {'Cycles': cycles, 'Instructions': instructions, 'branch_misses': branch_misses,'cache_misses' : cache_misses,'L1_dcache_load_misses' : L1_dcache_load_misses,'L1_icache_load_misses':L1_icache_load_misses,'LLC_load_misses':LLC_load_misses,
         'Mem_Stores': mem_stores,'l2_rqsts_code_rd_miss':l2_rqsts_code_rd_miss,'l2_rqsts_rfo_miss':l2_rqsts_rfo_miss,'l2_rqsts_demand_data_rd_miss':l2_rqsts_demand_data_rd_miss,
         'l1d_pend_miss_pending':l1d_pend_miss_pending,'frontend_retired_l1i_miss':frontend_retired_l1i_miss,'dTLB_load_misses':dTLB_load_misses,'dTLB_store_misses':dTLB_store_misses,'iTLB_load_misses':iTLB_load_misses}
    header = ['Cycles','Instructions', 'branch_misses','cache_misses','L1_dcache_load_misses','L1_icache_load_misses','LLC_load_misses',
         'Mem_Stores','l2_rqsts_code_rd_miss','l2_rqsts_rfo_miss','l2_rqsts_demand_data_rd_miss',
         'l1d_pend_miss_pending','frontend_retired_l1i_miss','dTLB_load_misses','dTLB_store_misses','iTLB_load_misses']



    df = pd.DataFrame.from_dict(d, orient='index')
    df = df.transpose()
    print(len(iTLB_load_misses))
    # write the DataFrame to a CSV file
    df.to_csv('op.csv')
    return df

#If you want to run 502 benchmark use this function instead of previous one.Because here we have used different set of events.

def CSV_502(path):

    cnt = 0
    cycles = []
    instructions = []
    l1d_replacement = []
    branch_misses = []
    L1_icache_load_misses = []
    l2_rqsts_all_demand_miss = []
    longest_lat_cache_miss = []
    br_inst_retired_all_branches = []
    dtlb_load_misses_walk_completed= []
    L1_dcache_load_misses = []
    dtlb_store_misses_walk_completed = []
    frontend_retired_itlb_miss = []
    itlb_misses_walk_completed = []


    # cache_misses = []
    # L1_icache_load_misses = []
    # LLC_load_misses = []
    dTLB_load_misses = []
    dTLB_store_misses = []
    iTLB_load_misses = []

    # mem_stores = []
    # l2_rqsts_code_rd_miss = []
    # l2_rqsts_rfo_miss = []
    # l2_rqsts_demand_data_rd_miss = []
    # l1d_pend_miss_pending = []

    with open(path) as topo_file:
      for line in topo_file:
              if(len(line.split())>2):
                  x = line.split()
                  z = x[1]
                  y = -1
                  if(z.isnumeric()):
                    y = int(z)
                  x = x[2]
                  if("cpu_core/cpu-cycles/" == x):
                    cycles.append(y)
                  elif("cpu_core/instructions/" == x):
                    instructions.append(y)
                  elif("cpu_core/l1d.replacement/" == x):
                    l1d_replacement.append(y)
                  elif("cpu_core/L1-icache-load-misses/" == x):
                    L1_icache_load_misses.append(y)
                  elif("cpu_core/l2_rqsts.all_demand_miss/" == x):
                    l2_rqsts_all_demand_miss.append(y)
                  elif("cpu_core/longest_lat_cache.miss/" == x):
                    longest_lat_cache_miss.append(y)
                  elif("cpu_core/br_inst_retired.all_branches/" == x):
                    br_inst_retired_all_branches.append(y)
                  elif("cpu_core/itlb_misses.walk_completed/"==x):
                    itlb_misses_walk_completed.append(y)
                  elif("cpu_core/frontend_retired.itlb_miss/"==x):
                    frontend_retired_itlb_miss.append(y)
                  elif("cpu_core/dtlb_store_misses.walk_completed/" == x):
                    dtlb_store_misses_walk_completed.append(y)
                  elif("cpu_core/branch-misses/"==x):
                    branch_misses.append(y)
                  elif("cpu_core/dtlb_load_misses.walk_completed/"==x):
                     dtlb_load_misses_walk_completed.append(y)
                  elif("cpu_core/dTLB-load-misses:u/" == x):
                    dTLB_load_misses.append(y)
                  elif("cpu_core/dTLB-store-misses:u/" == x):
                    dTLB_store_misses.append(y)
                  elif("cpu_core/iTLB-load-misses:u/"== x):
                    iTLB_load_misses.append(y)

    d = {'Cycles': cycles, 'Instructions': instructions, 'branch_misses': branch_misses,'l1d_replacement' : l1d_replacement,'L1_icache_load_misses':L1_icache_load_misses,'l2_rqsts_all_demand_miss' : l2_rqsts_all_demand_miss,'longest_lat_cache_miss':longest_lat_cache_miss,'br_inst_retired_all_branches':br_inst_retired_all_branches,'dtlb_load_misses_walk_completed':dtlb_load_misses_walk_completed,'dtlb_store_misses_walk_completed':dtlb_store_misses_walk_completed,'frontend_retired_itlb_miss': frontend_retired_itlb_miss,'itlb_misses_walk_completed':itlb_misses_walk_completed}
    header = ['Cycles', 'Instructions', 'branch_misses','l1d_replacement' ,'L1_icache_load_misses','l2_rqsts_all_demand_miss','longest_lat_cache_miss','br_inst_retired_all_branches','dtlb_load_misses_walk_completed','dtlb_store_misses_walk_completed' ,'frontend_retired_itlb_miss','itlb_misses_walk_completed']
    df = pd.DataFrame.from_dict(d, orient='index')
    df = df.transpose()
    print(len(cycles))
    # write the DataFrame to a CSV file
    df.to_csv('op.csv')
    return df