class Puzzle15:

    def is_even_permutation(self, permutation) -> bool:
        transpositions = 0
        permutation_length = len(permutation) - 1
        for ok_boundary_index in range(0, permutation_length):
            value_index_to_check = ok_boundary_index
            min_value_index = ok_boundary_index
            while value_index_to_check < permutation_length:
                value_index_to_check += 1
                if permutation[value_index_to_check] != 0 \
                        and permutation[value_index_to_check] < permutation[min_value_index]:
                    min_value_index = value_index_to_check
            if min_value_index != ok_boundary_index:
                tmp = permutation[ok_boundary_index]
                permutation[ok_boundary_index] = permutation[min_value_index]
                permutation[min_value_index] = tmp
                transpositions += 1
        return transpositions % 2 == 0
