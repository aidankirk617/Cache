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
column = "-------"    # Also for formatting

# Reference Variables
access = 0

#####----- TABLE BUILDING -----#####

# Table Building
print("Cache Configuration\n")
print("\t" + str(set) + "-way set associative entries")
print("\t" + str(set_associative) + " sets total")
print("\t" + str(set_words) + " words per set\n\n")
print("Results for Each Reference\n")

# References
print("%-10s %-10s %-10s %-10s %-10s %-10s %-10s" %("Access", "Address", "  Tag", "Index", "Offset", "Result", "Memrefs"))
print("%-10s %-10s %-10s %-10s %-10s %-10s %-10s" %(column, column, column, column, column, column, column))

#--- Reading goes here ---
def memory_check(total_mem_ref):
    count = 0   # Counter for how many times we do this

    while total_mem_ref < 7:    # Column 1 (Access)
        # if column 2 == "R":     pseudocode for when we figure out reading
        #   access = "read"
        # elif column 2 == "W":
        #   access = "write"

    # Put in all the data we collected, print it, start all over again until each line is full
    print("%-10s %-10s %-10s %-10s %-10s %-10s %-10s" %(str(access), "Address", "  Tag", "Index", "Offset", "Result", "Memrefs"))
    count += 1

# Build Summary
print("\n\nSimulation Summary Statistics\n-----------------------------")
print("Total hits\t\t: " + str(total_hits))
print("Total misses\t\t: " + str(total_misses))
print("Total accesses\t\t: " + str(total_accesses))
print("Total memory references\t: " + str(total_mem_ref))
print("Hit ratio\t\t: " + str(hit_ratio))
print("Miss ratio\t\t: " + str(miss_ratio))

# Final Data Cache State
print("\n\n\tFinal Data Cache State\n------------------------------")

while set < 2:
    print("Set " + str(set))
    while line < 2:
        print("\tline " + str(line) + " = byte addresses 40-47, tag 4, lru 0")
        line+=1
    set += 1
    line = 0
