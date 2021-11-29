import hashlib
for i in range(4097):
    hex_num = format(i, "X")
    hash_text = "a497453fe1eee3e0c4d44f2a74a1518744d247a1c6dd6c902a2b3367987f0e5d21fb1cbdd1af55ea78098be5a336ffaf06f19b8e5a5997e06d20ce00f9907424"
    clear_text = "FS{hash-I_had_corned_beef_and_hash_" + str(hex_num) + "}"
    if hash_text == hashlib.sha512(clear_text.encode()).hexdigest():
        print(clear_text)
        break
    else:
        continue