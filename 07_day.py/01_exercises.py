it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(f"The lenght of it companies is {len(it_companies)}")
#-------------------------------------------------------------------------------------
# 2.- Add Twiter.
it_companies.add("Twitter")
print(it_companies)
#-------------------------------------------------------------------------------------
# 3.- Insert multiple IT.
it_companies.update(["Youtube","Linux","Opera"])
print(it_companies)
#-------------------------------------------------------------------------------------
# 4.- Remove one of the companies.
it_companies.discard("Facebook")
print(it_companies)