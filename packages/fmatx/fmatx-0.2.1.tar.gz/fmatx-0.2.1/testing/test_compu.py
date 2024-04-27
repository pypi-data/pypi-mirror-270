from fmatx import Mat, ones
from mpmath import matrix as m_mat


class TestComputeMatrix :

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

		# matrix
		b = a + a
		m_b = m_a + m_a
		assert b.tolist() == m_b.tolist()

	def test_sub(self) :
		_ori = [[9, 5, 2,  2], [3, 9, 6,  8], [3, 6, 8, 10]]
		a = Mat(_ori)
		m_a = m_mat(_ori)

		# number
		b = a - 6
		m_b = m_a - 6
		assert b.tolist() == m_b.tolist()

		b = a - 0.5
		m_b = m_a - 0.5
		assert b.tolist() == m_b.tolist()

		# matrix
		b = a - a
		m_b = m_a - m_a
		assert b.tolist() == m_b.tolist()

	def test_mul(self) :
		_ori = [[19, 2, 29,  2], [2, 4, 69,  8], [8, 3, 8, 10]]
		a = Mat(_ori)
		m_a = m_mat(_ori)

		# number
		b = 7 * a * 6
		m_b = 7 * m_a * 6
		assert b.tolist() == m_b.tolist()

		b = 0.5 * a * 0.5
		m_b = 0.5 * m_a * 0.5
		assert b.tolist() == m_b.tolist()

		# matrix
		b = a * a.T
		m_b = m_a * m_a.T
		assert b.tolist() == m_b.tolist()

	def test_div(self) :
		_ori = [[1, 2, 2,  2], [2, 4, 6,  8], [3, 6, 8, 10]]
		a = Mat(_ori)
		m_a = m_mat(_ori)

		# number
		b = a / 6
		m_b = m_a / 6
		assert b.tolist() == m_b.tolist()

		b = a / 0.5
		m_b =  m_a / 0.5
		assert b.tolist() == m_b.tolist()

		# matrix
		b = a / a
		assert b.tolist() == ones(*b.shape).tolist()

	def test_pow(self) :
		_ori = [[1, 2, 2,  2], [2, 4, 6,  8], [3, 6, 8, 10], [7, 9, 9, 10]]
		a = Mat(_ori)
		m_a = m_mat(_ori)

		# number
		b = a ** 6
		m_b = m_a ** 6
		assert b.tolist() == m_b.tolist()
