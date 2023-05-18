from sim_lib import sim_lib

simulator = sim_lib()
#simulator.generate_clustering('00', '00', '0001', '0095', 2, 2, 0.02)

#simulator.generate_moments(n = 4, first_iteration = 4, last_iteration = 6, x_start = 0, x_end = 100, x_id = 0, y_id = 1, strategy1 = True, strategy2 = True, isPix = False, data_file_name = "gnn.dat")

#-----------
# simulator.generate_properties(first_iteration=4, last_iteration=6, skewness_and_kurtosis = True) ##########
#-----------

#-----------
#simulator.get_rdf(process_no_begin=0, process_no_end=0, file_start=1, file_end=95, molecule_type1=1, molecule_type2=2, particle_id1=1, particle_id2=1, nhis=10) # same molecule id g is filled other than 0
#-----------

simulator.generate_specific_rdf(process_no_begin=0, process_no_end=0, file_start=1, file_end=95, molecule_in_cluster=1, molecule_outside_cluster=2, particle_id1=1, particle_id2=2, r_cut=0.01, rho=5, nhis=42, box = 10)