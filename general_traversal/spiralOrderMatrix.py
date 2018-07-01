def printMatrixSpiral(mat,nos_rows,nos_columns):
    start_row_index=0
    end_row_index=nos_rows-1
    start_column_index=0
    end_column_index=nos_columns-1
    while(start_row_index<=end_row_index and start_column_index<=end_column_index):
        ##printing the first row in the remaining matrix
        for i in range(start_column_index,end_column_index+1):
            print mat[start_row_index][i],
        start_row_index=start_row_index+1
        ##pritning the last column in remaining matrix
        for j in range(start_row_index,end_row_index+1):
            print mat[j][end_column_index],
        end_column_index=end_column_index-1a
        ##printing the last row in remainig matrix
        if(start_row_index<=end_row_index):
            i=end_column_index
            while(i>=start_column_index):
                print mat[end_row_index][i],
                i=i-1
            end_row_index=end_row_index-1
        ##printing the first column of the remainig matrix
        if(start_column_index<=end_column_index):
            j=end_row_index
            while(j>=start_row_index):
                # print "I={value1},column={value2}".format(value1=j,value2=start_column_index)
                print mat[j][start_column_index],
                j=j-1
            start_column_index=start_column_index+1
if __name__ == '__main__':
    print("To print a given matrix in spiral order")
    mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    nosRows=len(mat)
    nosColumns=len(mat[0])
    printMatrixSpiral(mat,nosRows,nosColumns)