#########################################################
# Project 4: Cahce Simulator
# 11/29/21
# Aidan Kirk, Chris
#
# Program that simulates the behavior of a unified cache
#########################################################


# Check line size
# load byte
# load halfword
# load word
# load doubleword

# Import .dt file
file = input('trace.dt')

# Variables
set = 0    # Total sets
set_associative = 0    # Set Associativity
set_words = 0    # Words per set
total_hits = 0    # Total hits
total_misses = 0    # Total misses
total_accesses = 0    # Total accesses
total_mem_ref = 0    # Total memory references
hit_ratio = 0    # Hit ratio
miss_ratio = 0    # Miss ratio
line = 0    # Just a hold for formatting rn

#####----- TABLE BUILDING -----#####

# Table Building
print("Cache Configuration\n")
print("\t" + str(set) + "-way set associative entries")
print("\t" + str(set_associative) + " sets total")
print("\t" + str(set_words) + " words per set\n\n")
print("Results for Each Reference\n")

# Build Summary
print("Simulation Summary Statistics\n-----------------------------")
print("Total hits\t\t: " + str(total_hits))
print("Total misses\t\t: " + str(total_misses))
print("Total accesses\t\t: " + str(total_accesses))
print("Total memory references\t: " + str(total_mem_ref))
print("Hit ratio\t\t: " + str(hit_ratio))
print("Miss ratio\t\t: " + str(miss_ratio))

# Final Data Cache State
print("\n\tFinal Data Cache State\n------------------------------")

while set < 2:
    print("Set " + str(set))
    while line < 2:
        print("\tline " + str(line) + " = byte addresses 40-47, tag 4, lru 0")
        line+=1
    set += 1
    line = 0
