.PHONY: create_dataframe_files

big_seed = 445228303
medium_seed = 236678992
small_seed = 656809333

create_dataframe_files:
	mkdir test_files

#	Create big sized csv file
	python .\setup\setup.py 100000 500 $(big_seed) .\test_files\big.csv

#	Create medium sized csv file
	python .\setup\setup.py 20000 250 $(medium_seed) .\test_files\medium.csv

#	Create small sized csv file
	python .\setup\setup.py 10000 100 $(small_seed) .\test_files\small.csv