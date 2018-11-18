from mathematica.algebra.matrices import add_matrices, sub_matrices

def test_add_matrices:
    a = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    b = [
        [7, 8 , 9],
        [10, 11, 12],
    ]

    result = add_matrices(a, b)

    assert result == [
        [8, 10, 12],
        [14, 16, 18],
    ]

def test_add_matrices_witf_different_shape()
    a = [
        [1, 2],
        [3, 4],

    b = [
        [7, 8, 9],
        [10, 11, 12],
    ]

    with pytest.raises(ValueError) as e:
        result = add.Matrices(a, b)