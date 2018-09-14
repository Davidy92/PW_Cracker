import hashlib
passFile = open('passwords.txt', 'r')

salt_MD5 = []
hash_MD5 = []
salt_SHA512 = []
hash_SHA512 = []
for line in passFile:
	if "$6$" in line:
		temp1 = line.split(":")
		temp1 = temp1[1]
		temp1 = temp1.split('$')
		salt_SHA512.append(temp1[2])
		hash_SHA512.append(temp1[3])
	if "$1$" in line:
		temp1 = line.split(":")
		temp1 = temp1[1]
		temp1 = temp1.split('$')
		salt_MD5.append(temp1[2])
		hash_MD5.append(temp1[3])
print(salt_MD5, hash_MD5)
print(salt_SHA512, hash_SHA512)

#comparing the hashes
crackStation = open('crackstation-human-only.txt', 'r')

for line in crackStation:
	hashed_PW_1 = hashlib.md5(bytes(salt_MD5[0].encode() + line.encode()))
	hashed_PW_2 = hashlib.md5(bytes(salt_MD5[1].encode() + line.encode()))
	Hash1 = hashed_PW_1.hexdigest()
	Hash2 = hashed_PW_2.hexdigest()
	if Hash1 == hash_MD5[0]:
		print("First password Cracked")
		first_account_password = line
	if Hash2 == hash_MD5[1]:
		print("Second password Cracked")
		second_account_password = line
	
		
	
