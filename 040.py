from tqdm import tqdm
big_list = []
for i in tqdm(range(1, int(1e6)+1)):
    big_list += [int(n) for n in list(str(i))]
print(big_list[0] 
      * big_list[int(1e1)-1] 
      * big_list[int(1e2)-1] 
      * big_list[int(1e3)-1] 
      * big_list[int(1e4)-1] 
      * big_list[int(1e5)-1] 
      * big_list[int(1e6)-1])