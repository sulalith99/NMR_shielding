# NMR_shielding
# for NMR calculations # ADF

* nmr.py is a Python script that will extract all the NMR shielding values from the output file of an ADF calculation.

* this will generate two files that contain chemical shifts corresponding to all the atoms in the molecule, and one file that only contains the chemical shifts for the hydrogen atoms of the system.

* resulting files also indicate the labeling system used in both ADF and in the NMR calculation itself, where it will be important afterward to number the shielding values properly.

* nmr.py does not need to be in your working directory; you can create a custom command that can be accessible through any directory of interest.

* to execute the script use, "python3 nmr.py", which will then ask you to enter the name of the output file, and that's it. remember to include the ".out" when specifying the output file name.

* There are no changes required in the code itself but feel free to make any changes as necessary.
