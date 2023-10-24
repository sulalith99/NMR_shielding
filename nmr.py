import csv
#
string_to_search = "****  N U C L E U S : "
string_NMR = ""
#
atom_lines = []
atoms_labels = []
atoms_sort = []
adf_input_number = []
NMR_numbering = []
NMR = []
NMR_H = []
#
def atoms(file_name, string_to_search):
     with open(file_name, 'r') as read_obj:
         for line in read_obj:
              if line.startswith(string_to_search):
                    labels = ((line.split("****  N U C L E U S : "))[1]).rstrip()
                    line = ((line.split("("))[0].split("****  N U C L E U S : "))[1]
                    atom_lines.append(line)
                    atoms_labels.append(labels)
                    continue
     with open(file_name, 'r') as read_obj:
         for line in read_obj:
              if line.startswith(" Atom input number in the ADF calculation: "):
                    labels = ((line.split("Atom input number in the ADF calculation: "))[1]).rstrip()
                    labelsALL = (((labels.split("("))[1]).split(")"))[0]
                    adf_input_number.append(labelsALL)
                    continue
     with open(file_name, 'r') as read_obj:
         for line in read_obj:
              if line.startswith(" Internal NMR numbering of atoms: "):
                    labels = ((line.split("Internal NMR numbering of atoms: "))[1]).rstrip()
                    labelsALL = (((labels.split("("))[1]).split(")"))[0]
                    NMR_numbering.append(labelsALL)
                    continue
#
def atom_sort(atoms_sort,atom_lines):
    atom_n = list(dict.fromkeys(atom_lines))
#
#
#
    for n in range(len(atom_n)):
#
        atoms_sort.append(atom_n[n])
#
def nmr_search(file_name,atoms_sort,atoms_labels,string_NMR,string_to_search):
    for n in range(len(atoms_labels)):
        string_NMR = ""+string_to_search+atoms_labels[n]
        with open(file_name, 'r') as read_obj:
             word_match = ''
             for line in read_obj:
                  if line.startswith(string_NMR):
                        word_match = "YES"
                        continue
                  if word_match == "YES":
                        if line.startswith("===  TOTAL NMR SHIELDING TENSOR (ppm)"):
                             word_match = "YES-YES"
                        continue
                  if word_match == "YES-YES":
                        if (line.lstrip()).startswith("isotropic ="):
                             word_match = "DONE"
                             print(('NMR Shielding '+atoms_labels[n]+': '+(((line.lstrip()).lstrip("isotropic =")).lstrip()).rstrip()+' ppm'))
                             NMR.append(('NMR Shielding '+atoms_labels[n]+': '+(((line.lstrip()).lstrip("isotropic =")).lstrip()).rstrip()+' ppm   ADF-Numbering: '+adf_input_number[n]+'   NMR-Numbering: '+NMR_numbering[n]))
                        continue
                  if word_match == 'Done':
                        break
#
def nmr_search_H(file_name,atoms_sort,atoms_labels,string_NMR,string_to_search):
    for n in range(len(atoms_labels)):
      if (atoms_labels[n]).startswith("H"):
        string_NMR = ""+string_to_search+atoms_labels[n]
        with open(file_name, 'r') as read_obj:
             word_match = ''
             for line in read_obj:
                  if line.startswith(string_NMR):
                        word_match = "YES"
                        continue
                  if word_match == "YES":
                        if line.startswith("===  TOTAL NMR SHIELDING TENSOR (ppm)"):
                             word_match = "YES-YES"
                        continue
                  if word_match == "YES-YES":
                        if (line.lstrip()).startswith("isotropic ="):
                             word_match = "DONE"
                             NMR_H.append(('NMR Shielding '+atoms_labels[n]+': '+(((line.lstrip()).lstrip("isotropic =")).lstrip()).rstrip()+' ppm   ADF-Numbering: '+adf_input_number[n]+'   NMR-Numbering: '+NMR_numbering[n]))
                        continue
                  if word_match == 'Done':
                        break
#
print("")
print("**** NMR Shielding ****")
print("")
file_name = input('.out File name (file-name.out): ')
print("")         
#
out_file = ((file_name.split('_'))[0])+'-ALL-NMR'+'.txt'
atoms(file_name, string_to_search)
atom_sort(atoms_sort,atom_lines)
#atom_input_nmber(file_name)
nmr_search(file_name,atoms_sort,atoms_labels,string_NMR,string_to_search)
#
NMR = ["{}\n".format(i) for i in NMR]
with open(out_file,'w',encoding='UTF8',newline='') as f:
    f.writelines(NMR)
nmr_search_H(file_name,atoms_sort,atoms_labels,string_NMR,string_to_search)
out_file_H_NMR = ((file_name.split('_'))[0])+'-H-NMR'+'.txt'
NMR_H = ["{}\n".format(i) for i in NMR_H]
with open(out_file_H_NMR,'w',encoding='UTF8',newline='') as f:
    f.writelines(NMR_H)
