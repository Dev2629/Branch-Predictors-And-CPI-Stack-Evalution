

#include <map>

#include "perceptron.h"
#include "tage.h"
#include <ooo_cpu.h>

// TAGE defines start here.
// constexpr std::size_t NUM_BANKS = 4;
// constexpr std::size_t BIMODAL_SIZE = 4099;
// constexpr std::size_t LEN_BIMODAL = 2;
// constexpr std::size_t LEN_GLOBAL = 9;
// constexpr std::size_t LEN_TAG = 10;
// constexpr std::size_t LEN_COUNTS = 3;
// constexpr std::size_t MIN_HISTORY_LEN = 5;
// constexpr std::size_t MAX_HISTORY_LEN = 131;
// TAGE defines end here.

// Perceptron defines start here
// constexpr std::size_t PERCEPTRON_HISTORY = 24; // history length for the global history shift register
// constexpr std::size_t PERCEPTRON_BITS = 8;     // number of bits per weight
// constexpr std::size_t NUM_PERCEPTRONS = 5282;  // 163;

// constexpr std::size_t NUM_UPDATE_ENTRIES = 100; // size of buffer for keeping 'perceptron_state' for update
// // Perceptron defines end here

// // Bimodal metapredictor defines start here
// constexpr std::size_t BIMODAL_TABLE_SIZE = 16384;
// constexpr std::size_t BIMODAL_PRIME = 16381;
// constexpr std::size_t COUNTER_BITS = 2;
// // Bimodal metapredictor defines end here

// using MyTage = Tage<NUM_BANKS, BIMODAL_SIZE, LEN_BIMODAL, LEN_GLOBAL, LEN_TAG, LEN_COUNTS, MIN_HISTORY_LEN, MAX_HISTORY_LEN>;
// using MyPerceptron = PerceptronPred<PERCEPTRON_HISTORY, PERCEPTRON_BITS, NUM_PERCEPTRONS, NUM_UPDATE_ENTRIES>;
// using MyMetaPredictor = Bimodal<BIMODAL_TABLE_SIZE, BIMODAL_PRIME, COUNTER_BITS>;

// namespace
// {
// // std::map<O3_CPU*, MyTage> tage;
// // std::map<O3_CPU*, MyPerceptron> perceptron_predictor;
// std::map<O3_CPU*, MyMetaPredictor> metapredictor;
// } // namespace

std::vector<int> chooser_table;
uint64_t chooser_table_index_size;
uint8_t perceptron_prediction;
uint8_t tagged_prediction;

void O3_CPU::initialize_branch_predictor() { 
    tage_init(); 
    chooser_table_index_size=512;
    for(int i=0;i<512;i++){
        chooser_table.push_back(2);
    }
}

uint8_t O3_CPU::predict_branch(uint64_t ip)
{

  perceptron_prediction=perceptron_predict_branch(ip);
  tagged_prediction=tage_predict_branch(ip);
  auto chooser_table_index=ip%chooser_table_index_size;
  if(chooser_table[chooser_table_index]>=2){
    return tagged_prediction;
  }
  else{
    return perceptron_prediction;
  }
}


void O3_CPU::last_branch_result(uint64_t ip, uint64_t branch_target, uint8_t taken, uint8_t branch_type)
{

  auto chooser_table_index=ip%chooser_table_index_size;

  if(taken)
	{
		if(tagged_prediction == taken && perceptron_prediction != taken)
		{
			if(chooser_table[chooser_table_index] < 3)
				chooser_table[chooser_table_index] = chooser_table[chooser_table_index] + 1;
		}
		else if(perceptron_prediction == taken && tagged_prediction != taken)
		{
			if(chooser_table[chooser_table_index] > 0)
				chooser_table[chooser_table_index] = chooser_table[chooser_table_index] - 1;

		}
    }		
	else
	{	
		if(tagged_prediction == !taken && perceptron_prediction == taken)
		{
			if(chooser_table[chooser_table_index] < 3)
				chooser_table[chooser_table_index] = chooser_table[chooser_table_index] + 1;
		}
		else if(perceptron_prediction == !taken && tagged_prediction == taken)
		{
			if(chooser_table[chooser_table_index] > 0)
				chooser_table[chooser_table_index] = chooser_table[chooser_table_index] - 1;

		}
    }
    tage_train(ip, taken);
    perceptron_train(ip, branch_target, taken, branch_type);
}
