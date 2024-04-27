from fmatx import Mat, ones
from mpmath import matrix as m_mat

class TestLP :

	def test_plus(self) :
		_ori = [[6, 2, 3,  2], [2, 9, 6,  8], [3, 6, 8, 10]]
		a = Mat(_ori)
		m_a = m_mat(_ori)

		# number
		b = 7 + a + 6
		m_b = 7 + m_a + 6
		assert b.tolist() == m_b.tolist()

		b = 0.5 + a + 0.5
		m_b = 0.5 + m_a + 0.5
		assert b.tolist() == m_b.tolist()