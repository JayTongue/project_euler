from tqdm import tqdm

big_str = ''
for i in tqdm(range(1, int(1e6)+1)):
    big_str += str(i)
big_str = list(big_str)
print(int(big_str[0]) 
      * int(big_str[int(1e1)-1]) 
      * int(big_str[int(1e2)-1]) 
      * int(big_str[int(1e3)-1]) 
      * int(big_str[int(1e4)-1]) 
      * int(big_str[int(1e5)-1]) 
      * int(big_str[int(1e6)-1]))