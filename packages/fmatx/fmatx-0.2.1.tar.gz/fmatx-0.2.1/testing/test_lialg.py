from fmatx import Mat, ones
from sympy import Matrix as m_mat

class TestLinearAlgebra :

	def test_elimination(self) :
		_ori = [[6, 2, 3,  2], [2, 9, 6,  8], [3, 6, 8, 10]]
		a = Mat(_ori)
		m_a = m_mat(_ori)

		# number
		b = a.rref()[0]
		m_b = m_a.rref()[0]
		assert b.tolist() == m_b.tolist()

	def test_inv(self) :
		_ori = [[1, 8, 2,  2], [2, 4, 6,  8], [4, 6, 8, 10], [7, 9, 9, 10]]
		a = Mat(_ori)
		m_a = m_mat(_ori)

		b = a**-1
		m_b = m_a**-1
		assert b.tolist() == m_b.tolist()