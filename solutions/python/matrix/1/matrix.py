class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        array_of_rows = self.matrix_string.splitlines()
        target_row = array_of_rows[index-1]
        target_nums = target_row.split()
        output = [int(num) for num in target_nums]
        return output

    def column(self, index):
        array_of_rows = self.matrix_string.splitlines()
        target_column = []
        for row in array_of_rows:
            this_row = row.split()
            target_column.append(this_row[index-1])
        output = [int(num) for num in target_column]        
        return output
                
