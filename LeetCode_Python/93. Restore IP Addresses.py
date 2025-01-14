class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def combinations(s, pointer, dots, temp, subsets, count):
            if len(s) - 1 == pointer and count < 3:
                return
            
            elif len(s) - 1 == pointer or count == 3:
                subsets.append(temp[:])
                return
            
            temp.append(pointer)
            dots.append(pointer)
            combinations(s, pointer + 1, dots, temp, subsets, count + 1)
            

            temp.pop()
            dots.pop()
            combinations(s, pointer + 1, dots, temp, subsets, count)

        subsets = []
        result = []
        
        combinations(s, 0, [], [], subsets, 0)
        
        for pos in subsets:
            first_pos = pos[0]
            sec_pos = pos[1]
            third_pos = pos[2]

            # Extract potential IP parts
            first_int_str = s[:first_pos + 1]
            second_int_str = s[first_pos + 1:sec_pos + 1]
            third_int_str = s[sec_pos + 1:third_pos + 1]
            fourth_int_str = s[third_pos + 1:]

            # Validate the parts to form a valid IP address
            if (
                0 <= int(first_int_str) <= 255 and first_int_str == str(int(first_int_str)) and
                0 <= int(second_int_str) <= 255 and second_int_str == str(int(second_int_str)) and
                0 <= int(third_int_str) <= 255 and third_int_str == str(int(third_int_str)) and
                0 <= int(fourth_int_str) <= 255 and fourth_int_str == str(int(fourth_int_str))
            ):
                valid_ip = f"{first_int_str}.{second_int_str}.{third_int_str}.{fourth_int_str}"
                result.append(valid_ip)

        return result

